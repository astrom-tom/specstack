'''
########################################################
#####                                                  #
#####                  specstack                       #
#####                  R.THOMAS                        #
#####                    2019                          #
#####                    Main                          #
#####                                                  #
########################################################
@License: GPL - see LICENCE.txt
'''

####Public General Libraries
import os
import sys

####third party
from catscii import catscii
import  numpy

####local imports
from . import cli
from . import spec
from . import plot

__version__ = '19.4.2'

def main():
    '''
    This function is the main of the catmatch.
    '''
    
    try:
        ####get arguments from the command lien interface
        args = cli.CLI().arguments

        

        ###check normalisation limits
        lims = args.normlimits.split(',')
        lims = [float(lims[0]), float(lims[1])]
        if lims[0]>=lims[1]:
            print('\033[1m Normalisation limits error: l0>=l1, must be l0<l1! \033[0m')
            print('\033[1m Quitting... \033[0m')
            sys.exit()

        ###check if file exist
        if not os.path.isfile(args.speclist):
            print('\033[1m File %s not found \033[0m'%args.speclist)
            print('\033[1m Quitting... \033[0m')


        ##if everything is ready we start looking at the list of files
        ##we load the catalog
        catalog = catscii.load_cat(args.speclist, True)
        names = catalog.get_column('spec', str)
        redshift = catalog.get_column('redshift', float)

        ###we restframe all the files
        restframe = []
        waves_0 = []
        waves_f = []
        for (i,j) in zip(names, redshift):
            if not os.path.isfile(i):
                print('\033[1m Spectrum %s not found, skip \033[0m'%i)

            else:
                wave, flux = spec.restframe_normalised(i, j, lims[0], lims[1])
                restframe.append((wave, flux))
                waves_0.append(wave[0])
                waves_f.append(wave[-1])

        ##define limits of the spectrum
        minw = max(waves_0)
        maxw = min(waves_f)
        print('\033[1m The stack spectrum will be computed between %.1f and %.1f \033[0m'%(minw, maxw))
        grid = numpy.arange(minw, maxw, 1)

       ##and new grid
        
        ###and regrid all the spec
        rebinned = spec.regrid(restframe, grid)

        ##create stack
        stacked, std = spec.stack(rebinned, float(args.s))

        ##and prod 
        final_grid = numpy.arange(minw, maxw, float(args.bin))
        final_stack = numpy.interp(final_grid, grid, stacked)
        final_std = numpy.interp(final_grid, grid, std)
        
        wave, flux = spec.renorm(final_grid, final_stack, 0, lims[0], lims[1])

        ##and save it
        numpy.savetxt(args.f, numpy.array([wave, flux, final_std]).T)

        ##eventually plot
        if args.p:
            plot.plot(final_grid, final_stack, final_std, rebinned, grid)
                        
    except KeyboardInterrupt:
        print('quitting...')
        sys.exit()


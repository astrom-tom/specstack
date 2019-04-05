'''

specstack module 
-----------------
File: spec.py

This file contains the spectroscopic source code

@author: R. THOMAS
@year: 2019
@place:  ESO
@License: GPL v3.0 - see LICENCE.txt
'''

##Python standard library
import sys

##python third party
import numpy
import scipy.stats as stats

def restframe_normalised(spec, z, l0, l1):
    '''
    This function deredshift the wavelength grid
    and normalise the spectrum between l0 and l1

    Parameters
    ----------
    spec    str
            name of the spectrum to deredshift
    z       float
            redshift of the spectrum
    l0      float
            lower limit of the zone where we normalize
    l1      float
            upper limit ''' ''' ''' ''' ''' '''

    Returns
    -------
    wave_0  numpy array
            restframe wavelength
    flux_norm
            flux_density normalised in the normalisation region
    '''

    ##loadspectrum
    specdata = numpy.genfromtxt(spec,dtype='float').T
    wave = specdata[0]
    flux = specdata[1]

    ##deredshift the wavelength
    wave_0 = wave/(1+z) 

    ###find the region where to normalize
    reg = numpy.where(numpy.logical_and(numpy.greater_equal(wave_0,l0),numpy.less_equal(wave_0,l1)))
    ###check if the region reports anything
    if len(reg[0]) == 0:
        print('the region does not exist in spec %s(restframe), we skip'%spec)
        return [], []
    

    region = wave_0[reg]

    ###compute the median in the region
    med = numpy.mean(flux[reg])

    ##and devide all the spectrum by this amount
    flux_norm = flux/med 

    return wave_0, flux_norm


def renorm(wave, flux, z, l0, l1):
    '''
    This function deredshift the wavelength grid
    and normalise the spectrum between l0 and l1

    Parameters
    ----------
    wave    numpy array
            wavelength
    flux    numpy.array of flux

    z       float
            redshift of the spectrum
    l0      float
            lower limit of the zone where we normalize
    l1      float
            upper limit ''' ''' ''' ''' ''' '''

    Returns
    -------
    wave_0  numpy array
            restframe wavelength
    flux_norm
            flux_density normalised in the normalisation region
    '''

    ##deredshift the wavelength
    wave_0 = wave/(1+z) 

    ###find the region where to normalize
    reg = numpy.where(numpy.logical_and(numpy.greater_equal(wave_0,l0),numpy.less_equal(wave_0,l1)))
    ###check if the region reports anything
    if len(reg[0]) == 0:
        print('the region does not exist in spec %s(restframe), we skip'%spec)
        return [], []
    

    region = wave_0[reg]

    ###compute the median in the region
    med = numpy.median(flux[reg])

    ##and devide all the spectrum by this amount
    flux_norm = flux/med 

    return wave_0, flux_norm



def regrid(restframe,  grid):
    '''
    This function rebins all the spectra to the 
    new grid

    Parameters
    ----------
    restframe   list
                of all the spectra to stack

    grid        numpy.array
                new wave to interpolate the spectrum to

    Returns
    -------
    rebinned    list
                of all spectrum interpolated to the new grid
    '''

    rebinned = []
    for i in restframe:
        r = numpy.interp(grid, i[0], i[1])
        rebinned.append(r)

    return rebinned


def stack(rebinned, sigma):
    '''
    Function that stack the spectra
    using a sigmaclipping method.

    Parameters
    -----------
    rebinned    list
                of rebinned spectra
                
    sigma       floag
                sigmaclipping parameter
    return
    ------
    stacked     list
                stacked spectrum
    std         list
                associated standard deviation
    '''

    ##convert to numpy array
    specs = numpy.array(rebinned).T

    stacked = []
    std = []
    for i in specs:
        c, low, upp = stats.sigmaclip(i, sigma, sigma)
        stacked.append(numpy.mean(c))
        std.append(numpy.std(c))
        #std.append(numpy.median(numpy.abs(c-numpy.median(c))))

    return numpy.array(stacked), numpy.array(std)



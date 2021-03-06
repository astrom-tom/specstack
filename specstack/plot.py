'''

specstack module 
-----------------
File: ploy.py

This file configures the plotting lines

@author: R. THOMAS
@year: 2019
@place:  ESO
@License: GPL v3.0 - see LICENCE.txt
'''

#### Python third party
import matplotlib.pyplot as plt


def plot(grid, stacked, std, ermean, indiv, grid_indiv):
    '''
    Function that plots the stacked spectrum and the sigma

    Parameters
    ----------
    grid    numpy.array
            wavelength

    stacked numpy.array
            stacked spectrum

    std     numpy.array
            associated standard deviation

    ermean  numpy.array
            associated error on the mean

    Returns
    -------

    None    --> it is plot!
    '''

    print(len(indiv[0]))
    print(len(grid_indiv.shape))

    fig = plt.figure()
    aa = fig.add_subplot(111)
    aa.minorticks_on()

    #aa.fill_between(grid, 0, stacked, color='0.5', zorder=0)
    for i in indiv:
        aa.plot(grid_indiv, i, lw=0.1, zorder=0)

    aa.plot(grid, stacked, 'k', lw=0.5, zorder=1, label='Stacked Spectrum')
    aa.plot([grid[0], grid[-1]], [0, 0], lw=1, ls='--', zorder=1, color='k')
    aa.plot(grid, std, 'b', lw=0.5, zorder=1, label='1$\sigma$')
    aa.plot(grid, ermean, 'r', lw=0.5, zorder=1, label='Error on the mean')

    aa.legend()
    aa.set_xlim(grid[0], grid[-1])
    aa.set_xlabel('Wavelength [$\mathrm{\AA}$]')
    aa.set_ylabel('Normalised Flux Density [unitless]')

    plt.show()


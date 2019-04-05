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


def plot(grid, stacked, std):
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

    Returns
    -------

    None    --> it is plot!
    '''

    fig = plt.figure()
    aa = fig.add_subplot(111)
    aa.minorticks_on()

    aa.fill_between(grid, 0, stacked, color='0.5', zorder=0)
    aa.plot(grid, stacked, 'k', lw=0.5, zorder=1, label='Stacked Spectrum')
    aa.plot([grid[0], grid[-1]], [0, 0], lw=1, ls='--', zorder=1, color='k')
    aa.plot(grid, std, 'b', lw=0.5, zorder=1, label='1$\sigma$')

    aa.legend()
    aa.set_xlim(grid[0], grid[-1])
    aa.set_xlabel('Wavelength [$\mathrm{\AA}$]')
    aa.set_ylabel('Normalised Flux Density [unitless]')

    plt.show()


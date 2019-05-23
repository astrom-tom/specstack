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
import os
import time

##python third party
import numpy
import scipy.stats as stats

def restframe_normalised(spec, z, l0, l1, SNR, verbose):
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

    SNR     str
            SNR,l1_snr,l0_snr threshold of the SNR to compute in
            between snr_l0 and snr_l1

    verbose Bool
            True or false for printouts

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

    ###SNR --> if the user gave something then we must compute it!
    if SNR != None:
        snr_threshold = float(SNR.split(',')[0])
        snr_l0 = float(SNR.split(',')[1])
        snr_lf = float(SNR.split(',')[2])
        reg_snr = numpy.where(numpy.logical_and(numpy.greater_equal(wave_0,snr_l0),\
                numpy.less_equal(wave_0,snr_lf)))
        
        ##compute snr
        mean = numpy.median(flux[reg_snr])
        std = numpy.std(flux[reg_snr])
        snr_data = mean/std

        if snr_data < snr_threshold:
            if verbose:
                print('The SNR is too low for spec %s (SNR=%s)'%(os.path.basename(spec), snr_data))
            return [], []


    if z>7:
        return [], []
    ###find the region where to normalize
    reg = numpy.where(numpy.logical_and(numpy.greater_equal(wave_0,l0),numpy.less_equal(wave_0,l1)))

    ###check if the region reports anything
    if len(reg[0]) == 0:
        if verbose:
            print('The region does not exist in spec %s (restframe), we skip it'%os.path.basename(spec))
        return [], []
    
    region = wave_0[reg]

    ###compute the median in the region
    med = numpy.mean(flux[reg])

    ##and devide all the spectrum by this amount
    flux_norm = flux/med 

    return wave_0, flux_norm


def renorm(wave, flux, z, l0, l1, verbose):
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
        if verbose:
            print('The region does not exist in spec %s(restframe), we skip'%spec)
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
        index_nan_min = numpy.where(grid<i[0][0])
        r[index_nan_min] = numpy.nan
        index_nan_max = numpy.where(grid>i[0][-1])
        r[index_nan_max] = numpy.nan
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
    ermean = []
    N = []
    for i in specs:
        no_nan = numpy.count_nonzero(~numpy.isnan(i))
        index = numpy.where(numpy.isnan(i) == False)
        N.append(no_nan)
        if no_nan == 1:
            stacked.append(i[index][0])
            std.append(i[index][0])
            ermean.append(i[index][0])
        elif no_nan < 10:
            stacked.append(numpy.nanmedian(i[index]))
            std.append(numpy.nanstd(i[index]))
            ermean.append(numpy.nanstd(numpy.sqrt(no_nan)))
        else:
            c, low, upp = stats.sigmaclip(i[index], sigma, sigma)
            stacked.append(numpy.nanmedian(c))
            std.append(numpy.nanstd(c))
            ermean.append(numpy.nanstd(c)/numpy.count_nonzero(~numpy.isnan(c)))

    return numpy.array(stacked), numpy.array(std), numpy.array(ermean), numpy.array(N)

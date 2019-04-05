.. _how:

How does it work?
=================

Brief decription
^^^^^^^^^^^^^^^^
Specstack is reading the spectra file and is going to process each of them separaterly. First it **deredshift** the wavelenght grid and **normalize** the flux to the region given by the user using the 'normlimits' argument. In the region given by these limits, the mean of the flux is set to 1.

Once all the spectra are normalized and redshifted specstack is going to look at the maximal wavelength window where all the stacked spectrum can be computed with all the individual spectra. To do that it will look at all the de-redshifted grid and collect the starting-bluest and final-reddest wavelength. From the set of blue wavelengths it will take the maximal wavelength. From the set of red wavelength it will take the minimal wavelength. This define the final restframe window of the stacked spectrum (from Lb to Lr). **This ensure that each point in the stack spectrum is computed with the same amount of individual flux points.**

Then all the individual spectrum are regridded in a common wavelength grid of bin=1Angstrom and limits Lb and Lr.
Once it is done the final stack spectrum flux is computed computing the mean of all the individual spectrum using a **sigma-clipping** algorithm (default is 3-sigma but can be easily changed from the command line interface). 

Finally, the wavelength binning is changed a last time to the binning requested by the user, interpolating the spectrum to a new wavelength grid.

Final Result
^^^^^^^^^^^^
You can see below an animation of the stack of z>4 galaxies with different anount of individual galaxies, from N=2 to N=163.

.. image:: ./images/myimage.gif
        :width: 750px



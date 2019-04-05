.. _Usagecli:

Usage
=====

The command line interface help
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You start specstack from a terminal. specstack comes with a command line interface which includes a 'help' that you can display in your terminal using the help command. It must be called like this::

           [user@machine]$ specstack --help

This command will display the help of the program::

        usage: specstack [-h] [-s S] [-p] [--method METHOD] [-f F]
                         speclist normlimits bin

        specstack V19.4.0, R. Thomas, 2018, ESO, This program comes with ABSOLUTELY NO
        WARRANTY; and is distributed under the GPLv3.0 Licence terms.See the version
        of this Licence distributed along this code for details.

        positional arguments:
          speclist         File with col1 = spectra names, col2 = redshift
          normlimits       l1 and l2 in angstrom where the spectra will be normalised
          bin              Binning of the stacked spectrum

        optional arguments:
          -h, --help       show this help message and exit
          -s S             Sigma we use for the clipping, default=3
          -p               If plot at the end
          -f F             Name of the final file



specstack has few optionnal arguments and 3 mandatory arguements. You can not start specstack without any argument:

Mandatory arguments
^^^^^^^^^^^^^^^^^^^
	
* **speclist:** This is the file that contains the list of spectra you want to stack. This files should have two columns:
    * the **spec** column: name of the spectrum file to use
    * the **redshift** column: redshift of the spectrum
    * The header of the file should be **'#redshift spec'**. The names of the columns should be there.

Example::

        #redshift       spec
        3.5             spec1.txt
        3.7             spec2.txt
        3.65            spec3.txt
        .               .
        .               .
        .               .

.. warning::
        Each spectrum should be an ascii file with (wavelength-flux) columns. Wavelength should be in Angstrom.

* **normlimits**: This is where the spectra are going to be normalized. It consists of two wavelength in angstrom, separated by a coma. Example: **1020,1120**.

* **bin**: This is the final binning, in angstrom, of the spectrum. 

Optional arguments
^^^^^^^^^^^^^^^^^^
	
* -h and '- -help': Display this help in the terminal.
* **-s**: The program uses a simgal clipping algorithm to compute the stack. The default value is 3sigma but you can as well use a different number of sigma if you want too. Example: **-s 4** will use a 4-sigma clipping.
* **-p**: If you want to see the result of the stacking as a plot directly after the computation.
* **-f**: By default the stacked spectrum is saved in a text file with wavelength-stackflux-standard deviation. The file is by default called 'stacked.txt'. But if you want to give another name you can use that option. Example: **-f final_stack.txt**. This way the final file will be called final_stack.txt.





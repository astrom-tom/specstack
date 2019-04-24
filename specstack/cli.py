'''

specstack module 
-----------------
File: cli.py

This file configures the Command line interface 

@author: R. THOMAS
@year: 2019
@place:  ESO
@License: GPL v3.0 - see LICENCE.txt
'''

#### Python Libraries
import argparse

class CLI:
    """
    This Class defines the arguments to be calle to use specstack
    For the help, you can use 'specstack -h' or 'specstack --help'
    """
    def __init__(self,):
        """
        Class constructor, defines the attributes of the class
        and run the argument section
        """
        self.args()

    def args(self,):
        """
        This function creates defines the 7 main arguments of specstack using the argparse module
        """
        parser = argparse.ArgumentParser(description="specstack V19.4.1, R. Thomas, 2018, ESO, \
                This program comes with ABSOLUTELY NO WARRANTY; and is distributed under \
                the GPLv3.0 Licence terms.See the version of this Licence distributed along \
                this code for details.")

        parser.add_argument('speclist', help="File with col1 = spectra names, col2 = redshift")
        parser.add_argument('normlimits', help="l1 and l2 in angstrom where the spectra will be normalised")
        parser.add_argument('bin', help="Binning of the stacked spectrum")

        parser.add_argument('-s', help="Sigma we use for the clipping, default=3", default=3)
        parser.add_argument('-p', help="If plot at the end", action='store_true')
        #parser.add_argument('--method', default='sigmaclip', help="method used to stack spectrum, \
        #                                    can be sigma clipping, errors, mean, median. Default is sigmaclip")
        parser.add_argument('-f', help="Name of the final file", default='stacked.txt')
        parser.add_argument('--version', help="Display the version", action='store_true')
        ##### GET the Arguments for specstack startup
        self.arguments = parser.parse_args()



.. _installation:


Installation
============

specstack is written in python 3.7. It needs only the following libraries:

* Numpy v1.16: Numerical python
* catscii v1.3: catalog simple query tool 

Other libraries are used, but they are all part of the standard python library. As such no extra installations are needed.

1-from the python repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last specstack version is v19.4.0 and is available in the main pypi repository. To install it::

     pip install specstack --user

Using this command will allow you not to have to install any other package. Pip will install what is missing for you.


2-From the local the github repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The installable package can be found in the github directory under the ''dist'' directory. Take the last version and run::

	pip install specstack-X.Y.Z.tar.gz --user

In the version number of specstack, X is the year, Y is the month, and Z is the number of revisions in that month. Therefore 19.4.3 means, third revision of April 2019.


This will install specstack.

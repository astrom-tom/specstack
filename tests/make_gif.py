from catscii import catscii
import numpy
import os
import matplotlib.pyplot as plt


cat = catscii.load_cat('ALL_sup_423_good_col', True)
z = cat.get_column('redshift', str)
spec = cat.get_column('spec',str)

i=0
while i < cat.Nrows-2:
    j = i
    i+=2
    print(i)
    if len(str(i)) == 1:
        k = '00%s'%i
    if len(str(i)) == 2:
        k = '0%s'%i
    if len(str(i)) == 3:
        k = '%s'%i
    numpy.savetxt('file_%s'%k, numpy.array([z[0:i], spec[0:i]]).T, fmt='%s\t%s', header='redshift\tspec')
    os.system('specstack file_%s 1070,1170 1 -s 3 -f file_%s_stack'%(k,k))

    l,f,e = numpy.genfromtxt('file_%s_stack'%k).T

    fig = plt.figure()
    aa = fig.add_subplot(111)

    aa.fill_between(l,0,f, color='0.8')
    aa.plot(l,f, lw=0.75, color='k')
    aa.minorticks_on()
    aa.set_xlim(950,1400)
    aa.set_ylim(-0.7,4)
    aa.set_xlabel('Wavelength[$\mathrm{\AA}$]', fontsize=14)
    aa.set_ylabel('Flux [normalized]', fontsize=14)
    aa.text(950,3.7, 'N=%s'%len(z[0:i]), fontsize=14, color='r')
    plt.plot()
    aa.axvline(972, ls='--', color='0.55')
    aa.text(955,-0.32, r'Ly$_{\gamma}$', rotation=90, fontsize=17, color='r')
    aa.axvline(1025, ls='--', color='0.55')
    aa.text(1005,-0.32, r'Ly$_{\beta}$', rotation=90, fontsize=17, color='r')
    aa.axvline(1192, ls='--', color='0.55')
    aa.text(1175,-0.32, r'SiII', rotation=90, fontsize=17, color='r')
    aa.axvline(1215, ls='--', color='0.55')
    aa.text(1195,-0.32, r'Ly$_{\alpha}$', rotation=90, fontsize=17, color='r')
    aa.axvline(1260, ls='--', color='0.55')
    aa.text(1240,-0.32, r'SiII', rotation=90, fontsize=17, color='r')
    aa.axvline(1300, ls='--', color='0.55')
    aa.text(1280,-0.32, r'OI', rotation=90, fontsize=17, color='r')
    aa.axvline(1334, ls='--', color='0.55')
    aa.text(1315,-0.32, r'CII', rotation=90, fontsize=17, color='r')
    plt.savefig('stack_%s.eps'%k, quality=100, dpi=300)
    plt.close()

    

    




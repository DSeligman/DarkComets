#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.colors import LogNorm

from astropy.io import ascii

infile = sys.argv[1]


obox_smallIma = 15
obox_ima = 30
obox_largeIma = 200
oprof = 10

pix =  0.1943801 


profC   = ascii.read(infile+ '_C.ecsv')
profCav = ascii.read(infile+ '_Cav.ecsv')
profSav = ascii.read(infile+ '_Sav.ecsv')

skys = 10.


    
fig,ax = plt.subplots()

ax.scatter(  profC['r_arcsec'], profC['flux_sky'], marker='.', color='k', s=5)
ax.plot    ( profCav['r_arcsec'], profCav['flux_sky'], color='k')
ax.errorbar( profCav['r_arcsec'], profCav['flux_sky'], yerr=profCav['flux_skys'],
            marker='o', color='k')
ax.plot( profSav['r_arcsec'],
            profSav['flux_sky']/profSav['flux_sky'][0]*profCav['flux_sky'][0],
            color='r')

ax.set_xlim(-0.1,(oprof+0.5)*pix)
ax.set_ylim(-skys, max(profCav['flux_sky'])*1.1)
ax.set_xlabel('Radius [arcsec]')
ax.set_ylabel('Flux [adu/pix]')
                        

                        
plt.savefig(infile+'.png')

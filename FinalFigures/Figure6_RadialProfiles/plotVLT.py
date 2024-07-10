
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from astropy.io import fits
from astropy.io import ascii
from astropy.table import QTable, Table
from astropy.wcs import WCS
import astropy.units as u

if 1:
    rootFile = 'Sima_cM'
    profFile = rootFile+'_profAll.fits'
    profAvFile = rootFile+'_profAv.fits'
    profStFile = rootFile+'_profAvStar.fits'



    t = fits.open(profFile)
    prof = Table( t[1].data)

    t = fits.open(profAvFile)
    profAv = Table( t[1].data)

    t = fits.open(profStFile)
    profSt = Table( t[1].data)


    ephem = ascii.read(rootFile + '_eph.ecsv')

    mySky= np.average(prof['fluxStar'][  (prof['radarcsec'] > 2.) &
                                       (prof['radarcsec'] < 5.)   ])
    print('MySky', mySky)

    mySky = .15
    prof['fluxStar'] = prof['fluxStar'] - mySky
    profAv['fluxStar'] = profAv['fluxStar'] - mySky


    fig, ax = plt.subplots()
    ax.plot(profSt['radarcsec'], 
             profSt['fluxStar']/profSt['fluxStar'][0]*prof['fluxStar'][0], 
             color='r', label='Star')
    ax.scatter(prof['radarcsec']-0.05, prof['fluxStar'], 
                s=1, color='k', label='2001 ME1 pixels')
    ax.errorbar(profAv['radarcsec'], profAv['fluxStar'], profAv['fluxStars'],
                 fmt='.', color='k', label='2001 ME1 average')
  
    ax.set_xlim(0.1,4)

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('[arcsec]', fontsize=15)
    ax.set_ylabel('Flux [adu]', fontsize=15)
    ax.legend(fontsize=12)
    fig.tight_layout()
    fig.show()
    plt.savefig('2001ME1profile.pdf')
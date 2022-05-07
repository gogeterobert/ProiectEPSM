from unittest.util import unorderable_list_difference
import numpy
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy

class ProfilEnergie:
    def __init__(self, profil):
        self.profil = self.interpolareProfil(profil)

    def interpolareProfil(self, profil):
        putere = self.iaPutereMaxima(profil)
        profil.sort(key=self.sorteazaDupaPutere, reverse=False)
        numPuncteOriginale = len(profil)
        numPuncteNoi = putere+1
        
        xOriginal = numpy.zeros(numPuncteOriginale)
        index = 0
        for dataProfil in profil:
             xOriginal[index] = dataProfil['putere'] * 4
             index += 1

        yOriginal = numpy.zeros(numPuncteOriginale)
        index = 0
        for dataProfil in profil:
             yOriginal[index] = dataProfil['intensitate'] * 4
             index += 1

        xInterpolated = numpy.linspace(0, max(xOriginal), numPuncteNoi)
        yInterpolated = numpy.interp(xInterpolated, xOriginal, yOriginal)

        plt.plot(xInterpolated, yInterpolated, '')
        plt.xlabel("Putere in grame")
        plt.ylabel("Curent consumat in mA")
        plt.show()

        return yInterpolated

    def sorteazaDupaPutere(self, valoare):
        return valoare['putere']

    def iaPutereMaxima(self, profil):
        profil.sort(key=self.sorteazaDupaPutere, reverse=True)
        return profil[0]['putere'] * 4
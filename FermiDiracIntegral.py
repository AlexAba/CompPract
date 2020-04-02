from math import exp, gamma
from scipy import integrate
import numpy as np


class FermiDiracIntegral:
    @staticmethod
    def FermiFunction(Mu, Muf, j):
        if(Mu < Muf):
            return (Mu ** j) / (exp(Mu - Muf) + 1)
        else:
            return ((Mu ** j) * exp(Muf - Mu)) / (exp(Muf - Mu) + 1)

    @staticmethod
    def GetValue(j, Muf):
        if(j == -1):
            return FermiDiracIntegral.MinusOne(Muf)
        else:
            return FermiDiracIntegral.CommonIntegral(j, Muf)

    @staticmethod
    def MinusOne(x):
        return 1 / (exp(-x) + 1)

    @staticmethod
    def CommonIntegral(j, Muf):
        i, e = integrate.quad(
            FermiDiracIntegral.FermiFunction, 0, np.inf, args=(Muf, j))
        return 1 / (gamma(j + 1)) * i

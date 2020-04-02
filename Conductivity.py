import scipy.constants as const
from math import exp, gamma 
from FermiDiracIntegral import FermiDiracIntegral

class Conductivity:
    def __init__(self, type, temperature, L, r):
        self.elMob = type.elMob     #   Electron mobility
        self.q = const.e            #   Elementary charge    
        self.h = const.h            #   Planck's constant
        self.L = L                  #   Length
        self.T = temperature        #   Obviously
        self.r = r                  #   Roller scattering
        
        #   Mean free path
        self.MFP = (type.elMob * type.efMass * type.fermVel)/const.e  

    def Ballistic(self, range):
        ans = []
        for i in range:
            ans.append(2 * (self.q ** 2) * (FermiDiracIntegral.GetValue(-1, i)) / self.h)

        return ans

    def Difussion(self, range):
        ans = []
        for i in range:
            ans.append(2 * (self.q ** 2) / self.h * (self.MFP / self.L) * gamma(self.r + 1) * FermiDiracIntegral.GetValue(self.r - 1, i))

        return ans

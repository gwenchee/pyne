import numpy as np
from pyne.material import Material as m
from pyne import nucname
from scipy import constants as c

def test_decayheat(element): 
    """This function checks if decay is working correctly in pyne
    Input: 
    element: element name as a string ('u-235',etc.)
    halflife: half-life of element in years or seconds 
    time: type of timespan halflife was entered in 
    """
    original = m({element:1}) #1 gram
    decayheat = original.decay_heat()
    decayheat[nucname.id(element)]*= 10**6
    return decayheat #W

def calc_decayheat(E,halflife,molarmass):
    """This function gives the decay heat of an isotope
    Input: 
    E: decay energy in MeV 
    halflife: half life in years 
    molarmass: molar mass in g/mol
    """
    E_J = E * 1.60218*10**-13 #J
    lam = np.log(2)/(halflife*31556952) #/s
    A = lam*c.Avogadro
    decayheat = E_J*A/molarmass #W
    return decayheat #W

# Ag 108m 
print(test_decayheat('ag-108m'))
print(calc_decayheat(109.44*10**-3,418,108))
print(calc_decayheat(1.636,418,108))
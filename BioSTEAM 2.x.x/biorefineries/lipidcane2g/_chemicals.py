# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 06:42:02 2020

@author: yoelr
"""
from thermosteam import functional as fn
import thermosteam as tmo

__all__ = ('create_chemicals',)

def create_chemicals():
    from biorefineries import lipidcane as lc
    from biorefineries import cornstover as cs
    return tmo.Chemicals([*lc.chemicals, *cs.chemicals])
    

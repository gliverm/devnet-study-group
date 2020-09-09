# main.py

from sys import path

path.append('../packages')

from extra.iota import FunI
import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(FunI())
print(sig.FunS())
print(alp.FunA())
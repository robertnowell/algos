def findSpecialFactor(divisor):
   """for a certain divisor, find a factor of a product such that the number created 
      by removing first digit from the product will equal product/divisor.
      e.g. findSpecialDivisor(7) returns 5, because removing the first digit of 35 is 5, and 5*7=35"""
   for i in range(1, 1000):
     prod = i * factor
     if prod % findMod(prod) == i:
       return i

def findMod(i):
   mod = 1
   while (i/mod) > 10:
     mod *= 10
   return mod
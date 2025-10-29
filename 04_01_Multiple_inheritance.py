#here n = a will be the numerator
# and d = b will be the denominator
#div_mod class inherit both the division and modulus classes
class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d
      
class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)
   
nu = 10
di = 3
x=div_mod(nu,di)
print (f"{nu}/{di} = ",x.divide())
print (f"{nu}%{di} = ",x.mod_divide())
print (f"{nu}/{di} = {x.div_and_mod()[0]} and {nu}%{di} = {x.div_and_mod()[1]}")



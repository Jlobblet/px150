import math
m,s,x = 0,2,1
Gauss = math.exp(-0.5*((x-m)/s)**2)/(s*math.sqrt(2*math.pi))
print(Gauss)
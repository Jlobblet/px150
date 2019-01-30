from math import sqrt
coef = [1,-1.1,-7.26]
x1,x2 = (-coef[1]+sqrt(coef[1]**2-4*coef[0]*coef[2]))/2*coef[0],(-coef[1]-sqrt(coef[1]**2-4*coef[0]*coef[2]))/2*coef[0]
print(x1)
print(x2)
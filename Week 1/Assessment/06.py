import math
M,c,p,K,tw,ty = 67,3.7,1.038,5.4e-3,100,70

def time(t0):
    return (M**(2/3)*c*p**(1/3))/(K*(math.pi)**2*(4*math.pi/3)**(2/3))*math.log(0.76*(t0-tw)/(ty-tw))
    
print(time(4))
print(time(20))
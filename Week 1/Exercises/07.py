sides = [1,2,0.6]
errorABS = [0.04,0.04,0.06]
sumERROR = 0
volume = 1
for i in range(len(sides)):
    sumERROR = (errorABS[i]/sides[i])**2 + sumERROR
    volume = volume * sides[i]

print(volume)
print(volume*sumERROR**0.5)
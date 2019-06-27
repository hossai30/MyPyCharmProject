#Author: Sarah Hossain

import numpy as np
dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i ,"repetitions to get out of loop.")

for i in range(1,5):
    if (i!=2):
        print(i)


B = [1, 7, 5, 3, 2]
B.sort()
print(B)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]])
Z=np.dot(X,Y)
print(Z)
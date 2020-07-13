import numpy as np

#------------------------------------ QUIZ1 ------------------------------------
x = np.zeros(10)
print(x)
x = np.zeros((4,4))
print(x)
#------------------------------------ QUIZ2 ------------------------------------
x = np.full(5,1)
print(x)
x = np.full((3,3),1)
print(x)
#------------------------------------ QUIZ3 ------------------------------------
x = np.random.uniform(10,100,20)
print(x)
x = x**2
print(x)
#------------------------------------ QUIZ4 ------------------------------------
import random
x = []
for i in range(20):
    r = random.uniform(10,100)
    x.append(r)
print(x)

out = [x**2 for x in x]
print(out)
#------------------------------------ QUIZ5 ------------------------------------
import time
x = np.random.uniform(10,100,20)
time1 = time.time()
print(time1)
x = x**2
time2 = time.time()
print(time2)
print("dif time case 1 =",time2-time1)

import random
x = []
for i in range(20):
    r = random.uniform(10,100)
    x.append(r)
time1 = time.time()
print(time1)
out = [x**2 for x in x]
time2 = time.time()
print(time2)
print("dif time case 2 =",time2-time1)
#------------------------------------ QUIZ6 ------------------------------------
x = np.arange(10,1001)
print(x)
#------------------------------------ QUIZ7 ------------------------------------
x = np.arange(10,2002,2)
print(x)
#------------------------------------ QUIZ8 ------------------------------------
x = np.arange(12,901)
x = x[x%2==1]
print(x)
#------------------------------------ QUIZ9 ------------------------------------
x = np.eye(4,4)
print(x)
#------------------------------------ QUIZ10 ------------------------------------
x = np.linspace(5,25,100)
print(x)
#------------------------------------ QUIZ11 ------------------------------------
x = np.random.rand()
print(x)
#------------------------------------ QUIZ12 ------------------------------------
x = np.random.randint(50,101,(4,4))
print(x)
x = x.transpose()
print("----------------------")
print(x)
#------------------------------------ QUIZ13 ------------------------------------
x = np.arange(1,26)
x = x.reshape(5,5)
out = [x[1,2],x[1,3],x[2,2],x[2,3]]
print(out)
#------------------------------------ QUIZ14 ------------------------------------
x = np.arange(1,26)
x = x.reshape(5,5)

out = [x[3,2],x[3,3],x[3,4]]
print(out)
#------------------------------------ QUIZ15 ------------------------------------
x = np.arange(1,26)
x = x.reshape(5,5)

out = [x[3,0],x[3,1],x[4,0],x[4,1]]
print(out)
#------------------------------------ QUIZ16 ------------------------------------
x = np.arange(1,26)
x = x.reshape(5,5)

out = x[2,:]
print(out)
#------------------------------------ QUIZ17 ------------------------------------
x = np.arange(1,26)
x = x.reshape(5,5)
#------------------------------------ QUIZ18 ------------------------------------
x = np.random.randint(10,101,(5,5))
print(x)
x = x.reshape(25)
print(x)
for i in x:
    if(i>50):
        print(i)
#------------------------------------ QUIZ19 ------------------------------------
x = np.random.randint(10,101,(5,5))
print(x)
x2 = x[x>40]
print(x2)
#------------------------------------ QUIZ20 ------------------------------------
cnt = 0
out = np.array([])
while cnt < 9:
    print("input ",cnt+1)
    x = int(input())
    if(x in out):
        continue
    if(x >= 10 and x <= 100):
        out = np.append(out,x)
        cnt += 1
print(out)
out = out.reshape(3,3)
print(out)
out = out.transpose()
print(out)
print(out[2][2])

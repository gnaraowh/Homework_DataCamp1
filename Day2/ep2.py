#------------------------------------ QUIZ1 ------------------------------------
input1 = int(input())
if(input1 == 0):
    print("เลขศูนย์")
elif(input1%2):
    print("เลขคี่")
else:
    print("เลขคู่")

#------------------------------------ QUIZ2 ------------------------------------
input1 = float(input())
input2 = float(input())
while(not bool(input2)):
    input2 = float(input())

print(input1/input2)

#------------------------------------ QUIZ3 ------------------------------------
cnt = 0
input1 = float(input())
total = 0
while(bool(input1)):
    total += input1
    cnt += 1
    input1 = float(input())
print(total/cnt)

#------------------------------------ QUIZ4 ------------------------------------
if(int(input())%7):
    print("หาร 7 ไม่ลงตัว")
else:
    print("หาร 7 ลงตัว")

#------------------------------------ QUIZ5 ------------------------------------
# จากโจทย์ ไม่ได้ระบุว่า ตัวแปลใดคือ ด้านตรงข้ามมุมฉาก หรือ ชิดฉาก แสดงว่า a หรือ b หรือ c เป็นด้านตรงข้ามมุมฉากได้
# หากเอาตัวแปลโดดๆ มาประกอบกันเหมือนเอาไม้ไผ่ 3 ท่อนมาทำสามเหลี่ยม ถ้าค่าที่ได้ลงตามกฎ จะเป็นรูปมุมฉากเอง จึงเขียนไว้ 3 เคส
a,b,c = float(input()),float(input()),float(input())
if( ( (a**2)+(b**2)) == (c**2) ):
    print("สร้าง 3 เหลี่ยมมุมฉากได้")
elif( ( (a**2)+(c**2)) == (b**2) ):
    print("สร้าง 3 เหลี่ยมมุมฉากได้")
elif( ( (c**2)+(b**2)) == (a**2) ):
    print("สร้าง 3 เหลี่ยมมุมฉากได้")
else:
    print("สร้าง ไม่ได้")

#------------------------------------ QUIZ6 ------------------------------------
a,b,c = float(input()),float(input()),float(input())
if( ( (a**2)+(b**2)) == (c**2) ):
    print("สร้าง 3 เหลี่ยมมุมฉากได้")
elif( ( (a**2)+(c**2)) == (b**2) ):
    print("สร้าง 3 เหลี่ยมมุมฉากได้")
elif( ( (c**2)+(b**2)) == (a**2) ):
    print("สร้าง 3 เหลี่ยมมุมฉากได้")
elif( ( (a**2)+(b**2)) < (c**2) ):
    print("สร้าง 3 เหลี่ยมมุมป้านได้")
elif( ( (a**2)+(c**2)) < (b**2) ):
    print("สร้าง 3 เหลี่ยมมุมป้านได้")
elif( ( (c**2)+(b**2)) < (a**2) ):
    print("สร้าง 3 เหลี่ยมมุมป้านได้")
elif( ( (a**2)+(b**2)) > (c**2) ):
    print("สร้าง 3 เหลี่ยมมุมแหลมได้")
elif( ( (a**2)+(c**2)) > (b**2) ):
    print("สร้าง 3 เหลี่ยมมุมแหลมได้")
elif( ( (c**2)+(b**2)) > (a**2) ):
    print("สร้าง 3 เหลี่ยมมุมแหลมได้")

#------------------------------------ QUIZ7 ------------------------------------
total = 0
cnt = 0
while(cnt != 3):
    pay = float(input())
    if(pay < 1000 or pay > 6000):
        continue
    else:
        cnt += 1
        total += pay

if(total > 12000):
    total = total*0.75
elif(total > 6000):
    total = total*0.85

print(total)

#------------------------------------ QUIZ8 ------------------------------------
total = 0
cnt = 0
last = 0
while(cnt != 4):
    pay = float(input())
    if(pay < 1000 or pay > 5000):
        continue
    else:
        cnt += 1
        total += pay
        last = pay
if(total-last > 12000):
    last = last*0.75
elif(total-last > 6000):
    last = last*0.85

print("จ่าย มื้อที่ 4 = ",last)

#------------------------------------ QUIZ9 ------------------------------------
total = 0
cnt = 0
last = 0
while(cnt != 4):
    pay = float(input())
    if(pay < 1000 or pay > 5000):
        continue
    else:
        cnt += 1
        total += pay
        last = pay
if(total-last > 9000):
    last = last*0.7
elif(total-last > 4000):
    last = last*0.75

print("จ่าย มื้อที่ 4 = ",last)

#------------------------------------ QUIZ10 ------------------------------------
total = 0
cnt = 0
last = 0
while(cnt != 4):
    pay = float(input())
    if(pay < 1000 or pay > 5000):
        continue
    else:
        cnt += 1
        total += pay
        last = pay
print("มี บัตรเครดิต หรือไม่ 0/1 = ")
card = float(bool(input()))*0.05
print(card)
if(total-last > 9000):
    last = last*(0.7-card)
elif(total-last > 4000):
    last = last*(0.75-card)

print("จ่าย มื้อที่ 4 = ",last)

#------------------------------------ QUIZ11 ------------------------------------
str = input()
out = ""
if(len(str) >= 7):
    for i in str:
        print(ord(i))
        if(ord(i) >= 65 and ord(i) <= 90):
            out += i.lower()
        elif(ord(i) >= 97 and ord(i) <= 122):
            out += i.upper()  
    print(out) 
else:
    print("ต้องใส่อักษรมากกว่า 7 ตัว")
    
#------------------------------------ QUIZ12 ------------------------------------
a,b,c,d = input(),input(),input(),input()
lst = [a,b,c,d]
dic = {}
for i in lst:
    dic[i] = len(i)
print(sorted(dic.items(), key = lambda kv: (kv[1],kv[0]), reverse=True))

#------------------------------------ QUIZ13 ------------------------------------
inp1,inp2 = -1,-1
while inp1 < 0 or inp1 > 60:
    print("input Hour:")
    inp1 = int(input())
while inp2 < 0 or inp2 > 60:
    print("input Minute:")
    inp2 = int(input())
print("Time is {}:{}".format(inp1,inp2))
pay = (inp1*150+inp2*2)
print("Pay = ",pay)

#------------------------------------ QUIZ14 ------------------------------------
inp1,inp2 = -1,-1
while inp1 < 0 or inp1 > 60:
    print("input Hour:")
    inp1 = int(input())
while inp2 < 0 or inp2 > 60:
    print("input Minute:")
    inp2 = int(input())
print("Time is {}:{}".format(inp1,inp2))
if(inp2 > 15):
     inp1+=1
inp1-=1
pay = (inp1*300)
print("Pay = ",pay)

#------------------------------------ QUIZ15 ------------------------------------
print("Sum Head = ")
sumHead = int(input())
print("Sum Leg = ")
sumLeg = int(input())

ratio = sumHead/sumLeg

while(ratio < 0.25 or ratio > 0.5 or sumLeg%2 != 0):
    print("Sum Leg {} = ".format(ratio))
    sumLeg = int(input())
    ratio = sumHead/sumLeg
print("ratio => ", ratio)
print("Sum of Head:Leg {}:{}".format(sumHead, sumLeg))

def payTax(head,leg):
    numCow = 0
    numBird = 0

    leftLeg = leg%4 
    numCow = leg//4 
    numBird = head-numCow 
    
    if(leftLeg or numBird):
        if(numBird*2 > leftLeg):
            numCow -= 1
            leftLeg += 4
    numBird = leftLeg//2

    tax = (numCow*220) + (numBird*150)
    print("numCow:numBird {}:{}".format(numCow,numBird))
    return tax

print("Pay Tax for ",payTax(sumHead,sumLeg))
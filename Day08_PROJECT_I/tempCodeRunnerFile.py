# --------------------------------------- Quiz1 ---------------------------------------#
cnt = 0
sum = 0
while True:
    try:
        inp = float(input())
        if inp == 0.0:
            break
        sum += inp
        cnt += 1
    except Exception as e:
        print("Please input Number not String")
mean = sum/cnt
print("Mean= ", mean)
print("Result= ",mean*cnt)
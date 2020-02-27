# #QUIZ1
# q1 = (2345%13)
# q2 = 1567//17
# print(q1)
# print(q2)
# print("Q: Is FirstName Equal Firstname ")
# print("A: Not Equal")
# print("Q: Is 13Friday is valid value")
# print("A: Not Valid value")
# print("{}, {}".format(q1,q2))

# #QUIZ2
# f1 = lambda x: x/3
# print(f1(3))

# def f2(a,b,c,d) :
#     result = (a+b+c+d)/4
#     return result
# print(f2(1,2,3,4))

# f3 = lambda a,b,c: (a+b+c)/3
# print(f3(1,2,3))

# #QUIZ3
# myself = ["Tanawat", "Saitin", 34]
# print(myself)
# del (myself[2])
# print(myself)
# myself.insert(0, 24)
# print(myself)
# myself.append(73)
# myself.append(176)
# print(myself)
# print(myself[2:])

# #QUIZ4
# a = [
#         [
#             [1,3] , [3,4]
#         ] , 
#         [
#             5 , [5,6] , [7,8]
#         ]
#     ]
# print(a[1][1][1])

# name1 = ["fname1","lname1",10]
# name2 = ["fname2","lname2",20]
# name3 = ["fname3","lname3",30]
# name4 = ["fname4","lname4",40]
# name_all = [name1, name2, name3, name4]
# print(name_all)
# del name_all[3]
# print(name_all)
# name5 = ["fname5","lname5"]
# name_all.insert(0,name5)
# print(name_all)
# name_all[1][2] += 10
# print(name_all)

# #QUIZ5
# lst = [1,2,3,4,5,6,7,8,9,10]
# pow3_q1_1 = lambda x: pow(x,3)
# print(list(map(pow3_q1_1,lst)))

# def pow3_q1_2(x):
#     return pow(x,3)
# print(list(map(pow3_q1_2,lst)))

# pow3_q2_1 = filter(lambda x: pow(x,2)%2 != 0 , lst)
# print(list((pow3_q2_1)))

# def pow3_q2_2(x):
#     return pow(x,2)%2 != 0
# print(list(filter(pow3_q2_2,lst)))

# #QUIZ6
# lst = [1,2,3,4,5]
# lst2 = [(x*2)-1 for x in lst]
# print(lst2)

# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# lst3 = [pow(x,3) for x in lst if x%3 != 0]
# print(lst3)

#QUIZ7
def grade(x):
    if(x > 80): return 'A'
    elif(x > 70): return 'B'
    elif(x > 60): return 'C'
    elif(x >= 50): return 'D'
    else: return 'F'
print(grade(50)) 

lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]
result = map(lambda x, y: x+y,lst1,lst2)
print(list(result))
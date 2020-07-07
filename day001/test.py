# a = 1
# b = 6
# c = a+b
# print(c)

# a=66
# if(a>0 and a<=59):
#     print("不及格")
# elif(a>=60 and a<=70):
#     print("及格")
# elif(a>=71 and a<=80):
#     print("良好")
# elif(a>=81 and a<=100):
#     print("优秀")
# else:


# a=[1,2,3,4,5,6,7]
# for i in a:
#     print(i)

# for i in range(10):
#     print(i)


# for i in range(2,10,1):
# 	print(i)
# for i in range(10,1,-1):
#     print(i)

# for i in range(100):
#     print(i)
# s = 0
# for i in range(100):
#     s = s + i
# print(s)

# i=0
# while i < 5:
#     print(i)
#     i += 1
# a = 1
# for i in range(10,0,-1):
#    a = a * i
# print(a)

 # 九九乘法表
#
# for i in range(1,10):
#    print(i)
#    for j in range (1,i+1):
#     print(j,"x",i,"=",j*i,end="\t")
# print()


#冒泡循环
w = [2,5,9,45,14]
lenth = len(w)
# print(lenth)
for i in range(lenth-1,0,-1):
   # print(i)
   for j in range(i):
      if w[j] > w[j+1]:
        w[j],w[j+1] = w[j+1],w[j]

print(w)
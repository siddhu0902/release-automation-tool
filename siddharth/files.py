#Q1.
# a=open("sample.txt","r")
# print(a.read())

#Q2.
#a = open("sample.txt","r")
# b = open("sample.txt","w")
# print(a.read())

# for i in (a.readlines(1)):
#     print(a)

#for i in range(0,6):
#    print(a.readline())
    
#a.close()
# b.close()

#Q3.
# a = open("sample.txt","r")
# print(a.read())
# for i in a.readlines(5):
#     print(a.readline())
# a.close()

#Q4.
# a = open("sample.txt","r")
# b = open("hi.txt","w")
# for i in a.read():
#     b.write(i)
# b.close()

#Q5.
# a = open("sample.txt","r")
# b = 0
# c = a.read()
# for i in c.split():
#     b+=1
# print(b)
# a.close()

#Q6. 
# a = open("num_1.txt","r")
# b = open("num_1.txt","w")
# c=0
# for i in a.read():
#     x = int(i)
#     c+=x
# print(c)
# a.close()
# b.close()

#Q7.
a = open("num_1.txt","r")
b =open("odd.txt","w")
c = open("even.txt","w")
s = a.read()
l = len(s)
for i in range(l):
    f = int(s(i))
    if f%2==0:
        c.write(str(f))
    else:
        b.write(str(f))
a.close()
b.close()
c.close()

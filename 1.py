#comment 
if 5<2:
    print("hi")
x=5
y="hi"

#variables -------------------------------------------
a=str(9)
b=int(5)
c=float(3)
d=type(5) #type - shows data type 
print(type(a))
e,f,g = 1,2,3
q = w = r = '12'
fruits = "apple", "mango", 'banana' #array

#datatypes ---------------------------------------------

#string, int, float 
#list[] - mutable, tuple(), set{}
#bool - true/false 
#complex - lj
list = [1,2,3]
tuple = 1,2,3
u = range(6)
i = {"name" : "max", "age" : "21"} #dict 

#random ------------------------------------------------
import random
print(random.randrange(1,10))


#String -------------------------------------------------
o='''hhhhhhhhognoq'eurbg'orubg'rgb'reobgu'''
p = "Hello, World!"
print(p[1])
#looping through string 
for s in "banana":
  print(s)

print(len(p))

#checking
txt = "The best things in life are free!"
print("free" in txt) #not in ...

#slicing 
h = "Hello, World!"
print(h[2:5]) #print(h[:5]) - from the start / print(h[5:]) - from the end 
print(h[-5:-2])
print(h.upper())
print(h.lower())
print(h.strip()) #remove whitespace 
print(h.replace("H", "J"))
print(h.split(","))
j = "hello"
k = ' max'
l=j+k
print(l)
print(type(list))




if __name__ == '__main__':
    n = int(input())
    
def printString(n):
    for i in range(1,n+1):
          print(i, end='')
printString(n)
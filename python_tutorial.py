#odd and even numbers 
'''
num % 2 == 0 even
num % 2 != 0 odd
'''
#to print the number of lines 
n=5
def something(n):
    for i in range(1, n+1):
        print(i, end="")
#something(5)
"""
arr=[1,2,5,4,3,5]
newarr=sorted(set(arr)) #set method removes duplicates 
print(newarr)
"""

"""
something = "Maksim Rashchupkin 21 2002 1 20 40"
fname, lname, age, dob, *randomlist = something.split(" ")
scores = list(map(int, randomlist))
print(fname + "," + randomlist[1])


def calc_average_score():
    total_scores = sum(scores)
    average_score = total_scores/len(scores)
    print(average_score)

calc_average_score()
"""

"""
x=1
y=2
z=3
cordinates = [[l,m,f] for l in range(x+1) for m in range(y+1) for f in range(z+1)]
print(cordinates)
"""

"""students = []
for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])

grades = sorted(set([student[1] for student in students]))
second_lowest_grade = grades[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
print(second_lowest_students)"""

"""if __name__ == '__main__':
    N = int(input())
    
list=[]
for _ in range(N):
        command = input().split()
        
        if command[0] == "insert":
            index = int(command[1])
            value = int(command[2])
            list.insert(index, value)
        elif command[0] == "print":
            print(list)
        elif command[0] == "remove":
            value = int(command[1])
            list.remove(value)
        elif command[0] == "append":
            value = int(command[1])
            list.append(value)
        elif command[0] == "sort":
            list.sort()
        elif command[0] == "pop":
            list.pop()
        elif command[0] == "reverse":
            list.reverse()"""

"""m = int(input())
llist=[]
for _ in range(m):
    command = input().split()

    if command[0] == "insert":
        llist.insert(int(command[1]), int(command[2]))
        print(command)
    elif command[0] == "print":
        print(llist)
    else:
        print("error")"""
    

"""n = int(input())
t = tuple(map(int,input().split()))
x=hash(t)
print(x)"""

""""def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)"""

"""def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    return ''.join(string_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)"""


"""string = "12312345123"
sstring = "6"
count = 0
for i in range(len(string)-len(sstring)+1):
    if string[i:i + len(sstring)] == sstring:
        count +=1
print(count)"""
    

"""st = "maksim rashchupkin"
newst = st.split()
newst[0] = newst[0].capitalize()
newst[1] = newst[1].capitalize()
c = " ".join(newst)
print(c)"""

"""split_string = s.split()
    while split_string[0].isalpha and split_string[1].isalpha:
        split_string[0] = split_string[0].capitalize()
        split_string[1] = split_string[1].capitalize()
        x = " ".join(split_string)
        return x"""



"""def solve(s):
    while all(i.isalpha() or i.isspace() for i in s):
        capitalized_string = s.title()
        print(capitalized_string)
        break

solve("maksim rashchupkin ")"""

"""a = input().split()
b = input().split()
c = input().split()
d = input().split()

blist = set(map(int, b))
dlist = set(map(int, d))

combined = blist.symmetric_difference(dlist) 

for i in combined:
    print(i)"""
    
v = {4,5,6}
l = input().split()
l = set(map(int, l))
l |= v
print(l)
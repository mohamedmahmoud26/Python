#ASS1
# Input
from operator import index

num = int(input("Enter The number:"))
a=0
if num>0:
    while num >1:
        num -=1
        if num == 6:
            continue
        print(num)
        a+=1
    print(f"{a} printed succ")
else:
    print(f"Number {num} is Not larger than 0")
# Needed Output
#"Number 0 Is Not Larger Than 0"
#ASS2
# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
index=0
my_fname=0
while index<len(friends):
    if  friends[index].islower():
        index+=1
        my_fname+=1
    else:
        print(friends[index])
        index+=1
else:
    print(f"friends printed and my_fname count is {my_fname} ")
# Needed Output
#"Mohamed"
#"Shady"
#"Sherif"
#"Friends Printed And Ignored Names Count Is 2"
#ASS3
# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop())
# Type The Code Here in One Line
# Needed Output
#"HTML"
#"CSS"
#"JavaScript"
#"PHP"
#"Python"
#ASS4
# Input
#name = "OSAMA"
# Input
#name = "osama"
# Input
#name = "Ahmed"
#ass4
friends=[]
maxf=4
while maxf > 0:
    name=input("Please  Enter The name:")
    if name.isupper():
        print("invaild name")
    elif name.islower():
        friends.append(name.capitalize())
        maxf -= 1
        print(f"friends{name} added 1st letter become capital")
        print(f"names left in list is {maxf}")
    else:
        friends.append(name)
        maxf -=1
        print(f"friends {name} added ")
        print(f"names left in list is {maxf}")
else:
    print(friends)




# Needed Output
#"Friend Ahmed Added"
#"Names Left in List Is 2"
# Needed Output
#"Friend osama Added => 1st Letter Become Capital"
#"Names Left in List Is 3"
# Needed Output
#"Invalid Name"
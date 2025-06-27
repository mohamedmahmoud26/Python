# ASS 1
# Tests
from xml.sax.handler import property_interning_dict


def calculate(n1 , n2 , operation = " add"):
    operation=operation.lower()
    if operation in ["a" , "add"]:
        print(n1 + n2)
    elif operation in ["s" , "subtract"]:
        print(n1-n2)
    elif operation in ["m" , "multiply"]:
        print(n1 *n2)
    else:
        print("is not vaild")
calculate(10, 20) #30
calculate(10, 20, "AdD") # 30
calculate(10, 20, "a")# 30
calculate(10, 20, "A")# 30
calculate(10, 20, "S") # -10
calculate(10, 20, "subTRACT") # -10
calculate(10, 20, "Multiply") # 200
calculate(10, 20, "m") # 200
# ASS2
# Test
def addition(*additions):
    sum=0
    for num in additions:
        if num==10:
            continue
        elif num ==5:
            sum-=num
        else:
            sum+=num
    print(sum)
addition(10, 20, 30, 10, 15) # 65
addition(10, 20, 30, 10, 15, 5, 100) # 160
#ASS 3
# Input
def show_skills( name,*skills):
    if len(skills)>0:
        print(f"Hello {name} Your Skills Is")
        for skill in skills:
            print(f"- {skill}")
    else:
        print(f"Hello {name} You Have to skills to show")
show_skills("Osama", "HTML", "CSS", "JS", "Python")
# Output
#"Hello Osama Your Skills Is"
#"- HTML"
#"- CSS"
#"- JS"
#"- Python"
#ASS 4
# Input
def say_hello(name , age , country="unknown"):
    print(f"Hello {name} Your Age Is {age} And You Live In {country} ")

print(say_hello("Osama", 38, "Egypt"))

# Output
#"Hello Osama Your Age Is 38 And You Live In Egypt"

#ASS1
name="Osama",
print(name)
print(type(name))
# Needed Output
# "Osama"
# <class 'tuple'>
#ASS2
friends = ("Osama", "Ahmed", "Sayed")
print(len(friends))
print(type(friends))
x=list(friends)
x[0]= "Elzero"
a=tuple(x)
print(a)
# Needed Output
# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
#ASS3
nums = (1, 2, 3)
letters = ("A", "B", "C")
r=nums+letters
print(r)
print(len(r))
# Needed Output
# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements
#ASS4
my_tuple = (1, 2, 3, 4)
for num in my_tuple:
    if num==3:
        continue
    print(num)
# Needed Output
# 1
# 2
# 4
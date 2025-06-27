#ASS1
from os import remove

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list=set([])
unique_list.update(my_list)
print(unique_list)
unique_list= list (unique_list)
print(type(unique_list))
unique_list.remove(5)
print(unique_list)
# Needed Output
# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4
#ASS2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums|letters)
print(nums.union(letters))
nums.update(letters)
print(nums)
# Needed Output
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
#ASS3
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
# Needed Output
# {1, 2, 3}
# set()
my_set.update(['A' , 'B'])
print(my_set)
letters.discard("c")
# {"A", "B"}
#ASS4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issuperset(set_one))
print(set_two.issuperset(set_two))
# Needed Output
#True
#ASS5
# Create Dictionary Here
lang={
    "One":{
        "name":"HTML",
        "progress":"90%"
    },
    "Two":{
        "name":"CSS",
        "progress":"30%"
    },
    "Three":{
        "name":"Python",
        "progress":"20%"
    },
    "Four":{
        "name":"C+",
        "progress":"77%"
    }
}
print(lang)
# Needed Output
#"HTML Progress Is 90%"
#"CSS Progress Is 80%"
#"Python Progress Is 30%"
#"AI Progress Is 20%"
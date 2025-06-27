#ASS1
from string import printable


def get_score(**skill):
    for skill , vaule in skill.items():
        print(f"{skill} => {vaule}")
# Tests1
get_score(Math=90, Science=80, Language=70)

def get_score(**skill):
    for skill , vaule in skill.items():
        print(f"{skill} => {vaule}")
# Tests2
get_score(Logic=70, Problems=60)

#ASS 2
# Test 1
def get_people_scores(name , **skills):
   print(f"\"Hello {name} This Is Your Score Table:\"")
   for skill , vaule in skills.items():
        print(f"{skill} => {vaule}")
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
def get_people_scores(name , **skills):
   print(f"\"Hello {name} This Is Your Score Table:\"")
   for skill , vaule in skills.items():
       print(f"{skill} => {vaule}")

get_people_scores("Mahmoud", Logic=70, Problems=60)
# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

# Test 3
def get_people_scores(**skills):
   for skill , vaule in skills.items():
       print(f"{skill} => {vaule}")
get_people_scores(Logic=70, Problems=60)
# Output
"Logic => 70"
"Problems => 60"

# Test 4
def get_people_scores(name):
    print(f"\"Hello Ahmed You Have No Scores To Show\" ")
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"
#ASS 3
# Test 1
scores_list={
    "math":"90",
    "Science":"80",
    "Language":"70"
}
def get_the_scores(name ,**scores_list):
    print(f"\"Hello {name} This Is Your Score Table\": ")
    for skill , vaule in   scores_list.items():
        print(f"s{skill} => {vaule}")
get_the_scores("Osama", **scores_list)
# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"
# Test 2
def get_people_scores(name):
    print(f"\"Hello {name} You Have No Scores To Show\" ")
get_the_scores("Osama")

# Output
"Hello Osama You Have No Scores To Show"

# Test 3
scores_list={
    "math":"90",
    "Science":"80",
    "Language":"70"
}
def get_the_scores(**scores_list):
    for skill , vaule in   scores_list.items():
        print(f"s{skill} => {vaule}")
get_the_scores(**scores_list)
# Output
"Math => 90"
"Science => 80"
"Language => 70"
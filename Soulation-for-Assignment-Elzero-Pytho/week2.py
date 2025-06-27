#ASS1
name="'osama'"
age=38
country="Egypt"
print(f"\" Hello {name} , How You Doing \\ \"\"\" Your Age Is  \"{age}\"\" + And Your Country Is :{country} ")
#output
#"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
#Ass2
print(f"\" Hello {name} , How You Doing \\ \n \"\"\" Your Age Is  \"{age}\"\" +  \n And Your Country Is :{country} ")
#output
#"Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt
#ASS3
name = 'Elzero'
print("Second Letter Is "+  name[ 1 ])
print("Third Letter Is " + name[2])
print("Last Letter Is " + name[5])
# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
#ASS4
name = 'Elzero'
print(name[1:4])
print(name[0:5:2])
print(name[4::-2])
# Needed Output
# "lze"
# "Ezr"
# "rzE"
#ASS5
name = "#@#@Elzero#@#@"
print(name.strip("#@"))
# Needed Output
# Elzero
#ASS6
num1= "9"
num2= "15"
num3= "130"
num4= "950"
num5= "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500
#ASS7
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20 , "@"))
print(name_two.rjust(20 , "@"))
# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero
#ASS8
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
# Needed Output
# osAMa
# OSAma
#ASS9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
# Needed Output
# 2
#ASS10
name = "Elzero"
print(name.index("z"))
# Needed Output
# 2
#ASS11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3" , "love" , 1))
# Needed Output
# I Love Python And Although <3 Elzero Web School
#ASS12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3" , "love" ))
#ASS13
name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country} ")
# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
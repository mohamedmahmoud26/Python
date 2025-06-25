# ⚠️ IMPORTANT: Make sure to check the notes file in the main repository directory. It contains crucial information!


# -formating
# two way
# %s => string
# %d => number
# %f => float 

# --> Format in old way
name= 'Mohamed Elseragy'
age=22
rank= 10
print("my name is %s and my age is %d and my rank %.2f " %(name , age , rank))


# --> Format in new way
# {:s} ---> string
# {:d} ---> number
# {:f} ---> float
print('Ful name is: {} {} {}'.format('Mohamed', 'Mahmoud', 'Elseragy'))  
# Using format() to insert values into placeholders

print("Ful name is: {:.2s} {}".format('Mohamed', 'Mahmoud'))  
# Prints only the first 2 characters of 'Mohamed'

print('Ful name is: {f_name} {s_name} {l_name}'.format(f_name='Mohamed', s_name='Mahmoud', l_name='Elseragy'))  
# Using named placeholders in format()

nu = 10.2335261
print("Number: {n:2.5f}".format(n=nu))  
# Formats the float number with 5 digits after the decimal
num=12562165
print('my number is {:,d}'.format(num))
name = "Mohamed Mahmoud Elseragy"
country = 'Egypt'
age = 22
print(f'{name} is from {country} and he is {age} years old')
# f-string: inserts variables directly into the string
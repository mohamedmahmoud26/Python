# ⚠️ IMPORTANT: Make sure to check the notes file in the main repository directory. It contains crucial information!


# - Single quotes = Double quotes
print('Hello, World!')
print("Hello, World!")
# Both single and double quotes can be used for strings
# - \n
print("Hello, I\'m Mohamed Elseragy.\n My Age is 22")
# Using \ to escape characters, \n adds a new line

# - \t
print("Hello, I\'m Mohamed Elseragy.\t My Age is 22")
# \t adds a horizontal tab (space)

# - len()
Country = 'Egypt'
print(len(Country))  # 5
# len() returns the number of characters in the string

# - Index
full_name = 'Mohamed Mahmoud Elseragy'
print(full_name[0])  
# Prints the first character → M

print(full_name[-2])  
# Prints the second-to-last character → g

print(full_name[10])  
# Prints the character at index 10 → h

# - Slicing
full_name = 'Mohamed Mahmoud Elseragy'
print(full_name[0:8])  
# Slices from index 0 to 7 → 'Mohamed '

print(full_name[0:8:2])  
# Slices from index 0 to 7 with a step of 2 → 'Mhmd'

print(full_name[:25])  
# Slices from start to index 24 → 'Mohamed Mahmoud Elseragy'

print(full_name[7:])  
# Slices from index 7 to the end → 'Mahmoud Elseragy'

print(full_name[::-1])  
# Reverses the string

print(full_name[::-2])  
# Reverses the string with a step of 2

name = 'Mohamed Elseragy'
print("Hello, I'm " + name)
# Concatenates strings using +

part_name = name[:2]
print(part_name + " " + "Mahmoud")  
# Takes the first two letters and adds 'Mahmoud' → 'Mo Mahmoud'

x = name * 2
y = x[0:8]
print(x)
# Repeats the name twice

print(y)
# Prints the first 8 characters of the repeated string

# -Upper
string = 'Welcome to Egypt'
print(string.upper()) 
# Converts all characters to uppercase

# - lower
print(string.lower()) 
# Converts all characters to lowercase

# - split
print(string.split())
# Splits the string into a list of words

# - zfill
c, d, e = 10, 20, 30
print(str(c).zfill(10))  # Pads the number with zeros on the left to make the total length 10

# - rjust
name = 'Mohamed Mahmoud'
print(name.rjust(10, "#"))  # Right-justifies the string in a field of width 10, padding with '#'

# - replace
name = '-Mohamed Mahmoud'
print(name.replace('-', ''))  # Replaces all occurrences of '-' with an empty string

# - title 
name = 'Mohamed Mahmoud'
print(name.title())  # Capitalizes the first letter of each word in the string

# - strip
name = '          Mohamed Mahmoud         '
print(name.strip())  # Removes any leading and trailing whitespace from the string




print('Ful name is: {} {} {}'.format('Mohamed', 'Mahmoud', 'Elseragy'))  
# Using format() to insert values into placeholders

print("Ful name is: {:.2s} {}".format('Mohamed', 'Mahmoud'))  
# Prints only the first 2 characters of 'Mohamed'

print('Ful name is: {f_name} {s_name} {l_name}'.format(f_name='Mohamed', s_name='Mahmoud', l_name='Elseragy'))  
# Using named placeholders in format()

nu = 10.2335261
print("Number: {n:2.5f}".format(n=nu))  
# Formats the float number with 5 digits after the decimal

name = "Mohamed Mahmoud Elseragy"
country = 'Egypt'
age = 22
print(f'{name} is from {country} and he is {age} years old')
# f-string: inserts variables directly into the string



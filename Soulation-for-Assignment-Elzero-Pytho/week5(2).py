#ASS1
# Input
"     osAmA   "
name=input('What\'s Is Your Name:')
name=name.strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")
# Needed Output
#"Hello Osama, Happy To See You Here."
#ASS2
# Inputs

16 # Input One
24 # Input Two
Age=int(input('What\'s Is Your Age:'))
if Age<16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print("Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You")
# Needed Output
#"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
#"Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+
#ASS3
# Inputs

"Osama" # First Name
"Mohamed" # Second Name
Fname=input('What\'s Is Your Name:')
Lname=input('What\'s Is Your Name:')
Fname=Fname.strip().capitalize()
Lname=Lname.strip().upper()
print(f"Hello {Fname} {Lname:.1}")
# Needed Output
#"Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."
#ASS4
# Inputs

#"mohamedmahmoud2682003@gamil.com" # Email
email = str(input('Enter your personal mail : ')).strip().lower()
user_name = email[:email.index('@')]
site = email[email.index('@') + 1: email.index(".c")]
# how to get top domain
second_part = email[email.index('@') + 1:]
domain = second_part[second_part.index('.') + 1:]

print(f"Hello {user_name.capitalize()} in my program")
print(f"Email Service Provider Is >> {site}")
print(f'Top Level Domain Is >> {domain}')
# Needed Output
#"Your Name Is Osama"
#"Email Service Provider Is nn"
#"Top Level Domain Is sa"
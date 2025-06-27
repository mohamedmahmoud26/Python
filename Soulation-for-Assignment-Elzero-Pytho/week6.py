#ASS1
# Inputs

num1 =int(input("what\'s Your Frist Number:"))
num2 =int(input("what\'s Your Sec Number:"))
operation=input("What\'s Your The Operation:")
#operation = "+" Or "-" Or "*" Or "/" Or "%"
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "%":
    print(num1%num2)
elif operation == "/":
    print(num1/num2)
# Needed Output
# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800
#ASS2
age =int(input("How Old Are You:"))
if age >16:
    print("App Is Suitable For You")
else:
    print("App Is Not Suitable For You")
# Needed Output
"App Is Suitable For You" # If Age Larger Than 16
"App Is Not Suitable For You" # if Age Smaller Than 16
#ASS3
age =int(input("How Old Are You:"))
if age >10 and age <100:
    months=age *12
    weeks=months*4
    days=age*365
    hours=days*24
    min=hours*60
    print(f"Your Age In months Is {months} months")
    print(f"Your Age In weeks Is {weeks} weeks")
    print(f"Your Age In days Is {days} days")
    print(f"Your Age In hours Is {hours} hours")
    print(f"Your Age In minutes Is {min} months")
else:
    print('This out of range')
# Needed Output
#"Your Age In Months Is 456 Months" # Months Example
#"Your Age In Weeks Is 1824 Weeks" # Weeks Example

#ASS4
# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country")
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is: ${price-discount}")
else:
    print(f'Your Country Not Eligible For Discount And The Price Is ${price}')
# Needed Output
#"Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
#"Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example

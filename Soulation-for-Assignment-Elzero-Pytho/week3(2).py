#ASS1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two
print(friends[0])
print(friends[-5])
print(friends[4])
print(friends[-1])
#ASS2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0:5:2])
print(friends[1:4:2])
# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"
#ASS3
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(friends[1:4])
print(friends[3:5])
#ASS4
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]
friends.append("Elzero")
friends.append("Elzero")
print(friends)
#ASS5
friends = ["Osama", "Ahmed", "Sayed"]
# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.insert(0 , "Nasser")
print(friends)
friends.insert(5, "Salem")
print(friends)
#ASS6
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]
friends.remove("Nasser")
friends.remove("Osama")
print(friends)
friends.remove("Salem")
print(friends)
#ASS7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)
#ASS8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']
friends.sort()
print(friends)
friends.reverse()
print(friends)
#ASS9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# Needed Output
# 6
print(len(friends))
#ASS10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# Needed Output
# Django
# Web
print(technologies[4][0])
print(technologies[4][2])

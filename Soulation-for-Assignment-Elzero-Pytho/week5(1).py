#ASS1
print(bool(100))
print(bool(100.25))
print(bool("Mohamed"))
print(bool([12]))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
# Needed Output
#True
#True
#True
#True
#False
#False
#False
#False
#ASS2
html = 80
css = 60
javascript = 70
print(html>50 and css>50 and javascript>50)
# Needed Output
#True
#ASS3
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)
# Needed Output
#True
#False
#ASS4
num_one = 10
num_two = 20
r=num_one + num_two
print(r)
print(r**3)
print(r**3 %2600)
print(r**3 %2600 /5)
print(type(str(r**3 %2600)))
# Needed Output
#30
#27000
#1000
#200.0
#<class 'str'>
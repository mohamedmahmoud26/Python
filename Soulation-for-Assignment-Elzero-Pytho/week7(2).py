#ASS1
# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
x=0
for number in my_nums:
    x+=1
    print(f"{x} >> {number}")
print("All Number Printed")
# Needed Output
#"1 => 20"
#"2 => 15"
#"3 => 5"
#"All Numbers Printed"
#ASS2
for x in range(1,21):
    if x in [6,8,11]:
        continue
    elif x<10:
        print(f"{x}")
    else:
        print(x)
print('All Number printed')
#ASS3
my_ranks ={
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C',
}
points = {
    'A': 100,
    'B': 80,
    'C': 40
}
summ = 0
for mat in my_ranks:
    print(f'My Rank in {mat} Is {my_ranks[mat]} And This Equal {points[my_ranks[mat]]} Points')
    summ += points[my_ranks[mat]]
print(f'Total Points Is {summ}')
#ASS4
students = {
	"Ahmed": {
		"Math": "A",
		"Science": "D",
		"Draw": "B",
		"Sports": "C",
		"Thinking": "A"
	},
	"Sayed": {
		"Math": "B",
		"Science": "B",
		"Draw": "B",
		"Sports": "D",
		"Thinking": "A"
	},
	"Mahmoud": {
		"Math": "D",
		"Science": "A",
		"Draw": "A",
		"Sports": "B",
		"Thinking": "B"
	}
}
rank = {
	'A': 100,
	'B': 80,
	'C': 40,
	'D': 20
}

for name, values in students.items():
	print('*' * 50)
	print(f'Student Name => {name}'.center(50, '*'))
	print('*' * 80)
	total = 0
	for mat, degree in values.items():
		print(f'- {mat} ==> {rank[degree]}')
		total += rank[degree]
	print(f'Total  Points For {name} Is {total}')
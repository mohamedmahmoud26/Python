fre=['Mohamed', 'Ali', 'Mona', 'Sara']
for name in fre:
    if (name=='Mona'):
        print(f"Found {name}")
        break
    print(name)


frend=['Mohamed', 'Salah', 'Wafa','Ali', 'Mona', 'Sara']
for names in frend:
    if names == 'Wafa' or names == 'Ali':
        print(f"Found {names}")
        continue
    print(names)


people={
    '1':{'name':'Ali','age':10},
    '2':{'name':'Alaa','age':22},
    '3':{'name':'Mohamed','age':22},
    '4':{'name':'Mahmoud','age':45}

}

for key,person in people.items():
    if (person['age'] >=20):
        print(f" {person['name']} {person['age']}")
    if (key=='2'):
        print('canot continuo')
        break


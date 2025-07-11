friends=['mohamed','ali','mahmoud'] #List
print(friends)#['mohamed', 'ali', 'mahmoud']
print(friends[0])#mohamed
print(friends[1:])#['ali', 'mahmoud']

ls=[2,6,10,'mohamed',['ahmed','ali','essra']] # called nested 
print(ls[4])#['ahmed','ali','essra']
print(ls[4][0]) #ahmed
print(ls[4][2])#essra
print(ls[4][-2])#ali

# Add list into another
ls1=['mohamed',22]
ls2=['ali',23]
ls1.extend(ls2)
print(ls1)#['mohamed', 22, 'ali', 23]
# Another Way for add list into another
ls1=['mohamed',22]
ls2=['ali',23]
print(ls1+ls2)#['mohamed', 22, 'ali', 23]

# Replace list item by index
ls=['Mohamed',12]
ls[0]=1
print(ls) #[1, 12]

# append item to list
ls=['Mohamed',12]
ls.append("ali")
print(ls) #['Mohamed', 12, 'ali']

# pop items from lists
ls=['ali' , 'mohamed' , 'essra' ,'mona']
ls.pop() 
print(ls)#['ali', 'mohamed', 'essra']
ls.pop(0)
print(ls)#['mohamed', 'essra']
ls.pop(-2)
print(ls)#['essra']


# sort and reverse
ls=['ali' , 'mohamed' , 'essra' ,'mona']
ls.sort()
print(ls) #['ali', 'essra', 'mohamed', 'mona']
ls.reverse()
print(ls)#['mona', 'mohamed', 'essra', 'ali']

# len and type
ls=['ali' , 'mohamed' , 'essra' ,'mona']
print(len(ls)) #4
print(type(ls)) #<class 'list'>
print(type("100")) #<class 'str'>
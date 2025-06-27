
#ASS1
# Output
#"C:\Users\osama"
#"c:\Users\osama\Desktop\Python"
#"assign.py"
#4
import os
print(os.getcwd())
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
os.chdir(os.path.dirname (os.path.abspath(__file__)))
name_file=(os.path.abspath(__file__))
name_file=name_file [:-1]
name_file=name_file[:name_file.index("\\")]
name_file=name_file [:-1]
print(name_file)

files_number=1
for i in range(1,51):
    if i ==25:
        file_1=open(r"D:\pythonProject\pythonProject\text.txt" , "w")
        file_1.close()
    else:
        file_2=open(r"D:\pythonProject\pythonProject\text{i}.txt" , "w")
        file_2.write(f"Elzero web School => {i}\n")
        file_2.close()
        files_number+=1

print(files_number)

#ASS2
# Output
#Elzero Web School => 1
#Appended => Elzero Web School
#Appended => Elzero Web School
#.
#.
#Appended => Elzero Web School
#Appended => Elzero Web School
file=open(r"D:\pythonProject\pythonProject\text.txt" , "w")
file.write("Appended => Elzero Web School\n" *50)
file.close()
#ASS3

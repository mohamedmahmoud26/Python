## Python Language

1. Easy to Learn
2. Less coding
3. Easy to read
4. Libraries
------------------------------
## How

1. Listen and Watch
2. Take notes 
3. practice 
4. Share
------------------------------
## Data Type , Objects 

Integers (**int**)  => 1,2,3
Floating Point (**Float**) => 2.3 , 2.8 .100.1
Strings (**str**) => 'Hello' , "Hello"

--------------------------------------------------------------------------
## Data Structures 
Lists (**list**) **ordered**  => [1 , 'Hi' , 4.2]
Dictionaries (**dict**) ***unordered***   =>  {'key' : 'value'} 
                        => {'Name' : 'Mohamed'}
Sets (set) **unordered** { 'A' , 'B' , 'C' }
Tuples (**Tuple**) **immutable**(غير قابل للتغيير )  => (1 , 'Hi' , 4.2)
Booleans (**bool**) => True , False 

--------------------------------------------------------------------
## Data types numbers

+=> Addition 
 -=> Subtraction
 / => Division
% => Moduls 
** => Exponent
 // => Floor  Division
[[[Python/Number Calculations/Data_types numbers.py at main · mohamedmahmoud26/Python](https://github.com/mohamedmahmoud26/Python/blob/main/Number%20Calculations/Data_types%20%20numbers.py)]]

------------------------------------------------------
## The **backslash `\`** is used in Python to escape special characters inside strings.  
It tells Python **"the next character is not regular text"** — it has a special meaning.

---

###  **Example 1 — You want this output:**


`%% ''Hallo, Mohamed Elseragy  %%`

No special characters here, so you can just print it normally:



`print("%% ''Hallo, Mohamed Elseragy  %%")`




`%% ''Hallo, Mohamed Elseragy  %%`

---

###  **Example 2 — You want this output:**


`==%% " " " %%==`

Since you're using **double quotes `" "`** inside the string, you must escape them using `\"`:


`print("==%% \" \" \" %%==")`

 Output:

`==%% " " " %%==`

Or use single quotes `' '` around the whole string and keep double quotes inside:


`print('==%% " " " %%==')`



###  **Wrong Example:**


`print(\"\"\")`

 This will cause a **SyntaxError** — because Python thinks you're starting a triple-quoted string, but you never closed i

-----------------------------------------------------------------------
# String
- **Single quotes ('  ')= Double quotes("  ")** 


## Escaping:
- ( \n ) => New Line
- ( \t ) => Such as(Enter Tab)

### **Function**:
- len => Count This variable.

### Index:
 - **Indexing** means accessing a specific character in a string using its position (index).
    
- Indexing starts from **0** on the **left** (forward indexing),  
    and from **-1** on the **right** (backward indexing).
### Slicing:
- **Slicing** means cutting a string into parts by selecting a **range of characters** using their indexes.
    
- Syntax: `string[start:end:step]`

### Upper:
- The **`.upper()`** method is used to **convert all characters in a string to uppercase** (capital letters).

### Lower:
- The **`.lower()`** method is used to **convert all characters in a string to lowercase** (small letters).
### Split:
- The **`.split()`** method is used to **break a string into a list of words**, based on a **separator** (default is space).
-------------------------------------------------------------------
# Formatting

## What is String Formatting?

**String formatting** is the process of inserting variables or values into a string in a structured and readable way.

---

##  Why Use It?

- To create readable and dynamic messages
    
- To control the format of numbers (like decimals or comma separators)
    
- To keep code clean and professional
    

---

## Methods of String Formatting

### 1. **Old Style – Using `%` operator**

- `%s` → string
    
- `%d` → integer
    
- `%f` → float (e.g. `%.2f` = 2 decimal places)
    



---

### 2. **Using `str.format()`**


`print("My name is {} and I am {} years old.".format("Sergio", 22))`

Advanced formatting:


`print("Pi is approximately {:.2f}".format(3.14159))`

You can:

- Rearrange: `"Name: {1} {0}".format("Last", "First")`
    
- Use named placeholders: `"{name}".format(name="Sergio")`
    



---

### 3. **f-strings (Formatted String Literals)**




`name = "Mohamed Mahmoud" age = 22 
`print(f"My name is {name} and I am {age} years old.")`

You can format directly:

`pi = 3.14159 print(f"Pi to 2 decimals: {pi:.2f}")`

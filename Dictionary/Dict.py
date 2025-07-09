#  Create a dictionary with keys: "name" and "age"
d = {"name": "Mohamed", "age": 22}

#  Print the value associated with the key "name"
print(d['name'])  # Output: Mohamed


#  Create a nested dictionary with personal information
inf = {
    "name": "Mohamed Mahmoud",
    "info": {
        "age": 22,
        'country': 'Egypt'
    }
}

#  Print the inner dictionary under the key "info"
print(inf['info'])  # Output: {'age': 22, 'country': 'Egypt'}

#  Access and print the value of "age" from the nested dictionary
print(inf['info']['age'])  # Output: 22

#  Print name and age from dictionary `d` using an f-string
print(f"My name is {d['name']}, age is {d['age']}")  # Output: My name is Mohamed, age is 22


#  Create another dictionary containing a list and a string
d2 = {
    'my_list': [1, 2, 3],
    'my_string': 'hello'
}


#  Print the list stored under the key "my_list"
print(d2['my_list'])  # Output: [1, 2, 3]

#  Print the uppercase version of the string using .upper()
print(d2['my_string'].upper())  # Output: HELLO


#  Re-define the `inf` dictionary again
inf = {
    "name": "Mohamed Mahmoud",
    "info": {
        "age": 22,
        'country': 'Egypt'
    }
}

#  Get the value of the key "age" using .get() method
print(inf['info'].get("age"))  # Output: 22

#  Print all values in the inner dictionary
print(inf['info'].values())  # Output: dict_values([22, 'Egypt'])

#  Print all keys in the inner dictionary
print(inf['info'].keys())  # Output: dict_keys(['age', 'country'])

#  Print all key-value pairs (as tuples) in the inner dictionary
print(inf['info'].items())  # Output: dict_items([('age', 22), ('country', 'Egypt')])


#  Create a dictionary with two keys, each containing another dictionary with personal info
info = {
    "1": {
        "name": "Mohamed Mahmoud",
        "info": {
            "age": 22,
            'country': 'Egypt'
        }
    },
    "2": {
        "name": "Ali Mahmoud",
        "info": {
            "age": 25,
            'country': 'Egypt'
        }
    }
}

#  Update the value for key "2" (this will overwrite the previous data for key "2")
info["2"] = {
    "name": "Ahmed Mahmoud",
    "info": {
        "age": 30,
        'country': 'Egypt'
    }
}

# Print the updated dictionary
print(info)

# Output:
# {
#     '1': {'name': 'Mohamed Mahmoud', 'info': {'age': 22, 'country': 'Egypt'}},
#     '2': {'name': 'Ahmed Mahmoud', 'info': {'age': 30, 'country': 'Egypt'}}
# }

info = {
    "1": {
        "name": "Mohamed Mahmoud",
        "info": {
            "age": 22,
            'country': 'Egypt'
        }
    },
    "2": {
        "name": "Ali Mahmoud",
        "info": {
            "age": 25,
            'country': 'Egypt'
        }
    }
}

info.update({
    "3": {
        "name": "Sara Mahmoud",
        "info": {
            "age": 28,
            'country': 'Egypt'
        }
    }
})

# Print the updated dictionary with the new entry
print(info['3'])


inf = {
    "name": "Mohamed Mahmoud",
    "info": {
        "age": 22,
        'country': 'Egypt'
    }
}

print(inf.pop("name")) # Remove # Output: Mohamed Mahmoud
print(inf)  # Output: {'info': {'age': 22, 'country
print(inf.popitem())  # Remove and return the last inserted item, Output: ('info', {'age': 22, 'country': 'Egypt'})


inf = {
    "name": "Mohamed Mahmoud",
    "info": {
        "age": 22,
        "country": "Egypt"
    }
}

print(inf.clear)  # Output: Mohamed Mahmoud
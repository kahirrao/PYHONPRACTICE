# Example of a nested dictionary
nested_dict = {
    'person1': {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    },
    'person2': {
        'name': 'Bob',
        'age': 25,
        'city': 'Los Angeles'
    },
    'person3': {
        'name': 'Charlie',
        'age': 35,
        'city': 'Chicago'
    }
}

# Function to print the nested dictionary
def print_nested_dict(nested_dict):
    for key, value in nested_dict.items():
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")

# Function to add a new person to the nested dictionary
def add_person(nested_dict, person_id, name, age, city):
    nested_dict[person_id] = {
        'name': name,
        'age': age,
        'city': city
    }

# Print the original nested dictionary
print("Original nested dictionary:")
print_nested_dict(nested_dict)

# Add a new person to the nested dictionary
add_person(nested_dict, 'person4', 'David', 28, 'San Francisco')

# Print the updated nested dictionary
print("\nUpdated nested dictionary:")
print_nested_dict(nested_dict)
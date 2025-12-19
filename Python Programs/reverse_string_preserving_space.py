#  reverse string preserving space

# Function to reverse a string preserving spaces
# Function to reverse a string preserving spaces


def reverse_preserving_spaces(s):
    # Convert the string to a list of characters
    char_list = list(s)
    
    # Create a list to store the positions of spaces
    space_positions = []
    for i, char in enumerate(char_list):
        if char == ' ':
            space_positions.append(i)
    
    # Remove spaces from the list
    char_list_no_spaces = []
    for char in char_list:
        if char != ' ':
            char_list_no_spaces.append(char)
    
    # Reverse the list of characters without spaces
    char_list_no_spaces.reverse()
    
    # Insert spaces back into their original positions
    for pos in space_positions:
        char_list_no_spaces.insert(pos, ' ')
    
    # Convert the list back to a string
    return ''.join(char_list_no_spaces)

# Example usage
str1 = "Welcome to python"
reversed_str = reverse_preserving_spaces(str1)
print(reversed_str)  # Output: "nohtyp ot emocleW"




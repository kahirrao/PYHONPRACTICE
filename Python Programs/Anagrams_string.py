def are_anagrams(str1, str2):
    # Remove any spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Input strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if the strings are anagrams
if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

    # suggest this program using for loop to validate the anagrams.

# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")

# Remove any spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check if the length of both strings are the same
if len(str1) != len(str2):
    print("The strings are not anagrams.")
else:
    # Initialize a flag variable
    flag = True

    # Loop through each character in the first string
    for char in str1:
        # Check if the character is present in the second string
        if char not in str2:
            flag = False
            break



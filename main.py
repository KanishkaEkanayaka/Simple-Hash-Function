import numpy as np

print('****NOTE THE GIVEN INSTRUCTIONS***')
print('First enter a random number which is used as a random number for shuffle the array containing character.'
      ' ex:- 42')
print('DON\'T FORGET TO USE THE SAME RANDOM NUMBER WHEN HASHING THE SAME WORD AGAIN TO GET THE SAME HASH')
print('Then enter the plain text word to hash and then the secret. ex:- apples are red')
print('SECRET CAN BE ANYTHING..***DON\'T FORGET TO USE THE SAME SECRET WHEN HASHING THE SAME WORD AGAIN')
print()
print()

# Prompting user to enter a random number to set the random seed
random_seed = int(input('Enter the random number to shuffle the character array: '))
print(random_seed)
# Prompt user to enter the plain-text that need to hash
plain_text = input('Enter the word or password to hash: ')
# Prompt user to enter the secret
secret = input('Enter the secret: ')

full_plain_text_word = plain_text + secret
full_plain_text_word = full_plain_text_word.replace(' ', '')

# Set random seed
np.random.seed(random_seed)
# Creating lowercase array
lowercase_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z']
# Creating uppercase array
uppercase_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Creating special character array
special_character_array = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}',
                           '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']

# Creating numerical array
numerical_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Creating combined aray
combined_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '~', '`', '!', '@', '#', '$',
                  '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}',
                  '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?', '0', '1', '2', '3', '4', '5',
                  '6', '7', '8', '9']

# Shuffle the combined array
np.random.shuffle(combined_array)


# Function to hash the pain text
def hash_function(word=full_plain_text_word):
    """
    This function is used to convert the plain text into a hash
    :param word: pain text combined with the secret
    :return: hashed_word
    """
    hashed_word = ''
    para_to_hash = list(full_plain_text_word)
    for letter in para_to_hash:
        if letter.islower():
            index = lowercase_array.index(letter)
            rem_value = hash_algorithm(index)
            hash_character = combined_array[rem_value]
            hashed_word += hash_character
        elif letter.isupper():
            index = uppercase_array.index(letter)
            rem_value = hash_algorithm(index)
            hash_character = combined_array[rem_value]
            hashed_word += hash_character
        elif letter.isalnum():
            index = numerical_array.index(letter)
            rem_value = hash_algorithm(index)
            hash_character = combined_array[rem_value]
            hashed_word += hash_character
        else:
            index = special_character_array.index(letter)
            rem_value = hash_algorithm(index)
            hash_character = combined_array[rem_value]
            hashed_word += hash_character

    return hashed_word


def hash_algorithm(index):
    """
    This algorithm is using modular arithmetics to get the remainder values of g^x mod P(r1) and r1 mod 94 (r2) where 94
    is number of characters in combined array
    :param index: takes the index value of the plain text character from the array
    :return: r2
    """
    # Here I have used g^x mod P formula where P is a prime number and P and g are relatively prime.(It's better
    # if g is taken as a primitive root of P for the ease, I took relatively primeness)
    r1 = 2 ** index % 396127  # 396127 and 2 are relatively prime numbers
    r2 = r1 % 94  # 94 is the number of characters in the combined array
    return r2


# Calling the hash function value
print(hash_function(full_plain_text_word))

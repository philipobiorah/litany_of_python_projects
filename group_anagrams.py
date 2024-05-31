"""
An algorithm to group all the words which are anagrams of each other.

"""

def group_anagrams(a):
    # Create an empty dictionary to store  anagrams
    anagram_dict = {}

    #Iterate throught each word in the input list
    for word in a:
        #Sort the characters in the word and join them back into a string
        sorted_word = ''.join(sorted(word))
        print(f'Word: {word}, Sorted Word: {sorted_word}')


        #Check if the sorted word exists as a key in the dictionary
        if sorted_word in anagram_dict:
            #if the key exists, append the word to the list of anagrams
            anagram_dict[sorted_word].append(word)
        else:
            #if the key doesnot exit, create a new list with word as its first element
            anagram_dict[sorted_word] = [word]

        #Print the state of anagram_dict after each insertion
        print("Current anagram_dict: ", anagram_dict)








# Example usage
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(input_list)

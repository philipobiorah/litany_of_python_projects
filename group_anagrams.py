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
        print(sorted_word)





# Example usage
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(input_list)

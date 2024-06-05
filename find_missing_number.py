
def find_missing_number(n):
    #We put the array of n numbers in a set
    numbers = set(n)
    #create an empty dictionary to hold numbers on in the set
    output = []

    #loop  throught the number range
    for i in range(1, max(n)+1):
        if i not in numbers:
            output.append(i)
    return output


listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(find_missing_number(listOfNumbers))
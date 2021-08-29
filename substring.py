'''
It takes two strings and checks if the second string
is sub-string of the first string
'''


def isSubstring(substring, string):

    if len(substring) > len(string):
        return False
    
    else:
                
        for i in range(len(string)):
            total = 0
            if string[i] == substring[0]:
                for j in range(len(substring)):
                    if substring[j] != string[j+i]:
                        break
                    else:
                        total = total + 1
                        if total == len(substring):
                            return True
                                    
        return False


def main(): #asking for input and printing the result
    
    firstS = input("Enter the main string: ")

    while type('firstS') is not str:
        try:
            firstS = str(firstS)
        except ValueError:
            firstS = input("Please enter a valid main string: ")

    secondS = input("Enter the sub-string: ")

    while type('secondS') is not str:
        try:
            secondS = str(secondS)
        except ValueError:
            secondS = input("Please enter a valid sub-string: ")
    
    if isSubstring(secondS, firstS) == True:
        print("It is a substring of the main string.")
    else:
        print("It is not a substring of the main string.")

    
main()


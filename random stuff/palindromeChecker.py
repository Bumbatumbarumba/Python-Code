"""
palindrome checker
created by Bartosz Kosakowski
Sept 7th, 2017
"""

def palindromeChecker(myString):
	reversedWord = "";
	for i in myString:
		reversedWord = i + reversedWord;
	if reversedWord == myString:
		return True;
	else:
		return False;

if __name__ == '__main__':
	print(palindromeChecker(str(input("Enter a word: "))));
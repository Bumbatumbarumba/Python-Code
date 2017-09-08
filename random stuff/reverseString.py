"""
String reversing
created by Bartosz Kosakowski
Sept 7th, 2017
"""
#reverses string
def reverseString(myString):
	backwards = "";
	for i in myString:
		backwards = i + backwards;
	print(backwards);

if __name__ == '__main__':
    reverseString(input("Please enter a string; type EXIT to quit: "));
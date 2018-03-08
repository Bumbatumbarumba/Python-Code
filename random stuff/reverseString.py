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

def onbase():
	i = 0
	for i in range(101):
		if i % 3 == 0:
			if i % 7 == 0:
				print("OnBase");
			print("On");
		elif i % 7 == 0:
			print("Base");
		else:
			print(i);

if __name__ == '__main__':
    #reverseString(input("In quotation marks, enter a string: "));
    onbase();
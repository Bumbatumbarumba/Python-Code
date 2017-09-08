"""
fibonacci sequence generator
sums the preceding two digits to produce the next one in the sequence
created by Bartosz Kosakowski
Sept 7th, 2017
"""
def fib(x):
	fibList = [1,1]
	if x == 1:
		print(fibList[0]);
	elif x == 2:
		print(fibList);
	else:
		i = 1
		while (i < x):
			nextnum = fibList[i-1] + fibList[i];
			fibList.append(nextnum);
			i+=1;
		print(fibList);

if __name__ == '__main__':
	fib(input("Enter the desired fibonacci sequence length: "));
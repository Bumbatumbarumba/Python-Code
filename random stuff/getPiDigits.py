"""
Getting x digits of pi
created by Bartosz Kosakowski
Sept 7th, 2017
"""
import math;

def getPiDigits(x):
	print(round(math.pi,abs(x)));

if __name__ == '__main__':
	decimals = int(input("Enter the desired decimal accuracy of Pi: "));
	while decimals > 11:
		print("Only ints between 0 and 11, inclusively, are acceptable.\nNegative numbers are converted to positive.\nDecimals are rounded to the nearest whole.");
		decimals = int(input("Enter the desired decimal accuracy of Pi: "));
	print("Rounding Pi to " + str(decimals) + " decimal places:");
	getPiDigits(decimals);
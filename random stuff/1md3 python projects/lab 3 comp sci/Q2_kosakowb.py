#Bartosz Kosakowski
#400028494
#Lab 3 Question 2
######################

def occurrences(s:"string", t:"substring"):
	i = 0
	temp = 0
	while i < len(s):
		temp = temp + s[i:i+len(t)].count(t)
		i = i + 1
	return temp

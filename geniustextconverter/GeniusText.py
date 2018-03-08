import sys;

def GeniusText(change):
	newWord = "";
	for i in range(len(change)):
		if change[i] is "f":
			newWord += " ";
		elif change[i] is "l":
			newWord += "'";
		elif change[i] is "h":
			newWord += "sjk";
		else:
			newWord += change[i];
	print(newWord);

def run():
	userIn = "";
	while(True):
		userIn = raw_input("say something!\n");
		if userIn == "exit":
			sys.exit();
		else:
			GeniusText(userIn);

run();
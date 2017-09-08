#Bartosz Kosakowski, 15/08/17
#App used to log stuff being brought into the shed
#Basically a cooler sign-in, sign-out sheet

#Holds data associated with 
class Person():
	#name, date, sign-in quantity, sign-out quantity, tonto verification signature
	def __init__(self, n, a, iq, d):
		self.name = n;
		self.amount = a;
		self.inQuantity = iq;
		self.date = d;
		self.signInSignature = "Not Validated";
		self.signOutSignature = "Not Validated";

	#checks if account exists, if not then it prompts user to create an account
	#and then tries to validate once again
	#account is the person who validates username's sign-in/out
	def validate(self, username, admin, adminpswd):
		if (admin not in main.accountDict):
			main.createAccount();
			validate(username, admin, adminpswd);
		else:
			inOut = input("Please enter either 'in', 'out', or 'cancel' (not case-sensitive): ")
			if inOut.lower() not in ["in", "out", "cancel"]:
				print("Invalid argument!");
				validate(username, admin, adminpswd);
			elif admin not in main.adminList:
				print("Error, only " + main.adminList + "can validate sign-in/out");
			else:
				if inOut.lower() == "in":
					self.signInSignature = "Validated by " + admin;
				elif inOut.lower() == "out":
					self.signOutSignature = "Validated by " + admin;

#runs dis bitch
class main():
	#eventually make this to be saved in a txt or something so the user(s?) doesn't have
	#to create new accounts every time
	accountDict = {"":"password"};
	personDict = {};
	adminList = ["Tristan", "Bartosz"];

	#creates an account and adds it to the list of accounts
	@staticmethod
	def createAccount():
		userName = input("Enter a username: ");
		while (userName == ""):
			userName = input("Username cannont be empty! Enter a valid username: ");
		password = input("Enter a password: ");
		while (password == ""):
			password = input("Password cannot be empty! Enter a valid password: ");
		accountDict[userName] = password;

	#used to verify account activity, mostly geared towards admin stuff
	#the use of the number 67 is arbitrary lol				
	def verifyAccountActivity(username, password):
		if username in main.adminList:
			while (accountDict[username] != password):
				password = input("Invalid password, try again");
				verifyAccountActivity(username, password);
			return 67;
		elif username in accountDict:
			while (accountDict[username] != password):
				password = input("Invalid password, try again");
				verifyAccountActivity(username, password);
			return 1;
		elif username.lower == "cancel":
			print("Cancelling validation");
		else:
			username = input("Invalid username, try again");
			verifyAccountActivity(username, password);

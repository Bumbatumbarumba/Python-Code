#Bartosz Kosakowski
#400028494
#Lab 2 Question 2
#####################
def anandGrade(score):
    grade = score - 5
    if grade>=80:
        print('A')
    elif 80 > grade >= 70:
        print('B')
    elif 70 > grade >= 60:
        print('C')
    elif 60 > grade >= 50:
        print('D')
    else:
        print('F, you failed')

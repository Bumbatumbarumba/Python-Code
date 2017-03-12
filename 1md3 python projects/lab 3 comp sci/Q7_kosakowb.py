#Bartosz Kosakowski
#400028494
#Lab 3 Question 7
###################

def igpayatinlay(e):
    eSplit = e.split()
    ePig = ''
    i = 0
    temp = ''
    while i < len(eSplit):
        temp = eSplit[i]
        if (temp[0] == 'a' or temp[0] == 'e' or temp[0] == 'i' or temp[0] == 'o' or temp[0] == 'u'):
            eSplit[i] = temp  + 'way' + ' '
        else:
            j = 0
            while j < len(temp):
                if (temp[0] != 'a' or temp[0] != 'e' or temp[0] != 'i' or temp[0] != 'o' or temp[0] != 'u'):
                    eSplit[i] = temp[1:(len(temp)+1)] + temp[0]
                else:
                    eSplit[i]= temp
                j = j+1
            eSplit[i] = eSplit[i] + 'ay' + ' '
        ePig = ePig + eSplit[i] + ' '
        i = i+1
    return ePig


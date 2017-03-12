#Bartosz Kosakowski
#400028494
#Lab 2 Question 3
#####################
def minutes(d: 'days', h: 'hours', m: 'minutes'):
    if (d < 0):
        print('Found negative number (days); converting to positive')
        d =  d*(-1)
    if (h < 0):
        print('Found negative number (hours); converting to positive')
        h =  h*(-1)
    if (m < 0):
        print('Found negative number (minutes); converting to positive')
        m =  m*(-1)
    totalMinutes = d*24*60 + h*60 + m
    return totalMinutes

def daysHoursMinutes(m: 'minutes'):
    if (m < 0):
        print('Found negative number (minutes); converting to positive')
        m =  m*(-1)
    numDays = int(m/1440)
    numHours = int((m%1440)/60)
    numMinutes = m%60
    print('(',numDays,', ',numHours,', ',numMinutes,')')

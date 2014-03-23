message=input ("Enter your number here: ")
telno=str(message)
local = "Local: {0}-{1}".format (telno[3:6],telno[6:]);
domestic = "Domestic: ({0}) {1}-{2}".format(telno[0:3],telno[3:6],telno[6:]);
international = "International: +1-{0}-{1}-{2}".format (telno[0:3],telno[3:6],telno[6:]);
print "The phone number is",telno,"\n",local,"\n",domestic,"\n",international;  
#!/usr/bin/python

print("WELCOME")
print("CHOOSE A OPTION")
print("1->  LIST THE AGENDA")
print("2 -> ADD THE NEW CONTACT ")

option = input("> ")

if option == 1:
	print("CHOOSE YOU THE OPTION %i " %option) ,("=> LIST THE AGENDA")
	agenda = open("agenda.csv")

	for item in range(1,10):
		print(agenda.read())

elif option == 2:
	print("CHOOSE YOU THE OPTION %i" %option) , ("=> ADD THE CONTACT")	
	agenda = open("agenda.csv", 'a')
	name = raw_input("ENTER A NAME: ")
	number = raw_input("GOOD, NOW A CONTACT NUMBER'S ")

	agenda.write(name)
	agenda.write('\t')
	agenda.write(number)
	agenda.write('\n')
	agenda.close()


else:
	print("THE OPTION %i" %option), ("NOT IS CORRECT")

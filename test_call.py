from datetime import date
today = date.today()
print("Today is:", today)
newToday = today.strftime('%Y-%m-%d')
# Python Program to Print Lines
# Containing Given String in File

#week number
weekNumber = date.today().isocalendar()[1]

# input file name with extension
#file_name = open("on_call_list.txt")

# using try catch except to
# handle file not found error.

# entering try block
try:

	# opening and reading the file
	# list_of_names.txt will have the date in yyyy-mm-dd format
	file_read = open("list_of_names.txt", "r")

	# asking the user to enter the string to be
	# searched
	#text = (today)

	# reading file content line by line.
	lines = file_read.readlines()

	new_list = []
	idx = 0

	# looping through each line in the file
	for line in lines:
		
		# if line have the input string, get the index
		# of that line and put the
		# line into newly created list
		if newToday in line:
			new_list.insert(idx, line)
			idx += 1

	# closing file after reading
	file_read.close()

	# if length of new list is 0 that means
	# the input string doesn't
	# found in the text file
	if len(new_list)==0:
		print("\n\"" +newToday+ "\" is not found in \"" +file_read+ "\"!")
	else:

		# displaying the lines
		# containing given string
		lineLen = len(new_list)
		print("\n**** Lines containing \"" +newToday+ "\" ****\n")
		for i in range(lineLen):
			print(end=new_list[i])
		print()

# entering except block
# if input file doesn't exist
except :
    print("\nThe file doesn't exist!")

#List of names to pick from
First_Names = ["0. First Name", "1. Second Name", "2. Third Name", "3. Fourth Name", "4. Fifth Name" ]
Second_Names = [ "0. Sixth Name", "1. Seventh Name", "2. Eighth Name", "3. Ninth Name", "4. Tenth Name" ]

#List of names "pasted" in the email template
First = ["First Name - 555-123-4567", "Second Name - 555-123-4567", "Third Name - 555-123-4567", "Fourth Name - 555-123-4567", "Fifth Name - 555-123-4567" ]   
Second = [ "Sixth Name - 555-123-4567", "Seventh Name - 555-123-4567", "Eighth Name - 555-123-4567", "Ninth Name - 555-123-4567", "Tenth Name - 555-123-4567" ]

#Pick First from list
print("First List")
print("")
for item in First_Names:
    print(item)

First_Input = int(input("Please select number from list " ))
print("")
#Pick Second from list
print("Second List")
print("")
for item in Second_Names:
    print(item)

Second_Input = int(input("Please select number from list " ))


x = First[First_Input]
y = Second[Second_Input]

print("")

if(weekNumber %2) == 0:
    #EMAIL TEMPLATE for Second Primary##
    print("This week the following will be on call:")
    print("")
    print("Primary:")
    print(y)
    print("")
    print("Secondary")
    print(x)
    print("")
    print("If you have any questions, let me know.")
    print("")

else:
    #EMAIL TEMPLATE for First Primary##
    print("This week the following will be on call:")
    print("")
    print("Primary:")
    print(x)
    print("")
    print("Secondary")
    print(y)
    print("")
    print("If you have any questions, let me know.")
    print("")


input("Press enter to exit...")

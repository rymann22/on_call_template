# on_call_template
Python script to autogenerate a template for an on call email. 

Every week I send an email at work for the two people selected for being on call. 
I've changed this script so that it's just "First" and "Second" for the groups of people. 
The First and Second groups alternate everyweek as who is the primary person.

This script will display the date, then it will print out the line that matches the date from the "list_of_names.txt" file. 

From there, it will print out the first list of names. Select the name you want by hitting the corresponding letter and hitting enter.

Do the same for the second list.

Afterwords, it'll print out the template and tell you to hit enter to exit... This is done to give the user time to copy the text they want.

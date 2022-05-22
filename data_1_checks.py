#first data check
print("Hello! This is my first data check with Code Louisville.\n\t Proceed with caution!")
question= input("Are you positive you want to proceed? ").lower()
#import json module 
import json
import string
#create a dictionary to a string
str1= "string.ascii_letters + string.digits + !@#$%^&*()"
d = dict.fromkeys(string.ascii_lowercase, 0)
dict = { 'A'}
if question == "yes":
     print("Hello World!\n\t Please create a special password using these letters.") 
     print(str1)
else:
     print("Goodbye World!")






   


      
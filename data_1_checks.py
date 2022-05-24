#first data check
print("Hello! This is my first data check with Code Louisville.\n\t Proceed with caution!")
question= input("Are you positive you want to proceed? (YES OR NO) ").lower()
name = input("What is your name? (TYPE YOUR FIRST NAME)" )
#define dictionairies
#create a dictionary to a string & added tuples
password_requirements = [
    {
    "length" : 5,
    "digits" : 9,
    "characters" : "Hello World!"},
    {
    "length" : 6,
    "digits" : 9,
    "characters" : "Hello World!"}

    ]
password_list = ["characters",  "digits", "length"]
numbers = ("Welcome! You will use these instructions to formulate your own temporary password when you log in next time! Make sure you choose a secure password next time. (Press enter)!")
print(numbers)
print(password_requirements[1]["length"], password_list)
print(password_requirements[0]["characters"])


 
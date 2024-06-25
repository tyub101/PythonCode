#Password Generator Project
import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pwd_letters=""
for i in range (0,nr_letters) : 
  i=random.randint(0,len(letters)-1)
  pwd_letters+=letters[i]
#print(pwd_letters)

pwd_numbers=""
for n in range(0,nr_numbers):
 n=random.randint(0,len(numbers)-1)
 pwd_numbers +=numbers[n]
#print(pwd_numbers)

pwd_symbols=""
for k in range(0,nr_symbols):
  k=random.randint(0,len(symbols)-1)
  pwd_symbols +=symbols[k]
#print(pwd_symbols)
print(f"here is your password : {pwd_letters}{pwd_numbers}{pwd_symbols}  :) ")
  


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pwd_randomised= ""
pwd_not_randomised = pwd_letters+pwd_numbers+pwd_symbols
print(pwd_not_randomised)
for i in  pwd_not_randomised :
   i=random.randint(0,len(pwd_not_randomised)-1)
   pwd_randomised += pwd_not_randomised[i]
print(f"here is a randomised strong password :{pwd_randomised} ")
    

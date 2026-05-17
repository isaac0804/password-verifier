password = input("Please put a password\n")
score = 0

#checking Uppercase
has_upper = False
for c in password:
  if c.isupper():
    has_upper = True
# has_upper = any(c.isupper() for c in password)
if not has_upper:
  print("No upper case!!")
else: 
  # add 1 to score
  score = score + 1

#checking Lowercase
has_lower = False
for c in password:
  if c.islower():
    has_lower = True
if not has_lower:
  print ("No Lowercase")
else: 
  score = score +1

#checking numbers
has_num = False 
for num in password:
  if num.isdigit():
    has_num =True 
if not has_num:
  print ("No number")
else: 
  print ("You have not bad password")
  # add 1 to score
  score = score + 1

user = has_upper + has_num
print ("Score of your password: " + str(score))
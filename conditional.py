# score = int(input("What is the score: "))

#------> if statements

# if score > 5:
#   print(' the score is greater than 5')

#------> if/else statements

# if score > 10:
#   print('the score is greater than 10')
  
# else:
#   print("the scroe is not greater than 10")
  
#-----> if/elif/else statements

# if score > 10:
#   print("the score is greater than 10")
# elif score > 5:
#   print("The score is greater than 5, but not greater than 10")
# else:
#   print("The score is 5 or less")


#-----> AND, OR, NOT, IS NOT

age = int(input("What is the age? "))

if age > 12 and age < 20:
  print("teenager")

if age < 13 or age > 19:
  print("not a teenager")
  
authenticated = False

if not authenticated:
  print("You are not authenticated")

if authenticated is not True:
  print("Not authenticated")
  
if authenticated is not False:
  print("Not authenticated")
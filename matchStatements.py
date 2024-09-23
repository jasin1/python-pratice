# match case statements 

belt_color = input("What is your ninja belt color: ")

match belt_color:
  case "white":
    print("Ninja fledgling")
  case "red":
    print("Intermediate Ninja")
  case "blue":
    print("Advanced Ninja")
  case "purple":
    print("Advanced Ninja")
  case "black":
    print("Master Ninja!")
  case _:
    print("belt color is unknown!")  
  
    
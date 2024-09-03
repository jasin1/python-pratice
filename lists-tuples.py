# lists can be changes after they are created
# Tuples are immutable which means they can't be changed

names = ["Hassan", "Mark", "Oh luigi"]
print(names[2])
print('length of the list is: ', len(names))

names[1] = "Toad"
print(names)

names.append("Bowser")
print(names)

names.remove("Oh luigi")
print(names)

##Tuples
top_scores = (100, 95, 92, 92, 88, 85)

print(top_scores[0])
print(top_scores[1])
print('length scores', len(top_scores))

print(top_scores.count(92))
print(top_scores.index(85))

## Why use tuples? There are times when you don't want an item to change, like topscores, or more related info to a specific person that will never change, like birthday



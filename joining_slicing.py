# joining lists
ages_one = [25, 30, 49, 60, 75]
ages_two = [19, 65, 21, 44, 38]

joined_ages = ages_one + ages_two
print(ages_one)
print("joined ", joined_ages)

ages_one.extend(ages_two)
print("ages_one extended:", ages_one)

#slicing lists
scores = [100, 99, 25, 44, 85, 77, 64]
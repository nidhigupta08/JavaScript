import random

# Generate a list of 10 random integers between 1 and 100
random_list = []
for i in range(10):
    random_list.append(random.randint(1, 100))

# Print the random list
print("Random list:", random_list)

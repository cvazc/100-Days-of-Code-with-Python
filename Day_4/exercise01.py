import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 option
random_position = random.randint(0, 4)
print(friends[random_position])

# 2 Option
print(random.choice(friends))

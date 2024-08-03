import random
import matplotlib.pyplot as plt

n = 1000  # number of rolls
sides = 6 # number of sides

throws = [random.randrange(sides) for _ in range(n)]
nums = [throws.count(k) for k in range(sides)]

plt.bar(range(sides), nums)
plt.show()
import matplotlib.pyplot as plt
import random

pos = (0, 0)
path = [pos]
directions = ["up", "down", "left", "right"]


for i in range(100):
    rand_direction = random.choice(directions)
    if rand_direction == "up":
        pos = (pos[0], pos[1] + 1)
    elif rand_direction == "down":
        pos = (pos[0], pos[1] - 1)
    elif rand_direction == "left":
        pos = (pos[0] - 1, pos[1])
    else:
        pos = (pos[0] + 1, pos[1])

    path.append(pos)

x, y = zip(*path)

plt.plot(x, y, color='red', marker='x')
# plt.xlim(-10,10)
# plt.ylim(-10,10) -- I originally had these limits to make it cleaner and more consistant but it would cut off some of the plots 

print(f"Final position after 100 steps: {path[len(path)-1]}")
plt.title("Astronaut walk")
plt.show()
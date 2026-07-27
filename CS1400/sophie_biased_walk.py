import random

pos = (0, 0)
counts = {"up": 0, "down": 0, "left": 0, "right": 0}
directions = ["up", "down", "left", "right"]
percentages = [3, 1, 1, 1]

# Simulates walking n steps in weighted directions. 
for i in range(200):
    rand_direction = random.choices(directions, weights=percentages, k=1)[0]
    if rand_direction == "up":
        pos = (pos[0], pos[1] + 1)
        counts["up"] += 1
    elif rand_direction == "down":
        pos = (pos[0], pos[1] - 1)
        counts["down"] += 1
    elif rand_direction == "left":
        pos = (pos[0] - 1, pos[1])
        counts["left"] += 1
    else:
        pos = (pos[0] + 1, pos[1])
        counts["right"] += 1

print(f"Final position: {pos}")
print("Direction counts:")
print(f"Up: {counts["up"]}")
print(f"Down: {counts["down"]}")
print(f"Left: {counts["left"]}")
print(f"Right: {counts["right"]}")

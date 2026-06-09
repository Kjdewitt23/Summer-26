import math

# Determines the area of 1 regular pentagon. This formula can be used for any regular polygon which is really useful.

def areaRegularPentagon(lengthSide):
    ar = (5 * (lengthSide ** 2)) / (4 * math.tan(math.pi / 5))
    return ar


def areaMultiplePentagons(numPentagons, lengthSide):
    totalArea = numPentagons * areaRegularPentagon(lengthSide)
    return totalArea

# By reusing the 'areaRegularPentagon' function, I was able to follow what Professor Zaman always says about not repeating yourself.

total = areaMultiplePentagons(3, 7)
print(f"Total area for 3 pentagons with side 7: {total:.4f}")

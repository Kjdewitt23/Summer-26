coding_club = {"Alice", "Bob", "Charlie", "Dana"}
robotics_club = {"Charlie", "Eve", "Frank", "Bob"}

print(f"Students in both clubs: {coding_club & robotics_club}") # Shows the students who are in both clubs
print(f"Students in only one club: {coding_club ^ robotics_club}") 
print(f"Students only in the coding club: {coding_club - robotics_club}")

coding_club.add("Grace")

robotics_club.discard("Eve")

print(f"All unique students: {coding_club | robotics_club}")



eq_1 = 6 + 2 * 8 // 4 ** 2  # In order this is evaluated: 4**2 == 16 -> 2*8 == 16 -> 16/16 == 1 -> 6+1 == 7
print(eq_1)

eq_1_mod_1 = (6 + 2) * 8 // 4 ** 2 #In order this is evaluated: 6+2 == 8 -> 4**2 == 16 -> 8*8 == 64 -> 64/16 == 4
print(eq_1_mod_1)

eq_1_mod_2 = 6 + 2 * (8 // 4) ** 2 #In order this is evaluated: 8/4 == 2 -> 2**2 == 4 -> 2*4 == 8 -> 8+6 == 14 
print(eq_1_mod_2)

#Because the parentheses change the order of operations the total is different.

eq_2 = 12 + 6 // 3 * 9 # In order this is evaluated: 6//3 == 2 -> 2*9 == 18 -> 12+18 == 30
print(eq_2)

eq_2_mod_1 = (12 + 6) // 3 * 9 # In order this is evaluated: 12+6 == 18 -> 18//3 == 6 -> 6*9 == 54
print(eq_2_mod_1) 

eq_2_mod_2 = 12 + 6 // (3 * 9) #In order this is evaluated: 3*9 == 27 -> 6//27 == 0 -> 12+0 == 12
print(eq_2_mod_2) 

eq_3 = 10 + 2 - 5 * 6 // 2 #In order this is evaluated: 5*6 == 30 -> 30//2 == 15 -> 10+2 == 12 -> 12-15 == -3
print(eq_3)

eq_3_mod_1 = 10 + (2 - 5) * 6 // 2 #In order this is evaluated: 2-5 == -3 -> -3*6 == -18 -> -18//2 == -9 -> 10+(-9) == 1
print(eq_3_mod_1)

eq_3_mod_2 = (10 + 2 - 5) * 6 // 2 #In order this is evaluated: 10+2 == 12 -> 12-5 == 7 -> 7*6 == 42 -> 42//2 == 21
print(eq_3_mod_2)
citizens = int(input("How many citizens: "))
total_units = int(input("How many total units: "))
units_needed = (citizens - 2) * 3 

#It took me a little while to realize that Mira and Tov DO NOT receive the original 3. I wasn't sure where my math was going wrong until I realized that. 

remaining_supply = total_units - units_needed

m_spec = remaining_supply * 0.13
remaining_supply = remaining_supply - m_spec

t_spec = remaining_supply * 0.11
remainingSupply = remaining_supply - t_spec

crew_total = remainingSupply / citizens + 3
m_total = m_spec + crew_total - 3
t_total = t_spec + crew_total - 3

print(f"Mira's share: {m_total:.2f}")
print(f"Tov's share: {t_total:.2f}")
print(f"Crew's share: {crew_total:.2f}")



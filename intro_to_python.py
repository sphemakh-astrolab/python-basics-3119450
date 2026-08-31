# Exercise 1: Hello Universe
print("Hello, Universe!")
print("Hello, Universe!")
print("Fisokuhle")
print("white, Star")


# Exercise 2: variables and types
name = "Sirius"           
distance_ly = 8.6         
num_planets = 0          
naked_eye_visible = True

print(name,"has type", type(name))
print(distance_ly, "has type", type(distance_ly))
print(num_planets, "has_type", type(num_planets))
print(naked_eye_visible, "has_type", type(naked_eye_visible))


# --- Part B: arithmetic with astronomy -------------------------------------

# Exercise 3: unit conversions 
distance_pc = distance_ly / 3.26
distance_km =distance_ly  * 9.46e12
distance_pc = distance_ly / 3.26
print(f"Sirius is {distance_pc} parsecs away.")
print(f"Sirius {distance_km} kilometres away.")

# Exercise 4: we see the past
now = 2026
light_years_ago = 8.6
year_it_left_in = now - light_years_ago
print(f"year, {year_it_left_in}")
print(8.6 / 3)
print(8 // 3)
#Difference between the two operations is that the first one with a single slash prints an answer with decimals
#whereas the second one with double slash print out only the whole number with no decimal places

# Exercise 5: the power operator 
pi = 3.14159
radius_km = 696000 
volume = (4/3) * pi * radius_km ** 3
print(f"The Sun's volume is about {volume:.3e} cubic km.")


# --- Part C: talking to the user -------------------------------------------

# Exercise 6: reading input
text = input("Enter a distance in light-years: ")
print(f"That is {float(text) / 3.26:.2f} parsecs.")


# --- Optional extension ----------------------------------------------------
import math
print(math.pi)
print(math.log10(100))

d = 2.46 
mu = 5 * math.log10(d) -5 
print(f"distance modulus, {mu:.3f}")

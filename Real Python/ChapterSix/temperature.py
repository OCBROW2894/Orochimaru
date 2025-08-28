"""
6.3 Challenge: Convert Temperatures
F = C * 9/5 + 32
C = (F- 32) * 5/9
"""

def convert_cel_to_far(C):
    """Converts tempterature C to F """
    F = float((C * 9/5) + 32)
    return F

def convert_far_to_cel(F):
    """Converts temperature F to C """
    C = float((F - 32) * 5/9)
    return C

temp_far = float(input("Enter a temperature in degrees F: "))
temp_celsius = convert_far_to_cel(temp_far)
print(f"{temp_far} degrees F = {temp_celsius:.2f} degrees C")


temp_cel = float(input("Enter a temperature in degrees C: "))
temp_fahrenheit = convert_cel_to_far(temp_cel)
print(f"{temp_cel} degrees C = {temp_fahrenheit:.2f} degrees F")

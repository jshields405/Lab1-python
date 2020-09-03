# Author Jack Shields jcs6283@psu.edu
# Collaborator Chao-Yang Fang cbf5338@psu.edu
# Collaborator Tuan Nguyen tmn5319@psu.edu
# Collaborator Adam Greenberg aqg5910@psu.edu
temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temp = float(temp)

if (unit == 'c' or unit == 'C'):
  fahren = ((temp*9)/5)+32
  print(f"{temp}° in Celsius is equivalent to {fahren}° Fahrenheit.")
elif (unit == 'f' or unit =='F'):
  celc = ((temp-32)*5)/9
  print(f"{temp}° in Fahrenhiet is equivalent to {celc}° Celsius.")
else:
  print(f"Invlaid unit({unit})")
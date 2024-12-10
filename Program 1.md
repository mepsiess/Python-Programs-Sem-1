# Programming with Python Semester - 1
## Program-1 : Write a program to find the roots of a quadratic equation
---
## Code:

```
a = int(input("Enter the value: "))

b = int(input("Enter the value: "))

c = int(input("Enter the value: "))

d = b ** 2 - 4 * a * c

if d >= 0:

  r1 = (-b + (d) ** 0.5) / 2 * a
  r2 = (-b - (d) ** 0.5) / 2 * a
  
  print("The roots are real", r1, "and", r2)

else: 

  print("There are no real roots.")

```

![image](https://github.com/mepsiess/Python-Programs-Sem-1/blob/main/1.png?raw=true)


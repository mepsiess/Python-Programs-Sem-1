## Program-6: Write a program to swap the first n characters of two strings.

## Code:

```
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
n1 = int(input("Enter the number of characters to be swapped: "))
m = string1[:n1]
n = string2[:n2]
if n1 <= min(len(string1),len(string2)) :
  print("String 1 after swapping: ", string1.replace(m,n))
else :
  print("String 2 after swapping: ", string2.replace(n,m))

```
![image](https://github.com/mepsiess/images-repo/blob/main/17.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/18.png?raw=true)

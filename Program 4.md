##   Write a program that accepts a character and accepts the following:

## a) print whether the character is a letter or numeric digit or a special character

## b) if the character is a letter, print whether the letter is uppercase or lowercase

## c) if the character is a numeric digit, print its name in text

---
## Code:

```
charac = input("Enter the data: ")

if charac >= "A" and charac <= "Z" :

  print(charac, "is an uppercase letter")

elif charac >= "a" and charac <= "z" :

  print(charac, "is a lowercase letter")

elif charac >= "0" and charac <= "9" :

  print(charac, "is a numeric digit")
  
  n = int(charac)
  
  dict = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
  
  print(dict[n])

else :

  print(charac, "is a special character")

```

![image](https://github.com/mepsiess/images-repo/blob/main/8.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/9.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/10.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/11.png?raw=true)

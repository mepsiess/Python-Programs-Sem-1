## Program-2: Write a program to accept a number 'n' to compute :
## a) Check if 'n' is a prime number or not
## b) Generate all prime numbers till 'n'

a)
```
n = int(input("Enter the value: "))

if n > 1 :
  for i in range (2,n) :

    if n % i == 0 :
      print(n, "is not a prime number.")
      break
    else :
      print(n, "is a prime number.")
      break

  else : 
     print(n, "is not a prime number.")
```

![image](https://github.com/mepsiess/images-repo/blob/main/3.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/4.png?raw=true)

b)

```
n = int(input("Enter value: "))

for num in range (1,n) :

    if num > 1 :

        for i in range (2,num) :

            if num % i == 0 :

                break 

            else :

                print(num, end = ",")

```

![image](https://github.com/mepsiess/images-repo/blob/main/5.png?raw=true)









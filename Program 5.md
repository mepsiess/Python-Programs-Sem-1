## Program-5: Write a program to perform the following operations on a string

## a) Find the frequency of a character in a string.

## b) Replace a character by another character in a string.

## c) Remove the first occurence of a character from a string.

## d) Remove all occurences of a character from a string.

## Code:

a)

```
string = "hello, welcome to python"
charac = input("Enter a character: ")
f = 0
for i in string:
    if i == charac:
        f += 1
print ("Frequency of", charac, "is", f)
```

![image](https://github.com/mepsiess/images-repo/blob/main/12.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/13.png?raw=true)

b)

```
string = "hello, welcome to python"
print("The string is: ", string)
print('\n', "The string after removing first occurence is: ", string.replace('h','t'))

```

![image](https://github.com/mepsiess/images-repo/blob/main/14.png?raw=true)

c)

```
string = "hello, welcome to python"
print("The string is: ", string)
print('\n', "The string after removing first occurence is: ", string[1:len(string)])

```

![image](https://github.com/mepsiess/images-repo/blob/main/15.png?raw=true)

d)

```
string = "hello, welcome to python"
print("The string is: ", string)
print('\n', "The string after all occurences of a character is: ", string[:0])

```

![image](https://github.com/mepsiess/images-repo/blob/main/16.png?raw=true)

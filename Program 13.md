## Program-13: Write a program to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and / or special characters. 

## Code:

```
name = input("Enter a name: ")
try: 
  if name.isalpha():
    print("This is correct name")
  
  else:
    raise Exception("There is NameError")
except Exception as e:
  print(e)
```

![image](https://github.com/mepsiess/images-repo/blob/main/27.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/28.png?raw=true)

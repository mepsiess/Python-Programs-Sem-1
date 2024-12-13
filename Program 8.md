## Program-8: Write a program to create a list of cubes of only the even integers appearing in the input list (may have elements of other types also) using the following:

### a. 'for' loop

### b. list comprehension


## Code:

```
def cube_even_int():
  cubes = []
  number = [1, 2, "three", 4, 5, 6, "seven", 8, "nine", 10]
  
  for i in number:
    if type(i) == int:
      
      if i % 2 == 0:
        cubes.append(i ** 3)

  print(cubes)
cube_even_int()

```

![image](https://github.com/mepsiess/images-repo/blob/main/21.png?raw=true)
        

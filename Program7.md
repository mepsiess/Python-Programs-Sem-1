## Program-7: Write a function that accepts two strings and returns the indices of all the occurences of the second string in the first string as a list. If the second string is not present in the first string then it should return - 1.

## Code:

```
def occur(m,n) :
  indices = []
  index = m.find(n)
  
  while index != -1 :
    indices.append(index)
    index = m.find(n, index + 1)

  return indices if indices else -1

m = input("Enter the first string: ")
n = input("Enter the second string: ")
results = occur(m,n)
print("The occurences are ", results)

```
![image](https://github.com/mepsiess/images-repo/blob/main/19.png?raw=true)

![image](https://github.com/mepsiess/images-repo/blob/main/20.png?raw=true)
  


## Program-12: Consider a tuple t1 = (1,2, 3, 4, 5, 6, 7, 8, 9, 10). Write a program to perform following operations:

a) Print half the values of the tuple in one line and the other half in the next line.

b) Print another tuple whose values are even numbers in the given tuple.

c) Concatenate a tuple t2 = (11, 13, 15) with t1.

d) Return maximum and minimum value from this tuple.

---

## Code:

a)

```
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
half = len(t1) // 2
first = t1[:half]
print("The first half of the tuple is: ", first)
second = t1[half:]
print("The second half of the tuple is: ", second)
```

![image](https://github.com/mepsiess/images-repo/blob/main/23.png?raw=true)

b)

```
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_no = tuple(filter(lambda x: x % 2 == 0, t1))
print("The tuple with even number: ", even_no)
```

![image](https://github.com/mepsiess/images-repo/blob/main/24.png?raw=true)

c)

```
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t2 = (11, 13, 15)
print("Tuple 1: ", t1)
print("Tuple 2: ", t2)
concat = t1 + t2
print("The tuple after concatenation will be: ", concat)
```

![image](https://github.com/mepsiess/images-repo/blob/main/25.png?raw=true)

d)

```
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15)
print("The maximum value of tuple: ", max(t1))
print("The minimum value of tuple: ", min(t1))
```

![image](https://github.com/mepsiess/images-repo/blob/main/26.png?raw=true)

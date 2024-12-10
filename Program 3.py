## Program-3: Write a program to create a pyramid of the character ' * ' and a reverse pyramid.
## Code:

```
def print_pyramid(n):
  for i in range(n):
    # Print Spaces
    print(' ' * (n - i -1), end = '')
    # Print Astericks
    print('*' * (2 * i + 1))

# Number of rows for the pyramid
rows = 5
print("Pyramid:")
print_pyramid(rows)

```

![image](https://github.com/mepsiess/images-repo/blob/main/6.png?raw=true)

```
def print_reverse_pyramid(n):
    for i in range(n, 0, -1):
        # Print Spaces
        print(' ' * (n - i), end = '')
        # Print Astericks
        print('*' * (2 * i - 1))

# Number of rows for the reverse pyramid
rows = 5
print("\nReverse Pyramid:")
print_reverse_pyramid(rows)

```

![image](https://github.com/mepsiess/images-repo/blob/main/7.png?raw=true)

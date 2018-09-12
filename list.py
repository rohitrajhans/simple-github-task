# program to print square

n=int(input("Enter range to find squares:"))
print(*[i**2 for i in range(n+1) if (i % 2) == 0], end='')

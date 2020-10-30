import math

k = 14
j = -4
i = k/j  # division that returns a float.
g = k//j # division that returns a floored answer
m = k%j  # modulo passes the remainder of truncated k/j

print("k = ", k)
print("j = ", j)
print("k/j = ", i)
print("k//j = ", g)
print('k % j = ', m)

print("="*40)
print('k/j truncated: ', math.trunc(k/j))
print('k/j floored: ', math.floor(k/j))
print('k/j rounded: ', round(k/j))
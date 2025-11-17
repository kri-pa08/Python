x = 5        # int
y = 3.5      # float
z = x + y # implicit conversion (int -> float)
print("Implicit:", z, type(z))
num_str = "15"
num_int = int(num_str) # explicit conversion (str -> int)
print("Explicit:", num_int, type(num_int))
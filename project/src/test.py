from Float import Float
f = Float(1, length=64)
print(f.bin_readable)
f = Float('10000000000000000000000000000000')
print(f.bin)
print(f.float)
print(f.bin_readable)
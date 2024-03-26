# - Write a function to pack and return multiple values as a tuple. 
print("")
def pack_values(*args):
    return args
print("Packed multiple values as a tuple 10, \"hello\", [1, 2, 3] ", " -> ", pack_values(10, "hello", [1, 2, 3]))
print("")

# - Write a function to unpack a tuple returned by another function.
def unpack_tuple():
    return pack_values(10, "hello", [1, 2, 3])
print("Unpacked multiple values from a tuple ", pack_values(10, "hello", [1, 2, 3]), " -> ", *unpack_tuple())
print("")
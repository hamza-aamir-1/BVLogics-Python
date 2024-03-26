car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2012
}

# Iterate through all key-value pairs and print them
print("\nIterate all key-value pairs")
for key, val in car.items():
    print(key, " : ", val)

# Print only keys from the dictionary
print("\nPrint only keys")
for key in car.keys():
    print(key)

# Print only values from the dictionary
print("\nPrint only values")
for val in car.values():
    print(val)

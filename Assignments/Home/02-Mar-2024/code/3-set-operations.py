set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1: ", set1)
print("\nSet 2: ", set2)

# Perform union, intersection, and difference operations on two sets
print("\nUnion: ", set1.union(set2))
print("\nIntersection: ", set1.intersection(set2))
print("\nDifference: ", set1.difference(set2))

# Check if one set is a subset of another
print("\nSubset: ", set1.issubset(set2))

# Remove the 4th elements from a set
set1.discard(4)
print("\nRemove 4: ", set1)
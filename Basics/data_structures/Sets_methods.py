# --------------------------------------------
# PYTHON SET METHODS — COMPLETE GUIDE
# --------------------------------------------

# Sample sets for demonstration
set_a = {"Tokyo", "Madrid", "Berlin", "Delhi"}
set_b = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# --------------------------------------------
# 1. union() – Combines all elements, returns new set
# --------------------------------------------
result = set_a.union(set_b)
print("Union:", result)
# Output: {'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}

# --------------------------------------------
# 2. update() – Adds elements from another set into the original set
# --------------------------------------------
set_a.update(set_b)
print("After update():", set_a)
# Output: {'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}

# --------------------------------------------
# 3. intersection() – Returns elements common to both sets
# --------------------------------------------
set_a = {"Tokyo", "Madrid", "Berlin", "Delhi"}
result = set_a.intersection(set_b)
print("Intersection:", result)
# Output: {'Tokyo', 'Madrid'}

# --------------------------------------------
# 4. intersection_update() – Updates original set with common elements
# --------------------------------------------
set_a.intersection_update(set_b)
print("After intersection_update():", set_a)
# Output: {'Tokyo', 'Madrid'}

# --------------------------------------------
# 5. symmetric_difference() – Elements not common in both sets
# --------------------------------------------
set_a = {"Tokyo", "Madrid", "Berlin", "Delhi"}
result = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", result)
# Output: {'Seoul', 'Kabul', 'Berlin', 'Delhi'}

# --------------------------------------------
# 6. symmetric_difference_update() – Updates set with uncommon elements
# --------------------------------------------
set_a.symmetric_difference_update(set_b)
print("After symmetric_difference_update():", set_a)
# Output: {'Kabul', 'Delhi', 'Berlin', 'Seoul'}

# --------------------------------------------
# 7. difference() – Elements in first set but not in second
# --------------------------------------------
set_a = {"Tokyo", "Madrid", "Berlin", "Delhi"}
set_c = {"Seoul", "Kabul", "Delhi"}
result = set_a.difference(set_c)
print("Difference (A - C):", result)
# Output: {'Tokyo', 'Madrid', 'Berlin'}

# --------------------------------------------
# 8. difference_update() – Removes common elements from original set
# --------------------------------------------
set_a.difference_update(set_c)
print("After difference_update():", set_a)
# Output: {'Tokyo', 'Madrid', 'Berlin'}

# --------------------------------------------
# 9. isdisjoint() – True if sets have no items in common
# --------------------------------------------
print("Disjoint Check:", set_a.isdisjoint(set_c))
# Output: True

# --------------------------------------------
# 10. issubset() – True if all elements of set are in another set
# --------------------------------------------
small_set = {"Madrid", "Tokyo"}
print("Is Subset:", small_set.issubset(set_a))
# Output: True

# --------------------------------------------
# 11. issuperset() – True if all elements of another set are in original set
# --------------------------------------------
print("Is Superset:", set_a.issuperset(small_set))
# Output: True

# --------------------------------------------
# 12. add() – Adds a single element to the set
# --------------------------------------------
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print("After add():", cities)
# Output: {'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

# --------------------------------------------
# 13. update() – Add multiple elements from iterable
# --------------------------------------------
cities2 = {"Warsaw", "Seoul"}
cities.update(cities2)
print("After update():", cities)
# Output: {'Tokyo', 'Helsinki', 'Warsaw', 'Madrid', 'Berlin', 'Seoul', 'Delhi'}

# --------------------------------------------
# 14. remove() – Removes specified element (raises error if not found)
# --------------------------------------------
cities.remove("Tokyo")
print("After remove():", cities)
# Output: {...} without 'Tokyo'

# cities.remove("Rome")  # Raises KeyError if uncommented

# --------------------------------------------
# 15. discard() – Removes element if exists (NO error if not found)
# --------------------------------------------
cities.discard("Rome")  # Safe, does nothing if "Rome" not in set

# --------------------------------------------
# 16. pop() – Removes and returns a random element
# --------------------------------------------
sample = {1, 2, 3, 4}
removed_item = sample.pop()
print("Popped item:", removed_item)
print("Remaining after pop():", sample)
# Output: Item removed and rest of set (random order)

# --------------------------------------------
# 17. clear() – Empties the entire set
# --------------------------------------------
sample.clear()
print("After clear():", sample)
# Output: set()

# --------------------------------------------
# 18. del – Deletes the whole set object
# --------------------------------------------
temp = {1, 2, 3}
del temp
# print(temp)  # Uncommenting this will raise NameError

# --------------------------------------------
# 19. Membership Test – Check if item exists
# --------------------------------------------
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
# Output: Carla is present.

# --------------------------------------------
# SUMMARY of KEY NOTES
# --------------------------------------------
# - Sets are unordered and unindexed.
# - No duplicate elements allowed.
# - Set elements must be immutable (like int, str, tuple).
# - You can add, remove, and update sets efficiently.
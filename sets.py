materials = ["flour", "water", "salt", "yeast"]

print(materials)

materials.append("sugar")

print(materials)

materials.append("sugar")

print(materials)


materials_set = set(materials)

print(materials_set)


materials_set.add("egg")
materials_set.add("egg")


frozen_set = frozenset(materials)
print(frozen_set)

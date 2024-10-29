# from typing import List


# names: List[str] = ["Peyman", "Tim", "Saba"]

# if "Nick" in names:
#     print("Hast")
# else:
#     print("Nist")

# names.sort()
# print(names)


from typing import Dict

person: Dict[str, str] = {"first_name": "Peyman", "last_name": "Barjoueian", "age": 33}


# for key, value in person.items():
#     print(f"{key} -> {value}")


d = {0: "zero", 1: "one", 2: "two"}
# print(d.items())

d.update({0: "Test"})

print(d)

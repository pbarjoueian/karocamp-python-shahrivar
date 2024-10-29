# print("Hello World!")

# a = 5
# b = 4
# c = a + b

# print(c)


# Oct 1 2024.
# print("How old are you?")
# name = input()
# print(f"Nice to meet you, {name}")


# print(1, 2, 3, sep=", ", end="\n\n")

# import pprint

# pprint.pprint(
#     [
#         "Mercuy",
#         "Venus",
#         "Earth",
#         "Mars",
#         "Jupiter",
#         "Saturn",
#         "Uranus",
#         "Neptune",
#         "Pluto",
#     ]
# )


# name = input("What is your name?")
# print(name)


# file = open("message.txt", "w", encoding="utf-8")
# file.write("hello\n")
# file.write("world\n")
# file.close()


# import urllib.request

# # make a HTTP request
# req = urllib.request.urlopen("https://en.wikipedia.org")
# # read content as utf-8 string
# content = req.read().decode("utf-8")

# # save to file
# file = open("wikipedia.html", mode="w", encoding="utf-8")
# file.write(content)
# file.close()

# import random
# print(random.randint(1, 6))
# print(random.choice(["heads", "tails"]))

# number = int(input("Please enter a number: "))
# remaining = number % 2
# if remaining == 0:
#     print("Even")
# else:
#     if remaining == 1:
#         print("Odd")

# input_numbers = input()
# numbers = input_numbers.split(",")
# print(numbers)
# x = int(numbers[0])
# y = int(numbers[1])
# print(x)
# print(y)

# age = 18
# is_adult = age >= 18

# # if not is_adult:
# #     print("You can't login to system")

# if is_adult or age >= 19:
#     print("*************")
#     print()
#     input()
# else:
#     print("#############")


seconds = 100000

if seconds >= 1000000:
    print("Greater than 1 milion")
elif seconds >= 10000000:
    print("Greater than 10 milions")
else:
    print("None of these...")

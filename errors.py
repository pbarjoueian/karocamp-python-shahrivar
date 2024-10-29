# number_1: float = 5.0
# number_2: float = 0.0

# try:
#     result: float = number_1 / number_2
# except Exception:
#     print("Divided by zero replaced with 1")
#     number_2 = 1
#     result: float = number_1 / number_2
# print(result)


class DonNotLikeYourNameException(Exception):
    pass


def test(a, b):
    if a < b:
        raise ValueError("test")


try:
    name: str = "Peyman"
    if name == "Peyman":
        raise DonNotLikeYourNameException
except DonNotLikeYourNameException:
    ...

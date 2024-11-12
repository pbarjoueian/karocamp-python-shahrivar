from collections import namedtuple
from enum import Enum

Student = namedtuple("Student", ["name", "age"])
STU = Student("Peyman", 33)

print(STU.age)


class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


print(Day.FRIDAY.value)

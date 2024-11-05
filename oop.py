class Person:
    def __init__(self, first_name: str, last_name: str, birth_year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def print_name(self):
        print(self.first_name.upper() + " " + self.last_name.upper())

    def get_age(self) -> int:
        return 1403 - self.birth_year


class Student(Person):
    total_student_objects = 0

    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_year: int,
        student_id: int,
        password: str,
        major: str,
    ):
        """Initialize the Student object.

        Args:
            student_id (int): Student identifier
            major (str): Name of the major
        """
        super().__init__(
            first_name=first_name, last_name=last_name, birth_year=birth_year
        )
        self.student_id = student_id
        self._major = major
        self.__password = password
        Student.total_student_objects += 1

    def print_name(self):
        print(
            f"{self.major} | {self.student_id}: {self.first_name.upper()} {self.last_name.upper()}"
        )

    @staticmethod
    def get_total_student_objects() -> int:
        return Student.total_student_objects

    @property
    def major(self) -> str:
        return self._major

    @major.setter
    def major(self, new_major: str):
        self._major = new_major
        print("Major has been changed...!")

    def __get_password(self) -> str:
        return self.__password

    def get_hashed_password(self) -> str:
        password = self.__get_password()
        return "!@#$$" + str(password) + "ERFE%$@5252"

    def set_password(self, new_password: str):
        self.__password = new_password
        print("Password has been changed.")


class Employee(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_year: int,
        employee_id: int,
        department_name: str,
    ):
        super().__init__(
            first_name=first_name, last_name=last_name, birth_year=birth_year
        )
        self.employee_id = employee_id
        self.department_name = department_name

    def print_name(self):
        print(
            f"{self.department_name} -> {self.employee_id}:  {self.first_name} {self.last_name}"
        )


# st1 = Student(
#     first_name="Nima",
#     last_name="Jalali",
#     birth_year=1372,
#     student_id=12345,
#     password=1234567,
#     major="Computer Science",
# )

# st2 = Student(
#     first_name="Ahmad",
#     last_name="Mohammadi",
#     birth_year=1370,
#     student_id=54321,
#     password=98765,
#     major="Computer Engineering",
# )

# print(Student.get_total_student_objects())

# print(st1.get_hashed_password())
# st1.set_password(new_password=1234)
# print(st1.get_hashed_password())

# st1.major = "Mathematics"
# print(st1.major)


# emp1 = Employee(
#     first_name="Ahmad",
#     last_name="Ahmadian",
#     birth_year=1372,
#     employee_id=1234567,
#     department_name="HR",
# )


# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# final_list = list(filter(lambda x: (x % 2 != 0), li))
# print(final_list)


# def my_function(name, *args, **kwargs):
#     print(name)
#     for arg in args:
#         print(arg)
#     print(kwargs)


# my_function("Peyman", 2, 3, 4, grade=5, keyword1=4, keyword2="foo")


def print_fullname(first_name, last_name):
    print(first_name + " " + last_name)


my_dict = {"last_name": "Barjoueian", "first_name": "Peyman"}
print_fullname(**my_dict)

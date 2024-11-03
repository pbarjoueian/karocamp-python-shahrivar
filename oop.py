class Person:
    def __init__(self, first_name: str, last_name: str, birth_year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def print_name(self):
        print(self.first_name.upper() + " " + self.last_name.upper())

    def get_age(self) -> int:
        return 1403 - self.birth_year


# person_1 = Person(first_name="Peyman", last_name="Barjoueian", birth_year=1370)
# person_1.print_name()


# person_2 = Person(first_name="Mahsa", last_name="Aminian", birth_year=1385)
# person_2.print_name()


# print(person_1.get_age())
# print(person_2.get_age())


class Student(Person):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_year: int,
        student_id: int,
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
        self.major = major

    def print_name(self):
        print(
            f"{self.major} | {self.student_id}: {self.first_name.upper()} {self.last_name.upper()}"
        )

    def set_major(self, new_major: str):
        self.major = new_major
        print("Major has been changed...!")


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


st1 = Student(
    first_name="Nima",
    last_name="Jalali",
    birth_year=1372,
    student_id=12345,
    major="Computer Science",
)

emp1 = Employee(
    first_name="Ahmad",
    last_name="Ahmadian",
    birth_year=1372,
    employee_id=1234567,
    department_name="HR",
)

st1.print_name()
emp1.print_name()

st1.set_major(new_major="Mathematics")
st1.print_name()

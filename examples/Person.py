
class Person:
    # class variable
    species = "Homo sapiens"

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def greet(self) -> str:
        return f"Hello, my name is {self.full_name}."
    
    def say_hello(self) -> str:
        return "Olá!!!!"

    def __repr__(self) -> str:
        return f"Person({self.first_name!r}, {self.last_name!r}, age={self.age})"

    @classmethod
    def from_full_name(cls, full_name: str, age: int):
        first, *rest = full_name.split()
        last = " ".join(rest) if rest else ""
        return cls(first, last, age)

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18
from Person import Person
from Student import Student

p = Person("Davi", "Novaes", 30)
print(p)
print(p.greet())
print("Species:", p.species)
print("Is adult:", p.is_adult(p.age))

s = Student("Davi", "Novaes", 22, "S12345")
print(s.get_student_info())
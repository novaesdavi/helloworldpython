import Person

p = Person.Person("Davi", "Novaes", 30)
print(p)
print(p.greet())
print("Species:", p.species)
print("Is adult:", p.is_adult(p.age))
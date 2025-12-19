from Person import Person
from Student import Student
from SecondMain import second_main

if __name__ == "__main__":
    import sys
    p = Person(sys.argv[1], sys.argv[2], 30)
    print(p)
    print(p.greet())
    print("Species:", p.species)
    print("Is adult:", p.is_adult(p.age))

    s = Student("Davi", "Novaes", 22, "S12345")
    print(s.get_student_info())

    # Instancia `second_main` para executar seu __init__ e chamar teste()
    second_main()

    print(sys.path)
    

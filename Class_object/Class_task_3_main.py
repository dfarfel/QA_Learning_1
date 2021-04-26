from Class_object.Class_task_3 import Person

person_1 = Person()
person_1.name = "Adam"
person_1.age = 50
person_1.child_num = 2

person_1.print_()

if person_1.hasChildren():
    print(f"{person_1.name} has {person_1.child_num} children")
else:
    print(f"{person_1.name} hasn't childer")

print(person_1.ageGroup())



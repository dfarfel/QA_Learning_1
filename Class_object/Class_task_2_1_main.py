from Class_object.Class_task_2_1 import Animal
cat_1 = Animal("Emi")
user_input=int(input("What I should to do? : 1 - eat, 2 - play, 3 - rest, 0 - end program\n"))
while user_input != 0:
    if user_input == 1:
        cat_1.eat(int(input("How much food?min 50 gram: ")))
        print(cat_1)
        user_input = int(input("What I should to do? : 1 - eat, 2 - play, 3 - rest, 0 - end program\n"))
    elif user_input == 2:
        cat_1.play(int(input("How much time?: ")))
        print(cat_1)
        user_input = int(input("What I should to do? : 1 - eat, 2 - play, 3 - rest, 0 - end program\n"))
    elif user_input == 3:
        cat_1.rest(int(input("How much time?: ")))
        print(cat_1)
        user_input = int(input("What I should to do? : 1 - eat, 2 - play, 3 - rest, 0 - end program\n"))
    else:
        print("You can enter 1,2,3,0 only!")
        user_input = int(input("What I should to do? : 1 - eat, 2 - play, 3 - rest, 0 - end program\n"))
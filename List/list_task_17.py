import sys
string1=input("Enter your first list with comma: ")
string2=input("Enter your second list with comma: ")
list1=string1.split(",")
list2=string2.split(",")
for i in list1:
    for a in list2:
        if a==i:
            print("There is  member in common")
            sys.exit()
print("There is no member in common")
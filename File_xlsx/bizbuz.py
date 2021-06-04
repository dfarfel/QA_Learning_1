list_1 = []
temp_str_1 = ''
temp_str_2 = ''
gen_str = ''
index = -1
trig_1 = False
trig_2 = False
border_1 = 0
border_2 = 0
file_bizbuz_1 = ""
open_bizbuz = open('C://Users/dmoho/Desktop/bizbuz_1.txt', 'r+', encoding='UTF-8')
file_bizbuz = open_bizbuz.read()
open_bizbuz.close()
for char in file_bizbuz:
    if char != "-":
        file_bizbuz_1 += char
    elif char == "-" and not trig_1:
        file_bizbuz_1 += "-"
        trig_1 = True
    elif char == "-" and trig_1:
        file_bizbuz_1 += ":"
        trig_1 = False
print(file_bizbuz_1)
for letter in file_bizbuz_1:
    index += 1
    if letter == "-":
        border_1 = index + 1
    elif letter == ":":
        border_2 = index - 1
    if border_1 != 0 and border_2 != 0:
        temp_str_1 = file_bizbuz_1[border_1:border_2:]
        border_1 = 0
        border_2 = 0
        trig_2 = True

    if trig_2:
        for letter_1 in temp_str_1:
            if letter_1.isnumeric():
                temp_str_2 += letter_1
            elif letter_1 == "ח":
                temp_str_2 += ","
                trig_2 = False
index = -1
border_1 = 0
border_2 = 0
trig_1 = False
trig_2 = False
for digit in temp_str_2:
    index += 1
    if digit.isnumeric() and not trig_1:
        border_1 = index
        trig_1 = True
    elif not digit.isnumeric():
        border_2 = index
        trig_1 = False
    if border_2 != 0:
        list_1.append(int((temp_str_2[border_1:border_2:])))
        border_1 = 0
        border_2 = 0
print(list_1)
print(sum(list_1))

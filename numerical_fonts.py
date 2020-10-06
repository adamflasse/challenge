
#specify each variables that I need 

i = 0
zero = ''
one = ''
two = ''
three = ''
four = ''
five = ''
six = ''
seven = ''
eight = ''
nine = ''



# go through each line of the file and get every characters each 4 lines and store the value in the variable
with open('./assets/numerical_fonts.txt', 'r') as file :
    for row in file:
        i += 1
        if i in range(4):
            zero += row
        if i in range(5,8):
            one += row
        if i in range(9,12):
            two += row
        if i in range(13,16):
            three += row
        if i in range(17,20):
            four += row
        if i in range(21,24):
            five += row
        if i in range(25,28):
            six += row
        if i in range(29,32):
            seven += row
        if i in range(33,36):
            eight += row
        if i in range(37,40):
            nine += row


def check_input(string_to_check):
    if zero in string_to_check:
        return 0
    elif one in string_to_check:
        return 1
    elif two in string_to_check:
        return 2
    elif three in string_to_check:
        return 3
    elif four in string_to_check:
        return 4
    elif five in string_to_check:
        return 5
    elif six in string_to_check:
        return 6
    elif seven in string_to_check:
        return 7
    elif eight in string_to_check:
        return 8
    elif nine in string_to_check:
        return 9
    else: 
        return 'the input is garble, nice try'

with open('./assets/test_numbers.txt', 'r') as fichier:
    list_of_fichier = []
    string_of_fichier = ''
    y = 0
    for line in fichier:
        y += 1
        string_of_fichier += line
        if y % 4 == 0:
            list_of_fichier.append(string_of_fichier)
            string_of_fichier = ''

    for element in list_of_fichier:
        print(check_input(element)) 


    

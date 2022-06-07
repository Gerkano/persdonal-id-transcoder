from datetime import datetime

personal_code=str(input("iveskite koda: "))
code_len = len(personal_code)
count = 1
count2 = 3
c1 = 0
c2 = 0
cent1 = "18"
cent2 = "19"
cent3 = "20"
year1 = personal_code[1:3]
month1 = personal_code[3:5]
day1 = personal_code[5:7]
first_num = int(personal_code[0])
last_num = int(personal_code[10])

if first_num == 1 or first_num == 2:
    year1 = cent1 + year1
elif first_num == 3 or first_num == 4:
    year1 = cent2 + year1
elif first_num == 5 or first_num == 6:
    year1 = cent3 + year1
else:
    print("Wrong input")
    
if code_len == 11:

    # first_num=int(list_of_personal_code[0])
    # b=int(list_of_personal_code[1])
    # c=int(list_of_personal_code[2])
    # d=int(list_of_personal_code[3])
    # e=int(list_of_personal_code[4])
    # f=int(list_of_personal_code[5])
    # g=int(list_of_personal_code[6])
    # h=int(list_of_personal_code[7])
    # j=int(list_of_personal_code[8])
    # k=int(list_of_personal_code[9])
    # last_num=int(list_of_personal_code[10])

    for number in range(code_len-1):
        c1 = c1 + (int(personal_code[number]) * count)
        count = count+1
        if count == 9:
            count = 1
            continue
    
    for number in range(code_len-1):
        c2 = c2 + (int(personal_code[number]) * count2)
        count2 = count2+1
        if count2 == 9:
            count2 = 1
            continue

    controlm1 = c1 % 11
    # controlm1 = ((first_num * 1) + ( b * 2) + ( c * 3 )+ ( d * 4 )+ ( e * 5 ) + ( f * 6 ) + ( g * 7 )+ ( h * 8 ) + ( j * 9 ) + ( k * 1 )) % 11
    controlm2 = c2 % 11
    # controlm2 = (( first_num * 3 ) + ( b * 4)  + ( c * 5) + ( d * 6) + (e * 7) + (f * 8) + (g * 9) + (h * 1) + (j * 2) + (k * 3)) % 11


    def methods():
        if controlm1 == 10:
            if controlm2 == 10:
                return 0
            else:
                return controlm2
        else:
            return controlm1
    z=(methods())

    try:
        date_validity = datetime(int(year1), int(month1), int(day1))
    except:
        print("invalid input")

    if (z == last_num):
        print("Personal code is valid")
    else:
        print("Personal code is not valid")
else:
    print(f"This: {personal_code}  identification number is in wrong format")
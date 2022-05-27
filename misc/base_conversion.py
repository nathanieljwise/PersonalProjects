def base_conversion(user_number, user_base):
    converted_number = []
    for j in range(0,8):
        converted_number = converted_number + [int(user_number % user_base)]
        user_number = int(user_number / user_base)
    converted_number.reverse()
    return converted_number

if __name__ == '__main__':
    user_input = input("Convert what number to what base? ").split()
    dec_number, base = user_input
    dec_number = int(dec_number)
    base = int(base)
    output = base_conversion(dec_number, base)
    output_list = []
    for i in output:
        output_list += str(i)
    output_string = "".join(output_list)
    print("%d in base %d is %s." % (dec_number, base, output_string))
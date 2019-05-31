def run_length_encode(string):
    encoded = []

    run_char, run_length = string[0], 1

    for char in string[1:]:
        if char == run_char:
            run_length += 1
        else:
            encoded.append(str(run_length)+run_char)
            run_char, run_length = char, 1
    
    encoded.append(str(run_length)+run_char)


    return "".join(encoded)


def run_length_decode(string):
    decoded = []

    run_length = 0
    for char in string:
        if char.isdigit():
            run_length *= 10
            run_length += int(char) 

        else:
            decoded.append(char * run_length)
            run_length = 0

    decoded.append(string[-1] * run_length)


    return "".join(decoded)
    

if __name__ == "__main__":
    to_encode = input()
    print(run_length_encode(to_encode))

    to_decode = input()
    print(run_length_decode(to_decode))




def count_lower_upper(input_str):
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    count_lower=0
    count_upper=0
    for i in  input_str:
        if i in lower_case:
            count_lower+=1
        if i in upper_case:
            count_upper+=1

    return {"Lower chars:":count_lower,"Upper chars: ":count_upper}

input_str=str(input("Enter a string: "))
print(count_lower_upper(input_str))


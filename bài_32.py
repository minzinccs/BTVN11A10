def remove_letters_and_spaces(input_string):
    output_string = ""
    for character in input_string:
        if not character.isalpha() and not character.isspace():
            output_string += character
    return output_string

input_string = "Nhập xâu bất kì, in ra sau khi đã xóa hết chữ và cách"
output_string = remove_letters_and_spaces(input_string)
print(output_string)
#các tên gọi theo đúng nghĩa của nó nên đừng hỏi nhiều.
#nghĩa tiếng anh thuần 100% nên tự hiểu đi

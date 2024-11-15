



target_string = "testing line of string"
output_string = "cExampleSTRING dw "


for i in range(len(target_string)):
    output_string += "'"
    output_string += target_string[i]
    output_string += "', "

output_string += "0"
print(output_string)
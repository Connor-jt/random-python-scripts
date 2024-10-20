

input = """
      *(undefined4 *)error_output_buffer = 0x6c756f43;
      *(undefined4 *)(error_output_buffer + 4) = 0x6f6e2064;
      *(undefined4 *)(error_output_buffer + 8) = 0x65642074;
      *(undefined4 *)(error_output_buffer + 0xc) = 0x6d726574;
      *(undefined4 *)(error_output_buffer + 0x10) = 0x20656e69;
      *(undefined4 *)(error_output_buffer + 0x14) = 0x61657453;
      *(undefined4 *)(error_output_buffer + 0x18) = 0x6c63206d;
      *(undefined4 *)(error_output_buffer + 0x1c) = 0x746e6569;
      *(undefined4 *)(error_output_buffer + 0x20) = 0x736e6920;
      *(undefined4 *)(error_output_buffer + 0x24) = 0x6c6c6174;
      *(undefined4 *)(error_output_buffer + 0x28) = 0x72696420;
      *(undefined4 *)(error_output_buffer + 0x2c) = 0x6f746365;
      *(undefined2 *)(error_output_buffer + 0x30) = 0x7972;
      error_output_buffer[0x32] = '.';
      error_output_buffer[0x33] = '\0';
"""

output = ""

def handle_hex_string(hex_str):
    too_output = ""
    byte_count = len(hex_str)//2
    for i in range(byte_count):
        index = (byte_count - 1 - i) * 2 
        hex_byte = hex_str[index] + hex_str[index+1]
        char = bytearray.fromhex(hex_byte).decode()
        too_output += char
    return too_output



from io import StringIO
s = StringIO(input)
for line in s:
    parts = line.split(" = ")
    if len(parts) > 1:
        hex_parts = parts[1].split("0x")
        if len(hex_parts) > 1:
            output += handle_hex_string(hex_parts[1].split(";")[0])
        else:
            output += "\n" + parts[1]

print("GENERATED OUTPUT: ")
print(output)
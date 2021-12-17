filename = '/Users/alisonburgess/Documents/advent of code/2021/day16/test_input.txt'
all_lines = []
with open(filename, 'r') as txtfile:
    for row in txtfile:
        row = row.rstrip()
        all_lines.append(row)

packet_versions = []

def string_to_hex_converter(c_str):
    conversions = { '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 
    'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    converted_string = ''
    for char in c_str:
        converted_string += conversions.get(char)

    return converted_string

def process_hex_string(hex_string, bit_index=0):
    packet_version = hex_string[bit_index:bit_index+3] # version number
    type_ID = int(hex_string[bit_index+3:bit_index+6], 2)
    bit_index += 6

    packet_versions.append(int(packet_version, 2))
    print(sum(packet_versions))

    if type_ID == 4:  # literal value
        value = ''
        while(hex_string[bit_index] == '1'):
            value += hex_string[bit_index+1:bit_index+5]
            bit_index += 5
        value += hex_string[bit_index+1:bit_index+5]
        bit_index += 5
    else:
        length_type_id = hex_string[bit_index]
        bit_index += 1

        if length_type_id == "0":
            field_length = 15
        else:
            field_length = 11

        remaining = int(hex_string[bit_index:bit_index+field_length], 2)
        bit_index += field_length
        while remaining > 0:
            subpacket_length = process_hex_string(hex_string, bit_index) - bit_index
            bit_index += subpacket_length
            remaining -= subpacket_length if field_length == 15 else 1
    return bit_index
                
def part1(cur_string):
    hex_string = string_to_hex_converter(cur_string)
    process_hex_string(hex_string, 0)

if __name__ == "__main__":
    cur_string = str(all_lines[0])
    part1(cur_string)


RETURNED_MESSAGE = """
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
57 
98 
51 
98 
55 
51 
57 
50 
125 
10
"""

def decode_message(message):
    """
    Receives a message and decodes its lines with ASCII table.
    Lines should be separated with '\n'.
    """
    lines_list = message.split('\n')
    # print(lines_list)
    byte_number_list = [int(line) for line in lines_list if line != '']
    # print(byte_number_list)
    return bytes(byte_number_list)


if __name__ == '__main__':
    print(decode_message(RETURNED_MESSAGE))

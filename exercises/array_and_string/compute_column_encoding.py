"""
Compute spreadsheet column encoding: EPI 6.3
"""


def column_encoding_to_integer(column_id):
    int_value = 0

    for i, char in enumerate(column_id):
        # Convert character to integer according to ASCII table
        char_int_value = ord(char) - 64

        # Treat it like base-converter: base-26 to base-10
        int_value += 26 ** (len(column_id) - i - 1) * char_int_value

    return int_value


print(column_encoding_to_integer('AAZ'))

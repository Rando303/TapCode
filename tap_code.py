PolybiusSquare = [['A', 'B', 'C', 'D', 'E'],
                  ['F', 'G', 'H', 'I', 'J'],
                  ['L', 'M', 'N', 'O', 'P'],
                  ['Q', 'R', 'S', 'T', 'U'],
                  ['V', 'W', 'X', 'Y', 'Z']]

def code_to_letter(code):
    code = str(code)
    if code == ' ':
        return code
    if len(code) != 2 or int(code[0]) not in range(1,6) or int(code[1]) not in range(1,6):
        print(f"WARNING: Invalid code: \"{code}\", skipping...")
        return ' '
    return PolybiusSquare[int(code[0])-1][int(code[1])-1]


in_code = [13, 34, 45, 42, 11, 22, 15, ' ', 24, 43, ' ', 33, 34, 44, ' ', 44, 23, 15, ' ',
           11, 12, 43, 15, 33, 13, 15, ' ', 34, 21, ' ', 21, 15, 11, 42, ' ', 12, 45, 44, ' ', 44, 23, 15, ' ',
           13, 11, 35, 11, 13, 24, 44, 54, ' ', 44, 34, ' ', 11, 13, 44, ' ', 14, 15, 43, 35, 24, 44, 15, ' ',
           34, 45, 42, ' ', 21, 15, 11, 42, 43]
out_text = ''
for c in in_code:
    out_text += code_to_letter(c)
print(out_text)


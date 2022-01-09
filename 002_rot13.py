import string

lower = string.ascii_lowercase
print(f'{lower=}')
# letters = string.ascii_letters
# print(f'{letters=}')


def rotate_13(text):
    print(f'    text={text!r:>4}')
    new_text = ''
    for digit in text:
        if digit in lower or digit.lower() in lower:
            position = lower.find(digit.lower())
            # print(f'--({digit}:{position})', end=' ==> ')
            new_position = (position + 13) % 26
            new_digit = lower[new_position] if digit in lower else lower[new_position].upper()
            # print(f'({new_digit}:{new_position})')
            new_text += new_digit
        else:
            new_text += digit
    print(f'{new_text=}')
    

if __name__ == '__main__':
    rotate_13('az')
    rotate_13('Az')
    rotate_13('Za')
    rotate_13('"')
    rotate_13("'")
    rotate_13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}")

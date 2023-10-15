volume_of_disc = 1.44
quantity_of_sheets = 100
quantity_of_strings_in_sh = 50
quantity_of_chars_in_str = 25
char_weight = 4  #байта

volume_of_book = char_weight * quantity_of_chars_in_str * quantity_of_strings_in_sh\
                 * quantity_of_sheets  # в байтах
volume_of_book /= (1024*1024)  # в мегабайтах

print("Количество книг, помещающихся на дискету:", int(volume_of_disc//volume_of_book))

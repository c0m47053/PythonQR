alpha_conversion_table = {
"0" : 0,
"1" : 1,
"2" : 2,
"3" : 3,
"4" : 4,
"5" : 5,
"6" : 6,
"7" : 7,
"8" : 8,
"9" : 9,
"A" : 10,
"B" : 11,
"C" : 12,
"D" : 13,
"E" : 14,
"F" : 15,
"G" : 16,
"H" : 17,
"I" : 18,
"J" : 19,
"K" : 20,
"L" : 21,
"M" : 22,
"N" : 23,
"O" : 24,
"P" : 25,
"Q" : 26,
"R" : 27,
"S" : 28,
"T" : 29,
"U" : 30,
"V" : 31,
"W" : 32,
"X" : 33,
"Y" : 34,
"Z" : 35,
" " : 36,
"$" : 37,
"%" : 38,
"*" : 39,
"+" : 40,
"-" : 41,
"." : 42,
"/" : 43,
":" : 44
}


#def generate_qr():




def get_alpha_bitstream(to_encode):
  character_list = map(lambda x: alpha_conversion_table[x], list(to_encode.upper()))

  character_pairs = zip(*(iter(character_list),) * 2)

  return "".join(map(lambda pair: "{0:b}".format( pair[0] * 45 + pair[1]), character_pairs))


print get_alpha_bitstream("http://www.google.com")






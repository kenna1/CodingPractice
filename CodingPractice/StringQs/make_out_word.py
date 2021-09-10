'''

Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
'''

def make_out_word(out, word):
#get the substring or first two char, store in variable
    first2 = out[0:2]
#get the substring of the last two char, store in variable
    last2 = out[2:4]
#concatenate first2, word, last2 and return
    return first2+word+last2

print(make_out_word('[[]]', 'word'))
def reverse_words(s):
    words = s.split()
    words_reversed =" ".join(words[::-1])
    return words_reversed

st = input("Enter a string: ")
rev_st = reverse_words(st)
print(rev_st)

def reverse_words():
    user_input = input("Enter the sentence")
    split_word = user_input.split(' ')
    print(split_word)
    reverse_word = split_word[::-1]
    print(reverse_word)
    word_join = " ".join(reverse_word)
    print(word_join)


reverse_words()

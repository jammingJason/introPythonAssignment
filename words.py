def print_upper_words(words, must_start_with):
    """ Any word passed to words will be uppercase """ 
    
    for char in must_start_with:
        for word in words:
            if word[0] == char:
                print(word.upper())
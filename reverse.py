"""This file implements solution of codewars exercise 'Reverse Words'."""

def spin_words(phrase: str):
    words = phrase.split()
    new_words = []
    for word in words:
        if len(word) >= 5:
            reverse_word = word[::-1]
            new_words.append(reverse_word)
        else:
            new_words.append(word)
            
    new_phrase = ' '.join(new_words)
    return new_phrase


if __name__ == "__main__":
    
    a = spin_words("The life is beautiful around the world")
    print(a)
def sort_words(s):
    words = s.split()
    words.sort(key=str.lower)
    return ' '.join(words)


result = sort_words('banana ORANGE apple')
print(result)


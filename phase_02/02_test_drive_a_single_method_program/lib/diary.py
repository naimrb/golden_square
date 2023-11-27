def make_snippet(string):
    words = string.split()
    result = ' '.join(words[0:5])

    if len(words) > 5: return result + '...'
    else: return result

def count_words(string):
    words = string.split()
    return len(words)
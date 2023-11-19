def grammar(text):
    formatted = list(text)
    formatted[0] = formatted[0].upper()

    return ''.join(formatted) + '.'
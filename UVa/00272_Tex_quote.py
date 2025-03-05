def convert_quotes(text):
    open_quote = True
    result = []

    for char in text:
        print(char)
        if char == '"':
            if open_quote:
                result.append("``")
            else:
                result.append("''")
            open_quote = not open_quote
        else:
            result.append(char)

    return ''.join(result)

s = input()
print(convert_quotes(s))
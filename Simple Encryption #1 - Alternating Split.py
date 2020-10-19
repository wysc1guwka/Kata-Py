ef decrypt(encrypted_text, n):
    while n > 0:
        try:
            encrypted_text = list(encrypted_text)
        except TypeError:
            return encrypted_text
        new_arr = ['']*len(encrypted_text)
        new_str = ''
        for i in range(0, int((len(encrypted_text)/2))):
            new_arr[2*i+1] = encrypted_text[i]
            encrypted_text[i] = ''
        z = 0
        for i in range(int(len(encrypted_text)/2), len(encrypted_text)):
            new_arr[z] = encrypted_text[i]
            z += 2
        new_str += ''.join(new_arr)
        n -= 1
        if n > 0:
            new_str = decrypt(new_str, n)
        return new_str
    return encrypted_text


def encrypt(text, n):
    while n > 0:
        try:
            text = list(text)
        except TypeError:
            return text
        new_str = ''
        for i in range (1, len(text), 2):
            try:
                new_str += text[i]
                text[i] = ''
            except IndexError:
                break
        new_str += ''.join(text)
        n -= 1
        if n > 0:
            new_str = encrypt(new_str, n)
        return new_str
    return text

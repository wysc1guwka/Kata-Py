def rot13(message):
    key = list('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
    message = list(message)
    for i in range(0, len(message)):
        z = 0
        if message[i].isupper():
            while z < 27:
                if message[i].lower() == key[z]:
                    message[i] = key[z+13].upper()
                    break
                z += 1
        else:
             while z < 27:
                if message[i] == key[z]:
                    message[i] = key[z+13]
                    break
                z += 1
    message_str = ''
    message_str = ''.join(message)
    return message_str
            
                
        

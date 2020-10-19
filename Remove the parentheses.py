import re


def remove_parentheses(s):
    print(s)
    s = re.split('([(]|[)])', s)
    print(s)
    for i in range(0, len(s)):
        if s[i] == '(':
            s[i] = ''
            count = 1
            for z in range(i+1, len(s)):
                if count <= 0:
                    break
                if s[z] == '(':
                    count += 1
                if s[z] == ')':
                    count -= 1
                s[z] = ''
    new_s = ''
    new_s = ''.join([x for x in s])
    return new_s

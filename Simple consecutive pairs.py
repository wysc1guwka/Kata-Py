def pairs(ar):
    count = 0
    for n in range(0, len(ar), 2):
        try:
            if ar[n]+1 == ar[n+1] or ar[n]-1 == ar[n+1]:
                count += 1
        except IndexError:
            break
    return count
    pass

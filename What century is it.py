def what_century(year):
    if str(year)[2] == '0' and str(year)[3] == '0':
        cent = int(str(year)[0] + str(year)[1])
    else:
        cent = int(str(year)[0] + str(year)[1]) + 1
    print(year, cent, str(cent)[1])
    if str(cent)[1] == '1' and str(cent)[0] != '1':
        return str(cent) + "st"
    elif str(cent)[1] == '2' and str(cent)[0] != '1':
        return str(cent) + "nd"
    elif str(cent)[1] == '3' and str(cent)[0] != '1':
        return str(cent) + "rd"
    else:
        return str(cent) + "th"

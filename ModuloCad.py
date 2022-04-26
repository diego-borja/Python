def reemp_char(cad_0,char_0,char_1):
    cad_1 = ""
    for x in cad_0:
        if x == char_0:
            cad_1 += char_1
        else: 
            cad_1 += x
    return cad_1


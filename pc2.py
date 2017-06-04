import string

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb " \
        "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def translate(c):
    if c < "a" or c > "z":
        return c
    else:
        i = ord(c) + 2 - 97
        return chr(i % 26 + 97)


output = map(translate, input)

print "".join(output)

abc = string.ascii_lowercase
trans = string.maketrans(abc, abc[2:] + abc[:2])

print input.translate(trans)
print "map".translate(trans)
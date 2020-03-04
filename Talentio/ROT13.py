def rot13(message):
    special = "!@#$%^&*()1234567890"
    indi = []
    for i in message:
        indi.append(i)
    for i in range(len(indi)):
        if indi[i] not in special:
            k = indi[i]
            if ord(k) in range(78, 91):
                indi[i] = chr(64+13-(90-ord(k)))
            elif ord(k) in range(110, 123):
                indi[i] = chr(96+13-(122-ord(k)))
            else:
                indi[i] = chr(ord(k)+13)
    return ''.join(indi)


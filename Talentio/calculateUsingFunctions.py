def zero(x=None):
    if not x:
        return "0"
    else:
        return eval("0"+x)
def one(x=None):
    if not x:
        return "1"
    else:
        return eval("1"+x)
def two(x=None):
    if not x:
        return "2"
    else:
        return eval("2"+x)
def three(x=None):
    if not x:
        return "3"
    else:
        return eval("3"+x)
def four(x=None):
    if not x:
        return "4"
    else:
        return eval("4"+x)
def five(x=None):
    if not x:
        return "5"
    else:
        return eval("5"+x)
def six(x=None):
    if not x:
        return "6"
    else:
        return eval("6"+x)
def seven(x=None):
    if not x:
        return "7"
    else:
        return eval("7"+x)
def eight(x=None):
    if not x:
        return "8"
    else:
        return eval("8"+x)
def nine(x=None):
    if not x:
        return "9"
    else:
        return eval("9"+x)

def plus(x):
    return ("+"+x)
def minus(x):
    return ("-" + x)
def times(x):
    return ("*" + x)
def divided_by(x):
    return ("//" + x)

print(nine(plus(five())))
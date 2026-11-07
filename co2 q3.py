def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()
def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    if not reg[:2].isalpha():
        return False
    if not reg[2:4].isdigit():
        return False
    if len(reg[4:-4]) not in (1, 2):
        return False
    if not reg[4:-4].isalpha():
        return False
    if not reg[-4:].isdigit():
        return False
    return True
def format_reg(reg):
    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]
for raw in ['tn 09 ab 1234', 'KA-01-M-0007','TN9AB1234', 'TN 22 1234 AB']:
    reg = normalise(raw)
    if is_valid(reg):
        print(f"{raw:15} -> {reg:11} VALID")
    else:
        print(f"{raw:15} -> {reg:11} INVALID")

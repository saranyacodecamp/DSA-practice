def balancedparan(expr:str) -> bool:
    lookup = {'}':'{', 
              ']':'[',
              ')':'(',
            }
    open_paran = ('(','{','[')
    close_paran = (')','}',']')
    stac = []
    for char in expr:
        if char in open_paran:
            stac.append(char)
        elif char in close_paran:
            element = stac.pop()
            if element != lookup[char]:
                return False
        else:
            continue
    if not stac:
        return True
    return False
print(balancedparan("{[a)bc]}"))
print(balancedparan("{(a+b)*c}/d"))

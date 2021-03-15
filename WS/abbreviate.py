def abbreviate(name):
    result = ""
    for n in name.split():
        result += f"({n[0].lower()})"
    return result

print(abbreviate("Joker"))
print(abbreviate("Rap monster"))
print(abbreviate("jin young park"))

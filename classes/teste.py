
letras = ["A", "B", "C", "D"]
codigos = []


count = 1


while len(codigos) < 14:
    for l in letras:
        codigos.append(l+str(count))
        count += 1

print(codigos)
frases = ["En un lugar de la mancha","De alguna manera Palpatine ha vuelto","Luke yo soy tu padre"]
def Titulos(frase):
    return frase.title()

titulo = list(map(Titulos,frases))
print(titulo)
    
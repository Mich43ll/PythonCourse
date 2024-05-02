def no_space(texto):
    nuevo_text = ""
    for char in texto:
        if char != " ":
            nuevo_text += char
    return nuevo_text

def reverse(texto):
    texto_al_reves=""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

print(es_palindromo("Reconocer"))
print(es_palindromo("Hola mundo"))
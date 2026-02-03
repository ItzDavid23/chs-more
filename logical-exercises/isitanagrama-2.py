# Programa that verifies if a word is an anagrama using functions

def anagrama(word1 ,word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if word1 == word2:
        return False
    elif sorted(word1) == sorted(word2):
        return True
    else:
        return False

w1 = str(input("ingrese una palabra: "))
w2 = str(input("Ingrese una segunda palabra: "))

print(anagrama(w1, w2))






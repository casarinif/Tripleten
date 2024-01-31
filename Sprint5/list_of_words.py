# list_of_words.py
def list_of_words(text: str, sep: str = " ") -> list:
    return text.split(sep)

list_of_words("Maria tinha um cordeirinho", sep="a")
print("Hello from list_of_words.py")


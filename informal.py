"""
Prints a informal welcome
"""
from prep import names

artist = "Yoko Ono"
splitted = names.split(artist)
first_name = splitted[0]
print(f"Hi {first_name}")

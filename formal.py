"""
Prints a formal welcome
"""
from prep import names

artist = "Yoko Ono"
splitted = names.split(artist)
last_name = splitted[1]
print(f"Good morning, Ms {last_name}")

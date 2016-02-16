# start Garry's Mod

from time import sleep

switchApp("Garry's Mod")

for i in range(201):
    if not i % 50:
        Debug.user("i=%i" % (i))
    type("q")
    sleep(0.2)



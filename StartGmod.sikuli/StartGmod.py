# start Garry's Mod

import time

# switch to Steam
switchApp("Steam")
click("library.png")
# click("recent.png")
click("garrys_mod.png")
click("steam_play.png")

# wait
time.sleep(15)

#switchApp("Garry's Mod")
wait("start_new_game.png",20)
time.sleep(2)
click("start_new_game.png")

try:
    click("gm_construct.png")
except:
    time.sleep(2)
    click("start_new_game.png")

click("start_game.png")

# wait for level to load
wait(Pattern("construct_tower.png").similar(0.61),15)

for i in range(20):
    type("q")
    time.sleep(0.2)







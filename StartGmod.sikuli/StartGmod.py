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


wait("start_new_game.png",20)
wait(Pattern("g_garrys_mod_mainmenu.png").similar(0.76),5)
time.sleep(1)
click("start_new_game.png")

try:
    click("gm_construct.png")
except:
    time.sleep(2)
    click("start_new_game.png")

click("start_game.png")

# wait for level to load
wait(Pattern("construct_tower.png").similar(0.61),15)







# start Garry's Mod

import time

# switch to Steam
switchApp("Steam")
click("library.png")
# click("recent.png")
click("garrys_mod.png")
click("steam_play.png")

# wait
time.sleep(10)

switchApp("Garry's Mod")
wait("start_new_game.png",20)
click("start_new_game.png")
click("gm_construct.png")
click("start_game.png")







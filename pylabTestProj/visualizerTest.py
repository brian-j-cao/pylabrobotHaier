from pylabrobot.liquid_handling import LiquidHandler
from pylabrobot.liquid_handling.backends import LiquidHandlerChatterboxBackend
from pylabrobot.visualizer.visualizer import Visualizer

from pylabrobot.resources.hamilton import STARLetDeck
from pylabrobot.resources import Resource

from pylabrobot.resources import (
    TIP_CAR_480_A00,
    PLT_CAR_L5AC_A00,
    Cor_96_wellplate_360ul_Fb,
    Tube_CAR_24_A00,
    HTF,
)

lh = LiquidHandler(backend=LiquidHandlerChatterboxBackend(), deck=STARLetDeck())

import asyncio

async def main():
	await lh.setup()


asyncio.run(main())

vis = Visualizer(resource=lh)

async def setup_vis():
	await vis.setup()

asyncio.run(setup_vis())
# Add 4 tube carrier to the Track 3 to 7
tube_car1 = Tube_CAR_24_A00(name="tube carrier 1")
tube_car2 = Tube_CAR_24_A00(name="tube carrier 2")
tube_car3 = Tube_CAR_24_A00(name="tube carrier 3")
tube_car4 = Tube_CAR_24_A00(name="tube carrier 4")
lh.deck.assign_child_resource(tube_car1, rails=3)
lh.deck.assign_child_resource(tube_car2, rails=4)
lh.deck.assign_child_resource(tube_car3, rails=5)
lh.deck.assign_child_resource(tube_car4, rails=6)

tip_car = TIP_CAR_480_A00(name="tip carrier")
tip_car[0] = HTF(name="tips_01")
tip_car[1] = HTF(name="tips_02")

lh.deck.assign_child_resource(tip_car, rails=24)

plt_car = PLT_CAR_L5AC_A00(name="plate carrier")
plt_car[0] = Cor_96_wellplate_360ul_Fb(name="plate_01")
plt_car[1] = Cor_96_wellplate_360ul_Fb(name="plate_02")
# initialize liquid level
plt_car[0].liquid_level = 200
plt_car[1].liquid_level = 150

lh.deck.assign_child_resource(plt_car, rails=8)

lh.summary()



# Visualizer is now set up and ready to use
# add a wait to press enter before continuing
input("Press Enter to continue...")

# Close the visualizer

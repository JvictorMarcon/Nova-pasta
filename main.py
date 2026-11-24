import asyncio

import pygame

from guardiao_seguranca import Game


async def main():
    game = Game(scale=1.0, fullscreen=False)
    while game.running:
        dt = min(game.clock.tick(0) / 1000.0, 0.05)
        game.step(dt)
        await asyncio.sleep(0)
    pygame.quit()


asyncio.run(main())

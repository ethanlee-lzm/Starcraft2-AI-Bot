import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

class WorkerRushBot(sc2.BotAI):
    async def on_step(self, iteration: int):
        if iteration == 0:
            for worker in self.workers:
                worker.attack(self.enemy_start_locations[0])


sc2.run_game(
    sc2.maps.get("AcropolisLE"),
    [Bot(sc2.Race.Zerg, WorkerRushBot()), Computer(sc2.Race.Zerg, sc2.Difficulty.Medium)],
    realtime=True,
)
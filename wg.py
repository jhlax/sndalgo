"""
wg -- wikipedia golf
"""

import datetime
from pathlib import Path

# constants and macros
import yaml

NOW = lambda: '_'.join(str(datetime.datetime.now()).replace(":", "").replace(".", "-").replace("-", "", 2).split())
D_FP = Path(f"./wg_{NOW()}.yml")


# core library classes


class WGBase:
    pass


class Player(WGBase):
    pass


class Route(WGBase):
    pass


class Strokes(WGBase):
    pass


class ScoreCard(WGBase):
    pass


class Page(WGBase):
    pass


class WikipediaGolf(WGBase):
    """
    the wg main object
    """

    fp = None

    def __init__(self, players=None, name=None, **data):
        """
        wg takes player list and data dict options
        """

        if players is None:
            players = ["jack"]
        elif isinstance(players, str):
            players = players.capitalize().split()

        if name is None:
            name = "Parkland Exhibition League " + NOW()
        else:
            name = str(name).capitalize()

        # set instance variables

        self.data = {  # default dictionary for game data
            "name":    name,  # name of the session
            "n_holes": 6,  # holes per session before score and record
            "players": players,
            "scores":  [],  # todo: figure default; add option
            "routes":  [],  # todo: above
            "pages":   [],  # possibly a random page
        }
        self.data.update(data)  # update default with any given data
        self.fp = Path("_".join(name.split(" ")))

    # computed properties

    @property
    def scores(self):
        """
        get {player: score} for each player as defaultdict(0)
        """

        raise NotImplementedError

    #
    # data properties
    #

    @property
    def n_holes(self):
        raise NotImplementedError

    @property
    def players(self):
        return self.data["players"]

    @property
    def scores(self):
        return self.data["scores"]

    @property
    def routes(self):
        return self.data["routes"]

    # @property
    # def holes(self):
    #     return self.data["holes"]

    @property
    def pages(self):
        return self.data["pages"]

    #
    # saving and loading
    #

    def save(self, fp=None):
        """
        save file as yaml.
        """

        if fp is None:
            fp = self.fp
        fp = Path(fp)
        fp = fp.with_suffix(".yml")

        with open(fp, "w+") as f:
            yaml.dump(self.data, f)
            print(f"dumped to {fp.absolute()}")

    @staticmethod
    def load(fp):
        """
        load yaml file to new wg object.
        """
        raise NotImplementedError

    #
    # active game methods
    #

    def new_route(self, f=None, t=None, players=None):  # game affective method
        """
        this creates a new Route from f to t for each player. track forwards and backwards.
        """

        raise NotImplementedError

    def tally(self, player, num=0, route=None):  # player affective method
        """
        adds tally for player at route (or current route). returns players new tally.
        """

        raise NotImplementedError

    def forfeit(self, player, route, val=True):  # player affective method
        """
        sets the players forfeit status for a route.
        """

        raise NotImplementedError

    # class related functions and methods

    @staticmethod
    def route_stat(route, path=None):
        """
        return the difficulty for victory, quickest possible path, percentile for a path given a route.
        """

        raise NotImplementedError

    @staticmethod
    def path_score(route, path):
        """
        returns the score for path on a given route and victory if endpoint reached.
        """

        raise NotImplementedError


WG = WikipediaGolf  # alias

# module members

__all__ = [
    "WGBase",
    "WG",
    "WikipediaGolf",
    "Route",
    "Player",
    "ScoreCard",
    "Strokes",
    "Page",
]

if __name__ == '__main__':
    # main function

    wg = WG()
    wg.save()

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


class Bitcoin:
    """docstring for Bitcoin"""

    def __init__(self, cg):
        self.cg = cg
        self.name = 'bitcoin'


if __name__ == '__main__':
    b = Bitcoin()

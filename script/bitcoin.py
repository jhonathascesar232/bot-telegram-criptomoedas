from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def get_preco(moeda_id: str):
    dic = cg.get_price(moeda_id,  vs_currencies='brl')
    moeda['nome'] = dic.keys()[0]
    moeda['preco'] = dic.values()[0]

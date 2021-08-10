from script.bitcoin import Bitcoin, cg
from pprint import pprint

import logging

LOGGER = logging.getLogger(__name__)


def test_get_coins_list():
    '''
    Testa se o tamanho é igual
    '''
    lista_de_moedas = cg.get_coins_list()
    total_moedas = 8828

    LOGGER.info('Total Moedas: {}'.format(total_moedas))
    assert len(lista_de_moedas) == total_moedas


def test_get_coin_by_id():
    '''
    Testa se o id é igual
    '''
    MOEDA = {
        'id': '0-5x-long-cardano-token',
        'symbol': 'adahalf',
        'name': '0.5X Long Cardano Token'
    }
    moeda_id = cg.get_coins_list()[7]['id']
    assert MOEDA['id'] == moeda_id


def test_get_coins_markets_igual_name():
    '''
    Testa se o nome é igual
    '''
    DOGECOIN = {
        'id': 'dogecoin',
        'symbol': 'doge',
        'name': 'Dogecoin',
        'image': 'https://assets.coingecko.com/coins/images/5/large/dogecoin.png?1547792256',
        'current_price': 1.33,
        'market_cap': 174438414377,
        'market_cap_rank': 7,
        'fully_diluted_valuation': None,
        'total_volume': 15538290756,
        'high_24h': 1.36,
        'low_24h': 1.28,
        'price_change_24h': -0.007115498201,
        'price_change_percentage_24h': -0.53164,
        'market_cap_change_24h': 1436466035,
        'market_cap_change_percentage_24h': 0.83032,
        'circulating_supply': 130799611235.772,
        'total_supply': None,
        'max_supply': None,
        'ath': 3.83,
        'ath_change_percentage': -65.18702,
        'ath_date': '2021-05-08T05:08:23.458Z',
        'atl': 0.00024014,
        'atl_change_percentage': 555139.33203,
        'atl_date': '2014-08-18T00:00:00.000Z',
        'roi': None, 'last_updated':
        '2021-08-10T22:47:10.145Z'
    }
    markets = cg.get_coins_markets('brl')
    dogecoin = [moeda for moeda in markets if moeda['id'] == 'dogecoin'][0]
    assert DOGECOIN['name'] == dogecoin['name']

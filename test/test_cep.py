from script.cep import busca_cep

import logging

LOGGER = logging.getLogger(__name__)


def test_busca_cep():
    cep = '64012335'
    dic = busca_cep(**{"PARM": cep})
    # LOGGER.info('info: {}'.format(dic))

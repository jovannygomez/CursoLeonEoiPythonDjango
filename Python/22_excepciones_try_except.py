from libs.urlloader import load_url
from urllib.error import HTTPError

try:
    raise Exception('esto no funciona ni con dinero')
    print('funcionara ???')

except Exception as error:
    print('ha fallao:', repr(error))
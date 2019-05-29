'''
Dobi API Demo
'''
import time
import collections
import json
import binascii
import urllib.request
import hmac
from hashlib import sha1

class DobiAPI:
    '''
    Dobi API class
    '''
    def __init__(self, access_key, secret_key):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__api_url = 'https://api.dobitrade.com'
        self.__version = '1.0'
        self.__content_type = 'application/x-www-form-urlencoded; charset=UTF-8'
        self.__name_path_map = {}
        self.__add_path_map('myInfo', '/trade/myInfo')
        self.__add_path_map('market', '/market/quote')
        self.__add_path_map('trade_markets', '/trade/markets')
        self.__add_path_map('trade_rules', '/trade/rules')
        self.__add_path_map('myoders', '/trade/myOrders')
        self.__add_path_map('trade_cancel', '/trade/cancel')
        self.__add_path_map('order', '/trade/order')
        self.__request_generateor = {
            'POST': self.__generate_post_request,
            'GET':self.__generate_get_request
        }

    def __add_path_map(self, name, uri):
        self.__name_path_map[name] = self.__api_url + uri

    def __generate_post_request(self, url, query_string):
        request = urllib.request.Request(url)
        request.data = query_string.encode('utf-8')
        request.headers = {
            'Content-Type':self.__content_type
            }
        request.method = 'POST'
        return request

    def __generate_get_request(self, url, query_string):
        url = url + '?' + query_string
        request = urllib.request.Request(url)
        request.method = 'GET'
        return request

    def __hmac_sign(self, raw_string):
        key = self.__secret_key.encode('utf-8')
        value = raw_string.encode('utf-8')
        hashed = hmac.new(key, value, sha1)
        singed = binascii.hexlify(hashed.digest())
        return singed.decode('utf-8')

    def __get_query_string(self, params):
        params['timestamp'] = str(int(time.time()))
        params['accessKey'] = self.__access_key
        params['version'] = self.__version
        ordered_params = collections.OrderedDict(sorted(params.items()))
        query_string = ''
        for key, value in ordered_params.items():
            query_string += key + '=' + value + '&'
        query_string = query_string[:-1]
        sign = self.__hmac_sign(query_string)
        return query_string + '&sign=' + sign

    def api_call(self, action_name, method, params):
        try:
            query_string = self.__get_query_string(params)
            if method not in self.__request_generateor:
                raise 'method not support'
            request = self.__request_generateor[method]( \
                    self.__name_path_map[action_name], \
                    query_string)
            with urllib.request.urlopen(request) as file_object:
                response = file_object.read().decode('utf-8')
            return json.loads(response)
        except Exception as ex:
            raise 'dobi request ex: ' + str(ex)

    def support_action(self):
        for key, value in self.__name_path_map.items():
            print('action : %s, url : %s'%(key, value))

if __name__ == '__main__':
    ACCESS_KEY ='c6ef0e8daba515a8f37470b7c9d70d7a'
    SECRET_KEY ='15859b5e05bc210d34ddbd8609cbeb05'

    api = DobiAPI(ACCESS_KEY, SECRET_KEY)
    api.support_action()

    print(api.api_call('myInfo', 'POST', {})) # empty params
    params = {
	"market": "mcc_btc",
    }
    print(api.api_call('market', 'GET', params))

import requests
from pprint import pprint
from date import Date_and_time



def main():
    url='https://api.stackexchange.com/2.3/questions?site=stackoverflow'
    date=Date_and_time()
    params={'fromdate' : int(float(date.array())),
            'todate' : int(float(date.today())),
            'tagged': 'Python'}
    responce=requests.get(url, params = params)
    pprint(responce.json())


if __name__=='__main__':
    main()
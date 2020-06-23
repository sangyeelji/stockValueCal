import pandas
import requests


class GetCompanyFinacialData:
    __URL  = 'http://kind.krx.co.kr/compfinance/financialinfo.do'
    __POSTDATA = {\
    'A080': 'checkbox',\
    'A110': 'checkbox',\
    'A160': 'checkbox',\
    'A170': 'checkbox',\
    'A180': 'checkbox',\
    'A190': 'checkbox',\
    'A200': 'checkbox',\
    'B020': 'checkbox',\
    'B050': 'checkbox',\
    'B090': 'checkbox',\
    'acntgType': 'I',\
    'arrIsurCd': '00593',\
    'comAbbrv': '',\
    'fininfotype': 'finstat',\
    'finsearchtype': 'finstat',\
    'fiscalgubun': 'accntclosing',\
    'fiscalyear': '2019',\
    'forward': 'list',\
    'method': 'searchFinancialInfoOfSomeCorps',\
    'orderMode': 'A080',\
    'orderStat': 'D',\
    'searchCodeType':'',\
    'searchCorpName': '005930',\
    'titleofaccnt': 'A080|A110|A160|A170|A180|A190|A200'}
    
    def __init__(self):
        res = requests.post(GetCompanyFinacialData.__URL,data = GetCompanyFinacialData.__POSTDATA)
        print(res.text)
        
if __name__ == '__main__':
    parsedData = GetCompanyFinacialData()
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
    'arrIsurCd': '',\
    'comAbbrv': '',\
    'fininfotype': 'finstat',\
    'finsearchtype': 'finstat',\
    'fiscalgubun': 'accntclosing',\
    'fiscalyear': '',\
    'forward': 'list',\
    'method': 'searchFinancialInfoOfSomeCorps',\
    'orderMode': 'A080',\
    'orderStat': 'D',\
    'searchCodeType':'',\
    'searchCorpName': '',\
    'titleofaccnt': 'A080|A110|A160|A170|A180|A190|A200'}
    __START_YEAR = 1996
    __END_YEAR = 2020
    
    def __init__(self,stockCode):
        GetCompanyFinacialData.__POSTDATA['arrIsurCd'] = stockCode
        
        for i in range(GetCompanyFinacialData.__START_YEAR,GetCompanyFinacialData.__END_YEAR):
            GetCompanyFinacialData.__POSTDATA['fiscalyear'] = str(i)
            res = requests.post(GetCompanyFinacialData.__URL,data = GetCompanyFinacialData.__POSTDATA)
            companyFinacialDataList = pandas.read_html(res.text)
            self.financialDataInfoDf = companyFinacialDataList[0]
            self.financialDataInfoDf.columns = ['index','CompanyName','자산총계','부채총계','자본총계','매출액','영업이익','법인세차감전계속사업이익','당기순이익']
            print(self.financialDataInfoDf.loc[0])

        
if __name__ == '__main__':
    parsedData = GetCompanyFinacialData('00593')
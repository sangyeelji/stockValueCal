import pandas
import os
import requests
'''
https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage 홈페이지로 접속
Excel 버튼을 누를떄 chrom http trace를 이용해서 post 정보를을 캡쳐
해당 URL을 아래 __URL에 저장.
'''
class GetCompanyData:
    __URL  = ('http://kind.krx.co.kr/corpgeneral/corpList.do?'+
    'beginIndex=&'+
    'comAbbrv=&'+
    'comAbbrvTmp=&'+
    'currentPageSize=5000&'+
    'fiscalYearEnd=all&'+
    'marketType=&'+
    'method=download&'+
    'orderMode=3&'+
    'orderStat=D&'+
    'pageIndex=1&'+
    'repIsuSrtCd:&'+
    'searchCodeType:&'+
    'searchType=13')
    __SAVEDIR    = 'CompanyDataDir'
    
    def __init__(self):
        print(GetCompanyData.__URL)
        res = requests.get(GetCompanyData.__URL)
        print(res.text)

if __name__ == '__main__':
    companyData = GetCompanyData()

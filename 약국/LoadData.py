#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse
from openpyxl import load_workbook
import http.client
import folium
import webbrowser

DAILY = (0,)
WEEKLY = (1,)

THEATERnum = 0
THEATERID = 4
THEATERname = 15
THEATERstartdate = 5
THEATERlastdate = 18
THEATERstate = 6
THEATERcall = 10
THEATERaddress = 13
THEATERx = 19
THEATERy = 20
THEATERtype = 21



def LoadXMLFromDrug(page=1, city="", city1="",numOfPage=500):
    Data = None
    url = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown"
    key = "wq6dVQ3VqCjAjojine1n1bkftuuo1wptdEttrYpuzR2OBJ%2B7g3%2FnL0CsRu%2BhcpGkDmHkZO5DhwD4AkVp3UQWzw%3D%3D"
    url = url + "?serviceKey=" + key
    if city != None:
        url = url + "&Q0=" + urllib.parse.quote(city)
    if city1 != None:
        url = url + "&Q1=" + urllib.parse.quote(city1)
    url = url + "&pageNo=" + str(page) + "&numOfRows=" + str(numOfPage)
    data = urllib.request.urlopen(url).read()
    
    Data = BeautifulSoup(data, "html.parser")

    listChungNam = []
    listChungBuk = []
    listSeoul = []
    listKyungki = []
    listKangwon = []
    listKyungBuk = []
    listKyungNam = []
    listJunBuk = []
    listJunNam = []
    listJeJu = []

    listDaejun=[];
    listUlsan=[];
    listGwangju=[];
    listincheon=[];
    listDaegu=[];
    listBusan=[];

    for data in Data.find_all("item"):
        if "서울특별시" in data.dutyaddr.string:
            listSeoul.append(data);
        elif "경기도" in data.dutyaddr.string:
            listKyungki.append(data);
        elif "충청남도" in data.dutyaddr.string:
            listChungNam.append(data);
        elif "충청북도" in data.dutyaddr.string:
            listChungBuk.append(data);
        elif "강원도" in data.dutyaddr.string:
            listKangwon.append(data);
        elif "경상남도" in data.dutyaddr.string:
            listKyungNam.append(data);
        elif "경상북도" in data.dutyaddr.string:
            listKyungBuk.append(data);
        elif "전라남도" in data.dutyaddr.string:
            listJunNam.append(data);
        elif "전라북도" in data.dutyaddr.string:
            listJunBuk.append(data);

        elif "대전광역시" in data.dutyaddr.string:
            listDaejun.append(data);
        elif "대구광역시" in data.dutyaddr.string:
            listDaegu.append(data);
        elif "울산광역시" in data.dutyaddr.string:
            listUlsan.append(data);
        elif "광주광역시" in data.dutyaddr.string:
            listGwangju.append(data);
        elif "인천광역시" in data.dutyaddr.string:
            listincheon.append(data);
        elif "부산광역시" in data.dutyaddr.string:
            listBusan.append(data);
        elif "제주특별자치도" in data.dutyaddr.string:
            listJeJu.append(data);

        
  

    listAll=[listSeoul, listKyungki,listChungNam, listChungBuk, listKangwon, listKyungNam, listKyungBuk, listJunNam, listJunBuk,
             listDaejun, listDaegu, listUlsan, listGwangju, listincheon, listBusan, listJeJu];
    return listAll


def LoadXMLFromFileBoxOffice(type, date):

    Data = None
    savename = "BoxOffice.xml"
    if type == DAILY:
        url = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?serviceKey=wq6dVQ3VqCjAjojine1n1bkftuuo1wptdEttrYpuzR2OBJ%2B7g3%2FnL0CsRu%2BhcpGkDmHkZO5DhwD4AkVp3UQWzw%3D%3D&pageNo=1&numOfRows=10"
    else:
        url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.xml"
    key = "-"
    url = url + "?key=" + key +"&targetDt=" + str(date)
    data = urllib.request.urlopen(url).read()
  
    Data = BeautifulSoup(data, "html.parser")
    return Data

def LoadXMLFromFileMovieInfo(code):
    # 영화 코드로 조회하는 영화 상세정보 movieCd값
    Data = None
    savename = "MovieInfo.xml"
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.xml"
    key = "e4ef9cc26c8da2fbd710c5899e835cd7"
    url = url + "?key=" + key +"&movieCd=" + str(code)
    data = urllib.request.urlopen(url).read()

    Data = BeautifulSoup(data, "html.parser")
    return Data

def LoadXMLFromFileMovieList(page, name):
    # 영화 목록
    Data = None
    savename = "MovieList.xml"
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml"
    key = "70fb64767aa3cd31fb488fe55820bf17"
    url = url + "?key=" + key + "&curPage=" + str(page) + "&itemPerPage=50"
    if name != None:
        name = urllib.parse.quote(name)
        url = url + "&movieNm=" + name
        #url = url.encode('utf-8')
    data = urllib.request.urlopen(url).read()
    req.urlretrieve(url, savename)

    xml = open(savename, "r", encoding="utf-8").read()
    Data = BeautifulSoup(xml, "html.parser")
    return Data


def LoadXLSFromFileTheater():
    Data = load_workbook(filename = "Theater.xlsx")
    Data = Data.worksheets[0]
    return Data

def NaverAPI():
    server = 'openapi.naver.com'
    client_id = 'CauJEcypbFDul3iDdw3V'
    client_secret = '1gsH15h8bj'
    conn = http.client.HTTPSConnection(server)
    conn.request('GET', '/v1/serch/book.xml?query=love&display=10&start=1',None,
                 {'X-Naver-Clinet-Id':client_id, 'X-Naver-Client-Secret':client_secret})
    req = conn.getresponse()
    cLen = req.getheader("Content-Length")
    req.read(int(cLen))

# tkinter 버튼 함수
# command로 인자받는법 : 람다함수 사용
# command = lambda index = i: func(index)

if __name__ == '__main__':
    Data = LoadXMLFromDrug("서울시","강남", 1, None, 1, 20)
    for data in Data.find_all("item"):
        print(data.dutyaddr.string)

    #map_osm = folium.Map (location = [37.568477, 126.981611],zoom_start=13)
# 마커 지정
    #folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
# html 파일로 저장
    #map_osm.save('osm.html')
    #webbrowser.open_new('osm.html')
else:
    pass
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.ttk
from tkinter import font
import tkinter.messagebox
import LoadData
import http.client
import folium
import webbrowser
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

class Interface:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

        self.notebook = tkinter.ttk.Notebook(window, width = self.width, height = self.height-100)
        
        self.frame = Search(window)
        self.frame1 = E_MAIL(window)
 
        self.notebook.add(self.frame.GetFrame(), text = "정보 검색")
        self.notebook.add(self.frame1.GetFrame(), text = "통계 및 이메일")

    def SetPhotoImage(self):#아이콘 불러오기
        pass
    def Draw(self):
        self.notebook.place(x = 10, y = 20)
        self.frame.Draw()
        

class Search:
    def __init__(self, window):
        self.frame = Frame(window,width = 800, height = 600, bd = 2, relief = "solid")
        self.frame1 = Frame(self.frame, width = 300, height = 400, bd = 2, relief = "solid")

        self.frame2 = Frame(self.frame, width = 400, height = 300, background = "orange")
        self.frame3 = Frame(self.frame, width = 400, height = 300, background = "light blue", bd = 2, relief = "solid")

        self.ListboxScrollbar = Scrollbar(self.frame1)
        self.Listbox = Listbox(self.frame1, width = 45, height = 25, bd = 2, relief = "solid", yscrollcommand = self.ListboxScrollbar)
        self.ListboxScrollbar["command"] = self.Listbox.yview

        self.ListboxScrollbar2=Scrollbar(self.frame2);
        self.Listbox2=Listbox(self.frame2, width = 45, height = 10, bd = 2, relief = "solid", yscrollcommand = self.ListboxScrollbar2)
        self.ListboxScrollbar2["command"] = self.Listbox2.yview

        self.City1Name = ""
        self.City2Name = ""

        tempFont = font.Font(self.frame1, size = 9, weight = 'bold', family = 'Consolas')
        mainText = Label(self.frame1, font = tempFont, text = "[전국 약국정보 검색]")
        mainText.pack()
     
        Label(self.frame1, text = "시/도").place(x=70, y=20)
        self.e1 = Entry(self.frame1, width = 15)
        self.e1.pack(side = TOP)

        Label(self.frame1, text = "구/시/군").place(x=60, y=40)
        self.e2 = Entry(self.frame1, width = 15)
        self.e2.pack(side = TOP)
    
        self.button = Button(self.frame1, text = "검색", command=self.Searching)
        self.button.place(x = 230, y = 27)
        self.button1=Button(self.frame1, text="지도", command=self.ClickIndex)
        self.button1.pack(side=TOP)
        self.button2=Button(self.frame1, text="위치", command=self.ClickAdd)
        self.button2.pack(side=TOP)

        self.button2=Button(self.frame2, text="북마크 추가", command=self.BookMark);
        self.button2.place(x=0, y=20)
        self.button3=Button(self.frame2, text="북마크 삭제", command=self.BookMarkDel)
        self.button3.pack(side=LEFT);

        self.label4=Label(self.frame3, text="이름: ");
        self.label4.place(x=0,y=0);
        self.label1=Label(self.frame3, text="주소: ");
        self.label1.place(x=0,y=20);
        self.label2=Label(self.frame3, text="건물명: ");
        self.label2.place(x=0, y=40);
        self.label3=Label(self.frame3, text="전화번호: ");
        self.label3.place(x=0, y=60);

        self.e3=Entry(self.frame3, width=50);
        self.e4=Entry(self.frame3, width=50);
        self.e5=Entry(self.frame3, width=30);
        self.e6=Entry(self.frame3, width=50);

        self.e6.place(x=40,y=0);
        self.e3.place(x=40, y=20)
        self.e4.place(x=40, y=40)
        self.e5.place(x=60, y=60)

        self.BookMark=[];
        self.AllList=[];
        self.AllList=LoadData.LoadXMLFromDrug()

        for i in self.AllList:
            i.sort(key=lambda obj:obj.dutyaddr.string)
               

    def Draw(self):
        self.frame1.pack(side = LEFT)
        self.frame2.place(x=350, y=0) #orange
        self.frame3.place(x=350, y=230) #light Blue
        self.Listbox.pack(side = LEFT)
        self.Listbox2.pack(side = LEFT)
        self.ListboxScrollbar.pack(side=RIGHT, fill="y")
        self.ListboxScrollbar2.pack(side=RIGHT, fill="y")
    def Searching(self):
        self.Listbox.delete(0,'end');
        self.City1Name = self.e1.get()
        self.City2Name = self.e2.get()
        self.i = 0

        if self.City1Name=="서울특별시":
            for k in self.AllList[0]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="경기도":
            for k in self.AllList[1]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;  
                    
        elif self.City1Name=="충청남도":
            for k in self.AllList[2]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="충청북도":
            for k in self.AllList[3]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="강원도":
            for k in self.AllList[4]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;

        elif self.City1Name=="경상남도":
            for k in self.AllList[5]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;

        elif self.City1Name=="경상북도":
            for k in self.AllList[6]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;

        elif self.City1Name=="전라남도":
            for k in self.AllList[7]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="전라북도":
            for k in self.AllList[8]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;

        elif self.City1Name=="대전광역시":
            for k in self.AllList[9]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="대구광역시":
            for k in self.AllList[10]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="울산광역시":
            for k in self.AllList[11]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="광주광역시":
            for k in self.AllList[12]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="인천광역시":
            for k in self.AllList[13]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="부산광역시":
            for k in self.AllList[14]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
        elif self.City1Name=="제주특별자치도":
            for k in self.AllList[15]:
                if self.City2Name in k.dutyname.string:
                    self.Listbox.insert(self.i,k.dutyaddr.string);
                    self.i+=1;
      
    def GetFrame(self):
        return self.frame
    def ClickAdd(self):
        self.e3.delete(0,'end')
        self.e4.delete(0,'end')
        self.e5.delete(0,'end')
        self.e6.delete(0, 'end');
        try:
            self.index=self.Listbox.get(self.Listbox.curselection(), self.Listbox.curselection());
            self.index=self.index[0];
            for i in self.AllList:
                for j in i:
                    if self.index in j.dutyaddr.string:
                        self.e6.insert(0, j.dutyname.string);
                        self.e3.insert(0, j.dutyaddr.string)
                        self.e4.insert(0, j.dutymapimg.string)
                        self.e5.insert(0, j.dutytel1.string)
                        global name, address, buliding, phoneNum
                        name = self.e6.get()
                        address = self.e3.get()
                        buliding = self.e4.get()
                        phoneNum = self.e5.get()
                        break;
        except:
            name = self.e6.get()
            address = self.e3.get()
            buliding = self.e4.get()
            phoneNum = self.e5.get()
            pass
        try:
            self.index=self.Listbox2.get(self.Listbox2.curselection(), self.Listbox2.curselection());
            self.index=self.index[0];
            for i in self.AllList:
                for j in i:
                    if self.index in j.dutyaddr.string:
                        self.e6.insert(0, j.dutyname.string);
                        self.e3.insert(0, j.dutyaddr.string)
                        self.e4.insert(0,j.dutymapimg.string)
                        self.e5.insert(0, j.dutytel1.string)
                        name = self.e6.get()
                        address = self.e3.get()
                        buliding = self.e4.get()
                        phoneNum = self.e5.get()
                        break;
        except:
            name = self.e6.get()
            address = self.e3.get()
            buliding = self.e4.get()
            phoneNum = self.e5.get()
            pass
    def ClickIndex(self):
        try:
            self.index=self.Listbox.get(self.Listbox.curselection(), self.Listbox.curselection());
            self.index=self.index[0];
            for i in self.AllList:
                for j in i:
                    if self.index in j.dutyaddr.string:
                        self.lat=eval(j.wgs84lat.string);
                        self.lon=eval(j.wgs84lon.string);
                        
                        map_osm = folium.Map (location = [self.lat, self.lon],zoom_start=13)
                        folium.Marker([self.lat, self.lon], popup='Mt. Hood Meadows').add_to(map_osm)
                        map_osm.save('osm.html')
                        webbrowser.open_new('osm.html')
                        break;
        except:
            self.index=None;
        try:
            self.bookMarkIndex=self.Listbox2.get(self.Listbox2.curselection(), self.Listbox2.curselection());
            self.bookMarkIndex=self.bookMarkIndex[0];
            for i in self.AllList:
                for j in i:
                    if self.bookMarkIndex in j.dutyaddr.string:
                        self.lat=eval(j.wgs84lat.string);
                        self.lon=eval(j.wgs84lon.string);

                        map_osm = folium.Map (location = [self.lat, self.lon],zoom_start=13)
                        folium.Marker([self.lat, self.lon], popup='Mt. Hood Meadows').add_to(map_osm)
                        map_osm.save('osm.html')
                        webbrowser.open_new('osm.html')
                        break;
        except:
            self.bookMarkIndex=None;
    def BookMark(self):
        try:
            self.bookindex=0;
            self.index=self.Listbox.get(self.Listbox.curselection(), self.Listbox.curselection());
            self.index=self.index[0];
            for i in self.AllList:
                for j in i:
                    if self.index in j.dutyaddr.string:
                        self.BookMark.append(j)
                        self.Listbox2.insert(self.bookindex,j.dutyaddr.string)
                        self.bookindex+=1;
        except:
            pass;
    def BookMarkDel(self):
        try:
            self.bookindex=0;
            self.bookindex=self.Listbox2.get(self.Listbox2.curselection(), self.Listbox2.curselection());
            self.bookindex=self.bookindex[0];
            for i in self.AllList:
                for j in i:
                    if self.bookindex in j.dutyname.string:
                        self.BookMark.remove(j)
                        self.Listbox2.delete(self.Listbox2.curselection())
        except:
            pass


class E_MAIL:
    def __init__(self, window):
        self.frame = Frame(window, width = 800, height = 600)

        self.frame1 = Frame(self.frame)
        self.frame1.pack(side = LEFT)

        Canvas(self.frame1, width = 500, height = 350, bg = "white").pack(side = TOP)
        Button(self.frame1, text = "그래프 출력", command = self.DrawGraph).pack(side = BOTTOM)

        self.frame2 = Frame(self.frame)
        self.frame2.pack(side = LEFT)
        
        Label(self.frame2, text = "이메일 입력: ").grid(row = 0, column = 0)
        self.entry1 = Entry(self.frame2)
        self.entry1.grid(row = 0, column = 1)

        Button(self.frame2, text = "약국 정보 메일로 보내기", command = self.SendEmail).grid(row = 1, column = 1)

    def GetFrame(self):
        return self.frame

    def SendEmail(self):
        #global value
        host = "smtp.gmail.com" # Gmail STMP 서버 주소.
        port = "587"
        htmlFileName = "osm.html"
        
        senderAddr = "kyongmin96@gmail.com"     # 보내는 사람 email 주소.
        recipientAddr = self.entry1.get()  # 받는 사람 email 주소.

        text = "이름: " + name + '\n' + "주소: " + address + '\n' + "건물명: " + buliding + '\n' + "전화번호: " + phoneNum

        msg = MIMEText(text)
        msg['Subject'] = "요청한 약국 정보를 전송했습니다."
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        
        # MIME 문서를 생성합니다.
        htmlFD = open(htmlFileName, 'rb')
        HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )

        htmlFD.close()
        
        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        #msg.attach(HtmlPart)
        
        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("kyongmin96@gmail.com","whRkqudtls96")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

    def DrawGraph(self):
        pass
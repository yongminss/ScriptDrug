from tkinter import *
from tkinter.font import *
from LoadData import *
import LoadData


class List():
    def __init__(self, window, width, height):
        self.name = None
        self.page = 1
        self.width = width
        self.height = height
        self.SearchFrame = Frame(window, bd=2, relief="solid", background="light yellow")
        self.framesearch1 = Frame(self.SearchFrame, width=self.width / 2, height=100, bd=0, relief="solid",
                                  background="light yellow")
        self.framesearch2 = Frame(self.SearchFrame, width=self.width / 2, height=self.height, bd=0, relief="solid",
                                  background="light yellow")
        self.framelist = Frame(self.SearchFrame, width=330, height=350, background="white")
        self.listscrollbar = Scrollbar(self.framemovielist)
        self.listbox = Listbox(self.framemovielist, width=46, height=22, bd=6, relief="ridge",
                                    yscrollcommand=self.movielistscrollbar.set)
        self.listscrollbar["command"] = self.movielistbox.yview
        self.infocanvas = Canvas(self.framesearch2, width=self.width / 2 - 10, height=500, bd=4, relief="ridge",
                                      background="light yellow")

        self.SearchFrameLabel = Label(self.framesearch1, font=("Impact", 25, "bold"), text="상세 정보")

        self.search = Entry(self.framesearch1, font=("HYHeadLine", 15, "bold"), width=31, bd=6, relief="ridge")
        self.searchbutton = Button(self.SearchFrame, font=("HYHeadLine", 14, "bold"), text="검색", width=6,
                                        bd=3, command = self.Search)
        self.nextbutton = Button(self.SearchFrame, font=("HYHeadLine", 10, "bold"), text="다음 페이지", bd=3,
                                      width=9, command=self.NextMovie)
        self.prevbutton = Button(self.SearchFrame, font=("HYHeadLine", 10, "bold"), text="이전 페이지", bd=3,
                                      width=9, command=self.PrevMovie)
        self.infobutton = Button(self.SearchFrame, font = ("HYHeadLine", 10, "bold"), text = "상세 정보", bd = 3,
                                 width = 9, command = self.Info)
        self.ListData = LoadXMLFromFileMovieList(self.movielistpage, self.moviename)
        i = 0
        for data in self.ListData.find_all("movie"):
            self.listbox.insert(i, data.nm.string)
            i += 1

    def Search(self):
        self.name = self.search.get()
        print(self.name)
        self.ResetList()

    def Info(self):
        try:
            self.searchname = self.listbox.get(self.listbox.curselection(),self.listbox.curselection())
        except:
            self.searchname = None

    def Next(self):
        self.listpage += 1
        self.ResetList()
    def Prev(self):
        if self.listpage > 1:
            self.listpage -= 1
        self.ResetList()

    def ResetList(self):
        self.ListData = LoadXMLFromFileMovieList(self.listpage, self.name)

        self.listbox.delete(0, 49)
        i = 0
        for data in self.ListData.find_all("movie"):
            self.listbox.insert(i, data.nm.string)
            i += 1

    def Render(self):
        self.framesearch2.pack(side=RIGHT, anchor="ne", fill="y", expand=True)
        self.framesearch1.pack(anchor="nw", fill="both", expand=True)
        self.framelist.pack(anchor="sw")
        self.movielistscrollbar.pack(side=RIGHT, fill="y")
        self.movielistbox.pack(anchor="s")
        self.movieinfocanvas.pack(side=RIGHT)
        self.SearchFrameLabel.place(x=10, y=10)
        self.search.place(x=0, y=62)
        self.searchbutton.place(x=355, y=60)
        self.nextbutton.place(x=355, y=110)
        self.prevbutton.place(x=355, y=140)
        self.infobutton.place(x=355, y= 170)

    def GetFrame(self):
        return self.SearchFrame

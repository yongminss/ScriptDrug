from tkinter import *
from Interface import *


def main():
    window=Tk();
    window.title("Medicine");
    window.geometry("940x600+400+200");
    window.resizable(False, False);

    menu=Interface(window, 800, 600);
    menu.Draw();

    window.mainloop();


main();
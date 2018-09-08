from tkinter import *
import operator

window = Tk()
window.title("Remik")
window.geometry('500x300')

btn_list = []
entries = []
gracze = []
runda = 0
wynikidict = {}
przegr = []
wygr = ""


def inputGraczy():
    test = int(txt.get())
    print(test)
#   btn2 = Button(window, text="OK")
#   btn2.grid(column=1, row=3)
    for x in range(0, test):
        ent = Entry(window)
        gra = Label(window, text="Gracz " + str(x + 1))
        gra.grid(column=0, row=1 + x)
        ent.grid(column=1, row=1 + x)
        entries.append(ent)
        if x == test - 1:
            btn2 = Button(window, text="OK", command=Destroy)
            btn2.grid(column=0, row=x + 2)  # Przycisk w tej samej kolumnie
            print(entries)


def Destroy():
    x = 1
    y = 1
    global runda
    runda += 1
    print(runda)
    for i in entries:
        print(i)
        print(i.get())
        gracze.append(i.get())
        wynikidict[i.get()] = 0

    window.winfo_children()
    for widget in window.winfo_children():
        widget.destroy()

    run = Label(window, text="Runda " + str(runda))
    run.grid(column=0, row=0)

    kto = Label(window, text="Kto wygrał?")
    kto.grid(column=0, row=1)

    for g in gracze:
        wygr = Button(window, text=g)
        wygr.grid(column=1 + x, row=1)
        wygr.bind("<Button-1>", onClick)
        btn_list.append(wygr)
        x += 1


def Destroy2():
    x = 1
    y = 1
    global runda
    runda += 1

    window.winfo_children()
    for widget in window.winfo_children():
        widget.destroy()

    run = Label(window, text="Runda " + str(runda))
    run.grid(column=0, row=0)

    kto = Label(window, text="Kto wygrał?")
    kto.grid(column=0, row=1)

    for g in gracze:
        wygr = Button(window, text=g)
        wygr.grid(column=1 + x, row=1)
        wygr.bind("<Button-1>", onClick)
        btn_list.append(wygr)
        x += 1
# def Wygrany():
#   ile = Label(window, text="Ile kart zostało?")
#    ile.grid(column=0, row=2)
#    graczeTemp.remove()
#    for g in graczeTemp:
#        gracz = Label(window, text=g)
#        gracz.grid(column=0, row=y)
#        y += 1


def onClick(event):
    del entries[:]
    global wygr
    y = 4
    btn = event.widget  # event.widget is the wid get that called the event
    print(btn.cget("text"))  # Print the text for the selected button
    print(gracze)
    kto = Label(window, text="Ile kart zostało?")
    kto.grid(column=0, row=2)
    for gracz in gracze:
        if gracz != btn.cget("text"):
            ileLabel = Label(window, text=gracz)
            ileLabel.grid(column=0, row=y)
            karty = Entry(window, width=3)
            karty.grid(column=1, row=y)
            entries.append(karty)
            y += 1
            przegr.append(gracz)
        elif gracz == btn.cget("text"):
            wygr = gracz
    dalej = Button(window, text="OK", command=wyniki)
    dalej.grid(column=0, row=y + 1)


def wyniki():
    suma = 0
    i = 11
    for w, n in zip(entries, przegr):
        suma += int(w.get())
        wynikidict[n] -= int(w.get())
    wynikidict[wygr] += suma
    print(wygr)

    print(wynikidict)

    wynikLabel = Label(window, text="Wyniki: ")
    wynikLabel.grid(column=0, row=10)
    for oo in wynikidict:
        wyni = Label(window, text=oo + " : " + str(wynikidict[oo]))
        wyni.grid(column=0, row=i)
        i += 1
    nastepna = Button(window, text="Następna runda", command=Destroy2)
    nastepna.grid(column=0, row=i + 1)
    koniec = Button(window, text="Koniec gry", command=Kon)
    koniec.grid(column=1, row=i + 1)


def Kon():
    t = Toplevel(height=300, width=300)
    t.title("Wygrani")
    o = 1
    zwyciezca = Label(t, text="Zwycięzcą jest " +
                      str(max(wynikidict.items(), key=operator.itemgetter(1))[0]))
    zwyciezca.grid(column=0, row=0)
    sorted_by_value = sorted(wynikidict.items(), key=lambda kv: -kv[1])
    print(sorted_by_value )
    for oo in sorted_by_value:
        reszta = Label(t, text=oo)
        reszta.grid(column=0, row=o)
        o += 1


lbl = Label(window, text="Ile osób będzie grać")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

btn = Button(window, text="OK", command=inputGraczy)
btn.grid(column=2, row=0)

window.mainloop()

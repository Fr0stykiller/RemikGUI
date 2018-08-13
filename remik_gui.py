from tkinter import *

window = Tk()
window.title("Remik")
window.geometry('350x200')

#def liczbaGraczy():
#	ilosc = txt.get()
#	print(ilosc)

def inputGraczy():
	test = int(txt.get())
	print(test)
	#btn2 = Button(window, text="OK")
	#btn2.grid(column=1, row=3)
	for x in range(0, test):
		ent = Entry(window)
		ent.insert(10, "Gracz " + str(x+1))
		ent.grid(column=0, row=1+x)
		if x == test - 1:
			btn2 = Button(window, text="OK")
			btn2.grid(column=0, row=x+2) #Przycisk w tej samej kolumnie
			print(window.winfo_children())
			print(window.window_names())
			#window.destroy(<tkinter.Entry object .!entry5>)
			for widget in window.winfo_children():
			    widget.destroy()

	



lbl = Label(window, text="Ile osób będzie grać?")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

btn = Button(window, text="OK", command=inputGraczy)
btn.grid(column=2, row=0)



window.mainloop()
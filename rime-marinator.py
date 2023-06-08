from tkinter import *
import rime_marinator_app as rm

class Rime_Marinator(object):
	def __init__(self):	
		self.okno = Tk()
		self.okno.geometry("1024x600")
		self.okno.title("Rime Marinator")
		self.background_colour = '#121212'
		self.okno["bg"] = self.background_colour
		
		self.etykieta1 = Label(self.okno, font=("Verdana",18,"bold"), foreground='white',background='#272727',text='Rime Marinator - Słownik rymów')
		self.etykieta1.place(x=0,y=0,width=1024,height=64)
		self.okno.mainloop()
		
def main():
	rime_marinator = Rime_Marinator()
main()

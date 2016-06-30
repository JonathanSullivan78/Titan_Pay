from tkinter import *
import tkinter
import src.accounting.run_payroll
import src.views.main_gui


class RunPayrollGUI:

    def __init__(self):

        def ok_button():
            self.main_window.destroy()
            src.views.main_gui.MainGUI()

        self.main_window = tkinter.Tk()

        self.bottom_frame = tkinter.Frame(self.main_window)

        canvas = Canvas(width=1250, height=720, bg='black')

        canvas.pack(expand=YES, fill=BOTH)

        gif2 = PhotoImage(file='../src/images/wallpaper.gif')
        canvas.create_image(0, 0, image=gif2, anchor=NW)

        response = Label(canvas, text= 'Payroll Process Complete' , fg='white', bg='black')
        response.pack
        response_window = canvas.create_window(448, 335, anchor=NW, window=response)

        start_button = Button(canvas, text="Return to Main Menu", command=ok_button, anchor=W)
        start_button.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        start_button_window = canvas.create_window(450, 375, anchor=NW, window=start_button)

        quit_button = Button(canvas, text='Quit', command=self.main_window.destroy, anchor=W)
        quit_button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        quit_button_window = canvas.create_window(1080, 600, anchor=NW, window=quit_button)

        tkinter.mainloop()
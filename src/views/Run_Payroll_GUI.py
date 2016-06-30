from tkinter import *
import tkinter
import src.accounting.run_payroll
import src.views.main_gui
import src.views.payroll_complete_gui


class RunPayrollGUI:

    def __init__(self):

        def run_payroll_button():
            self.main_window.destroy()
            src.accounting.run_payroll.RunPayroll()
            src.views.payroll_complete_gui.RunPayrollGUI()

        def cancel_payroll_button():
            self.main_window.destroy()
            src.views.main_gui.MainGUI()

        self.main_window = tkinter.Tk()

        self.bottom_frame = tkinter.Frame(self.main_window)

        canvas = Canvas(width=1250, height=720, bg='black')

        canvas.pack(expand=YES, fill=BOTH)

        gif2 = PhotoImage(file='../src/images/wallpaper.gif')
        canvas.create_image(0, 0, image=gif2, anchor=NW)

        start_button = Button(canvas, text="Start Daily Payroll", command=run_payroll_button, anchor=W)
        start_button.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        start_button_window = canvas.create_window(450, 375, anchor=NW, window=start_button)

        cancel_button = Button(canvas, text="Cancel", command=cancel_payroll_button, anchor=W)
        cancel_button.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        cancel_button_window = canvas.create_window(650, 375, anchor=NW, window=cancel_button)

        #quit_button = Button(canvas, text='Quit', command=self.main_window.destroy, anchor=W)
        #quit_button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        #quit_button_window = canvas.create_window(1080, 600, anchor=NW, window=quit_button)

        tkinter.mainloop()
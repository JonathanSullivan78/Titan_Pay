from tkinter import *
import tkinter
import src.accounting.run_payroll

class ApplicationGUI:

    def __init__(self):

        def payroll_button():
            self.main_window.destroy()
            PayRollGUI()

        self.main_window = tkinter.Tk()

        self.bottom_frame = tkinter.Frame(self.main_window)

        canvas = Canvas(width = 1250, height = 720, bg = 'black')

        canvas.pack(expand = YES, fill = BOTH)

        gif1 = PhotoImage(file = 'application.gif')
        canvas.create_image(0, 0, image = gif1, anchor = NW)

        run_payroll_button = Button(canvas, text = "Run Payroll", command = payroll_button, anchor = W)
        run_payroll_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        run_payroll_button_window = canvas.create_window(1080, 408, anchor=NW, window=run_payroll_button)

        quit_button = Button(canvas, text = 'Quit', command = self.main_window.destroy, anchor = W)
        quit_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        quit_button_window = canvas.create_window(1080, 600, anchor = NW, window = quit_button)

        tkinter.mainloop()

class PayRollGUI:

    def __init__(self):

#        def cancel_button():
#            self.main_window.destroy()
#            applicationgui

        def start_daily_payroll_button():
            src.accounting.run_payroll.run_payroll()

        self.main_window = tkinter.Tk()

        self.bottom_frame = tkinter.Frame(self.main_window)

        canvas = Canvas(width=1250, height=720, bg='black')

        canvas.pack(expand=YES, fill=BOTH)

        gif2 = PhotoImage(file='wallpaper.gif')
        canvas.create_image(0, 0, image=gif2, anchor=NW)

        button1 = Button(canvas, text="Start Daily Payroll", command=start_daily_payroll_button(), anchor=W)
        button1.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button1_window = canvas.create_window(550, 375, anchor=NW, window=button1)

#        cancel_button = Button(canvas, text='Cancel', command=self.main_window.destroy, anchor=W)
#        cancel_button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
#        cancel_button_window = canvas.create_window(550, 600, anchor=NW, window=cancel_button)

        quit_button = Button(canvas, text='Quit', command=self.main_window.destroy, anchor=W)
        quit_button.configure(width=10, activebackground="#33B5E5", relief=FLAT)
        quit_button_window = canvas.create_window(1080, 600, anchor=NW, window=quit_button)

        tkinter.mainloop()

applicationgui = ApplicationGUI()

from tkinter import *
import tkinter
import src.views.Run_Payroll_GUI


class ApplicationGUI:

    def __init__(self):

        def payroll_button():
            self.main_window.destroy()
            src.views.Run_Payroll_GUI.RunPayrollGUI()


        self.main_window = tkinter.Tk()

        self.bottom_frame = tkinter.Frame(self.main_window)

        canvas = Canvas(width = 1250, height = 720, bg = 'black')

        canvas.pack(expand = YES, fill = BOTH)

        gif1 = PhotoImage(file = '../src/images/application.gif')
        canvas.create_image(0, 0, image = gif1, anchor = NW)

        run_payroll_button = Button(canvas, text = "Run Payroll", command = payroll_button, anchor = W)
        run_payroll_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        run_payroll_button_window = canvas.create_window(1080, 408, anchor=NW, window=run_payroll_button)

        quit_button = Button(canvas, text = 'Quit', command = self.main_window.destroy, anchor = W)
        quit_button.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
        quit_button_window = canvas.create_window(1080, 600, anchor = NW, window = quit_button)

        tkinter.mainloop()

applicationgui = ApplicationGUI()

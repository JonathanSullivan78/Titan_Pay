from tkinter import *
import tkinter
import tkinter.messagebox
import src.views.run_payroll_gui
import src.utilities.import_employees
import src.utilities.import_receipts
import src.utilities.import_timecards


class MainGUI:

    def __init__(self):

        def payroll_button():
            self.main_window.destroy()
            src.views.run_payroll_gui.RunPayrollGUI()

        def import_employee_button():
            src.utilities.import_employees.import_employees()
            tkinter.messagebox.showinfo('Import Employees Process', 'Import Complete.')

        def import_timesheets_button():
            src.utilities.import_timecards.import_timecards()
            tkinter.messagebox.showinfo('Import Time Cards Process', 'Import Complete.')

        def import_receipts_button():
            src.utilities.import_receipts.import_receipts()
            tkinter.messagebox.showinfo('Import Receipts Process', 'Import Complete.')

        self.main_window = tkinter.Tk()

        self.bottom_frame = tkinter.Frame(self.main_window)

        canvas = Canvas(width = 1250, height = 720, bg = 'black')

        canvas.pack(expand = YES, fill = BOTH)

        gif1 = PhotoImage(file = '../src/images/application.gif')
        canvas.create_image(0, 0, image = gif1, anchor = NW)

        run_payroll_button = Button(canvas, text = "Run Payroll", command = payroll_button, anchor = W)
        run_payroll_button.configure(width = 12, activebackground = "#33B5E5", relief = FLAT)
        run_payroll_button_window = canvas.create_window(1070, 458, anchor=NW, window=run_payroll_button)

        import_employee_button = Button(canvas, text = "Import Employees", command = import_employee_button, anchor = W)
        import_employee_button.configure(width = 12, activebackground = "#33B5E5", relief = FLAT)
        import_employee_button_window = canvas.create_window(1070, 308, anchor=NW, window=import_employee_button)
        
        import_timesheets_button = Button(canvas, text = "Import Time Cards", command = import_timesheets_button, anchor = W)
        import_timesheets_button.configure(width = 12, activebackground = "#33B5E5", relief = FLAT)
        import_timesheets_button_window = canvas.create_window(1070, 358, anchor=NW, window=import_timesheets_button)
        
        import_receipts_button = Button(canvas, text = "Import Receipts", command = import_receipts_button, anchor = W)
        import_receipts_button.configure(width = 12, activebackground = "#33B5E5", relief = FLAT)
        import_receipts_button_window = canvas.create_window(1070, 408, anchor=NW, window=import_receipts_button)

        quit_button = Button(canvas, text = 'Quit', command = self.main_window.destroy, anchor = W)
        quit_button.configure(width = 12, activebackground = "#33B5E5", relief = FLAT)
        quit_button_window = canvas.create_window(1070, 600, anchor = NW, window = quit_button)

        tkinter.mainloop()

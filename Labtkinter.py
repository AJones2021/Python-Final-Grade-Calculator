#
# Anna Jones
# 09/12/2023
# Using tkinter to create a simple GUI
#

import tkinter as tk
import tkinter.messagebox as mb
class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Grade Calculator')
        self.main_window.geometry('400x200')

        self.frame1 = tk.Frame(self.main_window)
        self.frame2 = tk.Frame(self.main_window)
        self.frame3 = tk.Frame(self.main_window)
        self.frame4 = tk.Frame(self.main_window)
        self.frame5 = tk.Frame(self.main_window)

        self.test_label = tk.Label(self.frame1, text='Tests Grade: ')
        self.test_label.pack(side='left')
        self.test_entry =tk.Entry(self.frame1, width=10)
        self.test_entry.pack(side='left')
        self.frame1.pack(side='top')

        self.lab_label = tk.Label(self.frame3, text='Labs Grade: ')
        self.lab_label.pack(side='left')
        self.lab_entry = tk.Entry(self.frame3, width=10)
        self.lab_entry.pack(side='left')
        self.frame3.pack(side='top')

        self.exam_label = tk.Label(self.frame2, text='Exams Grade:')
        self.exam_label.pack(side='left')
        self.exam_entry = tk.Entry(self.frame2, width=10)
        self.exam_entry.pack(side='left')
        self.frame2.pack(side='top')

        self.grading_label = tk.Label(self.frame4, text='Grade Average: ')
        self.output = tk.StringVar()
        self.output_label = tk.Label(self.frame4, textvariable=self.output)

        self.grading_label.pack(side='left')
        self.output.set('--------')
        self.output_label.pack(side='left')
        self.frame4.pack(side='top')

        self.calc_button = tk.Button(self.frame5, text='Calculate',command=self.calc_Results)
        self.quit_button = tk.Button(self.frame5, text='Quit',command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.frame5.pack(side='top')

        tk.mainloop()
    def calc_Results(self):

        twenty_perc = .20
        thirdy_perc = .30
        fifty_perc = .50
        try:
            results = (float(self.test_entry.get()) * twenty_perc) + (float(self.lab_entry.get()) * thirdy_perc) + (float(self.exam_entry.get()) * fifty_perc)

            if results >= 90.0:
                self.output.set(f'{results: .2f} (A)')
            if results > 79.9 and results < 90:
                self.output.set(f'{results: .2f} (B)')
            if results > 69.9 and results < 80:
                self.output.set(f'{results: .2f} (C)')
            if results > 59.9 and results < 70:
                self.output.set(f'{results: .2f} (D)')
            if results < 59.9:
                self.output.set(f'{results: .2f} (F)')
        except ValueError:
            mb.showerror("ValueError", "Invalid input, try again")
my_gui = MyGUI()
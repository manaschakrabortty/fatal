from tkinter import Tk, StringVar, ttk
from tkinter import *
import tkinter.messagebox          # For Message Box
import time                        # For Date and Time
import requests as req             # For requests
from bs4 import *                  # For BeautifulSoup


countries = ['US Dollar','Indian Rupee','Euro',
'Pakistani Rupee','Turkish Lira',
'Kuwaiti Dinar','Saudi Arabian Riyal',
            'Chinese Yuan Renminbi','Canadian Dollar',
    'Australian Dollar']


class currency_converter:

    def __init__(self, BaseAll):

        #main screen
        self.BaseAll = BaseAll
        self.BaseAll.title("Currency Converter")
        self.BaseAll.geometry("1400x670+0+0") #height and width of our main screen
        self.BaseAll.configure(background = '#2B7A77')



        # All variables that used in code
        date_today = StringVar()
        value0 = StringVar()
        value1 = StringVar()
        insert_value = DoubleVar()
        convert_value = DoubleVar()
        scale_insert = DoubleVar()
        scale_convert = DoubleVar()
        insert_value.set(1)
        date_today.set(time.strftime("%d/%m/%y"))


        # Function to exit or end everything
        def exit_window():
            exit_window = tkinter.messagebox.askyesno("Exit System", "Confirm if you want to exit")
            if (exit_window > 0):
                BaseAll.destroy()
                return


        # Function to reset everything in the screen and set to default
        def reset_all():
            value0.set("")
            value1.set("")
            insert_value.set(1)
            convert_value.set("0.00")
            scale_insert.set(0)
            scale_convert.set(0)



        # Function to convert currencies
        def value_converted():
            input_currency = value0.get()
            output_currency = value1.get()
            web_page = req.get(set_currency())
            beautiful_soap = BeautifulSoup(web_page.text, 'html.parser')
            rate_currency = beautiful_soap.find('table', class_ = 'tablesorter ratesTable').find('td', text = lambda x : x == output_currency).find_next('td').get_text()
            x = float(insert_value.get() * float(rate_currency))
            Final_value = str('%.2f' %(x))
            convert_value.set(Final_value)
            # giving currencies values to scale
            scale_insert.set(insert_value.get())
            scale_convert.set(Final_value)
            return Final_value

        def set_currency():
            input_currency = value0.get()

            if(input_currency == 'US Dollar'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=USD&amount=1"
            elif(input_currency == 'Indian Rupee'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=INR&amount=1"
            elif(input_currency == 'Euro'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=EUR&amount=1"
            elif(input_currency == 'Pakistani Rupee'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=PKR&amount=1"
            elif(input_currency == 'Australian Dollar'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=AUD&amount=1"
            elif(input_currency == 'Canadian Dollar'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=CAD&amount=1"
            elif(input_currency == 'Chinese Yuan Renminbi'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=CNY&amount=1"      
            elif(input_currency == 'Saudi Arabian Riyal'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=SAR&amount=1"
            elif(input_currency == 'Kuwaiti Dinar'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=KWD&amount=1"
            elif(input_currency == 'Turkish Lira'):
                Uniform_resource_locator = "https://www.x-rates.com/table/?from=TRY&amount=1"          
            return Uniform_resource_locator




        # Frame making in the gui
        Title_frame = Frame(self.BaseAll, bd = 10, width = 1350, height = 100, padx = 10, pady = 10, bg = "#3AAFA9", relief = RIDGE)
        Title_frame.grid(row = 0, column = 0)

        self.Title_lbl = Label(Title_frame, text = "Currency Converter", padx = 17, pady = 4, bd = 1, font = ('Lucida Console', 30, 'bold'), bg = "#2B7A77", fg ="#DEF2F1" , width = 50)
        self.Title_lbl.pack()

        Main_frame = Frame(self.BaseAll, bd = 10, width = 1350, height = 800, padx = 11, pady = 10, bg = "#3AAFA9", relief = RIDGE)
        Main_frame.grid(row = 1, column = 0)

        Frame_ScaleL = Frame(Main_frame, bd = 4, width = 100, height = 600, padx = 5, pady = 1, bg = "#3AAFA9", relief = RIDGE)
        Frame_ScaleL.grid(row = 0, column = 0)

        Frame_ScaleR = Frame(Main_frame, bd = 4, width = 100, height = 600, padx = 5, pady = 1, bg = "#3AAFA9", relief = RIDGE)
        Frame_ScaleR.grid(row = 0, column = 2)

        Frame_2 = Frame(Main_frame, bd = 4, width = 800, height = 600, padx = 0, pady = 2, bg = "#3AAFA9", relief = RIDGE)
        Frame_2.grid(row = 0, column = 1)

        Frame_2Top = Frame(Frame_2, width = 250, height = 300, bd = 4, padx = 80, pady = 2, bg = "#3AAFA9", relief = RIDGE)
        Frame_2Top.grid(row = 0, column = 0)

        Frame_2Buttom = Frame(Frame_2, width = 800, height = 300, bd = 4, padx = 5, pady = 2, bg = "#3AAFA9", relief = RIDGE)
        Frame_2Buttom.grid(row = 1, column = 0)

        Frame_2ButtomL = Frame(Frame_2Buttom, width = 450, height = 300, bd = 4, padx = 0, pady = 2, bg = "#3AAFA9", relief = RIDGE)
        Frame_2ButtomL.grid(row = 0, column = 0)

        Frame_2ButtomR = Frame(Frame_2Buttom, width = 350, height = 300, bd = 4, padx = 10, pady = 2, bg = "#3AAFA9", relief = RIDGE)
        Frame_2ButtomR.grid(row = 0, column = 1)


        # Names of group members
        self.name1 = Label(Frame_2ButtomL, font = ('Mongolian Baiti', 20, 'bold'), text = '-----------------------------\n-----------------------------\n|          Python         |\n|     Project    |\n|          Real-Time        |\n|        Currency Converter      |\n-----------------------------\n-----------------------------\n', padx = 2, pady = 10, bg = "#3AAFA9", fg = "#DEF2F1", bd = 2, width = 18)
        self.name1.grid(row = 0, column = 0)


        # Prints date
        self.date_title = Label(Frame_2Top, font = ('Mongolian Baiti', 20, 'bold'), text = 'Todays Date', padx = 2, pady = 10, bg = "#3AAFA9", fg = "#DEF2F1", bd = 2, width = 18)
        self.date_title.grid(row = 0, column = 0)
        self.Date_print = Label(Frame_2Top, font = ('Mongolian Baiti', 20, 'bold'), textvariable = date_today, padx = 2, pady = 10, bg = "#3AAFA9", fg = "#DEF2F1", bd = 2, width = 12, justify = 'center')
        self.Date_print.grid(row = 0, column = 1)


        # Scale on right side
        self.Converted = Scale(Frame_ScaleR, variable = scale_convert, from_ = 0, to = 3000, length = 500, tickinterval = 150, orient = VERTICAL, bg = '#2B7A77', fg = "#DEF2F1", label = "converted value", font = ('Microsoft Yi Baiti', 12))
        self.Converted.grid(row = 0, column = 0, rowspan = 2)

        # Scale on Left side
        self.Inserted = Scale(Frame_ScaleL, variable = scale_insert, from_ = 0, to = 3000, length = 500, tickinterval = 150, orient = VERTICAL, bg = '#2B7A77', fg = "#DEF2F1", label = "inserted value", font = ('Microsoft Yi Baiti', 12))
        self.Inserted.grid(row = 0, column = 0, rowspan = 2)

        # Selection of currency that we want to convert
        self.input_currency = ttk.Combobox(Frame_2Top, textvariable = value0, state = 'readonly', font = ('Myriad Arabic', 20, 'bold'), width = 20,justify = 'center')
        self.input_currency['values'] = countries
        self.input_currency.current(0)
        self.input_currency.grid(row = 1, column = 0, padx = 38, pady = 10 )
    
        # making a box in gui to enter the value of currency to convert
        self.EntCurrency = Entry(Frame_2Top, font = ('Myriad Arabic', 20, 'bold'), textvariable = insert_value, bd = 2, width = 23, justify = 'center')
        self.EntCurrency.grid(row = 1, column = 1, pady = 10)



        # Selection of currency in which we want to convert
        self.output_currency = ttk.Combobox(Frame_2Top, textvariable = value1, state = 'readonly', font = ('Myriad Arabic', 20, 'bold'), width = 20, justify = 'center')
        self.output_currency['values'] = countries
        self.output_currency.current(0)
        self.output_currency.grid(row = 2, column = 0, padx = 38, pady = 10)

        # making a box in gui which the conerted value of our currency
        self.lblCurrency = Label(Frame_2Top, font = ('Myriad Arabic', 20, 'bold'), textvariable = convert_value, bd = 2, width = 20, bg = 'white', pady = 2, padx = 2, relief = 'sunken')
        self.lblCurrency.grid(row = 2, column = 1)



        # Button to convert currencies
        self.btnconvert = Button(Frame_2ButtomR, text = "Convert Currency", padx = 2, pady = 8, bd = 2, bg = "#3AAFA9", fg = "#DEF2F1", font = ('Mongolian Baiti', 20, ), width = 14, height = 2, command = value_converted)
        self.btnconvert.grid(row = 4, column = 0)

        # Button to reset everything
        self.btnReset = Button(Frame_2ButtomR, text = "Reset All", padx = 2, pady = 7, bg = "#3AAFA9", fg = "#DEF2F1", font = ('Mongolian Baiti', 20,), width = 14, height = 2, command = reset_all)
        self.btnReset.grid(row = 5, column = 0)

        # Button to exit or kill the program
        self.btnExit = Button(Frame_2ButtomR, text = "Exit", padx = 2, pady = 8, bg = "#3AAFA9", fg = "#DEF2F1", font =('Mongolian Baiti', 20,), width = 14, height = 2, command = exit_window)
        self.btnExit.grid(row = 6, column = 0)



if __name__ == "__main__":
    BaseAll = Tk()                  
    app_main_converter = currency_converter(BaseAll)    
    BaseAll.mainloop()
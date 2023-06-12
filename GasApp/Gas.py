from tkinter import *
from tkinter import messagebox
import pickle



BG = 'Black'
FG = 'White'

app = Tk()
app.title('Gas App')
app.resizable(False, False)
app['background'] = BG

# Function to save the entries into a pickle file
def save_entries():
    entries = {
        'tank_size': tank_size_entry.get(),
        'usd_gas_price': usd_gas_price_entry.get(),
        'cad_gas_price': cad_gas_price_entry.get(),
        'one_gallon': one_gallon_entry.get(),
        'one_usd': one_usd_entry.get()
    }
    with open('entries.pickle', 'wb') as file:
        pickle.dump(entries, file)
    messagebox.showinfo('Save Entries', 'Entries saved successfully.')

# Function to load the entries from the pickle file
def load_entries():
    try:
        with open('entries.pickle', 'rb') as file:
            entries = pickle.load(file)
        tank_size_entry.delete(0, END)
        tank_size_entry.insert(0, entries['tank_size'])
        usd_gas_price_entry.delete(0, END)
        usd_gas_price_entry.insert(0, entries['usd_gas_price'])
        cad_gas_price_entry.delete(0, END)
        cad_gas_price_entry.insert(0, entries['cad_gas_price'])
        one_gallon_entry.delete(0, END)
        one_gallon_entry.insert(0, entries['one_gallon'])
        one_usd_entry.delete(0, END)
        one_usd_entry.insert(0, entries['one_usd'])
        messagebox.showinfo('Load Entries', 'Entries loaded successfully.')
    except FileNotFoundError:
        messagebox.showerror('Load Entries', 'Entries file not found.')

def get_savings():
    # Calculate the cost of filling the tank in the USA
    tank_size_gallons = float(tank_size_entry.get()) / float(one_gallon_entry.get())
    usd_cost = float(tank_size_gallons) * float(usd_gas_price_entry.get()) * float(one_usd_entry.get())

    # Calculate the cost of filling the tank in Canada
    cad_cost = float(tank_size_entry.get()) * float(cad_gas_price_entry.get())

    # Determine the cheaper option
    if usd_cost < cad_cost:
        cheaper_option = "United States"
        savings = cad_cost - usd_cost
    else:
        cheaper_option = "Canada"
        savings = usd_cost - cad_cost

    message = f'''
    Gas Price Comparison Results:\n
    ====================\n
    It is cheaper to buy gas in {cheaper_option}\n
    You would save ${round(savings, 2)}\n
    USA purchase cost: ${round(usd_cost, 2)} cannadian\n
    CAD purchase cost: ${round(cad_cost, 2)} cannadian\n
    '''
    messagebox.showinfo('Gas Savings', message)
    


tank_size_lbl = Label(app, text='Gas Tank Size(litres):', 
                      font=('', 9, 'bold'), background= BG, foreground= FG
                      )
tank_size_lbl.grid(row=0, column=0)

tank_size_entry = Entry(app, justify='center', font=('', 9, 'bold'))
tank_size_entry.grid(row=0, column=1)

usd_gas_price_lbl = Label(app, text=' '*11 +'USD Gas Price:',
                          font=('', 9, 'bold'), background= BG, foreground= FG
                          )
usd_gas_price_lbl.grid(row=1, column=0)

usd_gas_price_entry = Entry(app, justify='center', font=('', 9, 'bold'))
usd_gas_price_entry.grid(row=1, column=1)

cad_gas_price_lbl = Label(app, text=' '*11 +'CAD Gas Price:',
                          font=('', 9, 'bold'), background= BG, foreground= FG
                          )
cad_gas_price_lbl.grid(row=2, column=0)

cad_gas_price_entry = Entry(app, justify='center', font=('', 9, 'bold'))
cad_gas_price_entry.grid(row=2, column=1)


one_gallon_lbl = Label(app, text=' '*19 +'1 Gallon =',
                       font=('', 9, 'bold'), background= BG, foreground= FG
                       )
one_gallon_lbl.grid(row=3, column=0)


one_gallon_value = IntVar()
one_gallon_value.set(3.78541)
one_gallon_entry = Entry(app, justify='center', textvariable= one_gallon_value, font=('', 9, 'bold'))
one_gallon_entry.grid(row=3, column=1)

one_usd_lbl = Label(app, text=' '*23 +'1 USD =',
                    font=('', 9, 'bold'), background= BG, foreground= FG
                    )
one_usd_lbl.grid(row=4, column=0)

one_usd_entry = Entry(app, justify='center', font=('', 9, 'bold'))
one_usd_entry.grid(row=4, column=1)

calculate_btn = Button(app, text='Calculate', command=get_savings, 
                       border=6, font=('', 10, 'bold'), width=15
                       )
calculate_btn.grid(row=5, column=1, pady=10, padx=5)

save_btn = Button(app, text='Save Entries', command=save_entries, 
                  border=6, font=('', 10, 'bold'), width=15
                  )
save_btn.grid(row=6, column=0, pady=5, padx=5)

load_btn = Button(app, text='Load Entries', command=load_entries, 
                  border=6, font=('', 10, 'bold'), width=15
                  )
load_btn.grid(row=6, column=1, pady=5, padx=5)


app.mainloop()
from tkinter import *
from tkinter import messagebox


from reading_file import *
from helper_functions import *
arr = file_reading()

stops_chunk = train_and_stops(arr) #list of stops as a chunk
#print(stops_chunk)
sep_list = stops_seperator(stops_chunk) #sorted out list of stops
#print(sep_list)
trains = list_of_trains(sep_list) #list containing the names of trains
#print(trains)
trains_as_keys = add_nodes({}, trains) # dict creation of trains as keys
#print(trains_as_keys)
add_edges(trains_as_keys, sep_list)
#print(trains_as_keys) # This is the final version of the dict with train as keys
stops_ = list_of_stops(sep_list)
#print(stops_)

window = Tk()

#title
window.title('VIA Travel Planner')  
window.configure(background='white')

#banner
header=PhotoImage(file='TRAVEL PLANNER.png')
Label(window, image=header, bg='white').grid(row=0,column=0,sticky=W)

#click func
def clicked():
    required_path=[]
    src = tkvarA.get()
    required_path.append(str(src).upper())
    temp1=tkvarB.get()
    required_path.append(str(temp1).upper())
    temp2=tkvarC.get()
    required_path.append(str(temp2).upper())
    temp3=tkvarD.get()
    required_path.append(str(temp3).upper())
    temp4=tkvarE.get()
    required_path.append(str(temp4).upper())
    temp5=tkvarF.get()
    required_path.append(str(temp5).upper())
    dst=tkvarG.get()
    for i in range(len(required_path)):
        if required_path[i] == 'Station':
            required_path.pop(i)
    required_path.append(str(dst).upper())
    
    
    
#Starting station selector
tkvarA = StringVar(window)
choices = stops_
tkvarA.set('Station')

popupMenu = OptionMenu(window, tkvarA, *choices)
Label(window, text="Please Select Your Starting Station",bg='white',fg='black',font='none 12 bold').grid(row = 1, column = 0)
popupMenu.grid(row = 2, column =0)
    
#Stop1
tkvarB = StringVar(window)
choices = stops_
tkvarB.set('Station')

Label(window, text="Please Select Your 1st Stop",bg='white',fg='black',font='none 12 bold').grid(row =3, column = 0)
popupMenu = OptionMenu(window, tkvarB, *choices)
popupMenu.grid(row =4 , column =0)

#Stop2
tkvarC = StringVar(window)
choices = stops_
tkvarC.set('Station')

Label(window, text="Please Select Your 2nd Stop",bg='white',fg='black',font='none 12 bold').grid(row =5, column = 0)
popupMenu = OptionMenu(window, tkvarC, *choices)
popupMenu.grid(row =6 , column =0)

#Stop3
tkvarD = StringVar(window)
choices = stops_
tkvarD.set('Station')

Label(window, text="Please Select Your 3rd Stop",bg='white',fg='black',font='none 12 bold').grid(row =7, column = 0)
popupMenu = OptionMenu(window, tkvarD, *choices)
popupMenu.grid(row =8 , column =0)

#Stop4
tkvarE = StringVar(window)
choices = stops_
tkvarE.set('Station')

Label(window, text="Please Select Your 4th Stop",bg='white',fg='black',font='none 12 bold').grid(row =9, column = 0)
popupMenu = OptionMenu(window, tkvarE, *choices)
popupMenu.grid(row =10 , column =0)

#Stop5
tkvarF = StringVar(window)
choices = stops_
tkvarF.set('Station')

Label(window, text="Please Select Your 5th Stop",bg='white',fg='black',font='none 12 bold').grid(row =11, column = 0)
popupMenu = OptionMenu(window, tkvarF, *choices)
popupMenu.grid(row =12 , column =0)

#final destination

tkvarG = StringVar(window)
choices = stops_
tkvarG.set('Station')

Label(window, text="Please Enter Your Destination",bg='white',fg='black',font='none 12 bold').grid(row = 13, column = 0)
popupMenu = OptionMenu(window, tkvarG, *choices)
popupMenu.grid(row = 14, column =0)

Button3 = Button(window, text='Final', width=6, command=clicked).grid(row = 200, column =0)

window.mainloop()
    



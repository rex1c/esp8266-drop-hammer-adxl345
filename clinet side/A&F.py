import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Tkinter import *
from matplotlib import style
from tkFileDialog   import askopenfilename
from matplotlib import pyplot as plt
from tkColorChooser import askcolor 
import matplotlib.animation as animation
import serial,socket,time,sys,glob,xlsxwriter
import matplotlib.pyplot as plt
import pylab
import tkMessageBox
import ttk
import Tkinter as tk
import warnings
import tkFileDialog
warnings.filterwarnings("ignore",".*GUI is implemented.*")


LARGE_FONT= ("Verdana", 12)
style.use("seaborn")

f = Figure()
a = f.add_subplot(1,1,1)

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

#def getfile():



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "A & F meter")
        tk.Tk.resizable(self,False,True)
        
        container = tk.Frame(self)
        container.pack(side="bottom", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, BTCe_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

 
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


        def checkEnt():
            try:
                float(e1.get())
                canvas1.create_oval(10, 10, 15, 15, fill='green')        
            except:
                canvas1.create_oval(10, 10, 15, 15, fill='red') 
                tkMessageBox.showerror("Time Error","Please Check the time form")    
                button2.config(state=DISABLED)
            try:
                int(e2.get())
                canvas2.create_oval(10, 10, 15, 15, fill='green')
            except:
                canvas2.create_oval(10, 10, 15, 15, fill='red') 
                tkMessageBox.showerror("Delay Error","Please Check the delay form")    
                button2.config(state=DISABLED)
            try:
                if e3.get() == "":
                    e3.insert(0,cb.get())
                str(e3.get())[0]
                canvas3.create_oval(10, 10, 15, 15, fill='green')
            except:
                canvas3.create_oval(10, 10, 15, 15, fill='red')         
                tkMessageBox.showerror("Serial port Error","please check the serial port ")
                button2.config(state=DISABLED)
            try:
                if e4.get() == "":
                    e4.insert(0,cb2.get())
                int(e4.get())
                canvas4.create_oval(10, 10, 15, 15, fill='green')
            except:
                canvas4.create_oval(10, 10, 15, 15, fill='red')
                tkMessageBox.showerror("Timeout Error","Please Check the timeout form")
                button2.config(state=DISABLED)
            try:
                if e5.get() == "":
                    e5.insert(0,cb1.get())
                int(e5.get())
                canvas5.create_oval(10, 10, 15, 15, fill='green')    
            except:
                canvas5.create_oval(10, 10, 15, 15, fill='red')
                tkMessageBox.showerror("Baudrate Error","Please Check the baudrate form")
                button2.config(state=DISABLED)
            try:
                float(e1.get())
                int(e2.get())
                e3.get()[0]
                int(e4.get())
                int(e5.get())
                button2.config(state=NORMAL)
            except:
                pass
        def checkEnt1():
            try:
                float(e6.get())
                canvas6.create_oval(10, 10, 15, 15, fill='green')        
            except:
                canvas6.create_oval(10, 10, 15, 15, fill='red') 
                tkMessageBox.showerror("Time Error","Please Check the time form")    
                button6.config(state=DISABLED)
            try:
                int(e7.get())
                canvas7.create_oval(10, 10, 15, 15, fill='green')
            except:
                canvas7.create_oval(10, 10, 15, 15, fill='red') 
                tkMessageBox.showerror("Delay Error","Please Check the delay form")    
                button6.config(state=DISABLED)
            try:
                int(e8.get())
                canvas8.create_oval(10, 10, 15, 15, fill='green')
            except:
                canvas8.create_oval(10, 10, 15, 15, fill='red')         
                tkMessageBox.showerror("Wifi port Error","please check the wifi port")
                button6.config(state=DISABLED)
            try:
                if e9.get() == "":
                    e9.insert(0,cb4.get())
                int(e9.get())
                canvas9.create_oval(10, 10, 15, 15, fill='green')
            except:
                canvas9.create_oval(10, 10, 15, 15, fill='red')
                tkMessageBox.showerror("Timeout Error","Please Check the timeout form")
                button6.config(state=DISABLED)
            try:
                if e10.get() == "":
                    e10.insert(0,cb3.get())
                int(e10.get())
                canvas10.create_oval(10, 10, 15, 15, fill='green')    
            except:
                canvas10.create_oval(10, 10, 15, 15, fill='red')
                tkMessageBox.showerror("Baudrate Error","Please Check the baudrate form")
                button6.config(state=DISABLED)
            try:
                float(e6.get())
                int(e7.get())
                e8.get()[0]
                int(e9.get())
                int(e10.get())
                button6.config(state=NORMAL)
            except:
                pass     
        def default():
            e2.delete(0,END) 
            e4.delete(0,END)
            e5.delete(0,END)
            e2.insert(0,"0")
            e4.insert(0,"4")
            e5.insert(0,"115200")   
            cb2.insert(0,"4")
            cb1.insert(0,"115200")
        def default1():
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
            e10.delete(0,END)            
            e7.insert(0,"0")
            e8.insert(0,"4444")
            e9.insert(0,"4")
            e10.insert(0,"128000")    
            cb4.insert(0,"4")
            cb3.insert(0,"128000")
        def reset():
            e1.delete(0,END) 
            e2.delete(0,END) 
            e3.delete(0,END) 
            e4.delete(0,END) 
            e5.delete(0,END)
            cb1.delete(0,END) 
            cb2.delete(0,END) 
            l.delete(0,END)
        def reset1():
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
            e10.delete(0,END)
            cb3.delete(0,END)
            cb4.delete(0,END)
            l1.delete(0,END)
        def offset(): 
            a.set_xlim(float(e11.get()),float(e12.get()))
            a.set_ylim(float(e13.get()),float(e14.get()))
        
        def title():
            titleco = askcolor()
            a.set_title(e15.get(), color=titleco[1])
            
        def Xlabel():
            xlabelco = askcolor()
            a.set_xlabel(e16.get(), color=xlabelco[1])
            
        def Ylabel():
            ylabelco = askcolor()
            a.set_ylabel(e17.get(), color=ylabelco[1])
            
        def background():
            backco = askcolor() 
            a.set_facecolor(backco[1])
        lineco = "#0000ff"
        def line():
            global lineco
            lineco = askcolor() 
        def ticks():
            tickco = askcolor() 
            a.tick_params(labelcolor=tickco[1])
        
  
        def connection():
            global conn
            conn = socket.socket()
            conn.connect(('192.168.4.1', 4444)) 

        def Getfile():
            f = tkFileDialog.asksaveasfilename(defaultextension=".xlsx", filetypes=(("Excel file", "*.xlsx"),("All Files", "*.*") ))
            connection()
            conn.send("getfile")
            u = conn.recv(1024)
            workbook = xlsxwriter.Workbook(str(f))
            worksheet = workbook.add_worksheet()
            worksheet.write(0,0,"Acc")
            worksheet.write(0,1,"Time")
            for i in range(int(u)):
                w = conn.recv(1024)
                worksheet.write(i+1,0,w.split()[0])
                worksheet.write(i+1,1,w.split()[1])
            workbook.close()
            tkMessageBox.showinfo("Saved","File has been saved !")
            conn.close()
        def LAN():
            connection()
            conn.send("serial"+" "+e1.get())
            ser = serial.Serial(e3.get(), 115200, timeout=int(e4.get()))
            a1 = []
            a2 = []
            i = 0
            j = time.time()
            while i<float(e1.get()):
                i = time.time()-j
                time.sleep(int(e2.get()))
                z = float(ser.readline())
                a1.append([i])
                a2.append([i])
                l.insert('end',"Accelerometer=%s"%z+"  "+"Time=%s"%i)
                a.plot(a1,a2,lineco)           
            controller.show_frame(BTCe_Page)
            button3.config(state=NORMAL)
            conn.close()
        def NET():
            connection()
            conn.send("wifi"+" "+e6.get())
            a1 = []
            a2 = []
            i = 0
            j = time.time()
            while i<float(e6.get()):
                i = time.time()-j
                time.sleep(int(e7.get()))
                u = conn.recv(4)
                l.insert("Accelerometer=%s"%u+"  "+"Time=%s"%i)
                a1.append([float(u)])
                a2.append([i])
                a.plot(a2, a1,lineco)
            controller.show_frame(BTCe_Page)    
            button3.config(state=NORMAL)
        #Labels
        Label5 = LabelFrame(self,text="Serial Configuration:")
        Label1 = LabelFrame(Label5,text="Time:")
        Label2 = LabelFrame(Label5,text="Delay:")
        Label3 = LabelFrame(Label5,text="Serial port:")
        Label6 = LabelFrame(Label5,text="Timeout:")
        Label7 = LabelFrame(Label5,text="baudrate:")
        Label4 = LabelFrame(Label5,text="Preview:")
        Label8 = LabelFrame(self,text="Wifi Configuration:")
        Label9 = LabelFrame(Label8,text="Time:")
        Label10 = LabelFrame(Label8,text="Delay:")
        Label11 = LabelFrame(Label8,text="Wifi port:") 
        Label12 = LabelFrame(Label8,text="Timeout:")
        Label13 = LabelFrame(Label8,text="baudrate:")
        Label14 = LabelFrame(Label8,text="Preview:")        
        Label15 = LabelFrame(self,text="Graph Configuration & Comparison")
        Label16 = LabelFrame(Label15,text="X offset:")
        Label17 = LabelFrame(Label15,text="Y offset:")
        Label18 = LabelFrame(Label15,text="X offset:")
        Label19 = LabelFrame(Label15,text="Y offset:")
        Label20 = Label(Label15,text="Change Graph theme :")
        Label21 = Label(Label15,text="to:")
        Label22 = Label(Label15,text="to:")
        Label24 = Label(Label15,text="Title:")
        Label25 = Label(Label15,text="X label:")
        Label26 = Label(Label15,text="Y label:")
        Label27 = Label(Label15,text="background:")
        Label28 = Label(Label15,text="line:")
        Label29 = Label(Label15,text="ticks parameter:")
        Label5.place(width=220,height=718)
        Label1.place(x = 20, y = 10)
        Label2.place(x = 20, y = 60)
        Label3.place(x = 20, y = 110)
        Label4.place(x = 20, y = 280)
        Label6.place(x = 20, y = 160)
        Label7.place(x = 20, y = 210)
        Label8.place(x=270,y=0,width=220,height=718)
        Label9.place(x = 20, y = 10)
        Label10.place(x = 20, y = 60)
        Label11.place(x = 20, y = 110)
        Label14.place(x = 20, y = 280)
        Label12.place(x = 20, y = 160)
        Label13.place(x = 20, y = 210)
        Label15.place(x=540,y=0,width=220,height=718) 
        Label16.place(x = 20, y = 10,width=60)
        Label17.place(x = 20, y = 60,width=60)   
        Label18.place(x = 130, y = 10,width=60)   
        Label19.place(x = 130, y = 60,width=60)   
        Label20.place(x=5,y = 149)      
        Label21.place(x=95,y = 25)      
        Label22.place(x=95,y = 75)            
        Label24.place(x=5,y = 169)      
        Label25.place(x=5,y = 199)      
        Label26.place(x=5,y = 229)      
        Label27.place(x=5,y = 295)      
        Label28.place(x=5,y = 325)      
        Label29.place(x=5,y = 265)      
        #Entry's
        e1 = Entry(Label1)
        e2 = Entry(Label2)
        e3 = Entry(Label3)
        e4 = Entry(Label6)
        e5 = Entry(Label7)
        e6 = Entry(Label9)
        e7 = Entry(Label10)
        e8 = Entry(Label11)
        e9 = Entry(Label12)
        e10 = Entry(Label13)    
        e11 = Entry(Label16)
        e12 = Entry(Label18)
        e13 = Entry(Label17)
        e14 = Entry(Label19)
        e15 = Entry(Label15)
        e16 = Entry(Label15)
        e17 = Entry(Label15)
        e1.grid(row=0, column=0)
        e2.grid(row=0, column=0)
        e3.grid(row=0, column=0)
        e4.grid(row=0, column=0)
        e5.grid(row=0, column=0)
        e6.grid(row=0, column=0)
        e7.grid(row=0, column=0)
        e8.grid(row=0, column=0)
        e9.grid(row=0, column=0)
        e10.grid(row=5, column=0)
        e11.pack()
        e12.pack()        
        e13.pack()        
        e14.pack()        
        e15.place(x = 50 , y= 170 ,width=100)
        e16.place(x = 50 , y= 200 ,width=100)
        e17.place(x = 50 , y= 230 ,width=100)
        e11.insert(0,"0")
        e12.insert(0,"1")
        e13.insert(0,"0")
        e14.insert(0,"1")
        #separator
        s = ttk.Separator(self,orient = HORIZONTAL)
        s1 = ttk.Separator(self,orient = HORIZONTAL)
        s2 = ttk.Separator(self,orient = HORIZONTAL)
        s3 = ttk.Separator(self,orient = HORIZONTAL)
        s4 = ttk.Separator(self,orient = HORIZONTAL)
        s5 = ttk.Separator(self,orient = HORIZONTAL)
        s6 = ttk.Separator(self,orient = HORIZONTAL)
        s7 = ttk.Separator(self,orient = HORIZONTAL)
        s8 = ttk.Separator(self,orient = HORIZONTAL)
        s9 = ttk.Separator(self,orient = HORIZONTAL)
        s10 = ttk.Separator(self,orient = HORIZONTAL)
        s11 = ttk.Separator(self,orient = HORIZONTAL)
        s12 = ttk.Separator(self,orient = HORIZONTAL)
        s13 = ttk.Separator(self,orient = HORIZONTAL)
        s14 = ttk.Separator(self,orient = HORIZONTAL)
        s15 = ttk.Separator(self,orient = HORIZONTAL)
        s16 = ttk.Separator(self,orient = HORIZONTAL)
        s17 = ttk.Separator(self,orient = HORIZONTAL)
        s18 = ttk.Separator(self,orient = HORIZONTAL)
        s19 = ttk.Separator(self,orient = HORIZONTAL)
        s20 = ttk.Separator(self,orient = HORIZONTAL)
        s21 = ttk.Separator(self,orient = HORIZONTAL)
        s.place(x = 5, y = 75,relwidth=0.1)
        s1.place(x = 5, y = 125,relwidth=0.1)
        s2.place(x = 5, y = 175,relwidth=0.1)
        s3.place(x = 5, y = 225,relwidth=0.1)
        s4.place(x = 5, y = 275,relwidth=0.1)    
        s5.place(x = 25, y = 600,relwidth=0.2)    
        s6.place(x = 25, y = 605,relwidth=0.2)    
        s7.place(x = 280, y = 75,relwidth=0.1)
        s8.place(x = 280, y = 125,relwidth=0.1)
        s9.place(x = 280, y = 175,relwidth=0.1)
        s10.place(x = 280, y = 225,relwidth=0.1)
        s11.place(x = 280, y = 275,relwidth=0.1)    
        s12.place(x = 300, y = 600,relwidth=0.2)    
        s13.place(x = 300, y = 605,relwidth=0.2)
        s14.place(x = 550, y = 75,relwidth=0.1)    
        s15.place(x = 550, y = 160,relwidth=0.2)    
        s17.place(x = 550, y = 165,relwidth=0.2)    
        s18.place(x = 550, y = 270,relwidth=0.2)    
        s19.place(x = 550, y = 275,relwidth=0.2)    
        s20.place(x = 550, y = 415,relwidth=0.2)    
        s21.place(x = 550, y = 420,relwidth=0.2)    
        s16.place(x = 665, y = 75,relwidth=0.1)    
        #canvas
        canvas1 = Canvas(Label5,width=15,height=15)  
        canvas2 = Canvas(Label5,width=15,height=15)  
        canvas3 = Canvas(Label5,width=15,height=15)  
        canvas4 = Canvas(Label5,width=15,height=15)  
        canvas5 = Canvas(Label5,width=15,height=15)  
        canvas6 = Canvas(Label8,width=15,height=15)  
        canvas7 = Canvas(Label8,width=15,height=15)  
        canvas8 = Canvas(Label8,width=15,height=15)  
        canvas9 = Canvas(Label8,width=15,height=15)  
        canvas10 = Canvas(Label8,width=15,height=15)  
        canvas1.place(x=-1,y=20)               
        canvas2.place(x=-1,y=70)               
        canvas3.place(x=-1,y=120)               
        canvas4.place(x=-1,y=170)               
        canvas5.place(x=-1,y=220)               
        canvas6.place(x=-1,y=20)               
        canvas7.place(x=-1,y=70)               
        canvas8.place(x=-1,y=120)               
        canvas9.place(x=-1,y=170)               
        canvas10.place(x=-1,y=220)                                                              
                      
        #preview bar
        l = Listbox(Label4, height=15)
        sc = ttk.Scrollbar(self, orient=VERTICAL, command=l.yview)
        sc1 = ttk.Scrollbar(self, orient=HORIZONTAL, command=l.xview)
        l1 = Listbox(Label14, height=15)
        sc2 = ttk.Scrollbar(self, orient=VERTICAL, command=l.yview)
        sc3 = ttk.Scrollbar(self, orient=HORIZONTAL, command=l.xview)        
        l.grid(column=0, row=0, sticky=(N,W,E,S))
        sc.place(x = 150,y = 305,height=270)
        sc1.place(x = 20,y = 560,width=130)
        l1.grid(column=0, row=0, sticky=(N,W,E,S))
        sc2.place(x = 420,y = 305,height=270)
        sc3.place(x = 292,y = 560,width=130)
        l['yscrollcommand'] = sc.set
        l['xscrollcommand'] = sc1.set
        l1['yscrollcommand'] = sc2.set
        l1['xscrollcommand'] = sc3.set        
        #Combobox
        cb = ttk.Combobox(self, values=(serial_ports()))
        cb1 = ttk.Combobox(self, values=("2400","4800","7200","9600","115200","128000"))
        cb2 = ttk.Combobox(self, values=("1","2","3","4","5","6"))
        cb3 = ttk.Combobox(self, values=("2400","4800","7200","9600","115200","128000"))
        cb4 = ttk.Combobox(self, values=("1","2","3","4","5","6"))       
        cb.place(x = 158,y = 142,width=53)         
        cb1.place(x = 158, y = 242,width=53)
        cb2.place(x = 158, y = 192,width=53)    
        cb3.place(x = 430, y = 242,width=53)
        cb4.place(x = 430, y = 192,width=53)    
        #checkbox
        var = IntVar()
        var1 = IntVar()
        def checkbox():
            if var.get() == 1:
                e1.config(state=NORMAL)
                e2.config(state=NORMAL)
                e3.config(state=NORMAL)
                e4.config(state=NORMAL)
                e5.config(state=NORMAL)
                cb.config(state=NORMAL)
                cb1.config(state=NORMAL)
                cb2.config(state=NORMAL)
                l.config(state=NORMAL)
                button1.config(state=NORMAL)
                button4.config(state=NORMAL)
            elif var.get() == 0:
                e1.config(state=DISABLED)
                e2.config(state=DISABLED)
                e3.config(state=DISABLED)
                e4.config(state=DISABLED)
                e5.config(state=DISABLED)
                cb.config(state=DISABLED)
                cb1.config(state=DISABLED)
                cb2.config(state=DISABLED)
                l.config(state=DISABLED)              
                button1.config(state=DISABLED)
                button4.config(state=DISABLED)    
        def checkbox1():
            if var1.get() == 1:
                e6.config(state=NORMAL)
                e7.config(state=NORMAL)
                e8.config(state=NORMAL)
                e9.config(state=NORMAL)
                e10.config(state=NORMAL)
                cb3.config(state=NORMAL)
                cb4.config(state=NORMAL)
                l1.config(state=NORMAL)
                button5.config(state=NORMAL)
                button8.config(state=NORMAL)
            elif var1.get() == 0:
                e6.config(state=DISABLED)
                e7.config(state=DISABLED)
                e8.config(state=DISABLED)
                e9.config(state=DISABLED)
                e10.config(state=DISABLED)
                cb3.config(state=DISABLED)
                cb4.config(state=DISABLED)
                l1.config(state=DISABLED)                
                button5.config(state=DISABLED)
                button8.config(state=DISABLED)
        c = Checkbutton(self, command=checkbox,variable=var)
        c1 = Checkbutton(self, command=checkbox1,variable=var1)
        c.place(x=115,y=0)
        c1.place(x=377,y=0)
        e1.config(state=DISABLED)
        e2.config(state=DISABLED)
        e3.config(state=DISABLED)
        e4.config(state=DISABLED)
        e5.config(state=DISABLED)
        l.config(state=DISABLED)
        cb.config(state=DISABLED)    
        cb1.config(state=DISABLED)    
        cb2.config(state=DISABLED)
        e6.config(state=DISABLED)
        e7.config(state=DISABLED)
        e8.config(state=DISABLED)
        e9.config(state=DISABLED)
        e10.config(state=DISABLED)
        cb3.config(state=DISABLED)
        cb4.config(state=DISABLED)
        l1.config(state=DISABLED)    
        #Buttons
        button1 = Button(Label5,command=default,text="Default")
        button2 = Button(Label5,command=LAN,text="Start")
        button3 = Button(Label5,command=Getfile,text="Get File")
        button4 = Button(Label5,command=reset,text="reset")
        button5 = Button(Label8,command=default1,text="Default")
        button6 = Button(Label8,command=NET,text="Start")
        button7 = Button(Label8,command=Getfile,text="Get File")
        button8 = Button(Label8,command=reset1,text="reset")    
        button9 = Button(Label5,command=checkEnt,text="Ok")
        button4.place(x=77,y=670,width =50,height=25)
        button5.place(x=23,y=636,width =50,height=25)
        button6.place(x=77,y=602,width =50,height=25)
        button7.place(x=130,y=636,width =50,height=25)
        button10 =Button(Label8,command=checkEnt1,text="Ok")
        button11 = Button(Label15,command=offset,text="Set axes")
        button12 = Button(Label15,command=None,text="Set")
        button13 = Button(Label15,command=lambda:controller.show_frame(BTCe_Page),text="Plotter")
        button14 = Button(Label15,command=title,text="Color")
        button15 = Button(Label15,command=Xlabel,text="Color")
        button16 = Button(Label15,command=Ylabel,text="Color")
        button17 = Button(Label15,command=background,text="Color")
        button18 = Button(Label15,command=line,text="Color")
        button19 = Button(Label15,command=ticks,text="Color")
        button1.place(x=23,y=636,width =50,height=25)
        button2.place(x=77,y=602,width =50,height=25)
        button3.place(x=130,y=636,width =50,height=25)
        button8.place(x=77,y=670,width =50,height=25)
        button9.place(x=89,y=636,width =25,height=25)
        button10.place(x=89,y=636,width =25,height=25)
        button11.place(x=80,y=110,width =50,height=25)
        button12.place(x=65,y=360,width =50,height=25)
        button13.place(x=120,y=360,width =50,height=25)
        button14.place(x=160,y=165,width =37,height=25)
        button15.place(x=160,y=195,width =37,height=25)
        button16.place(x=160,y=225,width =37,height=25)
        button17.place(x=98,y=295,width =37,height=25)
        button18.place(x=98,y=323,width =37,height=25)
        button19.place(x=98,y=265,width =37,height=25)
        #Button Config
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)

                    
class BTCe_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button = ttk.Button(self, text="Back to configuration",command=lambda: controller.show_frame(StartPage))
        button.pack()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
app.geometry("760x720")
app.mainloop()
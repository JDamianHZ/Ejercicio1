from tkinter import *
from tkinter import ttk

raiz=Tk()
raiz.geometry("600x450")


#-------colores------

style = ttk.Style()
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "blue", "foreground": "white"},
        "map": {"background": [("selected", "blue")], "foreground": [("selected", "white")]}
    }
})
style.theme_use("MyStyle")

#--------tabs----------

panel= ttk.Notebook(raiz)
#panel.pack(fill=BOTH,expand=True)


tab1=ttk.Frame(panel)
tab2=ttk.Frame(panel)
tab3=ttk.Frame(panel)
tab4=ttk.Frame(panel)
tab5=ttk.Frame(panel)
    


#-------frames------
sub2_Frame= ttk.Frame(tab1, padding="77 35 77 35",relief="raised") #widget transparete hasta especificar
sub2_Frame.grid(column=0, row=1,sticky=(W,E,N,S))

sub3_Frame= ttk.Frame(tab1, padding="77 35 77 35", relief="raised") #widget transparete hasta especificar
sub3_Frame.grid(column=0, row=2,sticky=(W,E,N,S))

sub4_Frame= ttk.Frame(tab1,relief="raised", padding="77 35 77 35" ) #widget transparete hasta especificar
sub4_Frame.grid(column=0, row=3,sticky=(W,E,N,S))
     

sub5_Frame= ttk.Frame(tab1, relief="raised", padding="77 33 77 33") #widget transparete hasta especificar
sub5_Frame.grid(column=0, row=4,sticky=(W,E,N,S))

 

     
     
#--------------primer frame-----------


panel.add(tab1,text="Add                           ")

     

panel.add(tab2,text="Delete                                   ")

     

panel.add(tab3,text="Search                               ")

     

panel.add(tab4,text="Services                    ")

     

panel.add(tab5,text="Help                                ")

#----------frame 2-------------

ttk.Label(sub2_Frame, text="First Name: ").grid(column=0,row=0,sticky=(W, N))  
piesEntry= ttk.Entry(sub2_Frame,width=22)
piesEntry.grid(column=1,row=0)    

ttk.Label(sub2_Frame, text="Last Name: ").grid(column=2,row=0)  
piesEntry= ttk.Entry(sub2_Frame,width=22)
piesEntry.grid(column=3,row=0)

ttk.Label(sub2_Frame, text="Birth Date: ").grid(column=0,row=1)  

piesEntry= ttk.Entry(sub2_Frame,width=2)
piesEntry.grid(column=1,row=1, sticky=(W))

piesEntry= ttk.Entry(sub2_Frame,width=2)
piesEntry.grid(column=1,row=1, padx=20, sticky=(W))

piesEntry= ttk.Entry(sub2_Frame,width=2)
piesEntry.grid(column=1,row=1, padx=40, sticky=(W))

      
ttk.Label(sub2_Frame, text="Contry: ").grid(column=2,row=1)  
piesEntry= ttk.Entry(sub2_Frame,width=22)
piesEntry.grid(column=3,row=1) 

#for child in sub2_Frame.winfo_children(): 
 #   child.grid_configure(padx=10, pady=50)

#-------------------------------frame 3--------------
ttk.Label(sub3_Frame, text="Credit Cardt (if any) ").grid(column=0,row=0, sticky=(W))  

piesEntry= ttk.Entry(sub3_Frame,width=20)
piesEntry.grid(column=1,row=0, sticky=(W))

ttk.Label(sub3_Frame, text="Credit Cardt (if any) ").grid(column=0,row=1, sticky=(W))  
ttk.Radiobutton(sub3_Frame,text="Visa").grid(column=1,row=1,sticky=(W))
ttk.Radiobutton(sub3_Frame,text="Master card").grid(column=1,row=1,padx=80)

#-----------------------------frmae 4------------------------

ttk.Label(sub4_Frame, text="RoomType:  ").grid(column=0,row=0, sticky=(W))  
ttk.Radiobutton(sub4_Frame,text="Normal").grid(column=1,row=0,sticky=(W))
ttk.Radiobutton(sub4_Frame,text="Familiar").grid(column=1,row=1,sticky=(W))
ttk.Radiobutton(sub4_Frame,text="Special").grid(column=1,row=2,sticky=(W))

ttk.Label(sub4_Frame, text="Total Staying Time (days):  ").grid(column=2,row=0, sticky=(W))  
piesEntry= ttk.Entry(sub4_Frame,width=10)
piesEntry.grid(column=3,row=0,sticky=(W,E,N,S)) 

#---------------------------frame5------------------------------
boton = Button(sub5_Frame, text= " submit",width=15, height=1)
boton.grid(sticky=(W,E,N,S),padx=170)



panel.grid(column=0, row=0, sticky=(W,E,N,S))

raiz.mainloop()
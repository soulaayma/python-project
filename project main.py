from tkinter import *
from tkinter.messagebox import *
f=open('admin1.txt','r')
s=f.read()
f.close()


fenetre1=Tk()
fenetre1.title('session')


def Verif():
  if mdp.get()==s:
    fenetre3()
  else:
    showwarning('Résultat','Motde passe incorrect.\nVeuillezrecommencer !')
    mdp.set('')

def fenetre2():
  fenetre2=Toplevel(fenetre1)
  fenetre2.title('login')

  fjf
  global mdp
  mdp= StringVar()
  Champ=Entry(fenetre2, textvariable=mdp, show='*', bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)


  B2 = Button(fenetre2, text='Valider', command = Verif)
  B2.pack(side= LEFT, padx= 5, pady= 5)

def fenetre3():
    fenetre3=Toplevel(fenetre2)
    fenetre3.title('Administrator')

    add=Label(fenetre3,text='add new job offer')
    add.pack(side= LEFT, padx= 5, pady= 5)

    addb=button(fenetre3, text='add', command = addnew)
    addb.pack(side=BOTTOM, padx=5, pady=5)

    browse=Label(fenetre3,text='browse job offers')
    browse.pack(side= LEFT, padx= 5, pady= 5)

    browseb=button(fenetre3, text='browse', command = fenetre2)
    browseb.pack(side=BOTTOM, padx=5, pady=5)

    delete=Label(fenetre3,text='delete a job offer')
    delete.pack(side= LEFT, padx= 5, pady= 5)

    deleteb=button(fenetre3, text='delete', command = fenetre2)
    deleteb.pack(side=BOTTOM, padx=5, pady=5)

    browses=Label(fenetre3,text='browse job seekers')
    browses.pack(side= LEFT, padx= 5, pady= 5)

    browsesb=button(fenetre3, text='browse', command = fenetre2)
    browsesb.pack(side=BOTTOM, padx=5, pady=5)




    
    
  
def addnew():
  addnew=Toplevel(fenetre3)
  addnew.title('adding a new job ')

  add=Label(addnew,text='job ID')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global jobID
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=jobID, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='name')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global name
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=name, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='adresse')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global adresse
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=adresse, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='number')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global number
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=number, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='email')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global email
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=email, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='degre')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global degre
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=degre, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='qualification')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global qual
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=qual, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='experience')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global exp
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=exp, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)

  add=Label(addnew,text='mission description')
  add.pack(side= LEFT, padx= 5, pady= 5)
  global desc
  jobID= StringVar()
  Champ=Entry(addnew, textvariable=desc, bg='bisque', fg='white')
  Champ.focus_set()
  Champ.pack(side= LEFT, padx= 5, pady= 5)


  sb = Button(addnew, text='submit', command = sub)
  sb.pack(side= LEFT, padx= 5, pady= 5)


def sub ():
  f=open('job offers.csv','wr')
  w=csv.writer(f)
  w.writerow(jobID,name,adresse,number,email,degre,qual,exp,desc)
  f.close()



  

  









  


  

  
  



























admin1= Label(fenetre1, text= 'administrator')
admin1.pack(side= LEFT, padx= 5, pady= 5)


B1 = Button(fenetre1, text='Valider', command = fenetre2)
B1.pack(side= LEFT, padx= 5, pady= 5)




user1=Label(fenetre1, text= 'job seeker')
user1.pack(side= LEFT, padx= 5, pady= 5)



c = Button(fenetre1, text='Valider', command = Verif)
c.pack(side= LEFT, padx= 10, pady= 10)


fenetre1.mainloop()


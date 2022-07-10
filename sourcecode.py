from tkinter import *
import functools,random,secrets

window=Tk()

window.configure(background='black')
window.title('Password Generator & Strength Finder')

try:
    window.iconbitmap('logo.ico')
except:
    pass

window_width=1150
window_height=643

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=(screen_width/2)-(window_width/2)
y=(screen_height/2)-(window_height/2)

window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')


instructions='------Instructions------'
instructions1='''Password Generator:
- Give size of password through your keyboard
- Password size must be greater than or equal to 8
- Please enter only positive integers'''
instructions2='''Password Strength Finder:
- Give your password through your keyboard
- Password size must be greater than or equal to 8
'''


char_str='abcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()_+|{}<>?:/.,;[]\-=ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_list=['abcdefghijklmnopqrstuvwxyz','1234567890','ABCDEFGHIJKLMNOPQRSTUVWXYZ','`~!@#$%^&*()_+|{}<>?:/.,;[]\-=']

def click():
    size=str(entry1_input.get())
    if size.isdigit()==True:
        new_size=int(size)
        if new_size>=8:
            password_list=[]
            for i in char_list:
                for j in range(2):
                    password_list.append(secrets.choice(i))
            for i in range(new_size-8):
                password_list.append(secrets.choice(char_str))
            random.shuffle(password_list)
            password=functools.reduce(lambda x,y:x+y,password_list)
            exit1_input.delete(0,END)
            exit1_input.insert(0,"Password: "+password)
        else:
            exit1_input.delete(0,END)
            exit1_input.insert(0,"Oops! Password can't be less than 8 characters")
    else:
        exit1_input.delete(0,END)
        exit1_input.insert(0,"Please enter an positive integer")


def check():
    password=str(entry2_input.get())
    checker=set()
    if len(password)>=8:
        for i in password:
            if i in char_list[0]:
                checker.add(0)
            elif i in char_list[1]:
                checker.add(1)
            elif i in char_list[2]:
                checker.add(2)
            elif i in char_list[3]:
                checker.add(3)
        if len(checker)==0:
            exit2_input.delete(0,END)
            exit2_input.insert(0,"Please enter your password")
        elif len(checker)==1:
            exit2_input.delete(0,END)
            exit2_input.insert(0,"Strength: Your Password is Weak")
        elif len(checker)==2:
            exit2_input.delete(0,END)
            exit2_input.insert(0,"Strength: Your Password is Moderate")
        elif len(checker)==3:
            exit2_input.delete(0,END)
            exit2_input.insert(0,"Strength: Your Password is Strong")
        elif len(checker)==4:
            exit2_input.delete(0,END)
            exit2_input.insert(0,"Strength: Your Password is Very Strong")
    elif len(password)==0:
        exit2_input.delete(0,END)
        exit2_input.insert(0,"Please enter your password")
    else:
        exit2_input.delete(0,END)
        exit2_input.insert(0,"Strength: Size of your password is less than 8 characters")
        


def clear(a):
    if a=='f':
        entry1_input.delete(0,END)
        exit1_input.delete(0,END)
        exit1_input.insert(0,"Password: ")
    elif a=='c':
        entry2_input.delete(0,END)
        exit2_input.delete(0,END)
        exit2_input.insert(0,"Strength: ")


text1='Password Generator:\nPlease enter the size of password in the given below box'
text2='\n\nPassword Strength Finder:\nPlease enter your password in the given below box'


credit=Label(window,text='\n...Designed by Naga Sriram...',fg='white',bg='black')
instruct=Label(window,text=instructions,fg='white',bg='black')
instruct1=Label(window,text=instructions1,fg='white',bg='black')
instruct2=Label(window,text=instructions2,fg='white',bg='black')
enter1=Label(window,text=text1,fg='white',bg='black')
enter2=Label(window,text=text2,fg='white',bg='black')


entry1_input=Entry(window,width=60,borderwidth=10,fg='white',bg='black')
exit1_input=Entry(window,width=60,borderwidth=10,fg='white',bg='black')
entry2_input=Entry(window,width=60,borderwidth=10,fg='white',bg='black')
exit2_input=Entry(window,width=60,borderwidth=10,fg='white',bg='black')

exit1_input.insert(0,'Password: ')
exit2_input.insert(0,'Strength: ')

button_generate=Button(window,text="Generate Password",fg='white',bg='green',padx=130,pady=10,command=click)
button_check=Button(window,text="Check Strength",fg='white',bg='green',padx=130,pady=10,command=check)
button_clear1=Button(window,text="Clear",fg='white',bg='grey',padx=170,pady=10,command=lambda:clear('f'))
button_clear2=Button(window,text="Clear",fg='white',bg='grey',padx=170,pady=10,command=lambda:clear('c'))

l=[credit,instruct,instruct1,instruct2,enter1,enter2,entry1_input,exit1_input,entry2_input,exit2_input,button_generate,button_check,button_clear1,button_clear2]


for i in range(1,13):
    Grid.rowconfigure(window, index=i, weight=1)
for i in range(2):
    Grid.columnconfigure(window, index=i, weight=1)


enter1.grid(row=1,column=0,columnspan=2,sticky='nsew')
enter2.grid(row=5,column=0,columnspan=2,sticky='nsew')
credit.grid(row=11,column=0,columnspan=2,sticky='nsew')
instruct.grid(row=9,column=0,columnspan=2,sticky='nsew')
instruct1.grid(row=10,column=0,sticky='nsew')
instruct2.grid(row=10,column=1,sticky='nsew')

entry1_input.grid(row=2,column=0,columnspan=2,sticky='nsew')
exit1_input.grid(row=4,column=0,columnspan=2,sticky='nsew')
entry2_input.grid(row=6,column=0,columnspan=2,sticky='nsew')
exit2_input.grid(row=8,column=0,columnspan=2,sticky='nsew')

button_generate.grid(row=3,column=0,sticky='nsew')
button_check.grid(row=7,column=0,sticky='nsew')
button_clear1.grid(row=3,column=1,sticky='nsew')
button_clear2.grid(row=7,column=1,sticky='nsew')

def resize(e):
    wid=e.width
    button_newsize=int((12*wid)/(900))
    for i in l:
        i.config(font=('Arial',button_newsize))


window.bind('<Configure>',resize)
window.mainloop()

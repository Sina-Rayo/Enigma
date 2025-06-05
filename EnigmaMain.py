from tkinter import *

root = Tk()

######### Setting #########
root.title("ENIGMA")
w = 720
h = 700
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
xx = (ws/3) 
yy = (hs/1024)

root.geometry('%dx%d+%d+%d' % (w, h, xx, yy))
root.configure(bg="black")

######### Variables #########
msg_s = StringVar(value='')
passw_show = StringVar(value='')



alphabet = "abcdefghijklmnopqrstuvwxyz "

rotors = [  "xdfvghtljkqsewoycrui mapnzb",
            "nzlwmacqyetkr uivsopdfjxhbg",
            "rqdpoiw mvksxjefglhnabzctyu",
            "cgvrbzaikhtdeplqjf ywnxosum",
            "qa uewhcvoknilfdybjrmpgxszt",
            "nmpbyutr giwdqkczoeshjxlfva",
            "auoygfhmbvcxqni jdkelwzrtps",
            "hloersvbfkx qyzcmgatpuwjdin",
            "nxwatfbuyqrjcplhegokvizds m",
            "cpnumqodfylvstzagxbhjeir kw"
            ]

def Prepare(code):
    global r1 , r2 , r3
    r1 = rotors[int(code[0])]
    r2 = rotors[int(code[1])]
    r3 = rotors[int(code[2])]
    for i in r1:
        if i != code[3]:
            r1 = r1[1:] + r1[0]
        else:
            break
    for i in r2:
        if i != code[4]:
            r2 = r2[1:] + r2[0]
        else:
            break
    for i in r3:
        if i != code[5]:
            r3 = r3[1:] + r3[0]
        else:
            break


def reflector(c):
    return alphabet[len(alphabet) - 1 - alphabet.find(c)]

def matching(c):
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    ref = reflector(c3)
    c11 = alphabet[r3.find(ref)]
    c12 = alphabet[r2.find(c11)]
    c13 = alphabet[r1.find(c12)]

    return c13

def decode(word):
    global r1 , r2 , r3
    decoded = ""
    turns = 0
    for i in list(word):
        decoded += matching(i)
        r1 = r1[1:] + r1[0]
        turns += 1
        if(turns % 26):
            r2 = r2[1:] + r2[0]
            if(turns % (26 * 26)):
                r3 = r3[1:] + r3[0]
    return decoded

# code = input("Enter Todays Pass (123xyz) :   ")
# w = input("Enter your Words (just Lower English Letters) :   ")
# Prepare(code)
# print(decode(w))

def START(txt , pw):
    Prepare(pw)
    dd = decode(txt[:-1])
    ans.delete('1.0' , 'end')
    ans.insert(INSERT , dd)

######### Elements #########

msg = Label(root , text = '123abc' , bg='black' , fg='gray' , font='Arial 12')
msg.pack(pady=8)

passw = Entry(root , width=20 , bg='black' , fg="yellow" , font='Arial 24')
passw.pack(pady=5)

inp = Text(root ,bg='black' , fg='white' , insertbackground='light green',height=5 , width=40 , font ='Arial 18')
inp.pack(pady=20)

func_btn = Button(root ,command= lambda: START(inp.get('1.0' , 'end').lower() , passw.get().lower()) , text='Encode / Decode' , width=15 , height=1 
, bg='black' , fg="light green" , font='Arial 15')
func_btn.pack(pady=20)


cur_func_str = Label(root , textvariable=passw_show , bg='black' , fg="Green" , font='Arial 24')
cur_func_str.pack(pady=10)

ans = Text(root ,bg='black' , fg='white',height=5 , width=40 , font ='Arial 18')
ans.pack(pady=20)

root.mainloop()


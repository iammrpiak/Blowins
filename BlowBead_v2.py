import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import time
import winsound
from datetime import datetime
import csv

###############Writetocsv########################

def writetocsv(transaction, filename ='transaction.csv'):
    with open(filename, 'a', newline ='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(transaction)


############################################
GUI = Tk()

W = 1300
H = 600

#เปิดโปรแกรมทุกครั้งจะอยู่ตรงกลางหน้าจอ
#หาค่าขนาดหน้าจอที่ตั้งค่า Screen resolution
MW =GUI.winfo_screenwidth()
MH = GUI.winfo_screenheight()
SX = (MW/2) - (W/2) #Start X
SY = (MH/2) - (H/2)#Start Y
SY = SY-50 #diff up

# print('MW=',MW)
# print('MH=',MH)

GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
#GUI.geometry("1200x600")
GUI.title('BEAD DIRTY INSPECTION')
GUI.iconbitmap('insicon.ico')



frame_1 = Frame(GUI, width=1080, height=800, bg='light blue')
frame_1.place(x=0, y=0)

#frame for set up parameter
frame_2 = Frame(GUI, width=200, height=500, bg='orange')
frame_2.place(x=1080,y=100)

frame_3=Frame(GUI, width =200, height = 100, bg ='green')
frame_3.place(x=1080, y=0)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

Font1 = ('consolas',16,'bold')
Font2 = ('consolas',14,'bold')

#Transaction ID

v_transaction = StringVar()
trstamp = datetime.now().strftime('%Y%m%d%H%M%S') #generate trannsaction
v_transaction.set(trstamp)

# defect1=0
# defect2 =0

#Label Transaction
LTR = Label(GUI, textvariable=v_transaction).place()
def AddTransaction():
    #writetocsv('transaction.csv')
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = v_transaction.get()
    itemname = v_itemname.get()
    v_defect1 = 'NG'
    v_defect2 ='NG'
    
    A = [transaction,  stamp, itemname, v_defect1, v_defect2]

    print(A)

    # print(stamp)
    # print(transaction)
    # print(itemname)
    # print(v_defect1)
    # print(v_defect2)

    if v_rbutton.get()==1:
        writetocsv(A,'transaction.csv')


def HistoryWindow(event):
    HIS =Toplevel() # คำสั่งคล้ายๆกับ GUI =Tk()
    HIS.geometry('600x500')

    L =Label(HIS, text = 'DEFECT HISTORY',font = Font1).pack()
    #History table
    header =['TransactionID','Datetime', 'Item Name','Defect1','Defect2']
    hwidth = [150,150,150,50,50]

    table_history =ttk.Treeview(HIS, columns=header, show = 'headings', height =20)
    table_history.pack()

    #for loop สำหรับตาราง header  
    for hd,hw in zip(header,hwidth):
        table_history.column(hd, width =hw)
        table_history.heading(hd, text =hd)

    #Update from csv
    with open('transaction.csv', newline ='',encoding='utf-8') as file:
        fr =csv.reader(file) # file reader
        for row in fr:
            table_history.insert('',0,value= row)


    HIS.mainloop()
GUI.bind('<F1>', HistoryWindow)

def StartVideo():
    global cap1,cap2
    try:
        cap1 =cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap2 = cv2.VideoCapture(1,cv2.CAP_DSHOW)
        showframe()
    except:
        messagebox.showwarning('Warning', 'ไม่มีสัญญาณจากกล้อง\nตรวจสอบสายสัญญาณ')


W = 175
Thresh0 = Scale(frame_1, label="ThreshCam0", from_=0, to=255, orient=HORIZONTAL, variable=var1)
Thresh0.set(0)
Thresh0.place(x=10, y=10, width=W)

A_Min0 = Scale(frame_1, label="Area_Min0", from_=0, to=1000, orient=HORIZONTAL, variable=var2)
A_Min0.set(0)
A_Min0.place(x=180, y=10, width=W)

A_Max0 = Scale(frame_1, label="Area_Max0", from_=1001, to=2000, orient=HORIZONTAL, variable=var3)
A_Max0.set(0)
A_Max0.place(x=350, y=10, width=W)

Thresh1 = Scale(frame_1, label="ThreshCam1", from_=0, to=255, orient=HORIZONTAL, variable=var4)
Thresh1.set(0)
Thresh1.place(x=560, y=10, width=W)

A_Min1 = Scale(frame_1, label="Area_Min1", from_=0, to=1000, orient=HORIZONTAL, variable=var5)
A_Min1.set(0)
A_Min1.place(x=730, y=10, width=W)

A_Max1 = Scale(frame_1, label="Area_Max1", from_=1001, to=2000, orient=HORIZONTAL, variable=var6)
A_Max1.set(0)
A_Max1.place(x=900, y=10, width=W)

#set up จอจับภาพ

H1 = Scale(frame_2, label="H1", from_=0, to=160, orient=VERTICAL, variable=var7)
H1.set(0)
H1.place(x=20, y=190)

H2 = Scale(frame_2, label="H2", from_=161, to=320, orient=VERTICAL, variable=var8)
H2.set(0)
H2.place(x=100, y=190)

W1 = Scale(frame_2, label="W1", from_=0, to=250, orient=VERTICAL, variable=var9)
W1.set(0)
W1.place(x=20, y=300)

W2 = Scale(frame_2, label="W2", from_=251, to=520, orient=VERTICAL, variable=var10)
W2.set(0)
W2.place(x=100, y=300)

L = Label(frame_2, text='Set up Capture Area ', font = Font2)
L.place(x=0,y= 160)


##########Radio button ###########

v_rbutton = IntVar()
v_rbutton.set(0)


def clicked(value):
    print(v_rbutton.get())
    r_label = Label(frame_2, text = value)
    r_label.place(x=0, y=470)


Save_button = Radiobutton(frame_2, text= 'SAVE DATA', variable= v_rbutton, value = 1, command = lambda: clicked(v_rbutton.get()))
Save_button.place( x=0, y=420)

NotSave_button = Radiobutton(frame_2, text= 'NOT SAVE DATA', variable= v_rbutton, value = 2, fg='red', command = lambda: clicked(v_rbutton.get()))
NotSave_button.place( x=0, y=450)

print(v_rbutton.get())

# r_label = Label(frame_2, text = v_rbutton.get())
# r_label.place(x=0, y=470)

#for HikVision 

# if False == cap.isOpened():
#     print(0)#if it is not open, show '0'
# else:
#     print(1)#if it is open, show '1'
 
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)  # set width
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2048)  # set height
# cap.set(cv2.CAP_PROP_FPS , 15)   # set frame

label1 = Label(frame_1)
label2 = Label(frame_1)
label3 = Label(frame_1)
label4 = Label(frame_1)


def to_pil(img,label, x, y, w, h):
    img = cv2.resize(img, (w, h))
    image = Image.fromarray(img)
    imgTk = ImageTk.PhotoImage(image)
    label.configure(image=imgTk)
    label.image = imgTk
    label.place(x=x, y=y)


#defect variable 
v_defect1 = StringVar()
v_defect2 =StringVar()
defect1 =()
defect2 =()

def showframe():
    global Font1, cap1, cap2
#Cam0
    ret, img = cap1.read()
    H1=  var7.get()
    H2= var8.get()
    W1 = var9.get()
    W2 = var10.get()

    img = img[H1:H2, W1:W2] # set up ROI

    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    Thresh_bar = var1.get()
    A_Min_bar = var2.get()
    A_Max_bar = var3.get()
    

    Blurred = cv2.GaussianBlur(Gray, (5,5), 0)

    _,threshold = cv2.threshold(Blurred, Thresh_bar, 255, cv2.THRESH_BINARY_INV)

    #Kernel matrix 
    kernel = np.ones((5,5),np.uint8)
    closing =cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel, iterations=5)
    
    result_img = closing.copy() # clone คำสั่ง closing
    contours, hierachy = cv2.findContours(result_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Cam1
    ret1, img1 = cap2.read()
    img1 = img1[H1:H2, W1:W2] # set up ROI

    img1 = cv2.flip(img1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    Gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    
    Thresh_bar1 = var4.get()
    A_Min_bar1 = var5.get()
    A_Max_bar1 = var6.get()
    

    Blurred1 = cv2.GaussianBlur(Gray1, (5,5), 0)

    _,threshold1 = cv2.threshold(Blurred1, Thresh_bar1, 255, cv2.THRESH_BINARY_INV)

    #Kernel matrix 
    kernel = np.ones((5,5),np.uint8)
    closing1 =cv2.morphologyEx(threshold1, cv2.MORPH_CLOSE, kernel, iterations=5)
    
    result_img1 = closing1.copy() # clone คำสั่ง closing
    contours1, hierachy = cv2.findContours(result_img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    counter = 0
    counter1 = 0
    for cnt,cnt1 in zip(contours, contours1):
        area = cv2.contourArea(cnt)
        area1 = cv2.contourArea(cnt1)

        print("area="+str(area))
        print('area1='+ str(area1))

        (x,y,w,h) = cv2.boundingRect(cnt)
        (x1,y1,w1,h1) = cv2.boundingRect(cnt1)

        cv2.putText(img,str(int(area)),(20,20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),  1 )
        cv2.putText(img1,str(int(area1)),(10,10),cv2.FONT_HERSHEY_PLAIN,0.5,(255,0,0), 1 )

        if (ret==True):
            if area>A_Min_bar:

             
                winsound.PlaySound('NG_sound.wav',winsound.SND_ASYNC)
                winsound.Beep(1000,50)

                defect1 = 'NG'
                v_defect1 = defect1 

                AddTransaction()


                
                Label(frame_1, text = "NG", font= Font1, fg='red').place(x=380,y=450)   
                cv2.drawContours(img,contours,-1,(0,255,0),1)
                
                            
                cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),1)
                cv2.putText(img,str(area),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0),1)

                counter+=1
                text = print('No. of dirt Cam0 = '+ str(counter))

                cv2.putText(img,text,(30,150), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)
            else:
                Label(frame_1, text = 'OK', font= Font1, fg='green').place(x=380,y=450)
        else:
            print('Cam0 error')  
                

        if (ret1==True):
            if area1> A_Min_bar1:

              
                winsound.PlaySound('NG_sound.wav',winsound.SND_ASYNC)
                winsound.Beep(1000,50)

                defect2 = 'NG'
                v_defect2 = defect2

                AddTransaction()

                Label(frame_1, text = 'NG', font= Font1, fg='red').place(x=930,y=450)   

                cv2.drawContours(img1,contours1,-1,(0,0,255),1)
                #cv2.rectangle(img1,(x1,y1),(x1+w1, y1+h1), (0,0,255),1)
                cv2.putText(img1,str(area1),(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0),1)

                counter1+=1
                text1 = print('No. of dirt Cam1 = '+ str(counter1))
                cv2.putText(img1,text1,(30,150), cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),3)
            else:
                Label(frame_1, text = 'OK', font= Font1, fg='green').place(x=930,y=450) 

        else:
            #Label(frame_1, text = 'Camera Error', font= Font1, fg='red').place(x=380,y=450)
            Label(frame_1, text = 'Camera1 Error', font= Font1, fg='red').place(x=880,y=450)

    to_pil(img,label1, 10, 100,520, 320)
    to_pil(threshold, label2, 10, 430, 250, 150)
    to_pil(img1, label3, 540, 100,520, 320)
    to_pil(threshold1, label4, 550, 430, 250, 150)
    
    GUI.after(10, showframe)

BStart = Button(frame_2,text = 'START',font = Font1, width = 10, fg = 'blue', command = StartVideo)
BStart.place(x= 20,y=10, width =160)


B1 = Button(frame_2,text = 'EXIT',font = Font1, width = 10, fg = 'red', command = GUI.quit)
B1.place(x=20,y=80, width =160)

L1 = Label(frame_1, text ="Cam0\nJudge:", font = Font1).place(x=280,y=450)
L2 = Label(frame_1, text ="Cam1\nJudge:", font = Font1).place(x=820,y=450)

L3 = Label(frame_3,text ='Item Name', font = Font1).place(x=5,y=5)

v_itemname = StringVar()
E1 = Entry(frame_3, textvariable=v_itemname,font= Font2, width=18)
E1.place(x=10,y=50)

GUI.mainloop()


import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import numpy as np

Window = tk.Tk()
Window.title('hsv assignment')


mainFrame = tk.Frame(Window, bg='red')
mainFrame.pack(fill='both', expand=True)


def hsv(orginal_image, x1, x2, x3, x4, x5, x6):
    global val1, val2, val3, val4, val5, val6
    val1 = x1
    val2 = x2 
    val3 = x3
    val4 = x4
    val5 = x5
    val6 = x6
    hsvImage = cv2.cvtColor(orginal_image, cv2.COLOR_BGR2HSV)
    lower_color = np.array([x1, x2, x3])
    upper_color = np.array([x4, x5, x6])
    color_range = cv2.inRange(hsvImage, lower_color, upper_color)
    img = Image.fromarray(color_range)
    img=ImageTk.PhotoImage(img)
    imgLabelTwo= tk.Label(hsvFrame, image= img)
    imgLabelTwo.image= img
    imgLabelTwo.pack()
    if len(hsvFrame.winfo_children()) == 2:
        hsvFrame.winfo_children()[0].destroy()
    
    
       

def showimage():
    global orginal_image
    path= filedialog.askopenfilename(title="Select an Image", filetype=(('image    files','*.jpg'),('all files','*.*')))
    orginal_image = cv2.imread(path)
    img= Image.open(path)
    img=ImageTk.PhotoImage(img)
    imgLabelOne= tk.Label(orginalFrame, image= img)
    imgLabelOne.image= img
    imgLabelOne.pack()
    hsv(orginal_image, 0, 0, 0, 0, 0, 0)


def LowerText(a,b,c):
    sel = str(a) + ':' + str(b) + ':' + str(c) 
    lowerText.config(text = sel, font =("Courier", 14))
    hsv(orginal_image, x1= a, x2= b, x3= c, x4= val4, x5= val5, x6= val6)

def UpperText(a,b,c):
    sel = str(a) + ':' + str(b) + ':' + str(c) 
    upperText.config(text = sel, font =("Courier", 14))
    hsv(orginal_image, x4= a, x5= b, x6= c, x1= val1, x2= val2, x3= val3)

def lowerScale(arg):
    # print(lowerScaleOne.get(),":",lowerScaleTwo.get(),":", lowerScaleThree.get())
    LowerText(lowerScaleOne.get(),lowerScaleTwo.get(),lowerScaleThree.get())

def upperScale(arg):
    # print(upperScaleOne.get(),":",upperScaleTwo.get(),":", upperScaleThree.get()) 
    UpperText(upperScaleOne.get(),upperScaleTwo.get(),upperScaleThree.get())

# ImageFrame  frame work
ImageFrame = tk.Frame(mainFrame)

orginalFrame = tk.Label(ImageFrame, text='orginal image', bg='green', fg='white', padx=10, pady=10)
orginalFrame.grid(row=0, column=0, padx=10, pady=10)

hsvFrame = tk.Label(ImageFrame, text='hsv image', bg='green', fg='white', padx=10, pady=10)
hsvFrame.grid(row=0, column=1, padx=10, pady=10)


ImageFrame.grid_columnconfigure(0, weight=1)
ImageFrame.grid_columnconfigure(1, weight=1)

ImageFrame.pack(fill='x')
# ImageFrame frame work

#       value Frame start
valueFrame = tk.Frame(mainFrame)

# lower scale
lowerFrame = tk.Label(valueFrame, text='lower value', bg='green', fg='white', padx=10, pady=10)
lowerScaleOne = tk.Scale(lowerFrame, from_=0, to=255, orient='horizontal', length=150, command=lowerScale)
lowerScaleTwo = tk.Scale(lowerFrame, from_=0, to=255, orient='horizontal', length=150, command=lowerScale)
lowerScaleThree = tk.Scale(lowerFrame, from_=0, to=255, orient='horizontal', length=150, command=lowerScale)
lowerScaleOne.pack(padx=10, pady=10)
lowerScaleTwo.pack(padx=10, pady=10)
lowerScaleThree.pack(padx=10, pady=10)
lowerFrame.grid(row=0, column=0, padx=10, pady=10)
# lower scale

# upper scale
upperFrame = tk.Label(valueFrame, text='upper', bg='green', fg='white', padx=10, pady=10)
upperScaleOne = tk.Scale(upperFrame, from_=0, to=255, orient='horizontal', length=150, command=upperScale)
upperScaleTwo = tk.Scale(upperFrame, from_=0, to=255, orient='horizontal', length=150, command=upperScale)
upperScaleThree = tk.Scale(upperFrame, from_=0, to=255, orient='horizontal', length=150, command=upperScale)
upperScaleOne.pack(padx=10, pady=10)
upperScaleTwo.pack(padx=10, pady=10)
upperScaleThree.pack(padx=10, pady=10)
upperFrame.grid(row=0, column=1, padx=10, pady=10)
# upper scale

valueFrame.grid_columnconfigure(0, weight=1)
valueFrame.grid_columnconfigure(1, weight=1)

valueFrame.pack(fill='x')
#      value Frame end


# text area start
lowerTextFrame = tk.Label(mainFrame, text='lower value', bg='green', fg='white', padx=5, pady=5)
lowerText = tk.Label(lowerTextFrame, padx=5, pady=5)
sel = 'lower value'
lowerText.config(text = sel, font =("Courier", 14))
lowerText.pack(padx=5, pady=5)
lowerTextFrame.pack(padx=5, pady=5, fill='x')

upperTextFrame = tk.Label(mainFrame, text='upper value', bg='green', fg='white', padx=5, pady=5)
upperText = tk.Label(upperTextFrame, padx=5, pady=5)
sel = 'upper value'
upperText.config(text = sel, font =("Courier", 14))
upperText.pack(padx=5, pady=5)
upperTextFrame.pack(padx=5, pady=5, fill='x')

# text area end

#button
buttonFrame = tk.Frame(mainFrame, background='orange')

exitBtn = ttk.Button(buttonFrame, text='Exit',command=lambda:exit())
exitBtn.grid(row=0, column=0, padx=10, pady=10)

selectBtn = ttk.Button(buttonFrame, text='select image', command=showimage)
selectBtn.grid(row=0, column=1, padx=10, pady=10)

buttonFrame.pack(fill='x',side='bottom')
#button

Window.mainloop()

cv2.waitKey(0)


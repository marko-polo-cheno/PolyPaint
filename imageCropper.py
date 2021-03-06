# imageCropper
# Tool that allows the user to crop the chosen image

# Imports
import PIL.Image
from PIL import ImageTk
from tkinter import *
import sys

# Global variables used for cropping coordinates
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# Funtions for mouse actions

# Tracks click position
def mouseDown(event):
    #print ("clicked at", event.x, event.y)
    global x1,y1
    x1 = event.x
    y1 = event.y

# Tracks release position
def mouseUp(event):
    #print ("released at", event.x, event.y)
    global x1,y1,x2,y2
    x2 = event.x
    y2 = event.y
    cropImage(x1, x2, y1, y2)
    x1, y1, x2, y2 = 0, 0, 0, 0
    imageCanvas.coords(cursor_rect, 0, 0, 0, 0)

# Tracks movement
def mouseMove(event):
    global cursor_rect, imageCanvas, x1, y1
    imageCanvas.coords(cursor_rect, x1, y1, event.x, event.y)

# cropImage(x1, x2, y1, y2): Crops the image based on coordinates
# returns: cropped image
def cropImage(x1, x2, y1, y2):
    #print(x1, y1, x2, y2)
    if(y2 < y1):
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = temp
    
    # Crops image
    cropped = img.crop((min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)))
    cropped.show()
    return cropped

# Opens image file
imageFile = "./whale.jpg"
if(len(sys.argv) == 2):
    imageFile = "./" + sys.argv[1]
fp = open(imageFile,"rb")
img = PIL.Image.open(fp)
imgWidth, imgHeight = img.size

# Creates a canvas to display image
root = Tk()
imageCanvas = Canvas(root, bg="white", height=imgHeight, width=imgWidth)
imageCanvas.bind("<Button-1>", mouseDown)
imageCanvas.bind("<ButtonRelease-1>", mouseUp)
imageCanvas.bind("<B1-Motion>", mouseMove)
imageCanvas.pack()

whale = ImageTk.PhotoImage(PIL.Image.open(fp)) 
imageCanvas.create_image(0, 0, anchor=NW, image=whale)
cursor_rect = imageCanvas.create_rectangle(0,0,0,0)

root.mainloop()
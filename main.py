from PIL import Image
import os
import tkinter
import customtkinter
from customtkinter import filedialog
from customtkinter import *

def openfile():
    filepath = filedialog.askdirectory()
    print(filepath)

#file paths
sourceFolder = ""
outputFolder = ""
baseTexture = ""

#functions 
def selectSource():
    global sourceFolder
    sourceFolder = filedialog.askdirectory()

def selectOutput():
    global outputFolder
    outputFolder = filedialog.askdirectory()

def selectBaseMap():
    global baseTexture
    baseTexture = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])

def combineImages(basePath, overlayPath, outputPath):
    base = Image.open(basePath).convert("RGBA")
    overlay = Image.open(overlayPath).convert("RGBA")

    combined = Image.alpha_composite(base, overlay)
    combined.save(outputPath)

def mergeImages():
    if not sourceFolder or not outputFolder or not baseTexture:
        print("Please select all required paths")
        return
    for filename in os.listdir(sourceFolder):
        if filename.lower().endswith((".png", ".jpg")):
            overlayPath = os.path.join(sourceFolder, filename)
            outputPath = os.path.join(outputFolder, filename)
            combineImages(baseTexture, overlayPath, outputPath)

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("TextureColourCombiner")

#UI elements
title = customtkinter.CTkLabel(app,text="Insert source destination")
title.pack(padx = 10, pady = 10)

#source imput 
source = CTkButton(app,text="Open Source", command=selectSource)
source.pack(padx = 10, pady = 10)

#output source 
oSource = CTkButton(app,text="Open Destination", command=selectOutput)
oSource.pack(padx = 10, pady = 10)

#baseTexture 
bSource = CTkButton(app,text="Open Base Texture", command=selectBaseMap)
bSource.pack(padx = 10, pady = 10)

#combine 
combine = CTkButton(app,text="Combine", command=mergeImages)
combine.pack(padx = 10, pady = 10)

#run app
app.mainloop()
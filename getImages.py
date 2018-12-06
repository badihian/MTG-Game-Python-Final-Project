import json
from tkinter import *
from PIL import Image, ImageTk
from urllib import request
import io

with open("AllCards.json", "r") as mtgJSON:
    mtgString = json.load(mtgJSON)

with open("scryfall-default-cards.json", "r") as scryfallJSON:
    scryString = json.load(scryfallJSON)

# mainWindow = Tk()
# ====================================
# root = Tk()
# root.withdraw()
# master = Toplevel(root)
# master.protocol("WM_DELETE_WINDOW", close)
# Canvas.__init__(self, master, width = 500, height = 500, 
#                 highlightthickness = 0, bd = 0)
# master.title("Magic The Gathering!")
# Canvas.pack()
# ====================================

root = Tk()
root.geometry('500x500')
root.title("Magic the Gathering!")
# top = Toplevel()
# frame = Frame( width = 500, height = 500)
# frame.pack()

imageCount = 0
photos = []
i = 0


# ----------------------------------------------------------------
# for card in scryString:
#     if i == 1:
#         break
#     elif "image_uris" in card and "normal" in card["image_uris"]:
#         mainWindow.title(card['name'])
#         cover = (card["image_uris"]["normal"])
#         print(card["image_uris"]["normal"])
#         imageCount += 1

#         raw_data = request.urlopen(cover).read()
#         im = Image.open(io.BytesIO(raw_data))
#         photo = ImageTk.PhotoImage(im)
#         newWidth = 250
#         height = int(photo.height() * (newWidth/photo.width()))
#         im = im.resize((newWidth, height), Image.ANTIALIAS)
#         photo = ImageTk.PhotoImage(im)
#         canvas = Canvas(width = photo.width(), height = photo.height(), bg='black')
#         canvas.pack(expand=FALSE, fill = NONE)
#         canvas.create_image(10, 10, image = photo, anchor = NW)
#         # ====================================================
#         # label1 = Label(mainWindow, image=image)
#         # label1.grid(row=i, sticky=W)

#         # append to list in order to keep the reference
#         # ====================================================
#         photos.append(photo)

#         i += 1

# ----------------------------------------------------------------



print(f"imageCount = {imageCount}")
print(f"images = {photos}")

# mainWindow.mainloop()
# frame.mainloop()

x = input("Press enter to exit")


import tkinter

offset = 50
hspace = 50
vspace = 50
size   = 20
linespace = 4

def visualize(map):
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=(offset*2)+(len(map)*hspace), height=(offset*2)+(len(map[0])*vspace), borderwidth=0, highlightthickness=0, bg="white")
    canvas.grid()

    for i in range(len(map)):
        for j in range(len(map[0])):
        
            if map[i][j].name == None:
                continue
            
            canvas.create_rectangle(offset + i*hspace,offset + j*hspace, offset + i*hspace + size,offset + j*hspace + size)
            
            location = map[i][j]
            
            if location.e:
                canvas.create_line(offset + i*hspace + size/2 + linespace, offset + j*hspace + size/2 - linespace, offset + (i+1)*hspace + size/2 - linespace, offset + j*hspace + size/2 - linespace, fill="red")
            if location.w:
                canvas.create_line(offset + i*hspace + size/2 - linespace, offset + j*hspace + size/2 + linespace, offset + (i-1)*hspace + size/2 + linespace, offset + j*hspace + size/2 + linespace, fill="blue")
            
            if location.n:
                canvas.create_line(offset + i*hspace + size/2 + linespace, offset + j*hspace + size/2 - linespace, offset + (i)*hspace + size/2 + linespace, offset + (j-1)*hspace + size/2 + linespace, fill="gray")
            if location.n:
                canvas.create_line(offset + i*hspace + size/2 - linespace, offset + j*hspace + size/2 - linespace, offset + i*hspace + size/2 - linespace, offset + (j-1)*hspace + size/2 + linespace, fill="brown")

    root.wm_title("Map Visualization")
    root.mainloop()


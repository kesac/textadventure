
# PROTOTYPE
# Draws and displays generated maps onscreen
# It's purpose is to aid developers with map generation

import tkinter

OFFSET    = 50
H_SPACE   = 50
V_SPACE   = 50
RECT_SIZE = 25
LINESPACE = 6

def visualize(map):
    root = tkinter.Tk()
    canvas = tkinter.Canvas(
                root, 
                width  = (OFFSET*2) + (map.width  * H_SPACE), 
                height = (OFFSET*2) + (map.height * V_SPACE), 
                borderwidth = 0, 
                highlightthickness = 0, 
                bg = "white"
             )
    canvas.grid()

    for i in range(map.width):
        for j in range(map.height):
        
            location = map.get(i,j)
        
            if location.name == None:
                continue
            
            room_color = "white"
            
            if location == map.starting_location:
                canvas.create_text(
                    OFFSET + i*H_SPACE + RECT_SIZE/2,
                    OFFSET + j*H_SPACE + RECT_SIZE/2,
                    text = "S",
                    fill = "blue"
                )
            elif location == map.ending_location:
                canvas.create_text(
                    OFFSET + i*H_SPACE + RECT_SIZE/2,
                    OFFSET + j*H_SPACE + RECT_SIZE/2,
                    text = "E",
                    fill = "red"
                )
            elif location.is_leaf():
                canvas.create_text(
                    OFFSET + i*H_SPACE + RECT_SIZE/2,
                    OFFSET + j*H_SPACE + RECT_SIZE/2,
                    text = "L",
                    fill = "green"
                )
            else:
                canvas.create_text(
                    OFFSET + i*H_SPACE + RECT_SIZE/2,
                    OFFSET + j*H_SPACE + RECT_SIZE/2,
                    text = location.depth,
                    fill = "gray"
                )
            
            canvas.create_rectangle(
                OFFSET + i*H_SPACE,
                OFFSET + j*H_SPACE,
                OFFSET + i*H_SPACE + RECT_SIZE,
                OFFSET + j*H_SPACE + RECT_SIZE,
            )
            
            location = map.get(i,j)
            
            if location.e:
                canvas.create_line(
                    OFFSET + i*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    OFFSET + j*H_SPACE + RECT_SIZE/2 - LINESPACE, 
                    OFFSET + (i+1)*H_SPACE + RECT_SIZE/2 - LINESPACE, 
                    OFFSET + j*H_SPACE + RECT_SIZE/2 - LINESPACE, 
                    fill = "red"
                )
            if location.w:
                canvas.create_line(
                    OFFSET + i*H_SPACE + RECT_SIZE/2 - LINESPACE, 
                    OFFSET + j*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    OFFSET + (i-1)*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    OFFSET + j*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    fill = "blue"
                )
            
            if location.n:
                canvas.create_line(
                    OFFSET + i*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    OFFSET + j*H_SPACE + RECT_SIZE/2 - LINESPACE,
                    OFFSET + (i)*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    OFFSET + (j-1)*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    fill = "gray"
                )

            if location.s:
                canvas.create_line(
                    OFFSET + i*H_SPACE + RECT_SIZE/2 - LINESPACE, 
                    OFFSET + j*H_SPACE + RECT_SIZE/2 + LINESPACE, 
                    OFFSET + i*H_SPACE + RECT_SIZE/2 - LINESPACE, 
                    OFFSET + (j+1)*H_SPACE + RECT_SIZE/2 - LINESPACE, 
                    fill = "brown"
                )

    root.wm_title("Map Visualization")
    root.mainloop()


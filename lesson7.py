from tkinter import*
from time import*


class MyFrame (Frame):
  def __init__(self):
    # if next line does not work, try adding / removing spaces on "__"
    Frame.__init__(self)
        
    self.myCanvas=Canvas(width=500, height =400, bg="yellow")
    self.myCanvas.grid()
    
    self.myCanvas.create_rectangle(10,10,400,400, fill="green")
    self.myCanvas.update()

    sleep(3)
    
    self.myCanvas.create_oval(10,10,200,100, fill="gray")

    self.myCanvas.create_text(100,100, text="Hello World",
                              width=70, fill="beige", anchor="se",
                              justify="center",font=("Times",10))




        
frame01=MyFrame()
# use main loop to create the frame
frame01.mainloop()

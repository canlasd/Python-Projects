from tkinter import*
from time import*


class MyFrame (Frame):
  def __init__(self):
    # if next line does not work, try adding / removing spaces on "__"
    Frame.__init__(self)
        
    self.myCanvas=Canvas(width=500, height =400, bg="yellow")
    self.myCanvas.grid()
    
    my_rect_id=self.myCanvas.create_rectangle(10,10,40,40, fill="green")
    self.myCanvas.update()

    for count in range(10):
        increment=10*count
        self.myCanvas.coords(my_rect_id, 10 +increment, 10+increment,
                             50+increment, 50+increment)
        self.myCanvas.update()
        sleep(1)

    self.myCanvas.create_rectangle(300,300,150,150, fill="green")


    my_oval_id=self.myCanvas.create_oval(400,400,40,40, fill="blue")
    self.myCanvas.update()

    for count in range(20):
        increment=10*count
        self.myCanvas.coords(my_oval_id, 400 -increment, 400-increment,
                             50+increment, 50+increment)
        self.myCanvas.update()
        sleep(1)

    self.myCanvas.create_text(200,200, text="Hello", width=70, fill="black",
                              anchor="se", justify="right", font=("Times",12))




    
    """
    self.myCanvas.create_oval(10,10,200,100, fill="gray")

    self.myCanvas.create_text(100,100, text="Hello World",
                              width=70, fill="beige", anchor="se",
                              justify="center",font=("Times",16))

    """


        
frame01=MyFrame()
# use main loop to create the frame
frame01.mainloop()

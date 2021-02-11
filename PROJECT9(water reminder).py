import time
from plyer import notification
from tkinter import *
root = Tk()
root.title("Water reminder")
root.geometry("200x100")

Label(root,text = "minutes").grid(row = 0,column = 1)

s1 = Entry(root)
s1.grid(row = 0,column = 0,ipadx = 1)


def button_func():
    while True:
            notification.notify(
                title = "Please drink water",
                message = 'The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.',
                app_icon = r"C:\Users\cthag\AppData\Roaming\JetBrains\PyCharmCE2020.1\scratches\icon_water.ico",
                timeout  = 10)
            time.sleep(int(s1.get()) * 60)



b1 = Button(root,text = "Remind me in",command = button_func)
b1.grid()

root.mainloop()

'''
if you want to run this script in the background
then open terminal and type
"pythonw .\PROJECT9(water reminder).py"

'''
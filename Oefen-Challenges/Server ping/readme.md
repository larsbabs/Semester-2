
# Een simpele server checker:
Deze server checker pingt je server een aantal keren. Daarna kan je de resultaten zien in een window.

### Interface
Dit is de eerste keer dat ik een interface maak in python, ik had opgezocht welke opties er allemaal zijn. Ik ben bij **tkinter** uitgekomen

Aanmaken van window **root** 
 ```
 root.geometry("400x400")
 canvas1 = Canvas(root, width = 400, height = 300)
 canvas1.pack()
 ```
 toevoegen van input lines:
 ```
 l1 = Label(root, text="Aantal pings:")
 l2 = Label(root, text="IP:")
 ```
 
 De knop met de ping functie:
 ```
 def getPing ():
    x1 = entry1.get()
    x2 = entry2.get()
    if x2.strip().isdigit():
        x2 = x2
    else: x2 = 1
    x2 = int(x2)
    label1 = Label(root, text=pinger(x1, x2))
    canvas1.create_window(200, 300, window=label1)


button1 = Button(text='Ping host:', command=getPing)
 ```
 **x1** en **x2** zijn de 2 inputs die de user geeft.
 
resultaat:

![ping machine](https://user-images.githubusercontent.com/73792386/113689972-306e6200-96cb-11eb-8165-bcce9da6b475.PNG)

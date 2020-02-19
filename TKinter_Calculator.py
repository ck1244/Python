from tkinter import *

class Calculate(object):

    def __init__(self):
        self._isFirstOperand = True
        self._firstOperand = -1
        self._secondOperand = -1
        self._operator = None

    def isFirstOperand(self):
        if self._isFirstOperand:
            return True
        else:
            return False

    def setOperand(self, value):
        if self._isFirstOperand == True:
            self._firstOperand = value
            self._isFirstOperand = False
        else:
            self._secondOperand = value
            self._isFirstOperand = True
        return value

    def setOperator(self, value):
        #Provide an implementation for this method
        if value == '*':
            self._operator = '*'
        elif value == '-':
            self._operator = '-'
        elif value == '/':
            self._operator = '/'
        elif value == '+':
            self._operator = '+'

    def doCalculation(self):
        #Provide an implementation for this method
        result = 0
        if self._operator and self._firstOperand and self._secondOperand is not None:
            if self._operator == '*':
                result = float(self._firstOperand * self._secondOperand)
                label['text'] = "%.1f" % result
            elif self._operator == '+':
                result = float(self._firstOperand + self._secondOperand)
                label['text'] = "%.1f" % result
            elif self._operator == '/':
                result = float(self._firstOperand/self._secondOperand)
                label['text'] = "%.1f" % result
            elif self._operator =='-':
                result =float(self._firstOperand - self._secondOperand)
                label['text'] = "%.1f" % result

    def clear(self):
        result1 = "0.00"
        label['text'] = "%s" % result1


def setOperand(num, calculate):
    #Provide an implementation for this method
    calculate.setOperand(num)

def setOperator(operator, calculate):
    #Provide an implementation for this method
    calculate.setOperator(operator)

def equalsPressed(calculate):
    #Provide an implementation for this method
    calculate.doCalculation()

def clear():
    calculate.clear()

#Creates an instance of the class
calculate = Calculate()

#GUI starts here
root = Tk()
root.title('Assignment 4')

frame1 = Frame(root, height=600,width =90)

root.geometry("150x230")
root.resizable(width=FALSE, height=FALSE)


# Add the result of your GUI implementation here
label = Label(root, text="0.00",borderwidth=10, anchor=CENTER,relief="groove", bg='red', fg='white')
label.grid(row=0,columnspan=3, ipadx =50, ipady =5)


but1 = Button(root,text="1", command = (lambda:setOperand(1,calculate)))
but2 = Button(root,text="2",command = (lambda:setOperand(2,calculate)))
but3 = Button(root, text="3",command = (lambda:setOperand(3,calculate)))
but4 = Button(root, text="4",command = (lambda:setOperand(4,calculate)))
but5 = Button(root, text="5", command = (lambda:setOperand(5,calculate)))
but6 = Button(root, text="6", command = (lambda:setOperand(6,calculate)))
but7 = Button(root, text="7",command = (lambda:setOperand(7,calculate)))
but8 = Button(root, text="8", command = (lambda:setOperand(8,calculate)))
but9 = Button(root, text="9",command = (lambda:setOperand(9,calculate)))
but0 = Button(root, text="0", command = (lambda:setOperand(0,calculate)))
add= Button(root, text="+", command=(lambda:setOperator('+',calculate)))
sub = Button(root, text="-", command=(lambda:setOperator('-',calculate)))
mul = Button(root, text="*", command = (lambda:setOperator('*',calculate)))
div = Button(root, text="/", command =(lambda:setOperator('/',calculate)))
equ = Button(root, text="=", command =(lambda:equalsPressed(calculate)))
cl = Button(root, text="clear", command =(lambda:clear()))

but1.grid(row=1, column=0)
but2.grid(row=1, column=1)
but3.grid(row=1, column=2)
but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)
but7.grid(row=3, column=0)
but8.grid(row=3, column=1)
but9.grid(row=3, column=2)
but0.grid(row=4, column=0)
add.grid(row=4, column=1)
sub.grid(row=4, column=2)
mul.grid(row=5, column=0)
div.grid(row=5, column=1)
equ.grid(row=5, column=2)
cl.grid(row=6,columnspan=3)


root.mainloop()



import Tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        # Instantiate GUI objects
        tk.Tk.__init__(self)
        self.v = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.v)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.text = tk.Text()        

        # Configure text box
        self.text.config(width=100, height=30, state=tk.DISABLED)
        self.text.bind('<Button-1>', self.empty)

        # Bind the return key to submit whatever text is present
        self.bind('<Return>', self.on_button)
        
        # Pack GUI elements together
        self.button.pack(side=tk.BOTTOM)
        self.entry.pack(side=tk.BOTTOM)
        self.text.pack(side=tk.TOP)

    def on_button(self,*args):
        #print self.entry.get()
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END,self.entry.get()+'\n')
        self.v.set('')
        self.text.config(state=tk.DISABLED)

    def empty(self, *args):
        return 'break'

app = SampleApp()
app.mainloop()

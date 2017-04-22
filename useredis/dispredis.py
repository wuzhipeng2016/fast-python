import tkinter as tk
import myredis

class myframe():
    def __init__(self):
        self.root=tk.Tk()
        self.s=tk.Scrollbar(self.root)
        self.t=tk.Text(self.root)
        
        self.key=tk.StringVar()

        self.frame=tk.Frame()

        self.entry=tk.Entry(self.frame,textvariable=self.key,width=75)
        self.entry.pack(side=tk.LEFT)
        tk.Button(self.frame, text='Get',  command=self.ongetdata).pack()

        self.frame.pack(side=tk.TOP)
        self.entry.focus_set()
        self.s.pack(side=tk.RIGHT, fill=tk.Y)
        self.t.pack(side=tk.LEFT, fill=tk.Y)
        self.s.config(command=self.t.yview)
        self.t.config(yscrollcommand=self.s.set)

        tk.mainloop()

    def ongetdata(self):
        key=self.key.get()
        if key=='':
            return
        x=myredis.getvalue(key)
        self.t.delete(1.0,tk.END);
        self.t.insert(tk.END,x)

    if __name__=='__main__':
        print('hello')

m=myframe()


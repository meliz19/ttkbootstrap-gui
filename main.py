from pathlib import Path
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# PATH = Path(__file__).parent / 'assets'
# print(PATH)

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label, width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
    
    def create_form_dropdown(self, label, default_text, options):
        """Create a single form dropdown menu"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label, width=10)
        lbl.pack(side=LEFT, padx=5)

        self.mb = ttk.Menubutton(master=container, text=default_text)
        self.mb.pack(side=LEFT, padx=5, fill=X, expand=YES)

        menu = ttk.Menu(self.mb)
        for opt in options:
            menu.add_radiobutton(label=opt, command=lambda opt=opt: self.selected_option(opt))
        self.mb['menu'] = menu
    
    def selected_option(self, opt):
        print(f'The selected option was {opt}')
        self.mb.configure(text=opt)

    def create_buttonbox(self, func):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=lambda: self.on_submit(func),
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    def on_submit(self, func):
        """Call the func()."""
        func()
    
    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()

class CreateNotebook(ttk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=1, sticky=NSEW, pady=(25, 0))

    def createTab(self, frame_text):
        self.tab = ttk.Frame(self.notebook, padding=10)

        self.labelFrame = ttk.Labelframe(
            master=self.tab,
            text=frame_text,
            padding=(20, 5)
        )
        self.labelFrame.pack(fill=BOTH, expand=YES, padx=20, pady=10)

    def addTab(self, tab_text):
        self.notebook.add(self.tab, text=tab_text)

class CreateApp(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding=(20, 10), **kwargs)
        self.pack(fill=BOTH, expand=YES)
    
        notebook = CreateNotebook(self)

        # Tab 1
        notebook.createTab(frame_text='Frame 1')

        dataForm = DataEntryForm(notebook.labelFrame)
        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter your contact information" 
        hdr = ttk.Label(master=dataForm, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        dataForm.create_form_entry("name", self.name)
        dataForm.create_form_entry("address", self.address)
        dataForm.create_form_entry("phone", self.phone)
        dataForm.create_buttonbox(func=self.foo)

        notebook.addTab(tab_text='Tab 1')

        # Tab 2
        notebook.createTab(frame_text='Frame 2')

        dataForm = DataEntryForm(notebook.labelFrame)
        # form variables
        self.test1 = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter your contact information" 
        hdr = ttk.Label(master=dataForm, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form dropwdown
        dataForm.create_form_dropdown("test", "default_text", list(range(5)))
        dataForm.create_buttonbox(func=self.foo2)
        notebook.addTab(tab_text='Tab 2')

    def foo(self):
        print("Name:", self.name.get())
        print("Address:", self.address.get())
        print("Phone:", self.phone.get())
        return self.name.get(), self.address.get(), self.phone.get()

    def foo2(self):
        print("Dropdown menu tab has been run!")

if __name__ == '__main__':

    app = ttk.Window("First GUI", "pulse")
    CreateApp(app)
    app.mainloop()

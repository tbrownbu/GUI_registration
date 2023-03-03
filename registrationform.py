import tkinter as t 
import tkinter.messagebox

class registrationbox:
    def __init__(self):
        self.main_window = t.Tk()

        self.main_window.geometry('300x300')
        self.main_window.title('Responsive Registration Form')
        
        self.top_frame = t.Frame(self.main_window)
        self.registration_label = t.Label(self.top_frame, text='Responsive Registration Form')
        
        self.email_frame = t.Frame(self.main_window)
        self.email_label = t.Label(self.email_frame, text='Email')
        self.email_entry = t.Entry(self.email_frame,width=40)
    
        self.password_frame = t.Frame(self.main_window)
        self.password_label = t.Label(self.password_frame, text='Password')
        self.password_entry = t.Entry(self.password_frame,width=37,show='*')
    
        self.password2_frame = t.Frame(self.main_window)
        self.password2_label = t.Label(self.password2_frame, text='Re-type Password')
        self.password2_entry = t.Entry(self.password2_frame,width=30,show='*')

        self.name_frame = t.Frame(self.main_window)
        self.fname_label = t.Label(self.name_frame, text='First Name')
        self.fname_entry = t.Entry(self.name_frame,width=12)
        self.lname_label = t.Label(self.name_frame, text='Last Name')
        self.lname_entry = t.Entry(self.name_frame,width=13)

        self.radio_var = t.IntVar()
        self.gender_frame=t.Frame()
        self.rb1=t.Radiobutton(self.gender_frame,text='Male',variable=self.radio_var,value=5)
        self.rb1.pack(side='left')
        self.rb2=t.Radiobutton(self.gender_frame,text='Female',variable=self.radio_var,value=10)
        self.rb2.pack(side='right')

        self.cb_terms=t.IntVar()
        self.terms_frame = t.Frame(self.main_window)
        self.cb1=t.Checkbutton(self.terms_frame,text='I agree with terms and conditions',variable=self.cb_terms)

        self.cb_newsletter=t.IntVar()
        self.newsletter_frame = t.Frame(self.main_window)
        self.cb2=t.Checkbutton(self.newsletter_frame,text='I want to receive the newsletter',variable=self.cb_newsletter)

        self.register_button_frame = t.Frame(self.main_window)
        self.registerbutton = t.Button(self.register_button_frame,text='Register',command=self.validate)
        
        #pack
        self.top_frame.pack()
        self.registration_label.pack()

        #pack frames onto label
        self.email_frame.pack()
        self.email_label.pack(side='left')
        self.email_entry.pack(side='right')

        self.password_frame.pack()
        self.password_label.pack(side='left')
        self.password_entry.pack(side='right')

        self.password2_frame.pack()
        self.password2_label.pack(side='left')
        self.password2_entry.pack(side='right')

        self.name_frame.pack()
        self.fname_label.pack(side='left')
        self.fname_entry.pack(side='left')
        self.lname_label.pack(side='left')
        self.lname_entry.pack()

        self.gender_frame.pack()

        self.cb1.pack()
        self.terms_frame.pack()

        self.cb2.pack()
        self.newsletter_frame.pack()

        self.register_button_frame.pack()
        self.registerbutton.pack()


        t.mainloop()

    def validate(self):

        if self.password_entry.get() != self.password2_entry.get():
            tkinter.messagebox.showerror('Passwords must match')
        elif self.cb_terms.get() == 0 or self.cb_newsletter.get() == 0:
            tkinter.messagebox.showinfo('Missing Info','Please check both checkboxes')
        elif self.radio_var.get() == t.IntVar(value=0):
            tkinter.messagebox.showinfo('Missing Info','Please select a gender')
        else:
            tkinter.messagebox.showinfo('Submission','You have successfuly submitted your info')

myinstance = registrationbox()

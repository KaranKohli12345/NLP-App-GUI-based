from tkinter import *
from my_db import *
from tkinter import messagebox
from my_api import *


'''
tkinter: 
    The full form of Tkinter is "Toolkit interface." Tkinter is a standard Python library used to create graphical user interfaces (GUIs). It provides a way to create windows, dialogs, buttons, menus, and other GUI elements in a Python program.
'''

class NLPAppGuiBased:

    bg_color = '#17202A'
    font = 'poppins'

    def __init__(self):

        self.dbo = Database()

        self.apio = API()
        
        # main window
        self.root = Tk() # Tk is main class of tkinter
        self.root.title('NLP Based App')
        self.root.iconbitmap('Images/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg=NLPAppGuiBased.bg_color)
        
        self.login_page()

        self.root.mainloop() # gui ko hold karta hai screen me


    def login_page(self):

        self.clear_screen()

        heading = Label(self.root, text='NLP Based App', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')

        # we have two geometry managers in tkinter: pack and grid
        heading.pack(pady=(30, 20))
        heading.configure(font=(NLPAppGuiBased.font, 20, 'bold'))

        heading1 = Label(self.root, text='Enter your login credentials', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        heading1.pack(pady=(5, 10))
        heading1.configure(font=(NLPAppGuiBased.font, 12, 'bold'))

        email = Label(self.root, text = 'Enter email')
        email.pack(pady=(10,10))

        self.email_input1 = Entry(self.root, width=50)
        self.email_input1.pack(pady=(5,10), ipady=5)

        password = Label(self.root, text = 'Enter password')
        password.pack(pady=(10,10))

        self.password_input1 = Entry(self.root, width=50, show='*')
        self.password_input1.pack(pady=(5,10), ipady=5)

        login_btn1 = Button(self.root, text='Login', width=10, height=1, command=self.perform_login)
        login_btn1.pack(pady=(10,20))

        dhac = Label(self.root, text="Don't have an account?")
        dhac.pack(pady=(10,10))

        redirect_btn = Button(self.root, text='Register Now!', command=self.do_registration)
        redirect_btn.pack(pady=(10,10))


    def do_registration(self):

        self.clear_screen()
        
        heading = Label(self.root, text='NLP Based App', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        heading.pack(pady=(30, 20))
        heading.configure(font=(NLPAppGuiBased.font, 20, 'bold'))

        heading1 = Label(self.root, text='Enter your credentials', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        heading1.pack(pady=(5, 10))
        heading1.configure(font=(NLPAppGuiBased.font, 12, 'bold'))

        name = Label(self.root, text = 'Enter name')
        name.pack(pady=(10,10))

        self.name_input2 = Entry(self.root, width=50)
        self.name_input2.pack(pady=(5,10), ipady=5)

        email = Label(self.root, text = 'Enter email')
        email.pack(pady=(10,10))

        self.email_input2 = Entry(self.root, width=50)
        self.email_input2.pack(pady=(5,10), ipady=5)

        password = Label(self.root, text = 'Enter password')
        password.pack(pady=(10,10))

        self.password_input2 = Entry(self.root, width=50, show='*')
        self.password_input2.pack(pady=(5,10), ipady=5)

        register_btn = Button(self.root, text='Register', command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        aam = Label(self.root, text='Already a member?')
        aam.pack(pady=(10,10))

        login_btn2 = Button(self.root, text='Login Now?', command=self.login_page)
        login_btn2.pack(pady=(10,10))


    def clear_screen(self):

        # clear existing gui
        for widget in self.root.pack_slaves():
            widget.destroy()
            
    
    def perform_registration(self):

        # fetch data from the gui
        name = self.name_input2.get()
        email = self.email_input2.get()
        password = self.password_input2.get()

        if name.strip()=='' or email.strip()=='' or password=='':
            messagebox.showerror('Registration failed', "Input can't be empty")
        else:
            response = self.dbo.make_database(name.strip(), email.strip(), password)

            if response:
                messagebox.showinfo('Registration Success', 'Succesfully registered! You can login now.')
            else:
                messagebox.showerror('Registration Error', 'User already exists!')


    def perform_login(self):

        email = self.email_input1.get()
        password = self.password_input1.get()

        if email.strip()=='' or password=='':
            messagebox.showerror('Registration failed', "Input can't be empty")
        else:
            response = self.dbo.confirm_login(email.strip(), password)

            if response:
                messagebox.showinfo('Success', 'Login success!')
                self.home_page()
            else:
                messagebox.showerror('Error', 'Login failed!')


    def main_heading(self):

        heading = Label(self.root, text='NLP Based App', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        heading.pack(pady=(30, 20))
        heading.configure(font=(NLPAppGuiBased.font, 20, 'bold'))


    def home_page(self):

        self.clear_screen()

        self.main_heading()

        option1 = Button(self.root, text='Sentiment / Emotion Analysis', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0', command=self.do_Sentiment_Analysis)
        option1.pack(pady=(30, 20))
        option1.configure(font=(NLPAppGuiBased.font, 15, 'bold'))

        option2 = Button(self.root, text='NER (entity extraction)', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0', command=self.do_ner)
        option2.pack(pady=(30, 20))
        option2.configure(font=(NLPAppGuiBased.font, 15, 'bold'))
        
        option3 = Button(self.root, text='Language Detection', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0', command=self.do_language_detection)
        option3.pack(pady=(30, 20))
        option3.configure(font=(NLPAppGuiBased.font, 15, 'bold'))

        logout_btn = Button(self.root, text='Logout', command=self.login_page)
        logout_btn.pack(pady=(30, 20))


    def do_Sentiment_Analysis(self):

        self.clear_screen()

        self.main_heading()

        heading1 = Label(self.root, text='Sentiment / Emotion Analysis', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        heading1.pack(pady=(30, 20))
        heading1.configure(font=(NLPAppGuiBased.font, 15, 'bold'))

        self.text_sentiment = Label(self.root, text='Enter text')
        self.text_sentiment.pack(pady=(30, 20))

        self.text_input_sentiment = Text(self.root, wrap='word', width=50, height=5)
        self.text_input_sentiment.pack(pady=(10,10))

        analyse_btn = Button(self.root, text='Analyse', command=self.perform_sentiment_analysis)
        analyse_btn.pack(pady=(30, 20))

        self.sentiment_result = Label(self.root, bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=(NLPAppGuiBased.font, 10, 'bold'))

        go_back_btn = Button(self.root, text='Go Back', command=self.home_page)
        go_back_btn.pack(pady=(30, 20))


    def perform_sentiment_analysis(self):

        text = self.text_input_sentiment.get("1.0", "end-1c")

        result = self.apio.Sentiment_Analysis(text)

        self.sentiment_result['text'] = result
        

    def do_language_detection(self):

        self.clear_screen()

        self.main_heading()

        heading1 = Label(self.root, text='Language detection', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        heading1.pack(pady=(30, 20))
        heading1.configure(font=(NLPAppGuiBased.font, 15, 'bold'))

        self.text_Language = Label(self.root, text='Enter text')
        self.text_Language.pack(pady=(30, 20))

        self.text_input_Language = Text(self.root, wrap='word', width=50, height=5)
        self.text_input_Language.pack(pady=(10,10), ipady=20)

        analyse_btn = Button(self.root, text='Analyse', command=self.perform_Language_detection)
        analyse_btn.pack(pady=(30, 20))

        self.Language_detection_result = Label(self.root, bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        self.Language_detection_result.pack(pady=(10,10))
        self.Language_detection_result.configure(font=(NLPAppGuiBased.font, 10, 'bold'))

        go_back_btn = Button(self.root, text='Go Back', command=self.home_page)
        go_back_btn.pack(pady=(30, 20))


    def perform_Language_detection(self):

        text = self.text_input_Language.get("1.0", "end-1c")

        result = self.apio.Language_Detection(text)

        self.Language_detection_result['text'] = result


    def do_ner(self):

        self.clear_screen()

        self.main_heading()

        heading1 = Label(self.root, text='NER', bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        heading1.pack(pady=(10, 10))
        heading1.configure(font=(NLPAppGuiBased.font, 15, 'bold'))

        self.text_ner = Label(self.root, text='Enter text')
        self.text_ner.pack(pady=(10, 20))

        self.text_input_ner = Text(self.root, wrap='word', width=50, height=5)
        self.text_input_ner.pack(pady=(10,10), ipady=5)

        analyse_btn = Button(self.root, text='Analyse', command=self.perform_ner)
        analyse_btn.pack(pady=(10, 20))

        self.ner_result = Label(self.root, bg=NLPAppGuiBased.bg_color, fg='#f0f0f0')
        self.ner_result.pack(pady=(10,30))
        self.ner_result.configure(font=(NLPAppGuiBased.font, 10, 'bold'))

        go_back_btn = Button(self.root, text='Go Back', command=self.home_page)
        go_back_btn.pack(pady=(10, 20))


    def perform_ner(self):

        text = self.text_input_ner.get("1.0", "end-1c")

        response = self.apio.NER(text)

        result = ''

        for i in response:
            result += '{} -> {}\n'.format(i, response[i])

        self.ner_result['text'] = result


nlp = NLPAppGuiBased()

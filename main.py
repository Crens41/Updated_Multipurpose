import streamlit as st
from streamlit_option_menu import option_menu
import About, Trans, Chat, About_app, Calculator

class MultiPurpose:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):

        self.apps.append({
            "title": title,
            "function": function
        })
    def run():

        with st.sidebar:        
            app = option_menu(
                menu_title='Henitech Menu',
                options=['Translator','Chat','About Me', 'About App'],
                icons=['translate','chat-right-text','person-vcard','app-indicator'],
                menu_icon='h-circle',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == 'Translator':
            Trans.app()
        if app == 'About Me':
            About.app() 
        if app == "Chat" :
            Chat.app()  
        if app == "About App" :
            About_app.app()
          
             
    run()     



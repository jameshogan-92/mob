from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from database import Database
db = Database("test.db")

Builder.load_file("design.kv")

def validate(uname,pword):
        if uname != "" and pword != "":
            return True
        else :
            return False 

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'signup_screen'

class SignupScreen(Screen):
    def validate(uname,pword):
        if uname != "" and pword != "":
            return True
        else :
            return False 

    def add_user(self, username,password):
        print("{} : {}".format(username,password))
        if db.createUser(username,password) != "Fail":
            self.manager.current = "signup_screen_success"


class SignupScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.current = "login_screen"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

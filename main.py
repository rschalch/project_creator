#!/usr/bin/python3

import npyscreen
from projects import python

class MainForm(npyscreen.Form):
    def create(self):
        pass

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Project Creator")

    # print("---------------")
    # print("PROJECT CREATOR")
    # print("---------------")
    # print("1. Python")
    # print("2. PHP CodeIgniter")
    # print("3. Javascript")

    # while True:

    #     project = input('Choose your project: ')

    #     if project == "1":
    #         python.create_project()
    #         break
    #     elif project == "2":
    #         print("Ah, noooooo!")
    #         break
    #     elif project == "3":
    #         print("Ah, js noooooo!")
    #         break
    #     else:
    #         print("Oops! Wrong number. Try again...")

    # # print(os.getcwd())

if __name__ == "__main__":
    app = App().run()



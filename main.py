# This is a sample Python script.
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class firm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("FIRM")

        Label(self.root, text="Classic Firm", font=("Eras Bold ITC", 40), bg="Grey", fg="white").place(x=10, y=10, width=340, height=50)

        menu_frame = Frame(self.root, bg="Grey")
        menu_frame.place(x=360, y=10, height=50)  # Adjust x to position it beside the label

        # Create buttons for menu items
        home_button = Button(menu_frame, text="Home", bg="White", fg="black", font=("Arial", 14))
        home_button.pack(side="left", padx=40)

        about_us_button = Button(menu_frame, text="About US", bg="White", fg="black", font=("Arial", 14))
        about_us_button.pack(side="left", padx=40)

        about_us_button = Button(menu_frame, text="About US", bg="White", fg="black", font=("Arial", 14))
        about_us_button.pack(side="left", padx=40)

        contact_button = Button(menu_frame, text="Contact", bg="White", fg="black", font=("Arial", 14))
        contact_button.pack(side="left", padx=40)

        contact_button = Button(menu_frame, text="Call to Action", bg="Grey", fg="black", font=("Arial", 14))
        contact_button.pack(side="left", padx=40)

        Label(self.root, text="The future of web \n design, today", font=("Eras Bold ITC", 40), fg="black").place(x=50, y=120)
        Label(self.root, text="The future of web design, today", font=("Calibri", 20), fg="black").place(x=80, y=270)

        contact_button = Button(menu_frame, text="Call to Action", bg="Grey", fg="black", font=("Arial", 14))
        contact_button.place(x=80, y=300)



    # Press the green button in the gutter to run the script.
def main():
    root = Tk()
    obj = firm(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

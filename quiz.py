import sys
import tkinter as tk

def pick_you_want():
    print("\n" + "="*40)
    print("QUIZ PROGRAM LAUNCHER".center(40))
    print("="*40)
    print("1. Quiz Creator")
    print("2. Take Quiz")
    print("3. Exit")
    print("="*40)
    
    while True:
        choice = input("Enter which file you want (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Please only enter 1, 2, or 3.")

def launch_creator(): #launches the creator fie
    from PyQt6.QtWidgets import QApplication
    from oop_creation import QuizCreate
    
    app = QApplication(sys.argv)
    font = app.font()
    font.setFamily("Arial")
    app.setFont(font)
    
    window = QuizCreate()
    window.show()
    sys.exit(app.exec())

def launch_answer(): #launches the quiz answering file
    from oop_answer import TheQuiz
    root = tk.Tk()
    app = TheQuiz(root)
    root.mainloop()

def main():
    while True:
        choice = pick_you_want()
        
        if choice == "1":
            print("\nLaunching Quiz Creator...")
            launch_creator()
        elif choice == "2":
            print("\nLaunching Quiz...")
            launch_answer()
        elif choice == "3":
            print("\nAdios")
            sys.exit(0)

if __name__ == "__main__":
    main()
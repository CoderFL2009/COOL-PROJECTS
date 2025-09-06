import tkinter as tk


def submit_info():


def main():
    
    global root
    # Create the main window
    root = tk.Tk()

    # Set the title of the window
    root.title("Window sized to 500x400")

    # Set the dimensions of the window (width x height)
    root.geometry("500x400")  # Example: 1280 pixels wide and 720 pixels tall

    # Disable resizing
    root.resizable(False, False)

button_A = tk.Button(root, text="A", command=submit_info)
button_A.grid(row=0, columnspan=2, pady=20)

button_B = tk.Button(root, text="B", command=submit_info)
button_B.grid(row=0, columnspan=2, pady=20)

button_C = tk.Button(root, text="C", command=submit_info)
button_C.grid(row=0, columnspan=2, pady=20)

button_D = tk.Button(root, text="D", command=submit_info)
button_D.grid(row=0, columnspan=2, pady=20)

button_E = tk.Button(root, text="E", command=submit_info)
button_E.grid(row=0, columnspan=2, pady=20)

button_F = tk.Button(root, text="F", command=submit_info)
button_F.grid(row=0, columnspan=2, pady=20)


if __name__ == "__main__":
    main()
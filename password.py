import tkinter as tk
import string
import random
from tkinter import messagebox
history=[]
window = tk.Tk()
window.title("Password Generator")
window.geometry("610x465+360+40")
window.configure(bg="black")
def on_closing():
        if messagebox.askyesno(title="Quit", message="ARE YOU SURE YOU WANT TO QUIT?"):
            window.destroy()
            
window.protocol("WM_DELETE_WINDOW", on_closing)

# Create the main window

is_running=False 
def copy():
   
    def copy_password():
        file=open("documents/passcodes.txt","a")
        file.write(str(f"{history}\n"))
        file.close()

        window.clipboard_clear()
        window.clipboard_append(history)
    global is_running
    if is_running==False:  
    
        window2=tk.Tk()
        window2.title("Recent Passwords")
        window2.geometry("400x400+360+40")
        window2.resizable(False,False)
        tk.Label(window2,state="disabled",text="Your recent password was",font="Cambria, 24" ).pack(fill="both", pady=30)
        
        tk.Label(window2,state="disabled",font="Ariel, 20", text=history).pack(fill="both",pady=30) # type: ignore
        button_copy = tk.Button(window2, bd=10, text="Copy Password", command=copy_password)
        button_copy.pack(side="top") 
        is_running=True 
 
    else:
         return    
    
    def on_closing():
        global is_running
        is_running=False
       
        window2.destroy()
      

    window2.protocol("WM_DELETE_WINDOW", on_closing)   
    window2.mainloop()
    

# Initialize character sets
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation )





# Function to generate password
def generate_password():
    try:
        all_chars = []
        if var_lower.get():
            all_chars.extend(lowercase)
        if var_upper.get():
            all_chars.extend(uppercase)
        if var_numbers.get():
            all_chars.extend(numbers+numbers)
        if var_symbols.get():
            all_chars.extend(symbols)
        password_length = int(slider_length.get())
        password = ''.join(random.sample(all_chars, password_length))
        messagebox.showinfo("Your Password", password)
        history.clear()
        history.append(password)
        
        
        
    except ValueError:
        messagebox.showerror("Error",message="Could not generate a password because no character was included. Please choose a character or more.")
# Function to update the label showing the password length
def update_length_label(value):
    label_length.config(text=f"Password Length: {value}")

# Widgets
label_title = tk.Label(window, bg="black", fg="lightblue", font=("Cambria", 40), text="Password Generator")
label_title.pack(side="top")
label_welcome = tk.Label(window, bg="black", fg="orange", font=("Arial", 30), text="🎁🎁🎁 Welcome 🎁🎁🎁")
label_welcome.pack(side="top")
label_description = tk.Label(window, bg="black", fg="white", font=("Arial", 15), text="Select characters to include:")
label_description.pack(side="top")

var_lower = tk.BooleanVar()
check_lower = tk.Checkbutton(window, font=("Ariel",15),text="Lowercase", variable=var_lower, bg="black", fg="white",selectcolor="grey")
check_lower.pack(side="top")

var_upper = tk.BooleanVar()
check_upper = tk.Checkbutton(window,font=("Ariel",15), text="Uppercase", variable=var_upper, bg="black", fg="white",selectcolor='grey')
check_upper.pack(side="top")

var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(window,font=("Ariel",15), text="Numbers", variable=var_numbers, bg="black", fg="white",selectcolor='grey')
check_numbers.pack(side="top")

var_symbols = tk.BooleanVar()
check_symbols = tk.Checkbutton(window,font=("Ariel",15), text="Symbols", variable=var_symbols, bg="black", fg="white",selectcolor='grey')
check_symbols.pack(side="top")

label_length = tk.Label(window, bg="black", fg="white", font=("Cambria", 15), text="Password Length: 8")
label_length.pack(side="top")

slider_length = tk.Scale(window, from_=4, to=20, orient="horizontal", bg="black", fg="white", length=200, command=update_length_label)
slider_length.pack(side="top")

button_generate = tk.Button(window, bd=10, text="Generate Password", command=generate_password)
button_generate.pack(side="top")
button_generate = tk.Button(window, bd=10, text="View Recent Password", command=copy)
button_generate.pack(side="top")
# Run the GUI
window.mainloop()



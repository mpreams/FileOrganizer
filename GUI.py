import customtkinter as ctk
from main import organize_files

app = ctk.CTk()
app.geometry("400x300")
app.title("File Organizer")
app.resizable(False, False)
app.grid_rowconfigure((0, 2), weight=1)
app.grid_columnconfigure(0, weight=1)

entry = ctk.CTkEntry(app, placeholder_text="Enter directory path starting with '/' or 'C:'")
entry.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
directory_path = entry.get()

def submit():
    global directory_path
    directory_path = entry.get()
    try:
        organize_files(directory_path)
    except FileNotFoundError:
        label = ctk.CTkLabel(app, text="Directory not found. Please check the path.")
        label.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
    except Exception as e:
        label = ctk.CTkLabel(app, text=f"An error occurred: {e}")
        label.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")    


button = ctk.CTkButton(app, text="Organize Files", command=submit)
button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")


app.mainloop()

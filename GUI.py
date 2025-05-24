import customtkinter as ctk
from main import organize_files

app = ctk.CTk()
app.geometry("400x300")
app.title("File Organizer")
app.resizable(False, False)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(2, weight=1)

button = ctk.CTkButton(app, text="Organize Files", command=organize_files("/Users/matthewreams/Downloads/"))
button.grid(row=1, column=0, padx=20, pady=20)


app.mainloop()

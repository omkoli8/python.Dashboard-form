import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime


class HealthcareDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Healthcare Dashboard")
        self.root.geometry("600x600")
        self.root.configure(bg="#f5f5f5")

        # Center the content
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Variables
        self.name_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.file_path = tk.StringVar()

        # Main Frame to center content
        main_frame = tk.Frame(root, bg="#ffffff", relief=tk.RIDGE, bd=2, padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # Title
        tk.Label(
            main_frame,
            text="Healthcare Dashboard",
            font=("Arial", 16, "bold"),
            bg="teal",
            fg="white",
            pady=10,
        ).pack(fill=tk.X)

        # Form Frame
        form_frame = tk.Frame(main_frame, padx=20, pady=20, bg="#ffffff")
        form_frame.pack(expand=True)

        # Name Input
        tk.Label(
            form_frame, text="Name:", font=("Arial", 12), bg="#ffffff"
        ).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        tk.Entry(
            form_frame, textvariable=self.name_var, font=("Arial", 12), width=30
        ).grid(row=0, column=1, pady=10)

        # Gender Selection
        tk.Label(
            form_frame, text="Gender:", font=("Arial", 12), bg="#ffffff"
        ).grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        gender_dropdown = ttk.Combobox(
            form_frame,
            textvariable=self.gender_var,
            font=("Arial", 12),
            state="readonly",
            values=["Male", "Female", "Other"],
            width=28,
        )
        gender_dropdown.grid(row=1, column=1, pady=10)

        # DOB Input
        tk.Label(
            form_frame, text="Date of Birth (YYYY-MM-DD):", font=("Arial", 12), bg="#ffffff"
        ).grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        tk.Entry(
            form_frame, textvariable=self.dob_var, font=("Arial", 12), width=30
        ).grid(row=2, column=1, pady=10)

        # Calculate Age
        tk.Button(
            form_frame,
            text="Calculate Age",
            command=self.calculate_age,
            font=("Arial", 10),
            bg="#00796b",
            fg="white",
        ).grid(row=3, column=0, pady=10, padx=10, sticky=tk.W)
        tk.Entry(
            form_frame, textvariable=self.age_var, font=("Arial", 12), state="readonly", width=30
        ).grid(row=3, column=1, pady=10)

        # File Upload
        tk.Label(
            form_frame, text="Upload File:", font=("Arial", 12), bg="#ffffff"
        ).grid(row=4, column=0, sticky=tk.W, padx=10, pady=10)
        tk.Entry(
            form_frame, textvariable=self.file_path, font=("Arial", 12), state="readonly", width=30
        ).grid(row=4, column=1, pady=10)
        tk.Button(
            form_frame,
            text="Browse",
            command=self.upload_file,
            font=("Arial", 10),
            bg="#00796b",
            fg="white",
        ).grid(row=5, column=0, pady=10, padx=10, sticky=tk.W)

        # Submit Button
        tk.Button(
            form_frame,
            text="Submit",
            command=self.submit_form,
            font=("Arial", 12, "bold"),
            bg="#4caf50",
            fg="white",
            width=20,
        ).grid(row=6, columnspan=2, pady=20)

    def calculate_age(self):
        try:
            dob = datetime.strptime(self.dob_var.get(), "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            self.age_var.set(f"{age} years")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid Date of Birth (YYYY-MM-DD).")

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Images", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.file_path.set(file_path)

    def submit_form(self):
        name = self.name_var.get()
        gender = self.gender_var.get()
        dob = self.dob_var.get()
        age = self.age_var.get()
        file = self.file_path.get()

        if not name or not gender or not dob or not file:
            messagebox.showwarning("Missing Fields", "Please fill all the fields and upload a file.")
            return

        # Display Success Message
        messagebox.showinfo(
            "Form Submitted", f"Name: {name}\nGender: {gender}\nDOB: {dob}\nAge: {age}\nFile: {file}"
        )
        print("Form Submitted:", {"Name": name, "Gender": gender, "DOB": dob, "Age": age, "File": file})

        # Reset fields
        self.name_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.age_var.set("")
        self.file_path.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = HealthcareDashboard(root)
    root.mainloop()

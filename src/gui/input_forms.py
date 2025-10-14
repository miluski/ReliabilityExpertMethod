from tkinter import Tk, Label, Entry, Button, Frame, StringVar, IntVar, messagebox

class InputForm:
    def __init__(self, master):
        self.master = master
        master.title("Wprowadzenie danych")

        self.frame = Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.label_experts_mech = Label(self.frame, text="Liczba ekspertów mechanicznych:")
        self.label_experts_mech.grid(row=0, column=0, sticky="w")
        self.experts_mech_var = IntVar()
        self.entry_experts_mech = Entry(self.frame, textvariable=self.experts_mech_var)
        self.entry_experts_mech.grid(row=0, column=1)

        self.label_experts_elec = Label(self.frame, text="Liczba ekspertów elektronicznych:")
        self.label_experts_elec.grid(row=1, column=0, sticky="w")
        self.experts_elec_var = IntVar()
        self.entry_experts_elec = Entry(self.frame, textvariable=self.experts_elec_var)
        self.entry_experts_elec.grid(row=1, column=1)

        self.label_groups = Label(self.frame, text="Liczba grup (domyślnie 4):")
        self.label_groups.grid(row=2, column=0, sticky="w")
        self.groups_var = IntVar(value=4)
        self.entry_groups = Entry(self.frame, textvariable=self.groups_var)
        self.entry_groups.grid(row=2, column=1)

        self.submit_button = Button(self.frame, text="Zatwierdź", command=self.submit)
        self.submit_button.grid(row=3, columnspan=2, pady=10)

    def submit(self):
        experts_mech = self.experts_mech_var.get()
        experts_elec = self.experts_elec_var.get()
        groups = self.groups_var.get()

        if experts_mech <= 0 or experts_elec <= 0 or groups <= 0:
            messagebox.showerror("Błąd", "Wszystkie wartości muszą być większe od zera.")
            return

        messagebox.showinfo("Sukces", f"Wprowadzono:\nEksperci mechaniczni: {experts_mech}\nEksperci elektroniczni: {experts_elec}\nGrupy: {groups}")

if __name__ == "__main__":
    root = Tk()
    input_form = InputForm(root)
    root.mainloop()

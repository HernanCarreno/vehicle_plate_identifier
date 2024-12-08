import tkinter as tk
from tkinter import messagebox
from lib.plate_identifier import PlateIdentifier

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Identificador de Placas Vehiculares")
        self.geometry("500x500")
        self.configure(bg="#f5f5f5")
        self.create_widgets()

    def create_widgets(self):
        # Título
        tk.Label(self, text="Identificador de Placas Vehiculares", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)

        # Entrada de Placa
        self.plate_label = tk.Label(self, text="Ingrese la placa:", bg="#f5f5f5", font=("Arial", 12))
        self.plate_label.pack(pady=5)

        self.plate_entry = tk.Entry(self, font=("Arial", 12), width=20)
        self.plate_entry.pack(pady=5)
        self.plate_entry.bind("<KeyRelease>", self.convert_to_uppercase)  # Convierte a mayúsculas

        # Botón para identificar
        self.identify_button = tk.Button(self, text="Identificar", command=self.identify_plate, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.identify_button.pack(pady=10)

        # Resultados
        self.result_label = tk.Text(self, bg="#f5f5f5", font=("Arial", 12), height=15, width=50, state=tk.DISABLED, wrap=tk.WORD)
        self.result_label.pack(pady=10)

    def convert_to_uppercase(self, event=None):
        """Convierte el texto ingresado en el campo a mayúsculas."""
        current_text = self.plate_entry.get()
        self.plate_entry.delete(0, tk.END)
        self.plate_entry.insert(0, current_text.upper())

    def identify_plate(self):
        # Limpia los resultados previos
        self.result_label.configure(state=tk.NORMAL)
        self.result_label.delete(1.0, tk.END)

        plate = self.plate_entry.get().strip()
        if not plate:
            messagebox.showerror("Error", "Por favor, ingrese una placa.")
            return

        # Identificar la placa
        identifier = PlateIdentifier()
        matches = identifier.identify(plate)

        for match in matches:
            self.result_label.insert(tk.END, f"País: {match['country']}\n")
            self.result_label.insert(tk.END, f"Región: {match['region']}\n")
            self.result_label.insert(tk.END, f"Tipo de Vehículo: {match['vehicle_type']}\n")
            self.result_label.insert(tk.END, "-" * 40 + "\n")

        self.result_label.configure(state=tk.DISABLED)

def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
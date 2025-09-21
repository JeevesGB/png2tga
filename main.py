import os
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar, OptionMenu
from PIL import Image


class PNGtoTGAConverter:
    def __init__(self, master):
        self.master = master
        master.title("PNG to 32-bit TGA Converter")
        master.geometry("500x350")  
        master.resizable(False, False)  

        self.input_path = StringVar()
        Label(master, text="Input Folder:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Button(master, text="Browse", command=self.select_input).grid(row=0, column=1, padx=5, pady=5)

        self.output_path = StringVar()
        Label(master, text="Output Folder:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        Button(master, text="Browse", command=self.select_output).grid(row=1, column=1, padx=5, pady=5)

        self.scale_var = StringVar(master)
        self.scale_var.set("None")  # default (no resizing)
        sizes = ["None", "4", "8", "16", "32", "64", "128", "256", "512", "1024"]
        Label(master, text="Resize to:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        OptionMenu(master, self.scale_var, *sizes).grid(row=2, column=1, padx=5, pady=5)

        Button(master, text="Convert", command=self.convert).grid(row=3, column=0, columnspan=2, pady=20)

    def select_input(self):
        folder = filedialog.askdirectory(title="Select Input Folder")
        if folder:
            self.input_path.set(folder)

    def select_output(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_path.set(folder)

    def convert(self):
        input_folder = self.input_path.get()
        output_folder = self.output_path.get()
        resize_value = self.scale_var.get()

        if not input_folder or not output_folder:
            messagebox.showerror("Error", "Please select both input and output folders")
            return

        converted = 0
        for file in os.listdir(input_folder):
            if file.lower().endswith(".png"):
                in_file = os.path.join(input_folder, file)
                out_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".tga")

                try:
                    img = Image.open(in_file).convert("RGBA") 
                    if resize_value != "None":
                        size = int(resize_value)
                        img = img.resize((size, size), Image.LANCZOS)
                    img.save(out_file, format="TGA")
                    converted += 1
                except Exception as e:
                    print(f"Error converting {file}: {e}")

        messagebox.showinfo("Done", f"Converted {converted} PNG files to TGA")


if __name__ == "__main__":
    root = Tk()
    app = PNGtoTGAConverter(root)
    root.mainloop()

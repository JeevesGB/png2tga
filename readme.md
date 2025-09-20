# PNG to 32-bit TGA Batch Converter

A simple GUI tool to batch convert `.png` images to 32-bit `.tga` format.  
Built with **Python**, **Pillow**, and **Tkinter**.

---

## Features
- Select an **input folder** containing PNG files.
- Select an **output folder** where converted files will be saved.
- Converts all `.png` images into `.tga` with **RGBA (32-bit)** format.
- Lightweight and easy to use.

---

## Requirements
- [Python 3.9+](https://www.python.org/downloads/)  
- Pip packages:
  ```bash
  pip install pillow
  ```

*(Tkinter comes bundled with most Python installations, no extra install required.)*

---

## Running the Tool
1. Place your `.png` files in a folder.  
2. Run the script via the batch file:

   ```bash
   run_converter.bat
   ```

3. In the GUI:
   - Select the **Input Folder** containing PNG files.  
   - Select the **Output Folder** where `.tga` files will be saved.  
   - Click **Convert**.  

4. A message will confirm how many files were converted.

---

## Building as a Standalone EXE
This project can be built into a standalone Windows `.exe` using **PyInstaller**.

### 1. Install PyInstaller
```bash
pip install pyinstaller
```

### 2. Build with batch script
Run:
```bash
build_exe.bat
```

This will create an executable inside the `dist/` folder:
```
dist/PNGtoTGAConverter.exe
```

You can then distribute this `.exe` file — no Python required on the target machine.

---

## Files
- `converter.py` → Main program  
- `run_converter.bat` → Runs the script  
- `build_exe.bat` → Builds the `.exe`  

---

## Notes
- Input files must be `.png`.  
- Output files will be `.tga` with the same base name.  
- Existing `.tga` files in the output folder may be overwritten.  

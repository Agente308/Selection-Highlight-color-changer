import tkinter as tk
from tkinter import colorchooser, messagebox
import winreg

def aplicar_color():
    if not color_actual:
        messagebox.showwarning("Color no seleccionado", "Por favor selecciona un color primero.")
        return

    r, g, b = color_actual
    color_str = f"{r} {g} {b}"
    try:
        ruta = r"Control Panel\Colors"
        clave = winreg.OpenKey(winreg.HKEY_CURRENT_USER, ruta, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(clave, "Hilight", 0, winreg.REG_SZ, color_str)
        winreg.SetValueEx(clave, "HotTrackingColor", 0, winreg.REG_SZ, color_str)
        winreg.CloseKey(clave)
        messagebox.showinfo("Éxito", f"Colores aplicados: {color_str}\n(Reinicia tu computadora para ver los cambios)")
    except PermissionError:
        messagebox.showerror("Permiso denegado", "Debes ejecutar como administrador.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def seleccionar_color():
    global color_actual
    color = colorchooser.askcolor(title="Selecciona un color")[0]
    if color:
        color_actual = tuple(map(int, color))
        lbl_color.config(text=f"RGB: {color_actual[0]} {color_actual[1]} {color_actual[2]}")
        canvas_color.config(bg=f'#{color_actual[0]:02x}{color_actual[1]:02x}{color_actual[2]:02x}')

color_actual = None
root = tk.Tk()
root.title("Color Changer Windows")
root.geometry("300x200")
root.resizable(False, False)

btn_elegir = tk.Button(root, text="Elegir color RGB", command=seleccionar_color)
btn_elegir.pack(pady=10)

canvas_color = tk.Canvas(root, width=60, height=30, bg="white", highlightthickness=1, highlightbackground="black")
canvas_color.pack()

lbl_color = tk.Label(root, text="RGB: - - -")
lbl_color.pack(pady=10)

btn_aplicar = tk.Button(root, text="Aplicar al Registro", command=aplicar_color)
btn_aplicar.pack(pady=10)

lbl_footer = tk.Label(root, text="Desarrollado por el Agente 308", font=("Arial", 8), fg="gray")
lbl_footer.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)  

root.mainloop()

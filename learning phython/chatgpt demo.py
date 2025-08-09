import tkinter as tk

def perform_task(r, c):
    label.config(text=f"You clicked button at Row {r}, Column {c}")

root = tk.Tk()
root.geometry("300x300")
root.title("Grid with Output in Window")

# Output label
label = tk.Label(root, text="", font=("Algerian", 14))
label.grid(row=3, column=0, columnspan=3, pady=10)

# Create 3x3 grid of buttons
for row in range(3):
    for col in range(3):
        tk.Button(root,
                  text=f"{row},{col}",
                  command=lambda r=row, c=col: perform_task(r, c),
                  width=10, height=3).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()

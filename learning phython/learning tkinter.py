import tkinter as tk
root=tk.Tk()
root.title("hare krishna my first app")
root.geometry("300x250")
def takeentry():
   store=entry.get()
def printing():
   label=tk.Label(root,text="i am clicked",font="Algerian,17")
   
   
entry=tk.Entry(root,width=10)
entry.pack(padx=10,pady=10)
for row in range(3):
  for col in range(3):
     button=tk.Button(root,text=f"row={row+1} col={col+1}",width=10,height=5, command=lambda row=row,column=col:takeentry)
     button.grid(row=row,column=col,padx=5,pady=5)

root.mainloop()
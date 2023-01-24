import csv
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.geometry('750x500')
root.title('Compare CSV')

file1 = filedialog.askopenfilename(title='Browse for file 1')
file2 = filedialog.askopenfilename(title='Browse for file 2')

def compare_csv(file1, file2):
    non_matching_rows = []
    i = 0
    
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        csv1 = list(csv.reader(f1))
        csv2 = list(csv.reader(f2))
        for row1 in csv1:
            match = False
            i+= 1
            for row2 in csv2:
                if row1 == row2:
                    match = True
                    break
            if not match:
                non_matching_rows.append(file1 + ' ROW: ' + str(i) + '----->' + str(row1))
    if non_matching_rows:
        tk.Label(root, text="Non-matching rows:").pack()
        for row in non_matching_rows:
            tk.Label(root, text=row).pack()
    else:
        print("All rows matched.")

print('')
compare_csv(file1,file2)
print('')
compare_csv(file2,file1)

root.mainloop()
from tkinter import *
import sqlite3

root = Tk()
root.title('Pharmacy Management System')
root.geometry("1500x1500")

# Background color for the root window
root.configure(bg="#92badc")

# Title Label at the top of the window
title_label = Label(root, text="Pharmacy Management System", font=("Roboto", 35, "bold"),bg="#92badc")
title_label.grid(row=0, column=0, columnspan=1500, pady=20)

# Create a container (frame) with a background color
container = Frame(root, bg="#e8f5e9", bd=5)
container.grid(row=1, column=0, columnspan=1000, padx=350, pady=20, sticky="nsew")

# Submit function
def submit():
    conn = sqlite3.connect('pharmacy_info.db')
    c = conn.cursor()

    c.execute("INSERT INTO Pharmacy_info VALUES(:med_id, :med_name, :med_prize, :med_quantity, :med_prescription)",
              {
                  'med_id':med_id .get(),
                  'med_name': med_name.get(),
                  'med_prize': med_prize.get(),
                  'med_quantity': med_quantity.get(),
                  'med_prescription': med_prescription.get(),
                  
              })
    conn.commit()
    conn.close()

    # Clear the entry fields after submission
    med_id.delete(0, END)
    med_name.delete(0, END)
    med_prize.delete(0, END)
    med_quantity.delete(0, END)
    med_quantity.delete(0, END)
    med_prescription.delete(0, END)

# Query function to center the output
def query():
    conn = sqlite3.connect('Pharmacy_info.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM pharmacy_info")
    records = c.fetchall()

    query_frame=Frame(root, bg="white",bd=2,relief="solid")
    query_frame.grid(row=12,column=0,columnspan=100,pady=20,padx=350)

    Label(query_frame,text="Medicine ID", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10)
    Label(query_frame,text="Medicine Name", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10)
    Label(query_frame,text="Medicine Prize", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10)
    Label(query_frame,text="Medicine Quantity", font=("Arial", 10, "bold")).grid(row=0, column=3, padx=10)
    Label(query_frame,text="Medicine Prescription", font=("Arial", 10, "bold")).grid(row=0, column=4, padx=10)

    for idx, record in enumerate(records):
        Label(query_frame,text=record[0],font=("Arial", 9)).grid(row=idx+1, column=0, padx=10)
        Label(query_frame,text=record[1],font=("Arial", 9)).grid(row=idx+1, column=1, padx=10)
        Label(query_frame,text=record[2],font=("Arial", 9)).grid(row=idx+1, column=2, padx=10)
        Label(query_frame,text=record[3],font=("Arial", 9)).grid(row=idx+1, column=3, padx=10)
        Label(query_frame,text=record[4],font=("Arial", 9)).grid(row=idx+1, column=4, padx=10)
        
    conn.commit()
    conn.close()

# Delete function
def delete():
    conn = sqlite3.connect('Pharmacy_info.db')
    c = conn.cursor()
    c.execute("DELETE from pharmacy_info WHERE oid=" + delete_box.get())
    delete_box.delete(0, END)

    conn.commit()
    conn.close()
    
def update():
    conn = sqlite3.connect('Pharmacy_info.db')
    c = conn.cursor()

    # Ensure `record_id` is properly passed
    record_id = delete_box.get()  # or retain from the `edit()` function

    c.execute("""UPDATE Pharmacy_info SET
        med_id = :id,
        med_name = :name,
        med_prize = :prize,
        med_quantity = :quantity,
        med_prescription = :prescription
        WHERE oid = :oid""",
              {
                  'id': med_id_editor.get(),
                  'name': med_name_editor.get(),
                  'prize': med_prize_editor.get(),
                  'quantity': med_quantity_editor.get(),
                  'prescription': med_prescription_editor.get(),
                  'oid': record_id
              })

    conn.commit()
    conn.close()


# Edit function
def edit():
    editor = Tk()
    editor.title('Update Record')
    editor.geometry("500x500")
    editor.configure(bg="#f0f0f0")

    conn = sqlite3.connect('Pharmacy_info.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM Pharmacy_info WHERE oid=" + record_id)
    records = c.fetchall()

    global med_id_editor
    global med_name_editor
    global med_prize_editor
    global med_quantity_editor
    global med_prescription_editor
    
    med_id_editor = Entry(editor, width=30, bg="#ffffff", fg="black", bd=2)
    med_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    med_name_editor = Entry(editor, width=30, bg="#ffffff", fg="black", bd=2)
    med_name_editor.grid(row=1, column=1, padx=20)
    med_prize_editor = Entry(editor, width=30, bg="#ffffff", fg="black", bd=2)
    med_prize_editor.grid(row=2, column=1, padx=20)
    med_quantity_editor = Entry(editor, width=30, bg="#ffffff", fg="black", bd=2)
    med_quantity_editor.grid(row=3, column=1, padx=20)
    med_prescription_editor = Entry(editor, width=30, bg="#ffffff", fg="black", bd=2)
    med_prescription_editor.grid(row=4, column=1, padx=20)


    # Labels for the editor window
    med_id_label = Label(editor, text="Medicine ID", bg="#f0f0f0", fg="black")
    med_id_label.grid(row=0, column=0, pady=(10, 0))
    med_name_label = Label(editor, text="Medicine Name", bg="#f0f0f0", fg="black")
    med_name_label.grid(row=1, column=0)
    med_prize_label = Label(editor, text="Medicine Prize", bg="#f0f0f0", fg="black")
    med_prize_label.grid(row=2, column=0)
    med_quantity_label = Label(editor, text="Medicine Quantity", bg="#f0f0f0", fg="black")
    med_quantity_label.grid(row=3, column=0)
    med_prescription_label = Label(editor, text="Medicine Prescription", bg="#f0f0f0", fg="black")
    med_prescription_label.grid(row=4, column=0)

    for record in records:
        med_id_editor.insert(0, record[0])
        med_name_editor.insert(0, record[1])
        med_prize_editor.insert(0, record[2])
        med_quantity_editor.insert(0, record[3])
        med_prescription_editor.insert(0, record[4])
        
    save_btn = Button(editor, text="Save Record", command=update, bg="#4CAF50", fg="white", font=("Arial", 12))
    save_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=140)
        
    conn.commit()
    conn.close()
    
'''
c.execute("""CREATE TABLE "Pharmacy_info" (
        "med_id"	INTEGER,
	"med_name"	TEXT,
	"med_prize"	INTEGER,
	"med_quantity"	INTEGER,
	"med_prescription"	TEXT
)""")
'''

# Main form widgets inside the container frame
med_id = Entry(container, width=30, bg="#ffffff", fg="black", bd=2)
med_id.grid(row=0, column=1, padx=20, pady=5)
med_name = Entry(container, width=30, bg="#ffffff", fg="black", bd=2)
med_name.grid(row=1, column=1, padx=20, pady=5)
med_prize = Entry(container, width=30, bg="#ffffff", fg="black", bd=2)
med_prize.grid(row=2, column=1, padx=20, pady=5)
med_quantity = Entry(container, width=30, bg="#ffffff", fg="black", bd=2)
med_quantity.grid(row=3, column=1, padx=20, pady=5)
med_prescription = Entry(container, width=30, bg="#ffffff", fg="black", bd=2)
med_prescription.grid(row=4, column=1, padx=20, pady=5)

# Labels for the main form inside the container
med_id_label = Label(container, text="Medicine ID", bg="#e8f5e9", fg="black")
med_id_label.grid(row=0, column=0, pady=(10, 0))
med_name_label = Label(container, text="Medicine Name", bg="#e8f5e9", fg="black")
med_name_label.grid(row=1, column=0, pady=5)
med_prize_label = Label(container, text="Medicine Prize", bg="#e8f5e9", fg="black")
med_prize_label.grid(row=2, column=0, pady=5)
med_quantity_label = Label(container, text="Medicine Quantity", bg="#e8f5e9", fg="black")
med_quantity_label.grid(row=3, column=0, pady=5)
med_prescription_label = Label(container, text="Medicine Prescription", bg="#e8f5e9", fg="black")
med_prescription_label.grid(row=4, column=0, pady=5)

# Buttons beside the item_number entry (column=2)
submit_btn = Button(container, text="Add Record", command=submit, bg="#4CAF50", fg="white", font=("Arial", 12))
submit_btn.grid(row=0, column=2, pady=7, padx=15, ipadx=130)

query_btn = Button(container, text="Show Records", command=query, bg="#2196F3", fg="white", font=("Arial", 12))
query_btn.grid(row=1, column=2, pady=7, padx=15, ipadx=130)

delete_btn = Button(container, text="Delete Record", command=delete, bg="#f44336", fg="white", font=("Arial", 12))
delete_btn.grid(row=2, column=2, pady=7, padx=15, ipadx=130)

update_btn = Button(container, text="Edit Record", command=edit, bg="#FF9800", fg="white", font=("Arial", 12))
update_btn.grid(row=3, column=2, pady=7, padx=15, ipadx=130)

# 'Select Item Number' widget below the buttons
delete_box_label = Label(container, text="Select Item Number", bg="#e8f5e9", fg="black")
delete_box_label.grid(row=5, column=0, pady=5)
delete_box = Entry(container, width=30, bg="#ffffff", fg="black", bd=2)
delete_box.grid(row=5, column=1, padx=20)

root.mainloop()

from tkinter import *
from tkinter import messagebox   # <-- added to fix the bug
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#-----------------FUNCTIONALITY PART---------------------#

def total():
    bathsoap = int(bathsoapEntry.get() or 0)
    facewash = int(facewashEntry.get() or 0)
    hairoil = int(hairoilEntry.get() or 0)
    lipstick = int(lipstickEntry.get() or 0)
    nailpolish = int(nailpolishEntry.get() or 0)
    shampoo = int(shampooEntry.get() or 0)

    totalcosmeticprice = (
        bathsoap * 50 +
        facewash * 230 +
        hairoil * 150 +
        lipstick * 60 +
        nailpolish * 80 +
        shampoo * 210
    )

    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, str(totalcosmeticprice)+'tk')


    #------------------groceryprice calculation------------#
    rice = int(riceEntry.get() or 0)
    sugar = int(sugarEntry.get() or 0)
    salt = int(saltEntry.get() or 0)
    noodles = int(noodlesEntry.get() or 0)
    flour = int(flourEntry.get() or 0)
    coffee = int(coffeeEntry.get() or 0)

    totalgroceryprice = (
        rice * 60 +
        sugar * 70 +
        salt * 40 +
        noodles * 30 +
        flour * 55 +
        coffee * 450
    )

    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, str(totalgroceryprice)+'tk')

    #------------------drinksprice calculation------------#

    pepsi = int(pepsiEntry.get() or 0)
    sprite = int(spriteEntry.get() or 0)
    water = int(waterEntry.get() or 0)
    fanta = int(fantaEntry.get() or 0)
    cocacola = int(cocacolaEntry.get() or 0)
    energydrinks = int(energydrinksEntry.get() or 0)

    totaldrinksprice = (
        pepsi * 50 +
        sprite * 50 +
        water * 20 +
        fanta * 50 +
        cocacola * 60 +
        energydrinks * 120
    )

    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0, str(totaldrinksprice)+'tk')



    #------------------Tax Calculation------------------#

    cosmetictax = totalcosmeticprice * 0.03      # 3%
    grocerytax = totalgroceryprice * 0.05        # 5%
    drinkstax = totaldrinksprice * 0.02       # 2%

    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, f"{cosmetictax:.2f}"+'tk')

    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f"{grocerytax:.2f}"+'tk')

    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, f"{drinkstax:.2f}"+'tk')

    #-----------------tax calculation end----------------#


#-------------------bill function ----------------------------#
def bill():
    textarea.delete(1.0, END)

    textarea.insert(END, "\t Welcome To Grocery Shop\n")
    textarea.insert(END, "=" * 48 + "\n")

    textarea.insert(END, f" Bill No.   : {billnumberEntry.get()}\n")
    textarea.insert(END, f" Customer   : {nameEntry.get()}\n")
    textarea.insert(END, f" Phone No.  : {phoneEntry.get()}\n")

    textarea.insert(END, "=" * 48 + "\n")
    textarea.insert(END, "Product\t\tQty\tPrice\n")
    textarea.insert(END, "=" * 48 + "\n")

    # ---------------- Cosmetics ---------------- #

    if int(bathsoapEntry.get()) > 0:
        textarea.insert(END, f"Bath Soap\t{bathsoapEntry.get()}\t{int(bathsoapEntry.get()) * 50}\n")

    if int(facewashEntry.get()) > 0:
        textarea.insert(END, f"Face Wash\t{facewashEntry.get()}\t{int(facewashEntry.get()) * 230}\n")

    if int(hairoilEntry.get()) > 0:
        textarea.insert(END, f"Hair Oil\t{hairoilEntry.get()}\t{int(hairoilEntry.get()) * 150}\n")

    if int(lipstickEntry.get()) > 0:
        textarea.insert(END, f"Lipstick\t{lipstickEntry.get()}\t{int(lipstickEntry.get()) * 60}\n")

    if int(nailpolishEntry.get()) > 0:
        textarea.insert(END, f"Nail Polish\t{nailpolishEntry.get()}\t{int(nailpolishEntry.get()) * 80}\n")

    if int(shampooEntry.get()) > 0:
        textarea.insert(END, f"Shampoo\t\t{shampooEntry.get()}\t{int(shampooEntry.get()) * 210}\n")

    # ---------------- Grocery ---------------- #

    if int(riceEntry.get()) > 0:
        textarea.insert(END, f"Rice\t\t{riceEntry.get()}\t{int(riceEntry.get()) * 60}\n")

    if int(sugarEntry.get()) > 0:
        textarea.insert(END, f"Sugar\t\t{sugarEntry.get()}\t{int(sugarEntry.get()) * 70}\n")

    if int(saltEntry.get()) > 0:
        textarea.insert(END, f"Salt\t\t{saltEntry.get()}\t{int(saltEntry.get()) * 40}\n")

    if int(noodlesEntry.get()) > 0:
        textarea.insert(END, f"Noodles\t\t{noodlesEntry.get()}\t{int(noodlesEntry.get()) * 30}\n")

    if int(flourEntry.get()) > 0:
        textarea.insert(END, f"Flour\t\t{flourEntry.get()}\t{int(flourEntry.get()) * 55}\n")

    if int(coffeeEntry.get()) > 0:
        textarea.insert(END, f"Coffee\t\t{coffeeEntry.get()}\t{int(coffeeEntry.get()) * 450}\n")

    # ---------------- Drinks ---------------- #

    if int(pepsiEntry.get()) > 0:
        textarea.insert(END, f"Pepsi\t\t{pepsiEntry.get()}\t{int(pepsiEntry.get()) * 50}\n")

    if int(spriteEntry.get()) > 0:
        textarea.insert(END, f"Sprite\t\t{spriteEntry.get()}\t{int(spriteEntry.get()) * 50}\n")

    if int(waterEntry.get()) > 0:
        textarea.insert(END, f"Water\t\t{waterEntry.get()}\t{int(waterEntry.get()) * 20}\n")

    if int(fantaEntry.get()) > 0:
        textarea.insert(END, f"Fanta\t\t{fantaEntry.get()}\t{int(fantaEntry.get()) * 50}\n")

    if int(cocacolaEntry.get()) > 0:
        textarea.insert(END, f"Coca Cola\t{cocacolaEntry.get()}\t{int(cocacolaEntry.get()) * 60}\n")

    if int(energydrinksEntry.get()) > 0:
        textarea.insert(END, f"Energy Drink\t{energydrinksEntry.get()}\t{int(energydrinksEntry.get()) * 120}\n")

    # ---------------- Total ---------------- #

    textarea.insert(END, "=" * 48 + "\n")

    textarea.insert(END, f"Cosmetic Price : {cosmeticpriceEntry.get()}\n")
    textarea.insert(END, f"Grocery Price  : {grocerypriceEntry.get()}\n")
    textarea.insert(END, f"Drinks Price   : {drinkspriceEntry.get()}\n")

    textarea.insert(END, "-" * 48 + "\n")

    textarea.insert(END, f"Cosmetic Tax   : {cosmetictaxEntry.get()}\n")
    textarea.insert(END, f"Grocery Tax    : {grocerytaxEntry.get()}\n")
    textarea.insert(END, f"Drinks Tax     : {drinkstaxEntry.get()}\n")

    grandtotal = (
            float(cosmeticpriceEntry.get().replace("tk", ""))
            + float(grocerypriceEntry.get().replace("tk", ""))
            + float(drinkspriceEntry.get().replace("tk", ""))
            + float(cosmetictaxEntry.get().replace("tk", ""))
            + float(grocerytaxEntry.get().replace("tk", ""))
            + float(drinkstaxEntry.get().replace("tk", ""))
    )

    textarea.insert(END, "=" * 48 + "\n")
    textarea.insert(END, f"Grand Total : {grandtotal:.2f} Tk\n")
    textarea.insert(END, "=" * 48 + "\n")
    textarea.insert(END, "\nThank You dear customer.Visit Again.")

#-----------------bill function end-------------------------------#

#-------------------E-mail button function  start ---------------------------------------#

from tkinter import Toplevel, Label, Entry, Button, messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import tempfile
import os
import threading

def send_email():
    # Get the bill text
    bill_text = textarea.get("1.0", END).strip()
    if not bill_text:
        messagebox.showwarning("No Bill", "Please generate the bill first.")
        return

    #---------- HARDCODE YOUR SENDER CREDENTIALS HERE our App Password ---------#
    SENDER = "mdbyzeadbostame5@gmail.com"
    PASSWORD = "tmpybfwlcejspryz"


    # Create a pop-up window
    popup = Toplevel(root)
    popup.title("Send Receipt")
    popup.geometry("350x150")
    popup.resizable(False, False)
    popup.grab_set()

    Label(popup, text="Customer Email:", font=("Arial", 12)).pack(pady=10)
    email_entry = Entry(popup, font=("Arial", 12), width=30)
    email_entry.pack(pady=5)
    email_entry.focus()

    btn_frame = Frame(popup)
    btn_frame.pack(pady=15)

    # ---------- Sending function (will run in background) ----------
    def send_email_action():
        receiver = email_entry.get().strip()
        if not receiver:
            messagebox.showwarning("Missing Email", "Please enter the customer's email.")
            return

        # Disable the Send button to prevent double-click
        send_btn.config(state=DISABLED, text="Sending...")
        popup.update()

        # Run the actual sending in a separate thread
        def background_send():
            try:
                # Save bill to temp file
                with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
                    f.write(bill_text)
                    temp_filename = f.name

                msg = MIMEMultipart()
                msg["From"] = SENDER
                msg["To"] = receiver
                msg["Subject"] = "Your Grocery Bill Receipt"
                body = "Dear Customer,\n\nPlease find your grocery bill attached.\n\nThank you for shopping with us."
                msg.attach(MIMEText(body, "plain"))

                with open(temp_filename, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename= receipt.txt')
                    msg.attach(part)

                os.unlink(temp_filename)

                # Send email
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(SENDER, PASSWORD)
                server.send_message(msg)
                server.quit()

                # Success – close popup and show message
                popup.after(0, lambda: popup.destroy())
                popup.after(0, lambda: messagebox.showinfo("Success", f"Email sent successfully to {receiver}"))

            except smtplib.SMTPAuthenticationError:
                popup.after(0, lambda: messagebox.showerror(
                    "Email Error",
                    "Gmail login failed.\n"
                    "Check your email and App Password.\n"
                    "If you don't have an App Password, enable 'Less secure app access' at:\n"
                    "https://myaccount.google.com/lesssecureapps\n"
                    "Or generate an App Password (requires 2‑Step Verification)."
                ))
            except Exception as e:
                popup.after(0, lambda: messagebox.showerror("Email Error", str(e)))
            finally:
                # Re-enable the button (if popup still exists)
                popup.after(0, lambda: send_btn.config(state=NORMAL, text="Send") if popup.winfo_exists() else None)

        # Start background thread
        threading.Thread(target=background_send, daemon=True).start()

    # ---------- UI buttons ----------
    send_btn = Button(btn_frame, text="Send", font=("Arial", 12), bg="#27ae60", fg="white",
                      padx=20, pady=5, command=send_email_action)
    send_btn.pack(side=LEFT, padx=10)

    Button(btn_frame, text="Cancel", font=("Arial", 12), bg="#e74c3c", fg="white",
           padx=20, pady=5, command=popup.destroy).pack(side=LEFT, padx=10)

#------------------E-mail button  function  end--------------------------------------------#



#-------------------print function button are start form here --------------------------------------------#


from fpdf import FPDF
import os
import threading
import platform
import subprocess


def print_receipt():
    # Get the bill text
    bill_text = textarea.get("1.0", END).strip()
    if not bill_text:
        messagebox.showwarning("No Bill", "Please generate the bill first.")
        return

    # Disable the print button
    printButton.config(state=DISABLED, text="Generating PDF...")
    root.update()

    def background_pdf():
        try:
            # Parse the bill text
            lines = bill_text.split('\n')

            # Extract shop name, bill no, customer, etc.
            shop_name = "Grocery Shop Billing System"
            bill_no = ""
            customer = ""
            phone = ""
            items = []
            grand_total = 0.0

            for line in lines:
                if "Bill No." in line:
                    bill_no = line.split(":")[1].strip()
                elif "Customer" in line:
                    customer = line.split(":")[1].strip()
                elif "Phone" in line:
                    phone = line.split(":")[1].strip()
                elif "Grand Total" in line:
                    # Extract the number after "Grand Total : "
                    gt_part = line.split(":")[1].strip()
                    grand_total = float(gt_part.split()[0])  # e.g., "123.45 Tk"
                elif "Product" in line or "=" in line or "-" in line:
                    continue
                else:
                    # Check if line has product, qty, price (tab-separated)
                    parts = line.split('\t')
                    if len(parts) == 3:
                        product = parts[0].strip()
                        qty = parts[1].strip()
                        price = parts[2].strip()
                        try:
                            qty_int = int(qty)
                            price_float = float(price)
                            items.append((product, qty_int, price_float))
                        except:
                            pass

            # Create PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, shop_name, ln=True, align='C')
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 10, "=" * 40, ln=True, align='C')
            pdf.cell(0, 10, f"Bill No: {bill_no}", ln=True)
            pdf.cell(0, 10, f"Customer: {customer}", ln=True)
            pdf.cell(0, 10, f"Phone: {phone}", ln=True)
            pdf.cell(0, 10, "-" * 40, ln=True)

            # Table header
            pdf.set_font("Arial", "B", 12)
            pdf.cell(80, 10, "Product", border=1)
            pdf.cell(30, 10, "Qty", border=1, align='C')
            pdf.cell(40, 10, "Price", border=1, align='R')
            pdf.ln()

            # Table rows
            pdf.set_font("Arial", "", 12)
            for product, qty, price in items:
                pdf.cell(80, 10, product, border=1)
                pdf.cell(30, 10, str(qty), border=1, align='C')
                pdf.cell(40, 10, f"{price:.2f}", border=1, align='R')
                pdf.ln()

            # Totals (cosmetic, grocery, drinks, tax, grand total)
            # Extract from bill_text lines containing totals
            total_lines = []
            for line in lines:
                if "Cosmetic Price" in line or "Grocery Price" in line or "Drinks Price" in line or "Cosmetic Tax" in line or "Grocery Tax" in line or "Drinks Tax" in line:
                    total_lines.append(line)
                elif "Grand Total" in line:
                    total_lines.append(line)

            pdf.cell(0, 10, "-" * 40, ln=True)
            for tl in total_lines:
                pdf.cell(0, 10, tl, ln=True)

            # Thank you message
            pdf.cell(0, 10, "=" * 40, ln=True)
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 10, "Thank You. Visit Again.", ln=True, align='C')

            # Save to Desktop
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            pdf_path = os.path.join(desktop, "Receipt.pdf")
            pdf.output(pdf_path)

            # Open the PDF with default viewer
            if platform.system() == "Windows":
                os.startfile(pdf_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", pdf_path])
            else:  # Linux
                subprocess.Popen(["xdg-open", pdf_path])

            # Show success
            root.after(0, lambda: messagebox.showinfo("PDF Generated", f"Receipt saved to:\n{pdf_path}"))

        except Exception as e:
            root.after(0, lambda: messagebox.showerror("PDF Error", str(e)))
        finally:
            root.after(0, lambda: printButton.config(state=NORMAL, text="Print"))

    # Start background thread
    threading.Thread(target=background_pdf, daemon=True).start()


#--------------------print function button are exit form here ---------------------------------------#

#----------------------clear function button are start here-----------------------------------------#
from tkinter import filedialog
def clear_all():
    # Clear customer details
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    # Clear all product quantity entries (set to "0")
    bathsoapEntry.delete(0, END)
    bathsoapEntry.insert(0, "0")
    facewashEntry.delete(0, END)
    facewashEntry.insert(0, "0")
    hairoilEntry.delete(0, END)
    hairoilEntry.insert(0, "0")
    lipstickEntry.delete(0, END)
    lipstickEntry.insert(0, "0")
    nailpolishEntry.delete(0, END)
    nailpolishEntry.insert(0, "0")
    shampooEntry.delete(0, END)
    shampooEntry.insert(0, "0")

    riceEntry.delete(0, END)
    riceEntry.insert(0, "0")
    sugarEntry.delete(0, END)
    sugarEntry.insert(0, "0")
    saltEntry.delete(0, END)
    saltEntry.insert(0, "0")
    noodlesEntry.delete(0, END)
    noodlesEntry.insert(0, "0")
    flourEntry.delete(0, END)
    flourEntry.insert(0, "0")
    coffeeEntry.delete(0, END)
    coffeeEntry.insert(0, "0")

    pepsiEntry.delete(0, END)
    pepsiEntry.insert(0, "0")
    spriteEntry.delete(0, END)
    spriteEntry.insert(0, "0")
    waterEntry.delete(0, END)
    waterEntry.insert(0, "0")
    fantaEntry.delete(0, END)
    fantaEntry.insert(0, "0")
    cocacolaEntry.delete(0, END)
    cocacolaEntry.insert(0, "0")
    energydrinksEntry.delete(0, END)
    energydrinksEntry.insert(0, "0")

    # Clear price and tax fields
    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)
    cosmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)

    # Clear receipt text area
    textarea.delete(1.0, END)




#----------------------clear function button are exit here------------------------------------------#





#----------------------search option find previous recipte start ---------------------------------------#
def search_receipt():
    # Open file dialog to select a .txt receipt
    file_path = filedialog.askopenfilename(
        title="Select Receipt File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Display in textarea
        textarea.delete(1.0, END)
        textarea.insert(END, content)

        # Try to extract bill number, customer name, phone from the content
        lines = content.split('\n')
        for line in lines:
            if "Bill No." in line:
                bill_no = line.split(":")[1].strip()
                billnumberEntry.delete(0, END)
                billnumberEntry.insert(0, bill_no)
            elif "Customer" in line:
                customer = line.split(":")[1].strip()
                nameEntry.delete(0, END)
                nameEntry.insert(0, customer)
            elif "Phone" in line:
                phone = line.split(":")[1].strip()
                phoneEntry.delete(0, END)
                phoneEntry.insert(0, phone)

        messagebox.showinfo("Search", "Receipt loaded successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file:\n{e}")

#-----------------------search option find previous recipte exit----------------------------------------#


#-----------------GRAPHICAL USER INTERFACE part----------------#



root=Tk()
root.title('Grocery Shop billing system')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headingLabel=Label(root,text='Grocery Shop Billing System',font=('times new roman',30,'bold')
                   ,bg='gray20',fg='gold',bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='gold'
                )
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)



phoneLabel=Label(customer_details_frame,text='Phone number',font=('times new roman',15,'bold'),bg='gray20',fg='gold'
                )
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)



billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='gold'                )
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)


# ---------------- Search Button ---------------- #
searchButton = Button(
    customer_details_frame,
    text="Search",
    font=("Arial", 12, "bold"),
    bg="#27ae60",
    fg="white",
    bd=7,
    width=10,
    cursor="hand2",
    padx=10,
    command=search_receipt
)
searchButton.grid(row=0, column=6, padx=15)


#-----------------------CUSTOMER DETAILS FRAME EXIT------------------#

#----------------PRODUCT FRAME START FROM HERE-------------------#
productsFrame=Frame(root)
productsFrame.pack()


# ---------------- Cosmetics Frame ---------------- #
cosmeticsFrame = LabelFrame(
    productsFrame,
    text="Cosmetics",
    font=("Times New Roman", 15, "bold"),
    bg="#34495e",
    fg="#f1c40f",
    bd=8,
    relief=GROOVE,
)
cosmeticsFrame.grid(row=0, column=0)

bathsoapLabel = Label(cosmeticsFrame, text="Bath Soap", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
bathsoapLabel.grid(row=0, column=0,pady=9)

bathsoapEntry = Entry(cosmeticsFrame, font=("Times New Roman", 15,'bold'),  width=10,bd=5)
bathsoapEntry.grid(row=0, column=1, pady=9)
bathsoapEntry.insert(0,"0")



facewashLabel = Label(cosmeticsFrame, text="Face wash", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
facewashLabel.grid(row=1, column=0, pady=9)
facewashEntry = Entry(cosmeticsFrame, font=("Times New Roman", 15),width=10,bd=5)
facewashEntry.grid(row=1, column=1, pady=9)
facewashEntry.insert(0,"0")

hairoilLabel = Label(cosmeticsFrame, text="Hair oil", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
hairoilLabel.grid(row=2, column=0, pady=9)
hairoilEntry = Entry(cosmeticsFrame, font=("Times New Roman", 15), width=10, bd=5)
hairoilEntry.grid(row=2, column=1, pady=9)
hairoilEntry.insert(0,"0")

lipsticklLabel = Label(cosmeticsFrame, text="Lipstick", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
lipsticklLabel.grid(row=3, column=0, pady=9)
lipstickEntry = Entry(cosmeticsFrame, font=("Times New Roman", 15), width=10, bd=5)
lipstickEntry.grid(row=3, column=1, pady=9,padx=10)
lipstickEntry.insert(0,"0")

nailpolishLabel = Label(cosmeticsFrame, text="Nail polish", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
nailpolishLabel.grid(row=4, column=0, pady=9, padx=10)
nailpolishEntry = Entry(cosmeticsFrame, font=("Times New Roman", 15), bd=5, width=10)
nailpolishEntry.grid(row=4, column=1, pady=9, padx=10)
nailpolishEntry.insert(0,"0")

shampooLabel = Label(cosmeticsFrame, text="Shampoo", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
shampooLabel.grid(row=5, column=0, pady=9, padx=10)
shampooEntry = Entry(cosmeticsFrame, font=("Times New Roman", 15), bd=5, width=10)
shampooEntry.grid(row=5, column=1, pady=9, padx=10)
shampooEntry.insert(0,"0")


# ---------------- Grocery Frame ---------------- #
groceryFrame = LabelFrame(
    productsFrame,
    text="Grocery",
    font=("Times New Roman", 15, "bold"),
    bg="#34495e",
    fg="#f1c40f",
    bd=8,
    relief=GROOVE,
)
groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text="Rice", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")
riceEntry = Entry(groceryFrame, font=("Times New Roman", 15,'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0,"0")

sugarLabel = Label(groceryFrame, text="Sugar", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
sugarLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")
sugarEntry = Entry(groceryFrame, font=("Times New Roman", 15), bd=5, width=10)
sugarEntry.grid(row=1, column=1, pady=9, padx=10)
sugarEntry.insert(0,"0")

saltLabel = Label(groceryFrame, text="Salt", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
saltLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")
saltEntry = Entry(groceryFrame, font=("Times New Roman", 15), bd=5, width=10)
saltEntry.grid(row=2, column=1, pady=9, padx=10)
saltEntry.insert(0,"0")

noodlesLabel = Label(groceryFrame, text="Noodles", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
noodlesLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")
noodlesEntry = Entry(groceryFrame, font=("Times New Roman", 15), bd=5, width=10)
noodlesEntry.grid(row=3, column=1, pady=9, padx=10)
noodlesEntry.insert(0,"0")

flourLabel = Label(groceryFrame, text="Flour", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
flourLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")
flourEntry = Entry(groceryFrame, font=("Times New Roman", 15), bd=5, width=10)
flourEntry.grid(row=4, column=1, pady=9, padx=10)
flourEntry.insert(0,"0")

coffeeLabel = Label(groceryFrame, text="Coffee", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
coffeeLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")
coffeeEntry = Entry(groceryFrame, font=("Times New Roman", 15), bd=5, width=10)
coffeeEntry.grid(row=5, column=1, pady=9, padx=10)
coffeeEntry.insert(0,"0")

# ---------------- Drinks Frame ---------------- #
drinksFrame = LabelFrame(
    productsFrame,
    text="Drinks",
    font=("Times New Roman", 16, "bold"),
    bg="#34495e",
    fg="#f1c40f",
    bd=8,
    relief=GROOVE,
)
drinksFrame.grid(row=0, column=2)

pepsiLabel = Label(drinksFrame, text="Pepsi", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
pepsiLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")
pepsiEntry = Entry(drinksFrame, font=("Times New Roman", 15), bd=5, width=10)
pepsiEntry.grid(row=0, column=1, pady=9, padx=10)
pepsiEntry.insert(0,"0")

spriteLabel = Label(drinksFrame, text="Sprite", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
spriteLabel.grid(row=1, column=0, pady=9, padx=10, sticky="w")
spriteEntry = Entry(drinksFrame, font=("Times New Roman", 15), bd=5, width=10)
spriteEntry.grid(row=1, column=1, pady=9, padx=10)
spriteEntry.insert(0,"0")

waterLabel = Label(drinksFrame, text="Water", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
waterLabel.grid(row=2, column=0, pady=9, padx=10, sticky="w")
waterEntry = Entry(drinksFrame, font=("Times New Roman", 15), bd=5, width=10)
waterEntry.grid(row=2, column=1, pady=9, padx=10)
waterEntry.insert(0,"0")

fantaLabel = Label(drinksFrame, text="Fanta", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
fantaLabel.grid(row=3, column=0, pady=9, padx=10, sticky="w")
fantaEntry = Entry(drinksFrame, font=("Times New Roman", 15), bd=5, width=10)
fantaEntry.grid(row=3, column=1, pady=9, padx=10)
fantaEntry.insert(0,"0")

cocacolaLabel = Label(drinksFrame, text="Coca Cola", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
cocacolaLabel.grid(row=4, column=0, pady=9, padx=10, sticky="w")
cocacolaEntry = Entry(drinksFrame, font=("Times New Roman", 15), bd=5, width=10)
cocacolaEntry.grid(row=4, column=1, pady=9, padx=10)
cocacolaEntry.insert(0,"0")


energydrinksLabel = Label(drinksFrame, text="Energy drinks", font=("Times New Roman", 15, "bold"), bg="#34495e", fg="white")
energydrinksLabel.grid(row=5, column=0, pady=9, padx=10, sticky="w")
energydrinksEntry = Entry(drinksFrame, font=("Times New Roman", 15), bd=5, width=10)
energydrinksEntry.grid(row=5, column=1, pady=9, padx=10)
energydrinksEntry.insert(0,"0")

#----------------PRODUCT FRAME EXIT FROM HERE----------------#

# ---------------- Bill Frame  ---------------- #
billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billareaLabel = Label(billframe, text="Receipt area", font=("Times New Roman", 15, "bold"),
                      bd=7,  relief="groove")
billareaLabel.pack(fill=X)




scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)



#-------------------bill menu frame start-----------------------#

# ---------------- Bill Menu Frame  ---------------- #
billmenuFrame = LabelFrame(root,
    text="Bill menu",
    font=("Times New Roman", 15, "bold"),
    bg="#34495e",
    fg="gold",
    bd=8,
    relief="groove",
)
billmenuFrame.pack(fill=X)

#-------------Cosmetic Price ----------#
cosmeticpriceLabel = Label(
    billmenuFrame,
    text="Cosmetic price",
    font=("Times New Roman", 14, "bold"),
    bg="#34495e",
    fg="white"
)
cosmeticpriceLabel.grid(row=0, column=0, pady=5, padx=10, sticky="w")

cosmeticpriceEntry = Entry(
    billmenuFrame,
    font=("Times New Roman", 14),
    bd=5,
    width=10
)
cosmeticpriceEntry.grid(row=0, column=1, pady=5, padx=10)


# --------- Grocery Price---------------#
grocerypriceLabel = Label(
    billmenuFrame,
    text="Grocery price",
    font=("Times New Roman", 14, "bold"),
    bg="#34495e",
    fg="white"
)
grocerypriceLabel.grid(row=1, column=0, pady=5, padx=10, sticky="w")

grocerypriceEntry = Entry(
    billmenuFrame,
    font=("Times New Roman", 14),
    bd=5,
    width=10
)
grocerypriceEntry.grid(row=1, column=1, pady=5, padx=10)



#------------------drinks menu frame-------------------#

drinkspriceLabel = Label(
    billmenuFrame,
    text="Drinks price",
    font=("Times New Roman", 14, "bold"),
    bg="#34495e",
    fg="white"
)
drinkspriceLabel.grid(row=2, column=0, pady=5, padx=10, sticky="w")

drinkspriceEntry = Entry(
    billmenuFrame,
    font=("Times New Roman", 14),
    bd=5,
    width=10
)
drinkspriceEntry.grid(row=2, column=1, pady=5, padx=10)



#-------------------bill menu frame exit---------------------#




#-------------------------TAX MENU FRAME START -------------------------#
# ---------- Cosmetic tax ----------#
cosmetictaxLabel = Label(
    billmenuFrame,
    text="Cosmetic tax",
    font=("Times New Roman", 14, "bold"),
    bg="#34495e",
    fg="white"
)
cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky="w")

cosmetictaxEntry = Entry(
    billmenuFrame,
    font=("Times New Roman", 14),
    bd=5,
    width=10
)
cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

# ---------- Grocery tax ----------
grocerytaxLabel = Label(
    billmenuFrame,   text="Grocery tax",
    font=("Times New Roman", 13, "bold"),
    bg="#34495e",
    fg="white"
)
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky="w")

grocerytaxEntry = Entry(
    billmenuFrame,                          font=("Times New Roman", 14),
    bd=5,
    width=10
)
grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

# ---------- Drinks tax ----------
drinkstaxLabel = Label(
    billmenuFrame,                         text="Drinks tax",
    font=("Times New Roman", 14, "bold"),
    bg="#34495e",
    fg="white"
)
drinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky="w")

drinkstaxEntry = Entry(
   billmenuFrame,                         font=("Times New Roman", 14),
    bd=5,
    width=10
)
drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)


#-------------------------TAX MENU FRAME EXIT---------------------------#


#-----------------------button area start ------------#


buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4,rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10,
                     command=total, cursor="hand2")
totalButton.grid(row=0, column=0, pady=20,padx=4)

billButton = Button(
    buttonFrame,
    text='Bill',
    font=('arial', 16, 'bold'),
    bg='gray20',
    fg='white',
    bd=5,
    width=8,
    pady=10,command=bill,

    cursor="hand2"
)
billButton.grid(row=0, column=1, pady=20,padx=4)

# ---------- Fixed email button ----------
emailButton = Button(buttonFrame, text='E-mail', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10,
                     cursor="hand2", command=send_email)
emailButton.grid(row=0, column=2, pady=20,padx=4)
# ----------------------------------------

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10,
                     cursor="hand2", command=print_receipt)
printButton.grid(row=0, column=3, pady=20,padx=4)


clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'),
                     bg='gray20', fg='white', bd=5, width=8, pady=10,
                     cursor="hand2", command=clear_all)
clearButton.grid(row=0, column=4, pady=20,padx=4)




#-----------------------button area exit--------------#




root.mainloop()
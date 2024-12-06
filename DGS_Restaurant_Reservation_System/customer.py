from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk

class Cust_Win:
     def __init__(self,root):
        self.root=root
        self.root.title("DGS_Restaurant Reservation System")
        self.root.geometry("1300x550+240+250")



       # ==============Title==============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


       # ===============Logo===============
        img2=Image.open(r"C:\Users\Client 04\DGS_Restaurant_Reservation_System\All Image\DGS.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

       # ==============labelFrame==============
        labelframeleft=LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Deatils", font=("times new roman", 12, "bold"),padx=2,)
        labelframeleft.place(x=5,y=50, width=425,height=490)

       # ==============labels and entrys==============
       # custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("Arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=8,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=29,font=("Arial",13,"bold"))
        enty_ref.grid(row=0,column=1)

       # cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6) 
        cname.grid(row=1,column=0, sticky=W)
        txtcname=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1, column=1)

       # mother name
        lblmname=Label(labelframeleft,font=("arial",12,"bold"), text="Mother Name:", padx=2,pady=6)
        lblmname.grid(row=2,column=0, sticky=W)
        txtmname=ttk.Entry(labelframeleft,font=("arial",13, "bold"),width=29)
        txtmname.grid(row=2,column=1)

       # gender combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6) 
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27) 
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.grid(row=3,column=1)

       # postcode
        lblPostCode=Label(labelframeleft,font=("arial", 12,"bold"),text="PostCode:",padx=2,pady=6) 
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

       # mobilenumber
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6) 
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

       # email
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6) 
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

       # nationality
        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6) 
        lblNationality.grid(row=7,column=0,sticky=W)

       # idproof type combobox
        lblIdProof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8, column=0,sticky=W)

       # id number
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

       # address
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10, column=1)


if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
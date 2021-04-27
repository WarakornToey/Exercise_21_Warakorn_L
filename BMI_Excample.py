from tkinter import *   #Import Libray tkinter
import math

def Left_Click(event): # สร้างฟังชันก์แบบมีเหตุการณ์ event
    bmi_result = round(float(textbox_weight.get())/math.pow(float(textbox_hight.get())/100,2)) #round ปัดจำนวนจุดทศนิยมเป็นจำนวนเต็ม
     # สูตรคำนวณ BMI , Math.pow ยกกำลังสอง .get นำข้อมูลมาจาก textbox นั้นมาใช้งาน
 
    if bmi_result < 18.5 :
        bmi_detail = "ผอมเกินไป"
    elif bmi_result >= 18.5 and bmi_result < 23 :
        bmi_detail = "นำหนักปกติ เหมาะสม"
    elif bmi_result >= 23 and bmi_result < 25 :
        bmi_detail = "น้ำหนักเกิน"
    elif bmi_result >= 25 and bmi_result < 30 :
        bmi_detail = "อ้วน"
    elif bmi_result >= 30 :
        bmi_detail = "อ้วนมาก"
  
    label_result.configure(text = "ค่า BMI ของคุณคือ : " + str(bmi_result) + " ผลการประเมินคือ : " + bmi_detail) # แสดงผลลัพธ์ .configure ใช้เเสดงผล

windows_1 = Tk() #หน้าต่างแสดงผล TK() คือตัวหลักในการจัดการ GUI

label_hight = Label(windows_1,text="ส่วนสูง cm.")
label_hight.grid(row=0,column=0) #label ข้อความ
textbox_hight = Entry(windows_1)  # Entry ใช้สำหรับ textbox พื้นที่ว่างใส่ข้อความ
textbox_hight.grid(row=0,column=1) 

label_weight = Label(windows_1,text="น้ำหนัก Kg.")
label_weight.grid(row=1,column=0)
textbox_weight = Entry(windows_1)  # Entry ใช้สำหรับ textbox พื้นที่ว่างใส่ข้อความ
textbox_weight.grid(row=1,column=1)

calculate_button = Button(windows_1,text="คำนวณ") # สร้างปุ่มคำนวณ
calculate_button.bind('<Button-1>',Left_Click)
calculate_button.grid(row=2,column=0) 

label_result = Label(windows_1,text ="ผลลัพธ์")
label_result.grid(row=2,column=1)

windows_1.mainloop()

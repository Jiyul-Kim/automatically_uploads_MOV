from tkinter import * 
from tkinter import messagebox 
from tkinter import filedialog
import tkinter.ttk as ttk
import os.path
from os import path
import shutil


root = Tk()
root.title("MOV_move_EP_folder")
# root.geometry("640x400")
# root.resizable(False, False)

def close():
    root.quit()
    root.destroy()



# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="선택하세요.")
    filetypes = (("txt 파일", "*.txt"), ("MOV 파일", "*.mov"), ("PNG 파일", "*.png"), ("모든 파일", "*.*"))
    
    global file
    # 파일들을 리스트로 저장
    file = list(files)
    for f in file:
        list_file.insert(END, f)
        
        
top_frame = Frame(root)
top_frame.pack(fill="both")

list_frame = Frame(top_frame)
list_frame.pack(fill="both")

label1 = Label(list_frame, text="파일 선택 목록", font=("Helvetica", 10, "bold"))
label1.pack(side="top", fill="x")



scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill= "y")

list_file = Listbox(list_frame, selectmode=EXTENDED, yscrollcommand = scrollbar.set, width=0)
list_file.pack(fill = "x")
scrollbar.config(command=list_file.yview)






label2 = Label(root, text="에피소드 선택", padx=10, pady=5, font=("Helvetica", 10, "bold"))
label2.pack (fill="x")



# ep 콤보 박스
cmb_ep_list = []

# ep 네임 str으로 표현 > 리스트 화
ep_name = '5'
for num in range(1,29):
    if num <= 9:
        num = '0' + str(num)
    eps = ep_name + str(num)
    cmb_ep_list.append(str(eps))

values = cmb_ep_list
combobox  = ttk.Combobox(root, values=values, state="readonly", height=20, width=70)
combobox.pack(fill="both" , side="left")

# dest = 'D:\p38_MiniForce\RENDER\season05\ep{}'.format(values)
# print(dest)

def send_btn_cmd():
    dest = 'D:\p38_MiniForce\RENDER\season05\ep'+ combobox.get()
    print(dest)
    
    if path.exists(dest) == False:
        messagebox.showerror("에러", "폴더가 없습니다.")
     
    else:
        # 선택된 모든 파일들을 이동
        for src in file:
            shutil.move(src, dest)
        list_file.delete(0, END)

add_btn = Button(top_frame, text="add", height=2,command=add_file, padx=10, pady=5)
add_btn.pack( side="bottom", fill="x")

# send 버튼
send_btn = Button(root, text="send", command=send_btn_cmd, padx=10, pady=10)
send_btn.pack(fill="x", side="right")

def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# fileDrop 리스트 삭제 버튼
del_btn = Button(root, text="Del", command=del_file, padx=10, pady=10)
del_btn.pack(fill="x", side="left")


root.mainloop()
import tkinter
import tkinter.messagebox
import os
import shutil
import sys
from itertools import cycle
#加密
def crypt(source):
    result=''
    for ch in source:
        result=result+chr(ord(ch)^ord(next(cycle('$r@3'))))
    return result
#类，功能
class PeopleCount():
    def __init__(self,account,password):
        self.account=account
        self.password=password
    def reduction(self):
        shutil.rmtree('./user')
        os.mkdir('user')
        os.remove("account.txt")
        a=open("account.txt","a",encoding = 'utf-8')
        a.write("false")
        a.close()
    def inputInformation(self,ID,name,school_ID,c_score,m_score,e_score,s_score):
        usr=open("./user/"+self.account+"StudentInformation.txt","a",encoding = 'utf-8')
        usr.close()
        usr=self.returnInformation()
        repeat=False
        for i in usr:
            if(i[0]==str(ID)):
                repeat=True
        if repeat==False:
            usr=open("./user/"+self.account+"StudentInformation.txt","a",encoding = 'utf-8')
            usr.write(crypt(str(ID))+"_-_"+crypt(str(name))+"_-_"+crypt(str(school_ID))+"_-_"+crypt(str(c_score))+"_-_"+crypt(str(m_score))+"_-_"+crypt(str(e_score))+"_-_"+crypt(str(s_score))+"_-_"+"\n")
            usr.close()
            return "success"
        else:
            return "error:repeat"
    def returnInformation(self,ID=None,name=None,school_ID=None):
        if ID==None and name==None and school_ID==None:
            ans=[]
            usr=open("./user/"+self.account+"StudentInformation.txt","r",encoding = 'utf-8')
            content=usr.readlines()
            for i in content:
                b=i.split("_-_")
                b.pop(len(b)-1)
                for i in range(len(b)):
                    b[i]=crypt(b[i])
                ans.append(b)
            usr.close()
            return ans
        else:
            if ID!=None and name==None and school_ID==None:
                way=0
                IFM=ID
            elif ID==None and name!=None and school_ID==None:
                way=1
                IFM=name
            elif ID==None and name==None and school_ID!=None:
                way=2
                IFM=school_ID
            usrList=self.returnInformation()
            find=False
            for i in usrList:
                if i[way]==IFM:
                    find=True
                    return i
            if find==False:
                return "error:not find"
    def sort(self,method):
        try:
            method=int(method)
        except:
            return "error"
        else:
            if method>6 or method<1:
                return "error"
        method+=1
        usrList=self.returnInformation()
        if len(usrList)==0:
            return "error:not find student"
        elif len(usrList)==1:
            usrList[0].append(1)
            return usrList
        else:
            index=[]
            ans=[]
            for i in range(len(usrList)):
                index.append(i)
            if method==7:
                for i in range(len(usrList)):
                    for j in range(0,len(usrList)-i-1):
                        first=float(usrList[index[j]][3])+float(usrList[index[j]][4])+float(usrList[index[j]][5])+float(usrList[index[j]][6])
                        second=float(usrList[index[j+1]][3])+float(usrList[index[j+1]][4])+float(usrList[index[j+1]][5])+float(usrList[index[j+1]][6])
                        if first<second:
                            index[j], index[j+1] = index[j+1], index[j]
            elif method==2:
                for i in range(len(usrList)):
                    for j in range(0, len(usrList)-i-1):
                        if float(usrList[index[j]][method])>float(usrList[index[j+1]][method]):
                            index[j], index[j+1] = index[j+1], index[j]
            elif method<7:
                for i in range(len(usrList)):
                    for j in range(0, len(usrList)-i-1):
                        if float(usrList[index[j]][method])<float(usrList[index[j+1]][method]):
                            index[j], index[j+1] = index[j+1], index[j]
            for i in range(len(index)):
                usrList[index[i]].append(i+1)
                ans.append(usrList[index[i]])
            return ans
    def modifyInformation(self,modify,way,kind,new):
        IFM=self.returnInformation()
        IDX=-1
        for i in range(len(IFM)):
            if modify==1:
                if IFM[i][0]==way:
                    IDX=i
                    break
            elif modify==2:
                if IFM[i][1]==way:
                    IDX=i
                    break
            elif modify==3:
                if IFM[i][2]==way:
                    IDX=i
                    break
        if IDX==-1:
            return "error:not find"
        else:
            IFM[IDX][kind]=new
        os.remove("./user/"+self.account+"StudentInformation.txt")
        for i in IFM:
            self.inputInformation(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
        return "success"

def first_face_GUI():
    global login_interface
    login_interface=tkinter.Tk()
    login_interface.title("登录")
    login_interface.geometry("650x650")
    login_interface.wm_attributes('-topmost',1)
    logina=tkinter.Button(login_interface,width = 12,height = 1, text ="登录", font=("微软雅黑", "50"),command = login)
    reductiona=tkinter.Button(login_interface,width = 21,height = 3, text ="""清除所有账户
(此操作会初始化设置
用户文件将不被保留)""", font=("微软雅黑", "30"),command = reduction_GUI)
    add_c=tkinter.Button(login_interface,width = 12,height = 1, text ="添加账户", font=("微软雅黑", "50"),command = add_account_GUI_f)
    logina.place(x=75, y=20)
    add_c.place(x=75, y=200)
    reductiona.place(x=65, y=400)
    login_interface.mainloop()
def exit_GUI():
    global function_face
    function_face.destroy()
    sys.exit(0)
def asig():
    global ID_E
    global s_ID_E
    global sname_E
    global c_s_E
    global m_s_E
    global e_s_E
    global s_s_E
    global add_stuifm
    global user
    ID=ID_E.get()
    name=sname_E.get()
    s_ID=s_ID_E.get()
    c_s=c_s_E.get()
    m_s=m_s_E.get()
    e_s=e_s_E.get()
    s_s=s_s_E.get()
    a=user.inputInformation(ID,name,s_ID,c_s,m_s,e_s,s_s)
    if a=="success":
        tkinter.messagebox.showinfo("提示","录入成功")
        add_stuifm.destroy()
        function_GUI()
    else:
        tkinter.messagebox.showerror("错误","学生已存在")
def as_cancel():
    global add_stuifm
    add_stuifm.destroy()
    function_GUI()
def add_stu_ifm_GUI():
    global function_face
    global ID_E
    global s_ID_E
    global sname_E
    global c_s_E
    global m_s_E
    global e_s_E
    global s_s_E
    global add_stuifm
    function_face.destroy()
    add_stuifm=tkinter.Tk()
    add_stuifm.title("录入学生信息")
    add_stuifm.geometry("650x670")
    add_stuifm.wm_attributes('-topmost',1)
    name=tkinter.Label(add_stuifm, text="录入学生信息",font=("黑体", "40"))
    name.place(x=150, y=20)
    ID=tkinter.Label(add_stuifm, text="身份证号",font=("微软雅黑", "30"))
    ID.place(x=0, y=90)
    ID_1=tkinter.Label(add_stuifm, text="录入结束后无法修改",font=("微软雅黑", "10"),fg="#FF0000")
    ID_1.place(x=20, y=140)
    ID_E= tkinter.Entry(add_stuifm,width=20,font=("微软雅黑", "30"))
    ID_E.place(x=165, y=100)
    sname=tkinter.Label(add_stuifm, text="姓名",font=("微软雅黑", "30"))
    sname.place(x=30, y=165)
    sname_E= tkinter.Entry(add_stuifm,width=20,font=("微软雅黑", "30"))
    sname_E.place(x=165, y=170)
    s_ID=tkinter.Label(add_stuifm, text="学号",font=("微软雅黑", "30"))
    s_ID.place(x=30, y=240)
    s_ID_E= tkinter.Entry(add_stuifm,width=20,font=("微软雅黑", "30"))
    s_ID_E.place(x=165, y=240)
    c_s=tkinter.Label(add_stuifm, text="语文分数",font=("微软雅黑", "30"))
    c_s.place(x=0, y=305)
    c_s_E= tkinter.Entry(add_stuifm,width=20,font=("微软雅黑", "30"))
    c_s_E.place(x=165, y=310)
    m_s=tkinter.Label(add_stuifm, text="数学分数",font=("微软雅黑", "30"))
    m_s.place(x=0, y=375)
    m_s_E= tkinter.Entry(add_stuifm,width=20,font=("微软雅黑", "30"))
    m_s_E.place(x=165, y=380)
    e_s=tkinter.Label(add_stuifm, text="英语分数",font=("微软雅黑", "30"))
    e_s.place(x=0, y=445)
    e_s_E= tkinter.Entry(add_stuifm,width=20,font=("微软雅黑", "30"))
    e_s_E.place(x=165, y=450)
    s_s=tkinter.Label(add_stuifm, text="科学分数",font=("微软雅黑", "30"))
    s_s.place(x=0, y=515)
    s_s_E= tkinter.Entry(add_stuifm,width=20,font=("微软雅黑", "30"))
    s_s_E.place(x=165, y=520)
    confirm=tkinter.Button(add_stuifm,text ="确认",width=5,height=1,font=("微软雅黑", "20"),command=asig)
    confirm.place(x=530, y=580)
    Cancel=tkinter.Button(add_stuifm,text ="取消",width=4,height=1,font=("微软雅黑", "20"),command =as_cancel)
    Cancel.place(x=450,y=580)
def rfsifm():#read full student information
    global user
    global read_stuifm
    read_stuifm.wm_attributes('-topmost',0)
    a=user.returnInformation()
    faceList=[]
    for i in range(len(a)):
        faceList.append("")
    for i in range(len(a)):
        faceList[i]=tkinter.Tk()
        faceList[i].title(a[i][1])
        faceList[i].geometry("650x600")
        name=tkinter.Label(faceList[i], text=a[i][1],font=("黑体", "40"))
        name.place(x=200, y=20)
        ID=tkinter.Label(faceList[i], text="身份证号: "+a[i][0],font=("微软雅黑", "30"))
        ID.place(x=30, y=90)
        sname=tkinter.Label(faceList[i], text="姓名: "+a[i][1],font=("微软雅黑", "30"))
        sname.place(x=30, y=165)
        s_ID=tkinter.Label(faceList[i], text="学号: "+a[i][2],font=("微软雅黑", "30"))
        s_ID.place(x=30, y=240)
        c_s=tkinter.Label(faceList[i], text="语文分数: "+a[i][3],font=("微软雅黑", "30"))
        c_s.place(x=30, y=305)
        m_s=tkinter.Label(faceList[i], text="数学分数: "+a[i][4],font=("微软雅黑", "30"))
        m_s.place(x=30, y=375)
        e_s=tkinter.Label(faceList[i], text="英语分数: "+a[i][5],font=("微软雅黑", "30"))
        e_s.place(x=30, y=445)
        s_s=tkinter.Label(faceList[i], text="科学分数: "+a[i][6],font=("微软雅黑", "30"))
        s_s.place(x=30, y=515)
def Return():
    global Rasifm
    Rasifm.destroy()
    read_stu_ifm_GUI()
    return
def rasifm_s():
    global Rasifm
    global user
    global keyword
    Rasifm.wm_attributes('-topmost',0)
    key=[int(vn.get()),int(vs.get()),int(vi.get())]
    ifm=keyword.get()
    if (key[0]==1 and key[1]==1)or(key[0]==1 and key[2]==1)or(key[1]==1 and key[2]==1)or(key[0]==1 and key[1]==1 and key[2]==1):
        tkinter.messagebox.showerror("错误","请勿勾选两个及以上的查找方式")
        return
    if key[0]==1:
        IFM=user.returnInformation(name=ifm)
    elif key[1]==1:
        IFM=user.returnInformation(school_ID=ifm)
    elif key[2]==1:
        IFM=user.returnInformation(ID=ifm)
    else:
        tkinter.messagebox.showerror("错误","请勾选查找方式")
        return
    if IFM=="error:not find":
        tkinter.messagebox.showerror("错误","没有找到学生")
    else:
        stu=tkinter.Tk()
        stu.title(IFM[1])
        stu.geometry("650x600")
        name=tkinter.Label(stu, text=IFM[1],font=("黑体", "40"))
        name.place(x=200, y=20)
        ID=tkinter.Label(stu, text="身份证号: "+IFM[0],font=("微软雅黑", "30"))
        ID.place(x=30, y=90)
        sname=tkinter.Label(stu, text="姓名: "+IFM[1],font=("微软雅黑", "30"))
        sname.place(x=30, y=165)
        s_ID=tkinter.Label(stu, text="学号: "+IFM[2],font=("微软雅黑", "30"))
        s_ID.place(x=30, y=240)
        c_s=tkinter.Label(stu, text="语文分数: "+IFM[3],font=("微软雅黑", "30"))
        c_s.place(x=30, y=305)
        m_s=tkinter.Label(stu, text="数学分数: "+IFM[4],font=("微软雅黑", "30"))
        m_s.place(x=30, y=375)
        e_s=tkinter.Label(stu, text="英语分数: "+IFM[5],font=("微软雅黑", "30"))
        e_s.place(x=30, y=445)
        s_s=tkinter.Label(stu, text="科学分数: "+IFM[6],font=("微软雅黑", "30"))
        s_s.place(x=30, y=515)
def rasifm():#read appoint student infoemation
    global read_stuif
    global Rasifm
    global keyword
    global vn
    global vs
    global vi
    read_stuifm.destroy()
    Rasifm=tkinter.Tk()
    Rasifm.title("读取指定学生信息")
    Rasifm.geometry("600x550")
    Rasifm.wm_attributes('-topmost',1)
    name=tkinter.Label(Rasifm,text="读取指定学生信息",font=("黑体", "40"))
    name.place(x=80, y=50)
    uname=tkinter.Label(Rasifm, text="信息",font=("微软雅黑", "30"))
    uname.place(x=10, y=195)
    keyword= tkinter.Entry(Rasifm,width=20,font=("微软雅黑", "30"))
    keyword.place(x=100, y=200)
    pname=tkinter.Label(Rasifm, text="""请选择查询方法(只能勾选一种)
             请将姓名(学号或身份证号)填在上方信息输入框内""",font=("微软雅黑", "15"),fg="#FF0000")
    pname.place(x=5, y=285)
    vn = tkinter.StringVar(value="0")
    vs = tkinter.StringVar(value="0")
    vi = tkinter.StringVar(value="0")
    cname= tkinter.Checkbutton(Rasifm,text="按姓名查询",font=("微软雅黑", "20"),variable=vn)
    csID = tkinter.Checkbutton(Rasifm,text="按学号查询",font=("微软雅黑", "20"),variable=vs)
    cID = tkinter.Checkbutton(Rasifm,text="按身份证号查询",font=("微软雅黑", "20"),variable=vi)
    cname.place(x=50, y=365)
    csID.place(x=50, y=430)
    cID.place(x=50, y=490)
    confirm=tkinter.Button(Rasifm,text ="""继续""",width=4,height=1,font=("微软雅黑", "20"),command=rasifm_s)
    confirm.place(x=480, y=370)
    Cancel=tkinter.Button(Rasifm,text ="返回",width=4,height=1,font=("微软雅黑", "20"),command=Return)
    Cancel.place(x=480,y=450)
def read_stu_ifm_GUI():
    global function_face
    global read_stuifm
    try:
        function_face.destroy()
    except:
        pass
    read_stuifm=tkinter.Tk()
    read_stuifm.title("读取学生信息")
    read_stuifm.geometry("650x360")
    read_stuifm.wm_attributes('-topmost',1)
    name=tkinter.Label(read_stuifm, text="读取学生信息",font=("黑体", "40"))
    name.place(x=165, y=20)
    read_stu_f=tkinter.Button(read_stuifm,text ="""查看所有
学生信息""",width=9,height=2,font=("微软雅黑", "40"),command=rfsifm)
    read_stu_f.place(x=20, y=100)
    read_stu_o=tkinter.Button(read_stuifm,text ="""查看指定
学生信息""",width=9,height=2,font=("微软雅黑", "40"),command=rasifm)
    read_stu_o.place(x=335, y=100)
    Back=tkinter.Button(read_stuifm,text ="返回",width=4,height=1,font=("微软雅黑", "20"),command=back)
    Back.place(x=555,y=290)
def back():
    global read_stuifm
    read_stuifm.destroy()
    function_GUI()
def Return_cif():
    global Casifm
    Casifm.destroy()
    function_GUI()
    return
def Return_cis():
    global change
    change.destroy()
    change_ifm_f()
    return
def change_ifm_t():
    global find
    global ifm
    global user
    global keyword
    global vname
    global vsID
    global vc_c
    global vc_m
    global vc_e
    global vc_s
    global key_a
    key1=[int(vname.get()),int(vsID.get()),int(vc_c.get()),int(vc_m.get()),int(vc_e.get()),int(vc_s.get())]
    a=False
    for i in key1:
        if i==1:
            a=True
            break
    if a==False:
        tkinter.messagebox.showerror("错误","请勾选查找方式")
        return
    for i in range(len(key1)):
        for j in range(i+1,len(key1)):
            if key1[i]==1 and key1[j]==1:
                tkinter.messagebox.showerror("错误","请勿勾选一个以上的查找方式")
                return
    new_ifm=keyword.get()
    for i in range(len(key1)):
        if key1[i]==1:
            kind=i+1
            break
    user.modifyInformation(key_a,ifm,kind,new_ifm)
    tkinter.messagebox.showinfo("提示","修改成功")
    Return_cis()
    return
def change_ifm_s():
    global key_a
    global ifm
    global find
    global IFM
    global change
    global Casifm
    global user
    global keyword
    global vname
    global vsID
    global vc_c
    global vc_m
    global vc_e
    global vc_s
    key=[int(vn.get()),int(vs.get()),int(vi.get())]
    ifm=keyword.get()
    if (key[0]==1 and key[1]==1)or(key[0]==1 and key[2]==1)or(key[1]==1 and key[2]==1):
        tkinter.messagebox.showerror("错误","请勿勾选一个以上的查找方式")
        return
    find="False"
    if key[0]==1:
        key_a=2
        IFM=user.returnInformation()
        for i in range(len(IFM)):
            if IFM[i][1]==ifm:
                find=i
    elif key[1]==1:
        key_a=3
        IFM=user.returnInformation()
        for i in range(len(IFM)):
            if IFM[i][2]==ifm:
                find=i
    elif key[2]==1:
        key_a=1
        IFM=user.returnInformation()
        for i in range(len(IFM)):
            if IFM[i][0]==ifm:
                find=i
    else:
        tkinter.messagebox.showerror("错误","请勾选查找方式")
        return
    if find=="False":
        tkinter.messagebox.showerror("错误","没有找到学生")
    else:
        Casifm.destroy()
        change=tkinter.Tk()
        change.title("修改信息")
        change.geometry("620x500")
        name=tkinter.Label(change, text="修改信息",font=("黑体", "40"))
        name.place(x=200, y=20)
        uname=tkinter.Label(change, text="新信息",font=("微软雅黑", "30"))
        uname.place(x=5, y=145)
        keyword= tkinter.Entry(change,width=20,font=("微软雅黑", "30"))
        keyword.place(x=130, y=150)
        pname=tkinter.Label(change, text="""    请选择要修改的信息种类(只能勾选一种)
请将新信息填在上方新信息输入框内""",font=("微软雅黑", "15"),fg="#FF0000")
        pname.place(x=5, y=215)
        vname = tkinter.StringVar(value="0")
        vsID = tkinter.StringVar(value="0")
        vc_c = tkinter.StringVar(value="0")
        vc_m = tkinter.StringVar(value="0")
        vc_e = tkinter.StringVar(value="0")
        vc_s = tkinter.StringVar(value="0")
        cname= tkinter.Checkbutton(change,text="修改姓名",font=("微软雅黑", "20"),variable=vname)
        cname.place(x=50, y=275)
        csID = tkinter.Checkbutton(change,text="修改学号",font=("微软雅黑", "20"),variable=vsID)
        csID.place(x=350, y=275)
        c_c = tkinter.Checkbutton(change,text="修改语文成绩",font=("微软雅黑", "20"),variable=vc_c)
        c_c.place(x=50, y=325)
        c_m = tkinter.Checkbutton(change,text="修改数学成绩",font=("微软雅黑", "20"),variable=vc_m)
        c_m.place(x=350, y=325)
        c_e = tkinter.Checkbutton(change,text="修改英语成绩",font=("微软雅黑", "20"),variable=vc_e)
        c_e.place(x=50, y=375)
        c_s = tkinter.Checkbutton(change,text="修改科学成绩",font=("微软雅黑", "20"),variable=vc_s)
        c_s.place(x=350, y=375)
        confirm=tkinter.Button(change,text ="继续",width=4,height=1,font=("微软雅黑", "20"),command=change_ifm_t)
        confirm.place(x=500, y=420)
        Cancel=tkinter.Button(change,text ="取消",width=4,height=1,font=("微软雅黑", "20"),command=Return_cis)
        Cancel.place(x=400,y=420)
def change_ifm_f():
    global function_face
    global Casifm
    global keyword
    global vn
    global vs
    global vi
    try:
        function_face.destroy()
    except:
        pass
    Casifm=tkinter.Tk()
    Casifm.title("修改指定学生信息")
    Casifm.geometry("600x550")
    Casifm.wm_attributes('-topmost',1)
    name=tkinter.Label(Casifm,text="修改指定学生信息",font=("黑体", "40"))
    name.place(x=80, y=50)
    uname=tkinter.Label(Casifm, text="信息",font=("微软雅黑", "30"))
    uname.place(x=10, y=195)
    keyword= tkinter.Entry(Casifm,width=20,font=("微软雅黑", "30"))
    keyword.place(x=100, y=200)
    pname=tkinter.Label(Casifm, text="""请选择查询并修改方法(只能勾选一种)
             请将姓名(学号或身份证号)填在上方信息输入框内""",font=("微软雅黑", "15"),fg="#FF0000")
    pname.place(x=5, y=285)
    vn = tkinter.StringVar(value="0")
    vs = tkinter.StringVar(value="0")
    vi = tkinter.StringVar(value="0")
    cname= tkinter.Checkbutton(Casifm,text="按姓名查询并修改",font=("微软雅黑", "20"),variable=vn)
    csID = tkinter.Checkbutton(Casifm,text="按学号查询并修改",font=("微软雅黑", "20"),variable=vs)
    cID = tkinter.Checkbutton(Casifm,text="按身份证号查询并修改",font=("微软雅黑", "20"),variable=vi)
    cname.place(x=50, y=365)
    csID.place(x=50, y=430)
    cID.place(x=50, y=490)
    confirm=tkinter.Button(Casifm,text ="""继续""",width=4,height=1,font=("微软雅黑", "20"),command=change_ifm_s)
    confirm.place(x=480, y=370)
    Cancel=tkinter.Button(Casifm,text ="取消",width=4,height=1,font=("微软雅黑", "20"),command=Return_cif)
    Cancel.place(x=480,y=450)
def sort_return():
    global sort_face
    sort_face.destroy()
    function_GUI()
    return
def sort_1():
    s_sort_s(1)
def sort_2():
    s_sort_s(2)
def sort_3():
    s_sort_s(3)
def sort_4():
    s_sort_s(4)
def sort_5():
    s_sort_s(5)
def sort_6():
    s_sort_s(6)
def s_sort_s(b):
    a=user.sort(b)
    if a=="error:not find student":
        tkinter.messagebox.showerror("错误","没有学生，请先录入")
    else:
        sort_face.wm_attributes('-topmost',0)
        faceList=[]
        for i in range(len(a)):
            faceList.append("")
        for i in range(len(a)):
            faceList[i]=tkinter.Tk()
            faceList[i].title(a[i][1])
            faceList[i].geometry("650x650")
            name=tkinter.Label(faceList[i], text=a[i][1],font=("黑体", "40"))
            name.place(x=200, y=20)
            ID=tkinter.Label(faceList[i], text="身份证号: "+a[i][0],font=("微软雅黑", "30"))
            ID.place(x=30, y=90)
            sname=tkinter.Label(faceList[i], text="姓名: "+a[i][1],font=("微软雅黑", "30"))
            sname.place(x=30, y=165)
            s_ID=tkinter.Label(faceList[i], text="学号: "+a[i][2],font=("微软雅黑", "30"))
            s_ID.place(x=30, y=240)
            c_s=tkinter.Label(faceList[i], text="语文分数: "+a[i][3],font=("微软雅黑", "30"))
            c_s.place(x=30, y=305)
            m_s=tkinter.Label(faceList[i], text="数学分数: "+a[i][4],font=("微软雅黑", "30"))
            m_s.place(x=30, y=375)
            e_s=tkinter.Label(faceList[i], text="英语分数: "+a[i][5],font=("微软雅黑", "30"))
            e_s.place(x=30, y=445)
            s_s=tkinter.Label(faceList[i], text="科学分数: "+a[i][6],font=("微软雅黑", "30"))
            s_s.place(x=30, y=515)
            s=tkinter.Label(faceList[i], text="排名: "+str(a[i][7]),font=("微软雅黑", "30"))
            s.place(x=30, y=585)
def s_sort():
    global function_face
    global sort_face
    function_face.destroy()
    sort_face=tkinter.Tk()
    sort_face.title("成绩排名")
    sort_face.geometry("650x800")
    sort_face.wm_attributes('-topmost',1)
    name=tkinter.Label(sort_face, text="成绩排名",font=("黑体", "40"))
    name.place(x=210, y=20)
    sID_s=tkinter.Button(sort_face,text ="""按学号
排名""",width=9,height=2,font=("微软雅黑", "40"),command=sort_1)
    sID_s.place(x=20, y=100)
    c_s_s=tkinter.Button(sort_face,text ="""按语文
成绩排名""",width=9,height=2,font=("微软雅黑", "40"),command=sort_2)
    c_s_s.place(x=335, y=100)
    m_s_s=tkinter.Button(sort_face,text ="""按数学
成绩排名""",width=9,height=2,font=("微软雅黑", "40"),command=sort_3)
    m_s_s.place(x=20, y=300)
    e_s_s=tkinter.Button(sort_face,text ="""按英语
成绩排名""",width=9,height=2,font=("微软雅黑", "40"),command=sort_4)
    e_s_s.place(x=335, y=300)
    s_s_s=tkinter.Button(sort_face,text ="""按科学
成绩排名""",width=9,height=2,font=("微软雅黑", "40"),command=sort_5)
    s_s_s.place(x=20, y=500)
    f_s_s=tkinter.Button(sort_face,text ="""按总分
排名""",width=9,height=2,font=("微软雅黑", "40"),command=sort_6)
    f_s_s.place(x=335, y=500)
    Exit=tkinter.Button(sort_face,text ="返回",width=5,height=1,font=("微软雅黑", "30"),command=sort_return)
    Exit.place(x=500, y=700)
def function_GUI():
    global function_face
    function_face=tkinter.Tk()
    function_face.title("功能页")
    function_face.geometry("650x650")
    function_face.wm_attributes('-topmost',1)
    name=tkinter.Label(function_face, text="功能页",font=("黑体", "40"))
    name.place(x=238, y=20)
    key_in=tkinter.Button(function_face,text ="""录入
学生信息""",width=9,height=2,font=("微软雅黑", "40"),command=add_stu_ifm_GUI)
    key_in.place(x=20, y=100)
    key_out=tkinter.Button(function_face,text ="""读取
学生信息""",width=9,height=2,font=("微软雅黑", "40"),command=read_stu_ifm_GUI)
    key_out.place(x=335, y=100)
    sort=tkinter.Button(function_face,text ="成绩排名",width=9,height=2,font=("微软雅黑", "40"),command=s_sort)
    sort.place(x=20, y=300)
    change=tkinter.Button(function_face,text ="""修改信息
(除身份证号)""",width=9,height=2,font=("微软雅黑", "40"),command=change_ifm_f)
    change.place(x=335, y=300)
    Exit=tkinter.Button(function_face,text ="退出",width=5,height=1,font=("微软雅黑", "30"),command=exit_GUI)
    Exit.place(x=500, y=500)
    
def add_account_GUI_s():
    global add_account_face
    global passwd
    global account
    password=passwd.get()
    account_name=account.get()
    try:
        usr=open("./user/"+account_name+".txt","r",encoding = 'utf-8')
    except:
        usr=open("./user/"+account_name+".txt","a",encoding = 'utf-8')
        usr.write(crypt(password))
        usr.close()
        usr=open("./user/"+account_name+"StudentInformation.txt","a",encoding = 'utf-8')
        usr.close()
        tkinter.messagebox.showinfo("提示","注册成功，请重启程序")
        add_account_face.destroy()
        sys.exit(0)
        return
    else:
        usr.close()
        tkinter.messagebox.showerror("错误","账户已存在")
        return
def a_cancel():
    global add_account_face
    add_account_face.destroy()
    first_face_GUI()
def add_account_GUI_f():
    global add_account_face
    global login_interface
    global passwd
    global account
    login_interface.destroy()
    add_account_face=tkinter.Tk()
    add_account_face.title("添加账户")
    add_account_face.geometry("650x650")
    add_account_face.wm_attributes('-topmost',1)
    name=tkinter.Label(add_account_face, text="添加账户",font=("黑体", "50"))
    name.place(x=200, y=50)
    uname=tkinter.Label(add_account_face, text="用户名",font=("微软雅黑", "30"))
    uname.place(x=10, y=195)
    account= tkinter.Entry(add_account_face,width=20,font=("微软雅黑", "30"))
    account.place(x=140, y=200)
    pname=tkinter.Label(add_account_face, text="密码",font=("微软雅黑", "30"))
    pname.place(x=10, y=285)
    passwd= tkinter.Entry(add_account_face,width=20,font=("微软雅黑", "30"))
    passwd.place(x=140, y=290)
    confirm=tkinter.Button(add_account_face,text ="确认",width=4,height=1,font=("微软雅黑", "20"),command = add_account_GUI_s)
    confirm.place(x=530, y=360)
    Cancel=tkinter.Button(add_account_face,text ="取消",width=4,height=1,font=("微软雅黑", "20"),command =a_cancel)
    Cancel.place(x=450,y=360)
def login_f():
    global passwd
    global account
    global password
    global account_name
    global login_interface
    password=passwd.get()
    account_name=account.get()
    try:
        usr=open("./user/"+account_name+".txt","r",encoding = 'utf-8')
    except:
        tkinter.messagebox.showerror("错误","不存在这个用户")
        return login("GUI")            
    else:
        a_Password=usr.readline()
        if crypt(a_Password)==password:
            tkinter.messagebox.showinfo("提示","登录成功")
            global user
            user=PeopleCount(account_name,password)
            login_interface.destroy()
            function_GUI()
            return
        else:
            tkinter.messagebox.showerror("错误","用户名或密码错误")
            return login("GUI")
def cancel():
    global login_interface
    login_interface.destroy()
    first_face_GUI()
def login(t_g="GUI"):
    if t_g=="terminal":
        print("-- -- -- -- --登录-- -- -- -- --")
        usr_name = input("请输入用户名：")
        try:
            usr=open("./user/"+usr_name+".txt","r",encoding = 'utf-8')
        except:
            print("不存在这个用户")
            return login("terminal")            
        else:
            a_Password=usr.readline()
            u_Password=input("请输入密码：")
            if crypt(a_Password)==u_Password:
                print("登录成功！")
                global user
                user=PeopleCount(usr_name,u_Password)
            else:
                print("用户名或密码错误")
                return login("terminal")
    elif t_g=="GUI":
        global login_interface
        global passwd
        global account
        login_interface.destroy()
        login_interface=tkinter.Tk()
        login_interface.title("登录")
        login_interface.geometry("650x650")
        login_interface.wm_attributes('-topmost',1)
        name=tkinter.Label(login_interface, text="登录",font=("黑体", "50"))
        name.place(x=250, y=50)
        uname=tkinter.Label(login_interface, text="用户名",font=("微软雅黑", "30"))
        uname.place(x=10, y=195)
        account= tkinter.Entry(login_interface,width=20,font=("微软雅黑", "30"))
        account.place(x=140, y=200)
        pname=tkinter.Label(login_interface, text="密码",font=("微软雅黑", "30"))
        pname.place(x=10, y=285)
        passwd= tkinter.Entry(login_interface,width=20,font=("微软雅黑", "30"))
        passwd.place(x=140, y=290)
        confirm=tkinter.Button(login_interface,text ="确认",width=4,height=1,font=("微软雅黑", "20"),command = login_f)
        confirm.place(x=530, y=360)
        Cancel=tkinter.Button(login_interface,text ="取消",width=4,height=1,font=("微软雅黑", "20"),command =cancel)
        Cancel.place(x=450,y=360)
def First_logon():
    if account=="true":
        return
    else:
        global usr
        print("-- -- -- -- --注册-- -- -- -- --")
        aName = input("请输入管理员账户名（管理员账户将不能修改）：")
        aPassword = input("请输入管理员密码：")
        aPassword_a=input("确认密码：")
        if aPassword==aPassword_a:
            usr.close()
            usr=open("account.txt","w",encoding = 'utf-8')
            usr.write("true")
            usr.close()
            usr=open("./user/"+aName+".txt","a",encoding = 'utf-8')
            usr.write(crypt(str(aPassword)))
            usr.close()
            usr=open("./user/"+aName+"StudentInformation.txt","a",encoding = 'utf-8')
            usr.close()
            print("注册成功！")
            return
        else:
            print("密码前后不一致，请重新注册")
            First_logon()
def reduction_GUI():
    global login_interface
    yon=tkinter.messagebox.askquestion("警告", "此操作会初始化设置，用户文件将不被保留")
    if yon=="yes":
        a=PeopleCount("eg","eg")
        a.reduction()
        tkinter.messagebox.showinfo("提示","请重新启动程序")
        login_interface.destroy()
        sys.exit(0)
    else:
        login_interface.destroy()
        first_face_GUI()
def add_account():
    print("-- -- -- -- --添加账户-- -- -- -- --")
    Name = input("请输入账户名：")
    Password = input("请输入密码：")
    Password_a=input("确认密码：")
    if Password==Password_a:
        try:
            usr=open("./user/"+Name+".txt","r",encoding = 'utf-8')
        except:
            usr=open("./user/"+Name+".txt","a",encoding = 'utf-8')
            usr.write(crypt(Password))
            usr.close()
            usr=open("./user/"+Name+"StudentInformation.txt","a",encoding = 'utf-8')
            usr.close()
            print("注册成功！")
            return
        else:
            print("账户已存在")
            return
        
    else:
        print("密码前后不一致，请重新注册")
def tog():
    t_g=input("""1.图形界面
2.终端界面
请输入序号：""")
    if t_g=="1":
        return 1
    elif t_g=="2":
        return 2
    else:
        print("请输入序号（1或2）")
        return tog()
try:
    os.mkdir('user')
except:
    pass
print("-- -- -- -- --学生成绩管理系统-- -- -- -- --")
usr=open("account.txt","a",encoding = 'utf-8')
usr=open("account.txt","r",encoding = 'utf-8')
account=usr.readline()

First_logon()
usr.close()
tog=tog()
if tog==1:
    first_face_GUI()
else:
    while True:
        opt=input("""1.登录
2.清除所有账户(此操作会初始化设置，用户文件将不被保留)
3.添加账户
请选择序号: """)
        if opt=="1":
            login("terminal")
            break
        elif opt=="2":
            opt_1=input("确定要清除所有账户吗？(y/n)")
            if opt_1=="y" or opt_1=="Y":
                print("请重新启动程序")
                a=PeopleCount("eg","eg")
                a.reduction()
                sys.exit(0)
            elif opt_1=="n" or opt_1=="N":
                continue
        elif opt=="3":
            add_account()
        else:
            print("请选择1或2\n")
        
    while True:
        print("""
1.录入学生信息
2.读取学生信息
3.成绩排名
4.修改信息(除身份证号)
5.退出
请输入序号：""",end="")
        opt=input()
        if opt=="1":
            print("-- -- -- -- --录入信息-- -- -- -- --")
            ID=input("请输入身份证号码(无法修改)：")
            name=input("请输入学生姓名：")
            s_ID=input("请输入学号：")
            c_s=input("请输入语文分数：")
            m_s=input("请输入数学分数：")
            e_s=input("请输入英语分数：")
            s_s=input("请输入科学分数：")
            R=user.inputInformation(ID,name,s_ID,c_s,m_s,e_s,s_s)
            if R=="success":
                print("录入成功")
            elif R=="error:repeat":
                print("学生重复")
        elif opt=="2":
            print("-- -- -- -- --读取信息-- -- -- -- --")
            print("""1.查看所有学生信息
2.查看指定学生信息""")
            opt_1=input()
            if opt_1=="1":
                fullIFM=user.returnInformation()
                for i in fullIFM:
                    print("\n身份证号:",i[0],"\n姓名:",i[1],"\n学号:",i[2],"\n语文分数:",i[3],"\n数学分数:",i[4],"\n英语分数:",i[5],"\n科学分数:",i[6])
            elif opt_1=="2":
                print("""1.按身份证号查询
2.按姓名查询
3.按学号查询""")
                opt_2=input("请选择查看学生方式：")
                if opt_2=="1":
                    c_i=input("请输入身份证号")
                    u_IFM=user.returnInformation(ID=c_i)
                elif opt_2=="2":
                    n=input("请输入姓名")
                    u_IFM=user.returnInformation(name=n)
                elif opt_2=="3":
                    s_i=input("请输入学号")
                    u_IFM=user.returnInformation(school_ID=s_i)
                else:
                    print("请选择序号(1或2或3)")
                    continue
                if u_IFM=="error:not find":
                    print("找不到这个学生")
                else:
                    print("\n身份证号:",u_IFM[0],"\n姓名:",u_IFM[1],"\n学号:",u_IFM[2],"\n语文分数:",u_IFM[3],"\n数学分数:",u_IFM[4],"\n英语分数:",u_IFM[5],"\n科学分数:",u_IFM[6])
            else:
                print("请选择序号(1~3)")
                continue
        elif opt=="3":
            print("-- -- -- -- --排名-- -- -- -- --")
            opt_1=input("""1.按学号排名
2.按语文成绩排名
3.按数学成绩排名
4.按英语成绩排名
5.按科学成绩排名
6.按总分排名
""")
            ans=user.sort(opt_1)
            if ans=="error":
                print("请输入数字序号(1~6)")
            elif ans=="error:not find student":
                print("没有学生，请先录入")
            else:
                for i in ans:
                    print("\n身份证号:",i[0],"\n姓名:",i[1],"\n学号:",i[2],"\n语文分数:",i[3],"\n数学分数:",i[4],"\n英语分数:",i[5],"\n科学分数:",i[6],"\n排名：",i[7])
        elif opt=="4":
            print("-- -- -- -- --修改信息-- -- -- -- --")
            modify=input("""1.按身份证号查询并修改
2.按姓名查询并修改
3.按学号查询并修改
请选择序号""")
            try:
                modify=int(modify)
            except:
                print("请输入数字序号")
                continue
            else:
                if modify<1 or modify>3:
                    print("请输入序号（1~3）")
                    continue
            way=input("请输入姓名(学号或身份证): ")
            kind=input("""1.修改姓名
2.修改学号
3.修改语文分数
4.修改数学分数
5.修改英语分数
6.修改科学分数
请输入序号""")
            try:
                kind=int(kind)
            except:
                print("请输入数字序号")
                continue
            else:
                if kind<1 or kind>6:
                    print("请输入序号（1~6）")
                    continue
            new=input("请输入新的信息：")
            usr=user.modifyInformation(modify,way,kind,new)
            if usr=="error:not find":
                print("没有找到学生")
            else :
                print("成功")
        elif opt=="5":
            sys.exit(0)
        else:
            print("请输入序号1~5")


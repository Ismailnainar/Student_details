from flask import Flask,render_template,url_for,request,redirect,session

app=Flask(__name__)
app.secret_key ="Ismail@124"

student_list=[{"Name":"Sivapackia","Age":22 ,"Roll_NO": 101, "Marks":[90,75,80,98,65]},
                    {"Name":"Siva","Age":21 ,"Roll_NO": 102, "Marks":[90,75,80,78,99]},
                    {"Name":"Vilobin","Age":21 ,"Roll_NO": 103, "Marks":[94,75,80,88,35]},
                    {"Name":"Mahadevi","Age":27 ,"Roll_NO": 104, "Marks":[70,85,80,98,35]},          
                    {"Name":"Nisha","Age":23 ,"Roll_NO": 105, "Marks":[90,75,85,98,35]},
                    {"Name":"Vaisali","Age":27 ,"Roll_NO": 106, "Marks":[80,98,35,90,75]},
                    {"Name":"Vijay","Age":22 ,"Roll_NO": 107, "Marks":[90,80,98,35,75]},
                    {"Name":"Mohamed Ismail","Age":22 ,"Roll_NO": 108, "Marks":[75,80,90,98,35]}]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    User_name="Ismail"
    Password="Ismail@124"
    if request.method == "POST":
        user_name=request.form.get("user_name")
        password=request.form.get("password")
        if User_name == user_name and Password == password:
            session['user_name']  = user_name
            return redirect(url_for("page"))
        else:
            return "chek username and password"
           

    return render_template("login.html")
@app.route('/home')
def page():
    return render_template("home.html",student=student_list)

@app.route('/add_student',methods=["GET","POST"])
def Add():
     if request.method == "POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        RollNo=request.form.get("RollNo")
        Mark1=request.form.get("Mark1")
        Mark2=request.form.get("Mark2")
        Mark3=request.form.get("Mark3")
        Mark4=request.form.get("Mark4")
        Mark5=request.form.get("Mark5")
        mark_list=[]
        mark_list.append(Mark1)
        mark_list.append(Mark2)
        mark_list.append(Mark3)
        mark_list.append(Mark4)
        mark_list.append(Mark5)
        

        student_details={}
        student_details.update({"Name":Name})
        student_details.update({"Age":Age})
        student_details.update({"Roll_NO":RollNo})
        student_details.update({"Marks":mark_list})
        
        student_list.append(student_details)

        return redirect(url_for("page"))
     return render_template("add.html")

@app.route('/edit/<int:index>',methods=["GET","POST"])
def edit(index):
    if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        Roll_NO=request.form.get("Roll_NO")
        Mark1=request.form.get("Mark1")
        Mark2=request.form.get("Mark2")
        Mark3=request.form.get("Mark3")
        Mark4=request.form.get("Mark4")
        Mark5=request.form.get("Mark5")
        Marks=[Mark1,Mark2,Mark3,Mark4,Mark5]
        Student=student_list[index-1]

        Student['Name']=Name
        Student['Age']=Age
        Student['Roll_NO']=Roll_NO
        Student['Marks']=Marks
        return redirect(url_for('page'))
    student_edit=student_list[index-1]
    return render_template("edit.html",student=student_edit)
@app.route('/delete/<int:index>',methods=["GET","POST"])
def delete(index):
    student_list.pop(int(index-1))
    
    return render_template("home.html",student=student_list)
@app.route('/logout')
def logout():
    session.pop("user_name",None)
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)
 
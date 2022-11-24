from flask import Flask,render_template,url_for,redirect

import os

app = Flask('__main__')



@app.route("/")
def Home():
    return "<h1 align=center>Please Enter Valid Employee name in URL</h1>"

@app.route('/<string:name>/')
def func(name):
    x = name.lower()
    data_path = x
    p = "static/"+data_path
    img_names = os.listdir(p)
    i=0
    for img_name in img_names:
        if i==0:
            joined_path = os.path.join(p, img_name)
            print(joined_path)
            text_file = open(joined_path, "r")
            i+=1

            data = text_file.read()
            a= data.split()
            pan = a[-1]
            n = a[:len(a)-1]
            s=""
            for j in n:
                t = j+" "
                s+=t



        elif i == 1:
            path2 = name+"/"+img_name
            print(path2)
            i+=1
            continue
        #
        elif i == 2:
            path3 = name+"/"+img_name
            i+=1

            continue

    return render_template('index.html',temp1=s,temp2=pan,temp3=path2,temp4=path3)



if __name__ == "__main__":
    app.run()


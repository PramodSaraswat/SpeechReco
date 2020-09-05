from flask import Flask, render_template,request,redirect
import speech_recognition as sr


app=Flask(__name__)
app.config['SECRET_KEY']='DJDJVNJFJFJD34MDM'

@app.route("/",methods=['GET','POST'])
def home():
    text=""
    if request.method == "POST":
        print("received")

        if "file" not in request.files:
            return redirect(request.url)

        file=request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recognizer=sr.Recognizer()
            audioFile=sr.AudioFile(file)
            with audioFile as source:
                data=recognizer.record(source)
            text=recognizer.recognize_google(data,key=None)
    return render_template("home.html",text=text)

if __name__=="__main__":
    app.run(debug=True,threaded=True)
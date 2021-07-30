# import a library
from flask import Flask, render_template,request
import joblib
# instance of an app
app = Flask(__name__)
model=joblib.load('dib_79.pkl')
@app.route('/')
def hello():
    return render_template('welcome.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/contact', methods=['POST'])
def contact():
    a=request.form.get('a')
    b=request.form.get('b')
    c=request.form.get('c')
    d=request.form.get('d')
    e=request.form.get('e')
    f=request.form.get('f')
    g=request.form.get('g')
    h=request.form.get('h')
    print(a,b,c,d,e,f,g,h)
    pred=model.predict([[a,b,c,d,e,f,g,h]])
    if pred[0]==1:
        output="diabetic"
    else:
        output="not diabetic"
    return render_template('contact.html',predicted_text=f'the person is{output}')

# run the app
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,render_template,request,jsonify

app = Flask(__name__,static_url_path="",static_folder='static')
@app.route('/')
def exam():
    return render_template('second.html')

if __name__ == '__main__':
    app.run(debug=True)
    

app = Flask(__name__)


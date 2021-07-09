from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/emp')
def home():
    arr = ["김소희","이여강","오수연","최윤지","김지수"]
    arr2 = [
            {'name': '김소희', 'tel':'010-2222-3333'},
            {'name': '이여강', 'tel':'010-3333-4444'}
        ]
    return render_template('index.html', dan=2,arr=arr,arr2=arr2)
 
if __name__ == '__main__':
    app.run(debug=True)
  
   
















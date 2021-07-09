from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
 
    dan = request.form("dan")
    int_dan = int(dan)
    txt = ""
    txt += "{}*{}={}<br/>\n".format(int_dan,1,int_dan*1)
    txt += "{}*{}={}<br/>\n".format(int_dan,2,int_dan*2)
    txt += "{}*{}={}<br/>\n".format(int_dan,3,int_dan*3)
    txt += "{}*{}={}<br/>\n".format(int_dan,4,int_dan*4)
    txt += "{}*{}={}<br/>\n".format(int_dan,5,int_dan*5)
    txt += "{}*{}={}<br/>\n".format(int_dan,6,int_dan*6)
    txt += "{}*{}={}<br/>\n".format(int_dan,7,int_dan*7)
    txt += "{}*{}={}<br/>\n".format(int_dan,8,int_dan*8)
    txt += "{}*{}={}<br/>\n".format(int_dan,9,int_dan*9)
    
    return txt
    
    
if __name__ == '__main__':
    app.run(debug=True)    
     
  
   
















from flask import Flask,render_template,request,jsonify
from oauth2client.contrib.flask_util import UserOAuth2

app = Flask(__name__,static_url_path="",static_folder='static')
@app.route('/')
def exam():
    return render_template('userlogin.html')

if __name__ == '__main__':
    app.run(debug=True)
    

app = Flask(__name__)

app.config['SECRET_KEY'] = '아무 문자열이나 넣으면 된다. 용도는 대강 알기 때문에 설명 못 함.'

# API 사용을 위해서 아래와 같이 관련 정보를 담은 json 파일(개발자 페이지에서 받을 수 있다)을 사용할 수 있고,
app.config['GOOGLE_OAUTH2_CLIENT_SECRETS_FILE'] = 'client_secrets.json'

# 이렇게 코드에 직접 넣을 수도 있다.
app.config['GOOGLE_OAUTH2_CLIENT_ID'] = 'your-client-id'
app.config['GOOGLE_OAUTH2_CLIENT_SECRET'] = 'your-client-secret'

oauth2 = UserOAuth2(app)
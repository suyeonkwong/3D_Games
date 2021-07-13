from flask import Flask,render_template,request,jsonify
from day10.mydao_emp import DaoEmp
from day13.mydao_emp import DaoExam

app = Flask(__name__,static_url_path="",static_folder='static')

@app.route('/exam')
def exam():
    de = DaoExam()
    list = de.selectlist()
    return render_template('exam.html',list=list)

@app.route('/exam_insert.ajax', methods=['POST'])
def ajax_insert():
    d = request.get_json()
    print(d)
    de = DaoExam()
    cnt = de.insert(d['exam_id'],d['e_id'],d['kor'],d['eng'],d['mat'])
    msg = 'fail'
    if cnt ==1:
        msg ="success"
    return jsonify(result=msg)
        
@app.route('/exam_delete.ajax', methods=['POST'])
def ajax_delete():
    d = request.get_json()
    print(d)
    de = DaoExam()
    cnt = de.delete(d['exam_id'])
    msg = 'fail'
    if cnt ==1:
        msg ="success"
    return jsonify(result=msg)
        
@app.route('/exam_update.ajax', methods=['POST'])
def ajax_update():
    d = request.get_json()
    print(d)
    de = DaoExam()
    cnt = de.update(d['exam_id'],d['e_id'],d['kor'],d['eng'],d['mat'])
    print(cnt)
    msg = 'fail'
    if cnt ==1:
        msg ="success"
    return jsonify(result=msg)

if __name__ == '__main__':
    app.run(debug=True)
    

  
   
















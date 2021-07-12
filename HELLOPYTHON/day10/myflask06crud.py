from flask import Flask,render_template,request,jsonify
from day10.mydao_emp import DaoEmp

app = Flask(__name__,static_url_path="",static_folder='static')

@app.route('/emp')
def emp():
    de = DaoEmp()
    list = de.selectlist()
    return render_template('emp.html',list=list)

@app.route('/emp_insert.ajax', methods=['POST'])
def ajax():
    d = request.get_json()
    print(d)
    de = DaoEmp()
    cnt = de.insert(d['e_id'],d['e_name'],d['tel'],d['address'])
    msg = 'fail'
    if cnt ==1:
        msg ="success"
    return jsonify(result=msg)
        
@app.route('/emp_delete.ajax', methods=['POST'])
def ajax_delete():
    d = request.get_json()
    print(d)
    de = DaoEmp()
    cnt = de.delete(d['e_id'])
    msg = 'fail'
    if cnt ==1:
        msg ="success"
    return jsonify(result=msg)
        
@app.route('/emp_update.ajax', methods=['POST'])
def ajax_update():
    d = request.get_json()
    print(d)
    de = DaoEmp()
    cnt = de.update(d['e_name'],d['tel'],d['address'],d['e_id'])
    print(cnt)
    msg = 'fail'
    if cnt ==1:
        msg ="success"
    return jsonify(result=msg)

if __name__ == '__main__':
    app.run(debug=True)
    

  
   
















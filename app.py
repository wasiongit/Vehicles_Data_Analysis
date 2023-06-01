from flask import Flask,render_template,request
import pandas as pd
from query_function import main_query_f

app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('home.html')


@app.route("/api",methods = ['GET', 'POST'])
def GetData():
    try:
        input_time1=int(request.form.get('input_time1'))
        input_time2=int(request.form.get('input_time2'))

        query_response=main_query_f(input_time1,input_time2)
        if query_response==True:
            df = pd.read_excel("static/output.xlsx")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames)
        return query_response
    except:
        return 'Please enter Both the Values correctly'
    # static/output.xlsx

if __name__ == "__main__":
    app.run()
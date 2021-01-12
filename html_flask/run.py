from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('invoice.html')


@app.route("/", methods=['POST'])
def get_values():
    pid = request.form['p_id']
    pname = request.form['p_name']
    pdesc = request.form['p_desc']

    result = insert_into_db(pid, pname, pdesc)
    if result == "passed":
        return render_template("pass.html", pid=pid, pname=pname, pdesc=pdesc)
    else:
        return render_template("fail.html")


def insert_into_db(pid, pname, pdesc):
    mydb = mysql.connector.connect()
    cursor = mydb.cursor()
    insert_query = "Insert into product(product_id, product_name, product_desc) values (%s, %s, %s)"
    data = [(pid, pname, pdesc)]
    cursor.executemany(insert_query, data)
    mydb.commit()
    return "passed"


if __name__ == "__main__":
    app.run()

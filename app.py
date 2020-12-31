from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from csv_process import scv_validate,process_csv
import os
import pandas

app = Flask(__name__)

@app.route('/')
def health():
    return render_template('index.html', button="")


@app.route('/upload', methods=["POST"])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        if scv_validate(filename):
            if os.path.exists("./files/data.csv"):
                os.remove("./files/data.csv")
                print("exits")
            else:
                print("not exits")
            data_table = process_csv(file)
            data_table.to_csv('./files/data.csv')
            return render_template('index.html', table='<br><div class="center">' + data_table.to_html() + '</div>', button="button.html")
        else:
            text = "File is invalid, please check if file is csv type or it doesn't include Address column"
            return render_template('index.html', text=text, button="")


@app.route('/download')
def download():
    return send_file('./files/data.csv', attachment_filename="your.csv", as_attachment=True)


if __name__ == '__main__':
    app.run()

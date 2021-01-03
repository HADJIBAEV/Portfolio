from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__, static_folder="static")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


# def write_to_file(data):
#     with open('./database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')


# def write_to_csv(data):
#     with open('./database.csv', mode='a', newline='') as database2:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         csv_writer = csv.writer(database2, delimiter=',',
#                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email, subject, message])


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             write_to_csv(data)
#             return redirect('/thankyou')
#         except:
#             return 'Did not save to database'
#     else:
#         return 'Something went wrong!'

# if __name__ == '__main__':
#     # Threaded option to enable multiple instances for multiple user access support
#     app.run(threaded=True, port=5000)

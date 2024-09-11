from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/receive', methods=['GET', 'POST'])
def receive():
    if request.method == 'POST':
        receive_code = request.form.get('receive_code')
        # Implement your logic to handle the 9-digit receive code
        return f"Code entered: {receive_code}"
    return render_template('receive.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

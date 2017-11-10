from flask import Flask, request, jsonify

app = Flask (__name__)

@app.route('/')
def index():
    # stuurt inteface naar browser.
    return app.send_static_file('index.html')

@app.route('/light', methods=['POST'])
def lightPOST():
    data = request.get_json()
    data['light'] = not data['light']
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

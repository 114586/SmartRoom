from flask import Flask, request, jsonify

app = Flask (__name__)

@app.route('/')
def index():
    # stuurt inteface naar browser.
    return app.send_static_file('index.html')

@app.route('/light', methods=['GET'])
def light():
    data = {}
    #zet licht aan. Voeg commando's toe!
    #bevestig licht aan.
    data['light'] = 'ON'
    # converteer dict naat json en print naar interface.
    return jsonify(data) 

@app.route('/light', methods=['POST'])
def lightPOST():
    data = request.get_json()
    data['light'] = not data['light']
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
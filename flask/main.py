from flask import Flask, request, jsonify
#Install flask_cors: pip install flask-cors
from flask_cors import CORS
#Install jwt: pip install pyjwt
import jwt
#base64 encoding (for password). Wordt gebruikt om files via internet te versturen.
import base64
import datetime
from functools import wraps

app = Flask (__name__)
CORS(app)

# secret key om gegevens te versleutelen (encriptie) met jwt.
app.config["SECRET_KEY"] = 'asdfiheoifjcqpweiruvoq83ruigowiuefpqociwmefp[oaiuwnevoaiufmpawoeirvapw9eutnaoiwu'

'''
#Vervangen door flask CORS library.
def allowAllOrigins(response):
    # laat request van elk (*) ip toe.
    response.headers.add('Acces-Control-Allow-Origin', '*')
    return response
'''

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        '''
            # request naar server voor service. Argument wordt meegestuurd in url na vraagteken (?).
            # Parameters worden weergegen in url na ? en worden gescheiden door &.
            # Frontend geeft arguments mee, backend haalt ze eruit.
            # get token uit request.
            token = request.args.get('token')
        '''
        if 'x-smartroom-token' in request.headers:
            token = request.headers['x-smartroom-token']
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
            except:
                return jsonify({'message' : "Token is invalid."}), 498
        else:
            return jsonify({'message' : "Token is missing."}), 499
        # *args en **kwargs = arguments en keyword arguments.
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET'])
def index():
    # stuurt inteface naar browser.
    return app.send_static_file('index.html')

# stuurt extra files die worden aangesproken in index.html.
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.route('/login', methods=['POST'])
def login():
    # get dictionary auth from frontend.
    auth = request.get_json()
    print("auth = ", auth)
    # als auth != None en passwordt klopt dan maak jwt token.
    # frontend checkt voor username.
    # backend moet checken voor password, anders errror als login route wordt aangesproken via url.
    if auth and "password" in auth:

        p = base64.b64decode(auth["password"]).decode("utf-8", "ignore")

        if p == "password":
            token = jwt.encode({
                'user': auth["user"],
                # exp = geldigheidsduur van token.
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=90)
            }, app.config['SECRET_KEY'])
            tokenInfo = {
                'user' : auth["user"],
                'token' : token.decode("UTF-8") 
            }
            return jsonify(tokenInfo)
        else:
            return jsonify({'message' : "Password is incorrect."}), 401
    else:
        return jsonify({'message' : "Vul password in! :("}), 400

@app.route('/light', methods=['POST'])
@token_required
def lightPOST():
    data = request.get_json()
    print("data light", data)

    if data and "light" in data:
        if data["light"] == True:
            #hier moet code komen die het licht uit zet.
            pass
        else:
            #hier moet code komen die het licht aan zet.
            pass


        data['light'] = not data['light']
        return jsonify(data)
    else:
        return jsonify({"message" : "No data provided."}), 400
        
@app.route('/lock', methods=['POST'])
@token_required
def lockPOST():
    data = request.get_json()
    print("data lock", data)

    if data and "lock" in data:
        if data["lock"] == True:
            #hier moet code komen die het lock uit zet.
            pass
        else:
            #hier moet code komen die het lock aan zet.
            pass


        data['lock'] = not data['lock']
        return jsonify(data)
    else:
        return jsonify({"message" : "No data provided."}), 400

@app.route('/camera', methods=['POST'])
@token_required
def cameraPOST():
    data = request.get_json()
    print("data camera", data)

    if data and "camera" in data:
        if data["camera"] == True:
            #hier moet code komen die het camera uit zet.
            pass
        else:
            #hier moet code komen die het camera aan zet.
            pass


        data['camera'] = not data['camera']
        return jsonify(data)
    else:
        return jsonify({"message" : "No data provided."}), 400

@app.route('/motion', methods=['POST'])
@token_required
def motionPOST():
    data = request.get_json()
    print("data motion", data)

    if data and "motion" in data:
        data['motion'] = not data['motion']
        print("data motion", data)
        if data['motion'] == True:
            #Open file for communication with motion sensor.
            file = open("Communicate_motion", "w")
            file.write("1")
            print("writing 1...")
            file.close()
            
        else:
            #Open file for communication with motion sensor.
            file = open("Communicate_motion", "w")
            file.write("0")
            print("writing 0...")
            file.close()
        return jsonify(data)
    else:
        return jsonify({"message" : "No data provided."}), 400


if __name__ == "__main__":
    app.run(debug=True)

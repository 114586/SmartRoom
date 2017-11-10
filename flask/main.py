from flask import Flask, request, jsonify
#Install jwt: pip install pyjwt
import jwt
import datetime
from functools import wraps

app = Flask (__name__)

# secret key om gegevens te versleutelen (encriptie) met jwt.
app.config["SECRET_KEY"] = 'asdfiheoifjcqpweiruvoq83ruigowiuefpqociwmefp[oaiuwnevoaiufmpawoeirvapw9eutnaoiwu'

def allowAllOrigins(response):
    # laat request van elk (*) ip toe.
    response.headers.add('Acces-Control-Allow-Origin', '*')
    return response

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # get token uit request.
        token = request.args.get('token')

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : "Token is missing or invalid."})
        # *args en **kwargs = arguments en keyword arguments.
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    # stuurt inteface naar browser.
    return app.send_static_file('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    auth = request.authorization
    # als auth != None en passwordt klopt dan maak jwt token.
    if auth and auth.password == "password":
        token = jwt.encode({
            'user': auth.username
            # exp = geldigheidsduur van token.
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=90)
        }, app.config['SECRET_KEY'])
        tokenInfo = {
            'user' : auth.username,
            'token' : token.decode("UTF-8") 
        }
        return jsonify(tokenInfo)

    else:
        return make_response("You're not allowed to use this app.", 401, 
        {"WWW-Authenticate" : "Basic realm='Login Required'"})

@app.route('/light', methods=['POST'])
@token_required
def lightPOST():
    data = request.get_json()
    data['light'] = not data['light']
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
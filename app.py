from flask import Flask
import socket
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Welcome to Samruddi Farms'

@app.route('/name')
def name():
    return 'This is name'

@app.route('/ip')
def ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

if __name__ == '__main__':
    app.run()

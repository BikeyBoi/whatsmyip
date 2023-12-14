import os
from flask import Flask, render_template
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Configure BasicAuth using environment variables
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME', 'Your Username')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD', 'Your Password')

basic_auth = BasicAuth(app)

def get_ip():
    try:
        # Run the command and redirect the output to a file
        os.system('curl https://api.ipify.org?format=json > ip_output.txt')

        # Read the content of the file
        with open('ip_output.txt', 'r') as file:
            ip_address = file.read().strip()

        return ip_address
    except Exception as e:
        # Handle the exception, for example, print an error message
        print(f"Error retrieving IP: {str(e)}")
        return "Error retrieving IP"

@app.route('/')
@basic_auth.required
def home():
    ip_address = get_ip()
    return render_template('index.html', ip_address=ip_address)

if __name__ == '__main__':
    app.run()
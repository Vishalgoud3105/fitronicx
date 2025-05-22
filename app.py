from flask import Flask, render_template, request, jsonify
from x_logic import process_fitness_submission
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data['name']
    email = data['email']
    gender = data['gender']
    diet = data['diet']

    subject, body = process_fitness_submission(name, email, gender, diet)

    try:
        # Email sending setup (update SMTP credentials accordingly)
        msg = MIMEText(body, "plain")
        msg['Subject'] = subject
        msg['From'] = "your@email.com"
        msg['To'] = email

        # Uncomment this for actual email sending
        # with smtplib.SMTP('smtp.example.com', 587) as server:
        #     server.starttls()
        #     server.login("your@email.com", "your-password")
        #     server.send_message(msg)

        return jsonify({"message": f"Success! Email sent to {email}."})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

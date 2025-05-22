from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data['name']
    email = data['email']
    gender = data['gender']
    diet = data['diet']

    # Example only: integrate actual logic from x.py here
    subject = "Your Fitness Evaluation Result"
    body = f"Hi {name},\n\nThank you for submitting your fitness details. You have selected a {diet} diet.\n\nStay healthy!"

    # Send Email (use your actual SMTP configuration here)
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "your@email.com"
        msg['To'] = email

        # Uncomment and configure
        # with smtplib.SMTP('smtp.example.com', 587) as server:
        #     server.starttls()
        #     server.login('your@email.com', 'your-password')
        #     server.send_message(msg)

        return jsonify({"message": f"Email sent successfully to {email}!"})
    except Exception as e:
        return jsonify({"message": f"Failed to send email: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

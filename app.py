from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    total_claim_amount = float(request.form['Amount'])

    police_value = request.form['police_report_available']
    if police_value == "yes":
        police_report_available = 1
    else:
        police_report_available = 0

    policy_number = int(request.form['policy_number'])

    # TEMP LOGIC
    if total_claim_amount > 50000 and police_report_available == 0:
        prediction = "🚨 Fraud Reported"
    else:
        prediction = "✅ No Fruad Reported"

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

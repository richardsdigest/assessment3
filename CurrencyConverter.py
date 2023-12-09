from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# exchangerate.host API endpoint
API_ENDPOINT = "https://api.exchangerate.host/latest"

@app.route('/')
def index():
    return render_template('Currency.html')

@app.route('/convert', methods=['POST'])
def convert():
    # Get user input from the form
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])

    # Make a request to exchangerate.host API
    params = {'base': from_currency, 'symbols': to_currency}
    response = requests.get(API_ENDPOINT, params=params)

    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['rates'][to_currency]
        converted_amount = round(amount * conversion_rate, 2)
        result = f"{amount} {from_currency} is equal to {converted_amount} {to_currency}"
    else:
        result = "Error fetching exchange rates."

    return render_template('Currency.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

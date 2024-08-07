from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/stk-push/', methods=['POST'])
def stk_push_callback():
    payment_data = request.json  # Assuming the payment processor sends JSON data
    
    # Forward the data to your Django app
    django_callback_url = 'http://127.0.0.1:8000/cart/checkout'
    response = requests.post(django_callback_url, json=payment_data)
    
    return jsonify({'status': 'success', 'message': 'Callback forwarded to Django app'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

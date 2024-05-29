from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        net_income = float(data['net_income'].replace(',', ''))
        total_assets = float(data['total_assets'].replace(',', ''))
        total_liabilities = float(data['total_liabilities'].replace(',', ''))
        current_assets = float(data['current_assets'].replace(',', ''))
        current_liabilities = float(data['current_liabilities'].replace(',', ''))

        roa = net_income / total_assets
        leverage = total_liabilities / total_assets
        current_ratio = current_assets / current_liabilities
        zmijewski_score = -4.336 - 4.513 * roa + 5.679 * leverage + 0.004 * current_ratio

        risk = "High risk of bankruptcy" if zmijewski_score > 0 else "Lower risk of bankruptcy"
        return jsonify({'zmijewski_score': zmijewski_score, 'risk': risk})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


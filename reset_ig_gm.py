from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_reset', methods=['POST'])
def send_reset():
    email = request.form.get('email')

    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
    
    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "Mozilla/5.0 (Linux; Android 10)",
        "x-csrftoken": "BbJnjd.Jnw20VyXU0qSsHLV"
    }

    data = {
        "email_or_username": email,
        "flow": "fxcal"
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.json()

        if result.get("email_or_sms_sent") == True:
            return jsonify({"success": True, "message": "✅ E-posta gönderme başarılı!"})
        else:
            return jsonify({"success": False, "message": "❌ E-posta gönderimi başarısız."})
    except Exception as e:
        return jsonify({"success": False, "message": "❌ Hata: " + str(e)}), 500

# ✅ Render için doğru port ayarı
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

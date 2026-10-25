import hashlib
import time
from flask import Flask, request, jsonify, render_template
import user_agents  # pip install pyyaml ua-parser user-agents

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def home():
    # Încarcă fișierul index.html separat
    return render_template('index.html')

def get_client_ip(req):
    if req.headers.get('X-Forwarded-For'):
        ip = req.headers.get('X-Forwarded-For').split(',')[0].strip()
    elif req.headers.get('X-Real-IP'):
        ip = req.headers.get('X-Real-IP')
    else:
        ip = req.remote_addr
    return ip

@app.route('/track', methods=['POST'])
def collect_user_data():
    # Extragere date din body (numele studentului)
    if request.is_json:
        data = request.get_json()
        student_name = data.get('student_name', 'Anonim')
    else:
        student_name = request.form.get('student_name', 'Anonim')

    # Extragere date din Request Headers
    client_ip = get_client_ip(request)
    ua_string = request.headers.get('User-Agent', '')
    user_agent = user_agents.parse(ua_string)
    
    timestamp = int(time.time())
    
    # Generare amprenta unica
    raw_signature = f"{student_name}-{client_ip}-{ua_string}-{timestamp}"
    run_signature = hashlib.sha256(raw_signature.encode('utf-8')).hexdigest()[:12]

    collected_data = {
        'student': student_name,
        'run_info': {
            'timestamp': timestamp,
            'verification_hash': run_signature
        },
        'network': {
            'ip_address': client_ip
        },
        'device_context': {
            'browser': f"{user_agent.browser.family} {user_agent.browser.version_string}",
            'os': f"{user_agent.os.family} {user_agent.os.version_string}",
            'device_type': 'Mobile' if user_agent.is_mobile else ('Tablet' if user_agent.is_tablet else 'Desktop'),
            'raw_user_agent': ua_string
        },
        'user_preferences_implicit': {
            'preferred_language': request.headers.get('Accept-Language', '').split(',')[0]
        }
    }

    print(f"[{time.strftime('%H:%M:%S')}] Cerere primită de la studentul: {student_name}")
    return jsonify(collected_data), 200

if __name__ == '__main__':
    print("Serverul ruleaza la http://127.0.0.1:5000")
    app.run(debug=True, port=5000)

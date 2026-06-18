from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

FEEDBACK_FILE = 'feedback.txt'

def save_feedback(email, text):
    """
    MENYIMPAN DATA KE FILE TXT
    Format: email|pesan|tanggal-waktu
    Setiap baris = 1 entri feedback
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Gunakan '|' sebagai pemisah agar mudah dibaca/diurai
    entry = f"{email}|{text}|{timestamp}\n"
    # Mode 'a' = append (tambah di akhir file)
    with open(FEEDBACK_FILE, 'a', encoding='utf-8') as f:
        f.write(entry)

@app.route('/', methods=['GET', 'POST'])
def index():
    button_python = None
    button_discord = None
    button_html = None
    button_db = None
    email = ''
    text = ''
    feedback_success = False

    if request.method == 'POST':
        if 'send_feedback' in request.form:
            email = request.form.get('email', '').strip()
            text = request.form.get('text', '').strip()
            if email and text:
                save_feedback(email, text)
                feedback_success = True
            return render_template('index.html',
                                   feedback_success=feedback_success,
                                   email=email,
                                   text=text)

        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')

    return render_template('index.html',
                           button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db,
                           email=email,
                           text=text,
                           feedback_success=feedback_success)

if __name__ == "__main__":
    app.run(debug=True)

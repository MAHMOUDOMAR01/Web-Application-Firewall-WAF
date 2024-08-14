from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from waf.checker import (
    check_for_sql_injection, check_for_xss, check_for_lfi,
    check_for_rfi, check_for_csrf, check_for_xxe, check_for_command_injection
)
from waf.logger import log_attack, read_logs, analyze_logs

app = Flask(__name__)
app.secret_key = 'mrhak'  # تغيير المفتاح السري حسب الحاجة

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        data = request.form['data']
        ip_address = request.remote_addr
        if check_for_sql_injection(data):
            result = "Warning: Potential SQL Injection attack detected!"
            log_attack('SQL Injection', data, ip_address)
        elif check_for_xss(data):
            result = "Warning: Potential XSS attack detected!"
            log_attack('XSS', data, ip_address)
        elif check_for_lfi(data):
            result = "Warning: Potential LFI attack detected!"
            log_attack('LFI', data, ip_address)
        elif check_for_rfi(data):
            result = "Warning: Potential RFI attack detected!"
            log_attack('RFI', data, ip_address)
        elif check_for_csrf(data):
            result = "Warning: Potential CSRF attack detected!"
            log_attack('CSRF', data, ip_address)
        elif check_for_xxe(data):
            result = "Warning: Potential XXE attack detected!"
            log_attack('XXE', data, ip_address)
        elif check_for_command_injection(data):
            result = "Warning: Potential Command Injection attack detected!"
            log_attack('Command Injection', data, ip_address)
        else:
            result = "No attacks detected."
    return render_template('index.html', result=result)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['username']
        login_user(User(user_id))
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin():
    logs = read_logs()
    analysis = analyze_logs()
    return render_template('report.html', logs=logs, analysis=analysis)

if __name__ == '__main__':
    app.run(debug=True)

import os
from datetime import datetime
from collections import Counter

LOG_FILE = 'logs/attack_logs.txt'

def log_attack(attack_type, data, ip_address):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"[{datetime.now()}] {attack_type} detected! Data: {data}, IP: {ip_address}\n")

def read_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as log_file:
            return log_file.readlines()
    return []

def analyze_logs():
    logs = read_logs()  # استخدام الدالة الصحيحة لقراءة السجلات
    attack_types = []
    for log in logs:
        parts = log.split(' ')
        if len(parts) > 2:  # تأكد من أن هناك عدد كافٍ من العناصر
            attack_types.append(parts[1])  # تغيير الفهرس إلى 1 ليتناسب مع صيغة السجل
        else:
            attack_types.append('Unknown')  # إضافة قيمة بديلة إذا كان السجل غير صحيح

    # تحليل الأنواع
    analysis = Counter(attack_types)  # استخدام Counter لتحليل الأنواع بشكل أسرع

    return analysis

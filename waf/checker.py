from waf.rules import (
    SQL_INJECTION_PATTERNS, XSS_PATTERNS, LFI_PATTERNS,
    RFI_PATTERNS, CSRF_PATTERNS, XXE_PATTERNS, COMMAND_INJECTION_PATTERNS
)

def check_for_sql_injection(data):
    return any(pattern in data.lower() for pattern in SQL_INJECTION_PATTERNS)

def check_for_xss(data):
    return any(pattern in data.lower() for pattern in XSS_PATTERNS)

def check_for_lfi(data):
    return any(pattern in data.lower() for pattern in LFI_PATTERNS)

def check_for_rfi(data):
    return any(pattern in data.lower() for pattern in RFI_PATTERNS)

def check_for_csrf(data):
    return any(pattern in data.lower() for pattern in CSRF_PATTERNS)

def check_for_xxe(data):
    return any(pattern in data.lower() for pattern in XXE_PATTERNS)

def check_for_command_injection(data):
    return any(pattern in data.lower() for pattern in COMMAND_INJECTION_PATTERNS)

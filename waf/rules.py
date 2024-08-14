SQL_INJECTION_PATTERNS = [
    "' OR '1'='1", "--", "SELECT", "UNION", "INSERT", "UPDATE", "DELETE"
]

XSS_PATTERNS = [
    "<script>", "</script>", "<img src=", "javascript:", "onerror="
]

LFI_PATTERNS = [
    "..", "/etc/passwd", "/etc/shadow", "file://"
]

RFI_PATTERNS = [
    "http://", "https://", "ftp://"
]

CSRF_PATTERNS = [
    "csrf_token", "<input type='hidden' name='csrf_token'"
]

XXE_PATTERNS = [
    "<!ENTITY", "file://", "<!DOCTYPE"
]

COMMAND_INJECTION_PATTERNS = [
    ";", "|", "&", "$", ">", "<", "`", "ls", "cat", "echo"
]

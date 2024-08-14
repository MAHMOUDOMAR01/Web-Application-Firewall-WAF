# Web Application Firewall (WAF) Project

## Overview

This project is a Web Application Firewall (WAF) designed to detect and log various types of attacks on a web application. It provides a basic implementation to monitor and analyze attack patterns, generating reports on detected threats.

## Features

- **Attack Logging:** Logs attacks with details such as type, data, and IP address.
- **Log Reading:** Reads and processes log files for analysis.
- **Attack Analysis:** Analyzes attack logs to provide insights into attack types and their frequencies.
- **Web Interface:** Provides a simple web interface for accessing reports and viewing attack data.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/waf-project.git
    cd waf-project
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

5. **Access the web interface:**
    - Open your browser and go to `http://127.0.0.1:5000`

## Usage

- **Logging Attacks:**
    - Calls to `log_attack(attack_type, data, ip_address)` will log new attacks.
- **Viewing Reports:**
    - Navigate to `/admin` to view attack logs and analysis.

## Configuration

- **Log File:** The log file is located at `logs/attack_logs.txt`.
- **Web Interface:** Accessible at `/admin` after starting the application.

## Contributing

1. **Fork the repository.**
2. **Create a new branch:**

    ```bash
    git checkout -b feature/your-feature
    ```

3. **Commit your changes:**

    ```bash
    git commit -m "Add new feature"
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature/your-feature
    ```

5. **Create a pull request.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bootstrap](https://getbootstrap.com/) for the front-end styling.

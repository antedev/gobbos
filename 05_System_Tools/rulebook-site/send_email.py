#!/usr/bin/env python3
import os
import sys
import json
import smtplib
from email.mime.text import MIMEText

def main():
    if len(sys.argv) < 3:
        print("Usage: send_email.py <subject> <body>")
        sys.exit(1)

    subject = sys.argv[1]
    body = sys.argv[2]

    # Resolve paths
    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(script_dir, "email-config.json")
    example_path = os.path.join(script_dir, "email-config.example.json")

    if not os.path.exists(config_path):
        print(f"WARNING: Email notification not sent because '{config_path}' does not exist.")
        print(f"To configure emails, copy '{example_path}' to '{config_path}' and fill in your SMTP credentials.")
        sys.exit(0)

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to read email configuration from '{config_path}': {e}", file=sys.stderr)
        sys.exit(1)

    # Check required fields
    required = ["smtp_host", "smtp_port", "smtp_user", "smtp_pass", "from_addr", "to_addr"]
    missing = [field for field in required if not config.get(field) or "example.com" in str(config.get(field))]
    if missing:
        print(f"WARNING: Email notification not sent. The following fields in '{config_path}' are missing or still set to defaults: {', '.join(missing)}")
        sys.exit(0)

    # Prepare email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config["from_addr"]
    msg["To"] = config["to_addr"]

    try:
        print(f"Connecting to SMTP server {config['smtp_host']}:{config['smtp_port']}...")
        if config.get("use_tls", True):
            server = smtplib.SMTP(config["smtp_host"], config["smtp_port"], timeout=10)
            server.ehlo()
            server.starttls()
            server.ehlo()
        else:
            server = smtplib.SMTP_SSL(config["smtp_host"], config["smtp_port"], timeout=10)
            server.ehlo()

        server.login(config["smtp_user"], config["smtp_pass"])
        server.sendmail(config["from_addr"], [config["to_addr"]], msg.as_string())
        server.quit()
        print(f"Email successfully sent to {config['to_addr']}.")
    except Exception as e:
        print(f"ERROR: Failed to send email to {config['to_addr']} via SMTP: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

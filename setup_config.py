
import json
import os

config_path = "config.json"

def prompt_config():
    print("🔧 Initial Setup: Enter your configuration details\n")

    config = {
        "virustotal_api_key": input("Enter your VirusTotal API key: ").strip(),
        "email": {
            "smtp": input("Enter SMTP server (e.g., smtp.gmail.com): ").strip(),
            "port": int(input("Enter SMTP port (e.g., 587): ").strip()),
            "sender_email": input("Enter sender email: ").strip(),
            "password": input("Enter email password or app password: ").strip()
        },
        "webhook_url": input("Enter your webhook URL (e.g., Discord/Slack): ").strip()
    }

    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
    print("\n✅ Configuration saved to config.json")

if __name__ == "__main__":
    if not os.path.exists(config_path):
        prompt_config()
    else:
        print("✅ config.json already exists. You can delete it to reconfigure.")

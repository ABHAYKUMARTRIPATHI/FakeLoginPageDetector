# 🛡️ Fake Login Page Detector

A powerful cybersecurity tool that detects fake or phishing login pages using multiple analysis layers — including URL inspection, SSL verification, WHOIS data, and content behavior. It includes a dashboard, browser extension support, VirusTotal integration, and real-time alerting.

---

## 🔍 Features

- ✅ Phishing detection using:
  - URL structure analysis
  - SSL certificate inspection
  - WHOIS domain lookup (age, registrar)
  - HTML form and content behavior
- 🧠 VirusTotal API Integration
- 📊 Real-time dashboard for scan logs
- 🔔 Email and Webhook alerts (Slack, Discord, etc.)
- 👁️ Chrome Extension (Phase 2 support)
- 💾 Suspicious page logging
- 🧪 One-click dynamic config setup script

---

## 📂 Project Structure

FakeLoginPageDetector/
│
├── backend/                
│   ├── app.py             
│   ├── detector.py        
│   ├── virustotal.py       
│   ├── notifier.py         
│   └── database.py         
│
├── dashboard/              
│   ├── templates/
│   │   └── dashboard.html
│   └── static/
│       └── dashboard.js
│
├── extension/              
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── background.js
│
├── utils/                  
│   ├── ssl_checker.py
│   ├── whois_lookup.py
│   └── content_scanner.py
│
├── logs/                   
│   └── suspicious_sites.log
│
├── setup_config.py         
├── config.json            
├── requirements.txt       
└── README.md   

---

## ⚙️ First-Time Setup

 📥 Install Dependencies

pip install -r requirements.txt
python setup_config.py

It will ask for:
	•	VirusTotal API key
	•	SMTP email credentials
	•	Webhook URL (for alerts)

 🚀 Start the Server
 
 python backend/app.py

 ---

 🧪 Test URLs

You can test using:
	•	Real phishing links (from PhishTank, for testing purposes)
	•	Fake login HTML saved locally
	•	Any suspicious-looking login URL

 ---

🔐 Security Tip

Never test this with actual credentials.
Use fake inputs or test accounts only.

---

👨‍💻 Author

Abhay Kumar Tripathi

[GitHub](https://github.com/ABHAYKUMARTRIPATHI)  
[LinkedIn](https://www.linkedin.com/in/abhay-kumar-tripathi-54899b31a)  
[Instagram](https://www.instagram.com/abhaytripathi_46)
 

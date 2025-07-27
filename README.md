🔍 Log Analyzer for Suspicious Behavior

A lightweight Streamlit-based web application that helps analyze server log files (like Apache logs) to detect signs of suspicious or malicious activity. This tool is useful for cybersecurity students, SOC analysts, or sysadmins looking to quickly investigate unauthorized access attempts or brute-force patterns.

✅ Features

📤 Upload .log or .txt server log files (Apache-style)

🔍 Extract key fields: IP address, method, path, status, and timestamp

🚨 Identify:

Unauthorized access attempts (401 errors)

Forbidden resource access (403 errors)

IPs with multiple failed attempts (potential brute-force)

📊 Tabular visualization of logs and filtered alerts

⬇️ Export suspicious entries as CSV

📁 Sample Log Format Supported

192.168.1.10 - - [27/Jul/2025:10:20:34 +0530] "GET /login HTTP/1.1" 401 128

🛠 Technologies Used

Python 3

Streamlit – for building the interactive UI

Pandas – for log data handling

Regular expressions – for log parsing

🚀 How to Run (in GitHub Codespaces or locally)

# 1. Clone the repository
git clone https://github.com/your-username/log-analyzer.git
cd log-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py

📌 Use Cases

Security Operations Center (SOC) interns or students for log analysis practice

Lightweight log triage tool for CTFs or lab environments

Quick detection of unauthorized access behavior in test servers

📦 Future Enhancements

GeoIP mapping of IP addresses

Visual graphs for attack frequency

Support for additional log formats (Nginx, SSH, Windows Event Logs)

Integration with threat intelligence APIs


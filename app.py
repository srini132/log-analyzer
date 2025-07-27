import streamlit as st
import re
import pandas as pd

st.set_page_config(page_title="Log Analyzer", layout="centered")
st.title("🔍 Suspicious Log Analyzer")

uploaded_file = st.file_uploader("Upload your server log file (.log)", type=["log", "txt"])

log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*\[(?P<date>[^\]]+)\] "(?P<method>GET|POST|HEAD|PUT|DELETE) (?P<path>.*?) HTTP.*" (?P<status>\d{3})')

def parse_logs(content):
    entries = []
    for line in content.splitlines():
        match = log_pattern.search(line)
        if match:
            entries.append(match.groupdict())
    return entries

if uploaded_file:
    content = uploaded_file.read().decode('utf-8')
    parsed_data = parse_logs(content)
    df = pd.DataFrame(parsed_data)

    if df.empty:
        st.warning("No valid log entries found.")
    else:
        st.success(f"Parsed {len(df)} log entries.")
        st.dataframe(df.head(10))

        st.subheader("🚨 Suspicious Activity Report")

        suspicious_df = df[df["status"].isin(["401", "403"])]
        st.write(f"🔴 {len(suspicious_df)} unauthorized or forbidden attempts")

        if not suspicious_df.empty:
            st.dataframe(suspicious_df)

            # Top attacking IPs
            ip_counts = suspicious_df["ip"].value_counts()
            high_risk_ips = ip_counts[ip_counts > 5]

            if not high_risk_ips.empty:
                st.write("⚠️ High-risk IPs (>5 failed attempts):")
                st.write(high_risk_ips)

            # Export CSV
            csv = suspicious_df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download Suspicious Logs", csv, "suspicious_logs.csv", "text/csv")

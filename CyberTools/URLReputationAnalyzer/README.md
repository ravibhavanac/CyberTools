# URL Reputation Analyzer

A Python-based cybersecurity tool that analyzes URLs for common phishing and scam indicators.

## Features

- HTTPS Detection
- Domain Length Analysis
- Numeric Domain Detection
- Suspicious Keyword Detection
- Excessive Hyphen Detection
- Raw IP Address Detection
- Risk Scoring System

## Why It Matters

Attackers often use deceptive URLs to trick users into revealing credentials or downloading malware.

Examples:

- amaz0n-login.com
- paypal-security-update.net
- microsoft-account-verification.com

This tool evaluates URLs and provides a risk assessment based on commonly observed phishing techniques.

## Example

Input:

https://amaz0n-security-update.com

Output:

Risk Score: 55

Risk Level: HIGH

Reasons:
- Numbers detected in domain
- Suspicious keywords detected
- Excessive hyphens detected

## Technologies Used

- Python
- URL Parsing
- String Analysis

## Future Improvements

- WHOIS Lookup
- Domain Age Detection
- VirusTotal Integration
- Threat Intelligence Feeds
- Machine Learning Risk Models

## Disclaimer

This project is intended for educational and cybersecurity learning purposes.

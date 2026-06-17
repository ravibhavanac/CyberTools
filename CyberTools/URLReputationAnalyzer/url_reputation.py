from urllib.parse import urlparse

url = input("Enter URL: ")

parsed = urlparse(url)

domain = parsed.netloc.lower()

risk_score = 0
reasons = []

suspicious_keywords = [
    "login",
    "signin",
    "verify",
    "verification",
    "update",
    "account",
    "secure",
    "security",
    "password",
    "bank",
    "wallet",
    "payment",
    "reset"
]

# HTTPS Check

if parsed.scheme != "https":
    risk_score += 25
    reasons.append("HTTPS not enabled")

# Long Domain Check

if len(domain) > 30:
    risk_score += 15
    reasons.append("Suspiciously long domain")

# Number Detection

if any(char.isdigit() for char in domain):
    risk_score += 15
    reasons.append("Numbers detected in domain")

# Excessive Hyphens

if domain.count("-") >= 2:
    risk_score += 15
    reasons.append("Excessive hyphens detected")

# Suspicious Keywords

found_keywords = []

for word in suspicious_keywords:

    if word in domain:

        found_keywords.append(word)

if found_keywords:

    risk_score += 20

    reasons.append(
        "Suspicious keywords: "
        + ", ".join(found_keywords)
    )

# Raw IP Address Detection

parts = domain.split(".")

if len(parts) == 4:

    if all(part.isdigit() for part in parts):

        risk_score += 30

        reasons.append("Raw IP address detected")

# Final Classification

if risk_score >= 60:

    level = "HIGH"

elif risk_score >= 30:

    level = "MEDIUM"

else:

    level = "LOW"

print("\nURL Analysis Report")
print("-" * 40)

print("Domain:", domain)

print("Risk Score:", risk_score)

print("Risk Level:", level)

print("\nReasons:")

if reasons:

    for reason in reasons:

        print("-", reason)

else:

    print("- No suspicious indicators detected")

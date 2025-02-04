import re

def evaluate_password(password):
    score = 0
    recommendations = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        recommendations.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        recommendations.append("Password should include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        recommendations.append("Password should include at least one digit.")

    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        recommendations.append("Password should include at least one special character (@, $, !, %, *, ?, &).")

    # Strength assessment
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, recommendations

# Example usage
password = input("Enter a password to evaluate: ")
strength, recommendations = evaluate_password(password)
print(f"Password Strength: {strength}")
if recommendations:
    print("Recommendations:")
    for rec in recommendations:
        print(f" - {rec}")

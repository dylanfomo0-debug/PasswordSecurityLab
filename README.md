# Password Attack Simulation Study

An educational project exploring the fundamentals of password attacks, human vulnerability, and the mechanics of modern authentication security.

## Overview
This project demonstrates common password attack methodologies—Brute Force, Dictionary Attacks, and Password Spraying—to illustrate how attackers exploit human behavior and computational patterns to compromise accounts.

## How It Works
The simulation includes:
1. **Brute Force**: Exhaustive search of all character combinations.
2. **Dictionary Attack**: Targeted search using a curated list of likely passwords.
3. **Password Spraying**: Horizontal attack testing one common password across many accounts to avoid lockouts.

## Tech Stack
- **Language**: Python 3
- **Libraries**: `hashlib` (for SHA-256 hashing simulation)

## Project Structure
```
.
├── src/
│   └── simulate_attacks.py  # Main simulation script
└── README.md                # Documentation and theory
```

## How to Run
```bash
cd src
python3 simulate_attacks.py
```

## Background Theory

### Brute Force Attacks
Brute force attacks rely on exhaustive search rather than strategy. They systematically attempt every possible combination of characters using automated scripts and bots. While success is guaranteed over time, it becomes exponentially more expensive as password length and complexity increase.

### Dictionary Attacks
A refined form of brute force that substitutes exhaustive search with a curated list of likely candidates. Instead of all combinations, attackers use pre-built lists of common words, phrases, and patterns. This is significantly more efficient because it targets predictable human behavior.

### Password Spraying
Shifts the attack surface from one account to many. It tries one common password across a large number of accounts before cycling to the next. This avoids triggering account lockout mechanisms, which are typically activated by repeated failures on a single account.

### The Human Factor — Password Psychology
- **Convenience vs. Security**: Users consistently choose convenience, leading to simple, predictable passwords.
- **Password Reuse**: Enables credential stuffing, where breached credentials from one service are tested against others.
- **Cognitive Limits**: Humans struggle to retain strong, unique passwords across multiple services without assistance.

### Password Storage and Hashing
Modern systems store hashed versions of passwords rather than plain text. Hashing is a one-way transformation. However, attackers can still perform dictionary or brute force attacks against these hashes. Without **salting**, identical passwords produce identical hashes, facilitating large-scale attacks.

### Defensive Measures
- **Rate Limiting & Lockouts**: Slow down attacks but can be bypassed via distributed IPs.
- **Multi-Factor Authentication (MFA)**: Adds a critical second layer of defense.
- **Password Managers**: Help users manage unique, complex passwords.
- **Passkeys**: Remove the password vulnerability at its root by using cryptographic keys.

## References
- LastPass, The Psychology of Passwords
- Cloudflare, What is Credential Stuffing?
- Cloudflare, What is a Brute Force Attack?
- Kaspersky, Password Attacks Explained
- NIST, Special Publication 800-63B: Digital Identity Guidelines

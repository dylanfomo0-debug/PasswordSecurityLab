from __future__ import annotations
import hashlib
import itertools
import string

TARGETS = [
    ("short_random", "kqvz"),
    ("human_pattern", "Password123!"),
    ("long_phrase", "blue-orbit-lantern-river"),
    ("common_word", "qwerty"),
    ("mixed_random", "a7Q!m2Z@"),
]
DICTIONARY = ["password", "password123", "qwerty", "welcome", "admin", "letmein", "blue-orbit-lantern-river"]

def digest(value): return hashlib.sha256(value.encode()).hexdigest()

def dictionary_attack(target_hash):
    for attempts, guess in enumerate(DICTIONARY, 1):
        if digest(guess) == target_hash: return attempts
    return None

def pattern_attack(target_hash):
    guesses = [f"{word}{n}{suffix}" for word in ("Password", "password", "Welcome") for n in ("123", "2026") for suffix in ("", "!")]
    for attempts, guess in enumerate(guesses, 1):
        if digest(guess) == target_hash: return attempts
    return None

def bounded_bruteforce(target_hash, max_length=4):
    attempts = 0
    for length in range(1, max_length + 1):
        for chars in itertools.product(string.ascii_lowercase, repeat=length):
            attempts += 1
            if digest("".join(chars)) == target_hash: return attempts
    return None

def run():
    results = []
    for category, password in TARGETS:
        h = digest(password)
        results.append({"category": category, "dictionary": dictionary_attack(h), "pattern": pattern_attack(h), "bruteforce_4": bounded_bruteforce(h)})
    return results

def main():
    print("Category          Dictionary  Pattern  Brute-force(<=4)")
    print("-" * 60)
    for row in run(): print(f"{row['category']:<17} {str(row['dictionary']):<11} {str(row['pattern']):<8} {row['bruteforce_4']}")
    print("\nA blank result means the strategy did not find the synthetic target within its stated limit.")

if __name__ == "__main__": main()

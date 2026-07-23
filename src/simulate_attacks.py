import hashlib
import time
import random
import string

# Mock database of hashed passwords
# In a real scenario, these would be stored in a DB
user_db = {
    "admin": hashlib.sha256("password123".encode()).hexdigest(),
    "user1": hashlib.sha256("qwerty".encode()).hexdigest(),
    "user2": hashlib.sha256("letmein1".encode()).hexdigest(),
    "dev": hashlib.sha256("supersecret".encode()).hexdigest()
}

def brute_force_simulation(target_user, max_length=4):
    """Simulates a brute force attack by trying all combinations up to max_length."""
    print(f"\n[!] Starting Brute Force Attack on user: {target_user}")
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()
    
    # This is a simplified simulation for demonstration
    # In reality, this would use nested loops or recursion
    target_hash = user_db.get(target_user)
    
    # For simulation, we'll just show the concept
    for length in range(1, max_length + 1):
        # We'll skip the actual full iteration to keep it fast for the demo
        # but simulate the logic
        attempts += len(chars) ** length
        if attempts > 10000: break 

    end_time = time.time()
    print(f"[-] Simulated {attempts} combinations.")
    print(f"[-] Time taken: {end_time - start_time:.4f} seconds")

def dictionary_attack_simulation(target_user, dictionary):
    """Simulates a dictionary attack using a list of common passwords."""
    print(f"\n[!] Starting Dictionary Attack on user: {target_user}")
    target_hash = user_db.get(target_user)
    start_time = time.time()
    
    for word in dictionary:
        word_hash = hashlib.sha256(word.encode()).hexdigest()
        if word_hash == target_hash:
            print(f"[+] Success! Password found: {word}")
            break
    
    end_time = time.time()
    print(f"[-] Time taken: {end_time - start_time:.4f} seconds")

def password_spraying_simulation(users, common_password):
    """Simulates password spraying by trying one password across multiple accounts."""
    print(f"\n[!] Starting Password Spraying Attack with password: '{common_password}'")
    start_time = time.time()
    
    successes = []
    for user in users:
        target_hash = user_db.get(user)
        if hashlib.sha256(common_password.encode()).hexdigest() == target_hash:
            successes.append(user)
    
    if successes:
        print(f"[+] Success! Found matches for users: {', '.join(successes)}")
    else:
        print("[-] No matches found.")
        
    end_time = time.time()
    print(f"[-] Time taken: {end_time - start_time:.4f} seconds")

def main():
    # Common passwords for dictionary and spraying
    common_passwords = ["123456", "password", "password123", "qwerty", "admin", "welcome"]
    
    # 1. Brute Force
    brute_force_simulation("admin", max_length=3)
    
    # 2. Dictionary Attack
    dictionary_attack_simulation("user1", common_passwords)
    
    # 3. Password Spraying
    password_spraying_simulation(list(user_db.keys()), "password123")

if __name__ == "__main__":
    main()

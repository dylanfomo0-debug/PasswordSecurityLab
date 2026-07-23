import hashlib
import time
import csv
import itertools
import string
import os

class PasswordAttackExperiment:
    def __init__(self, users_file, dictionary_file):
        self.users = self.load_users(users_file)
        self.dictionary = self.load_dictionary(dictionary_file)
        self.results = []

    def load_users(self, file_path):
        users = []
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['Hash'] = hashlib.sha256(row['Password'].encode()).hexdigest()
                users.append(row)
        return users

    def load_dictionary(self, file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def dictionary_attack(self):
        print("[!] Starting Dictionary Attack...")
        for user in self.users:
            attempts = 0
            start_time = time.time()
            success = False
            found_password = None
            
            for word in self.dictionary:
                attempts += 1
                if hashlib.sha256(word.encode()).hexdigest() == user['Hash']:
                    success = True
                    found_password = word
                    break
            
            end_time = time.time()
            self.results.append({
                "User": user['User'],
                "Attack": "Dictionary",
                "Success": "Yes" if success else "No",
                "Attempts": attempts,
                "Time": round(end_time - start_time, 6),
                "Password_Length": len(user['Password']),
                "Difficulty": user['Difficulty']
            })

    def brute_force_attack(self, max_length=4):
        print(f"[!] Starting Brute Force Attack (max length {max_length})...")
        chars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
        
        for user in self.users:
            # Skip if already found by dictionary to save time in experiment, 
            # or run anyway for comparison? Let's run for comparison but limit length.
            attempts = 0
            start_time = time.time()
            success = False
            
            # Real brute force generation
            found = False
            for length in range(1, max_length + 1):
                if found: break
                for guess in itertools.product(chars, repeat=length):
                    attempts += 1
                    guess_str = "".join(guess)
                    if hashlib.sha256(guess_str.encode()).hexdigest() == user['Hash']:
                        success = True
                        found = True
                        break
                    if attempts > 500000: # Safety break for experiment speed
                        break
            
            end_time = time.time()
            self.results.append({
                "User": user['User'],
                "Attack": "Brute Force",
                "Success": "Yes" if success else "No",
                "Attempts": attempts,
                "Time": round(end_time - start_time, 6),
                "Password_Length": len(user['Password']),
                "Difficulty": user['Difficulty']
            })

    def password_spraying(self):
        print("[!] Starting Password Spraying...")
        test_passwords = ["password123", "123456", "welcome", "admin", "qwerty"]
        
        for pwd in test_passwords:
            attempts = 0
            start_time = time.time()
            compromised_users = []
            
            for user in self.users:
                attempts += 1
                if hashlib.sha256(pwd.encode()).hexdigest() == user['Hash']:
                    compromised_users.append(user['User'])
            
            end_time = time.time()
            # Record result per spray attempt
            self.results.append({
                "User": "MULTIPLE",
                "Attack": f"Spraying ({pwd})",
                "Success": "Yes" if compromised_users else "No",
                "Attempts": attempts,
                "Time": round(end_time - start_time, 6),
                "Compromised": len(compromised_users),
                "Details": ", ".join(compromised_users)
            })

    def export_results(self, output_file):
        if not self.results: return
        # Get all unique keys across all result dictionaries
        keys = set()
        for r in self.results:
            keys.update(r.keys())
        
        with open(output_file, 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=sorted(list(keys)))
            dict_writer.writeheader()
            dict_writer.writerows(self.results)
        print(f"[+] Results exported to {output_file}")

    def generate_report(self):
        print("\n" + "="*40)
        print("         PASSWORD ATTACK REPORT")
        print("="*40)
        
        attacks = ["Dictionary", "Brute Force"]
        for attack_type in attacks:
            data = [r for r in self.results if r['Attack'] == attack_type]
            if not data: continue
            
            successes = [r for r in data if r['Success'] == "Yes"]
            success_rate = (len(successes) / len(data)) * 100
            avg_attempts = sum(r['Attempts'] for r in data) / len(data)
            avg_time = sum(r['Time'] for r in data) / len(data)
            
            print(f"\n{attack_type} Attack")
            print(f"Success Rate:     {success_rate:.1f}%")
            print(f"Average Attempts: {avg_attempts:,.0f}")
            print(f"Average Time:     {avg_time:.4f}s")
            print("-" * 30)
            
        sprays = [r for r in self.results if "Spraying" in r['Attack']]
        if sprays:
            total_compromised = sum(r.get('Compromised', 0) for r in sprays)
            print(f"\nPassword Spraying")
            print(f"Passwords Tested:     {len(sprays)}")
            print(f"Accounts Compromised: {total_compromised}")
        
        print("\n" + "="*40)

if __name__ == "__main__":
    # Ensure directories exist
    os.makedirs("../data", exist_ok=True)
    
    experiment = PasswordAttackExperiment("../data/users.csv", "../data/common_passwords.txt")
    experiment.dictionary_attack()
    experiment.brute_force_attack(max_length=4)
    experiment.password_spraying()
    experiment.export_results("../data/results.csv")
    experiment.generate_report()

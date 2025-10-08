import itertools
import string
import os
import random
import threading
import time
from datetime import datetime
import webbrowser
import json

class DarkBoss1BDUltimateGenerator:
    def __init__(self):
        self.brand_name = "darkboss1bd"
        self.version = "v3.0"
        self.author = "Dark Boss"
        self.telegram_id = "https://t.me/darkvaiadmin"
        self.telegram_channel = "https://t.me/windowspremiumkey"
        self.output_folder = "DarkBoss_Generated_Lists"
        self.config_file = "generator_config.json"
        self.setup_environment()
        
    def setup_environment(self):
        """Create necessary folders and display banner"""
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        self.load_config()
        self.display_banner()
        
    def load_config(self):
        """Load or create configuration file"""
        self.config = {
            "max_passwords_per_file": 1000000,
            "chunk_size": 50000,
            "auto_save_interval": 10000
        }
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    self.config.update(json.load(f))
            except:
                pass
        
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
        
    def display_banner(self):
        """Display professional hacker-style banner"""
        banner = f"""
\033[92m
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    ██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗██████╗ ███████╗║
║    ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝██╔══██╗██╔════╝║
║    ██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║  ███╗███████╗██████╔╝███████╗║
║    ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║╚════██║██╔══██╗╚════██║║
║    ██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝╚██████╔╝███████║██║  ██║███████║║
║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝║
║                                                                              ║
║              [ {self.brand_name.upper()} - ULTIMATE PASSWORD & USERNAME GENERATOR ]         ║
║                             Version: {self.version}                                 ║
║                         Author: {self.author}                              ║
║                                                                              ║
║         Telegram: {self.telegram_id}           ║
║         Channel:  {self.telegram_channel}            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
\033[0m
"""
        print(banner)
        
    def open_links(self):
        """Automatically open Telegram links when script runs"""
        try:
            webbrowser.open(self.telegram_id)
            webbrowser.open(self.telegram_channel)
            print("\033[94m[*] Opening Telegram links...\033[0m")
            time.sleep(2)
        except Exception as e:
            print(f"\033[91m[!] Error opening links: {e}\033[0m")

    def generate_unlimited_passwords(self, pattern_type="comprehensive", min_length=4, max_length=16, 
                                   custom_chars=None, output_size=1000000):
        """Generate unlimited passwords with various patterns"""
        print(f"\033[93m[*] Generating {output_size} passwords...\033[0m")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/unlimited_passwords_{timestamp}.txt"
        
        characters = self.get_character_set(pattern_type, custom_chars)
        
        if not characters:
            print("\033[91m[!] No character set available!\033[0m")
            return
        
        generated_count = 0
        chunk_count = 0
        
        with open(filename, 'w', encoding='utf-8') as f:
            while generated_count < output_size:
                # Generate passwords of random lengths
                length = random.randint(min_length, max_length)
                password = ''.join(random.choice(characters) for _ in range(length))
                f.write(password + '\n')
                generated_count += 1
                
                # Progress reporting
                if generated_count % 10000 == 0:
                    print(f"\033[94m[*] Generated {generated_count} passwords...\033[0m")
                
                # Save in chunks to prevent memory issues
                if generated_count % self.config['chunk_size'] == 0:
                    f.flush()
                    chunk_count += 1
                    print(f"\033[96m[*] Saved chunk {chunk_count}...\033[0m")
        
        print(f"\033[92m[+] Unlimited password list saved: {filename}\033[0m")
        print(f"\033[92m[+] Total passwords generated: {generated_count}\033[0m")
        return filename

    def get_character_set(self, pattern_type, custom_chars):
        """Get character set based on pattern type"""
        if custom_chars:
            return custom_chars
        
        char_sets = {
            "comprehensive": string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?",
            "alphanumeric": string.ascii_letters + string.digits,
            "lowercase": string.ascii_lowercase + string.digits,
            "uppercase": string.ascii_uppercase + string.digits,
            "digits_only": string.digits,
            "special_chars": string.ascii_letters + "!@#$%^&*()_+-=[]{}|;:,.<>?",
            "hexadecimal": string.hexdigits.lower(),
            "binary": "01"
        }
        
        return char_sets.get(pattern_type, char_sets["comprehensive"])

    def generate_username_list(self, username_type="mixed", quantity=100000, min_length=3, max_length=12):
        """Generate unlimited username lists"""
        print(f"\033[93m[*] Generating {quantity} usernames...\033[0m")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/usernames_{timestamp}.txt"
        
        first_names = ["john", "jane", "alex", "mike", "sarah", "david", "lisa", "robert", 
                      "emma", "admin", "user", "test", "demo", "guest", "root", "support"]
        
        last_names = ["smith", "johnson", "williams", "brown", "jones", "miller", "davis",
                     "garcia", "rodriguez", "wilson", "anderson", "thomas", "taylor"]
        
        companies = ["tech", "corp", "inc", "ltd", "company", "enterprise", "global", "digital"]
        
        domains = ["gmail", "yahoo", "hotmail", "outlook", "proton", "aol"]
        
        generated_count = 0
        
        with open(filename, 'w', encoding='utf-8') as f:
            while generated_count < quantity:
                username = self.generate_single_username(username_type, first_names, last_names, companies, domains, min_length, max_length)
                if username:
                    f.write(username + '\n')
                    generated_count += 1
                    
                    if generated_count % 10000 == 0:
                        print(f"\033[94m[*] Generated {generated_count} usernames...\033[0m")
        
        print(f"\033[92m[+] Username list saved: {filename}\033[0m")
        print(f"\033[92m[+] Total usernames generated: {generated_count}\033[0m")
        return filename

    def generate_single_username(self, username_type, first_names, last_names, companies, domains, min_length, max_length):
        """Generate a single username based on type"""
        if username_type == "first_last":
            return random.choice(first_names) + random.choice(last_names) + str(random.randint(1, 999))
        
        elif username_type == "first_dot_last":
            return random.choice(first_names) + "." + random.choice(last_names) + str(random.randint(1, 99))
        
        elif username_type == "company_based":
            return random.choice(companies) + str(random.randint(1, 999)) + random.choice(domains)
        
        elif username_type == "random_mixed":
            patterns = [
                lambda: random.choice(first_names) + str(random.randint(100, 9999)),
                lambda: random.choice(last_names) + random.choice(first_names)[:2],
                lambda: random.choice(domains) + str(random.randint(10, 999)),
                lambda: random.choice(companies) + random.choice(last_names),
                lambda: "user" + str(random.randint(1000, 99999)),
                lambda: "admin" + str(random.randint(100, 9999)),
                lambda: random.choice(first_names) + "_" + random.choice(last_names)
            ]
            return random.choice(patterns)()
        
        elif username_type == "professional":
            return random.choice(first_names)[0] + random.choice(last_names) + str(random.randint(1, 999))
        
        else:  # mixed - default
            types = ["first_last", "first_dot_last", "company_based", "random_mixed", "professional"]
            return self.generate_single_username(random.choice(types), first_names, last_names, companies, domains, min_length, max_length)

    def generate_combo_list(self, username_quantity=50000, password_quantity=50000):
        """Generate username:password combination lists"""
        print(f"\033[93m[*] Generating combo list ({username_quantity} usernames : {password_quantity} passwords)...\033[0m")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/combo_list_{timestamp}.txt"
        
        # Generate usernames and passwords
        usernames = set()
        passwords = set()
        
        # Generate usernames
        while len(usernames) < username_quantity:
            username = self.generate_single_username("mixed", 
                ["john", "jane", "alex", "mike", "sarah", "admin", "user", "test"],
                ["smith", "johnson", "brown", "davis", "wilson", "admin", "user"],
                ["tech", "corp", "inc", "company"],
                ["gmail", "yahoo", "hotmail"],
                4, 10
            )
            if username and len(username) >= 3:
                usernames.add(username)
        
        # Generate passwords
        characters = self.get_character_set("comprehensive", None)
        while len(passwords) < password_quantity:
            length = random.randint(6, 12)
            password = ''.join(random.choice(characters) for _ in range(length))
            passwords.add(password)
        
        # Write combinations
        with open(filename, 'w', encoding='utf-8') as f:
            for username in list(usernames)[:min(username_quantity, len(usernames))]:
                password = random.choice(list(passwords))
                f.write(f"{username}:{password}\n")
        
        print(f"\033[92m[+] Combo list saved: {filename}\033[0m")
        return filename

    def generate_pattern_based_passwords(self, base_words, variations=100000):
        """Generate passwords based on patterns and base words"""
        print(f"\033[93m[*] Generating {variations} pattern-based passwords...\033[0m")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/pattern_passwords_{timestamp}.txt"
        
        patterns = [
            lambda w: w + str(random.randint(1, 9999)),
            lambda w: w + "!" + str(random.randint(1, 99)),
            lambda w: w + "@" + str(random.randint(2020, 2025)),
            lambda w: str(random.randint(1, 99)) + w,
            lambda w: w.upper() + str(random.randint(1, 999)),
            lambda w: w.capitalize() + "!" + str(random.randint(1, 9)),
            lambda w: w + "_" + str(random.randint(100, 999)),
            lambda w: w + "#" + str(random.randint(1, 999)),
            lambda w: w + random.choice(["123", "321", "007", "111", "999"]),
            lambda w: w + random.choice(["!", "@", "#", "$", "&"]) + str(random.randint(1, 99))
        ]
        
        generated = set()
        
        with open(filename, 'w', encoding='utf-8') as f:
            while len(generated) < variations:
                word = random.choice(base_words)
                pattern = random.choice(patterns)
                password = pattern(word)
                
                if password not in generated:
                    f.write(password + '\n')
                    generated.add(password)
                
                if len(generated) % 10000 == 0:
                    print(f"\033[94m[*] Generated {len(generated)} pattern passwords...\033[0m")
        
        print(f"\033[92m[+] Pattern-based passwords saved: {filename}\033[0m")
        return filename

    def bulk_generator(self, list_type="both", total_items=1000000):
        """Generate massive lists of passwords, usernames, or both"""
        print(f"\033[93m[*] Starting bulk generation of {total_items} items...\033[0m")
        
        if list_type == "passwords" or list_type == "both":
            self.generate_unlimited_passwords(output_size=total_items // 2 if list_type == "both" else total_items)
        
        if list_type == "usernames" or list_type == "both":
            self.generate_username_list(quantity=total_items // 2 if list_type == "both" else total_items)
        
        if list_type == "combo":
            self.generate_combo_list(total_items // 2, total_items // 2)
        
        print(f"\033[92m[+] Bulk generation completed!\033[0m")

    def show_statistics(self):
        """Show statistics about generated files"""
        if not os.path.exists(self.output_folder):
            print("\033[91m[!] No generated files found!\033[0m")
            return
        
        files = os.listdir(self.output_folder)
        if not files:
            print("\033[91m[!] No files in output folder!\033[0m")
            return
        
        print(f"\033[96m\n╔══════════════════════════════════════════════════╗")
        print(f"║                 GENERATION STATISTICS               ║")
        print(f"╠══════════════════════════════════════════════════╣\033[0m")
        
        total_files = 0
        total_lines = 0
        
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(self.output_folder, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = sum(1 for _ in f)
                    print(f"\033[96m║ {file[:40]:<40} {lines:>8,} lines \033[96m║\033[0m")
                    total_files += 1
                    total_lines += lines
                except:
                    continue
        
        print(f"\033[96m╠══════════════════════════════════════════════════╣")
        print(f"║ Total Files: {total_files:>30} ║")
        print(f"║ Total Items: {total_lines:>30,} ║")
        print(f"╚══════════════════════════════════════════════════╝\033[0m")

    def show_menu(self):
        """Display main menu"""
        menu = """
\033[96m
╔══════════════════════════════════════════════════════════════╗
║               ULTIMATE GENERATOR MENU - darkboss1bd          ║
╠══════════════════════════════════════════════════════════════╣
║  1. 🔐 Unlimited Password List Generator                    ║
║  2. 👤 Unlimited Username List Generator                    ║
║  3. 🔗 Username:Password Combo List                         ║
║  4. 🎯 Pattern-Based Password Generator                     ║
║  5. 💥 Bulk Mass Generator (All Types)                      ║
║  6. 📊 Show Generation Statistics                           ║
║  7. ⚙️  Configuration Settings                              ║
║  8. 🚪 Exit                                                 ║
╚══════════════════════════════════════════════════════════════╝
\033[0m
"""
        print(menu)

    def configuration_menu(self):
        """Display configuration menu"""
        config_menu = """
\033[95m
╔══════════════════════════════════════════════════════════════╗
║                     CONFIGURATION SETTINGS                   ║
╠══════════════════════════════════════════════════════════════╣
║  1. Max Passwords Per File: {:<30} ║
║  2. Chunk Size: {:<37} ║
║  3. Auto Save Interval: {:<34} ║
║  4. Back to Main Menu                                        ║
╚══════════════════════════════════════════════════════════════╝
\033[0m
""".format(self.config['max_passwords_per_file'], 
          self.config['chunk_size'], 
          self.config['auto_save_interval'])
        print(config_menu)

    def run(self):
        """Main execution function"""
        # Open links automatically
        link_thread = threading.Thread(target=self.open_links)
        link_thread.daemon = True
        link_thread.start()
        
        while True:
            self.show_menu()
            choice = input("\033[95m[?] Select option (1-8): \033[0m").strip()
            
            if choice == '1':
                print("\033[93m[*] Unlimited Password Generator\033[0m")
                pattern_type = input("[?] Pattern type (comprehensive/alphanumeric/lowercase/uppercase/special_chars): ") or "comprehensive"
                min_len = int(input("[?] Min length (4): ") or 4)
                max_len = int(input("[?] Max length (16): ") or 16)
                quantity = int(input("[?] How many passwords? (100000): ") or 100000)
                self.generate_unlimited_passwords(pattern_type, min_len, max_len, None, quantity)
                
            elif choice == '2':
                print("\033[93m[*] Unlimited Username Generator\033[0m")
                username_type = input("[?] Username type (mixed/first_last/first_dot_last/company_based/professional): ") or "mixed"
                quantity = int(input("[?] How many usernames? (50000): ") or 50000)
                min_len = int(input("[?] Min length (3): ") or 3)
                max_len = int(input("[?] Max length (12): ") or 12)
                self.generate_username_list(username_type, quantity, min_len, max_len)
                
            elif choice == '3':
                print("\033[93m[*] Combo List Generator\033[0m")
                quantity = int(input("[?] How many combinations? (50000): ") or 50000)
                self.generate_combo_list(quantity, quantity)
                
            elif choice == '4':
                print("\033[93m[*] Pattern-Based Password Generator\033[0m")
                words_input = input("[?] Enter base words (comma separated): ")
                base_words = [word.strip() for word in words_input.split(',')] if words_input else ["password", "admin", "user", "test"]
                quantity = int(input("[?] How many variations? (100000): ") or 100000)
                self.generate_pattern_based_passwords(base_words, quantity)
                
            elif choice == '5':
                print("\033[93m[*] Bulk Mass Generator\033[0m")
                list_type = input("[?] Generate (passwords/usernames/both/combo): ") or "both"
                total_items = int(input("[?] Total items to generate (1000000): ") or 1000000)
                self.bulk_generator(list_type, total_items)
                
            elif choice == '6':
                self.show_statistics()
                
            elif choice == '7':
                self.configuration_menu()
                config_choice = input("\033[95m[?] Select config option (1-4): \033[0m")
                if config_choice == '1':
                    new_val = int(input("[?] New max passwords per file: ") or 1000000)
                    self.config['max_passwords_per_file'] = new_val
                elif config_choice == '2':
                    new_val = int(input("[?] New chunk size: ") or 50000)
                    self.config['chunk_size'] = new_val
                elif config_choice == '3':
                    new_val = int(input("[?] New auto save interval: ") or 10000)
                    self.config['auto_save_interval'] = new_val
                self.save_config()
                print("\033[92m[+] Configuration updated!\033[0m")
                
            elif choice == '8':
                print("\033[92m[+] Thank you for using darkboss1bd Ultimate Generator!\033[0m")
                print(f"\033[94m[*] Contact: {self.telegram_id}\033[0m")
                break
                
            else:
                print("\033[91m[!] Invalid choice! Please select 1-8\033[0m")
            
            input("\n\033[95m[Press Enter to continue...]\033[0m")

if __name__ == "__main__":
    try:
        generator = DarkBoss1BDUltimateGenerator()
        generator.run()
    except KeyboardInterrupt:
        print("\n\033[91m[!] Program interrupted by user\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Error: {e}\033[0m")

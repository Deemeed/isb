import pyinputplus as pyip
import easygui
import json
from cryptosistem.cryptosistem import CryptoSistem
from cryptosistem.filework import readfile


def main():
    settings = readfile("settings.json", "r")
    print(settings)
    crypto = CryptoSistem(settings["key_length"])

    while True:
        print("\n=== Hybrid CryptoSystem ===")
        choice = pyip.inputMenu([
            "1. Generate keys",
            "2. Encrypt data",
            "3. Decrypt data",
            "4. Change key length",
            "5. Load custom settings",
            "6. Exit"
        ], numbered=True)

        if choice == "1. Generate keys":
            crypto.generate_hybrid_keys(
                settings["symmetric_key"],
                settings["public_key"],
                settings["private_key"]
            )
            print("Keys generated successfully!")

        elif choice == "2. Encrypt data":
            crypto.encrypt_data(
                settings["plain_text"],
                settings["private_key"],
                settings["symmetric_key"],
                settings["encrypted_text"]
            )
            print("Data encrypted successfully!")

        elif choice == "3. Decrypt data":
            crypto.decrypt_data(
                settings["encrypted_text"],
                settings["private_key"],
                settings["symmetric_key"],
                settings["decrypted_text"]
            )
            print("Data decrypted successfully!")

        elif choice == "4. Change key length":
            new_length = pyip.inputMenu(["128", "192", "256"],
                                        prompt="Select new key length:\n",
                                        numbered=True)
            settings["key_length"] = int(new_length)
            crypto = CryptoSistem(settings["key_length"])
            print(f"Key length changed to: {new_length} bits")

        elif choice == "5. Load custom settings":
            custom_settings = easygui.fileopenbox("Select settings file", default="*.json")
            if custom_settings:
                try:
                    with open(custom_settings) as f:
                        new_settings = json.load(f)
                        settings.update(new_settings)
                        crypto = CryptoSistem(settings["key_length"])
                except Exception as e:
                    print(f"Error loading settings: {e}")

        elif choice == "6. Exit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
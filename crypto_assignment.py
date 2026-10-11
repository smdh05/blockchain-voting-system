import hashlib
import rsa

def generate_hash(message):
    # Generates a SHA-256 hash of the input string
    return hashlib.sha256(message.encode()).hexdigest()

def main():
    vehicles = {} # Dictionary to store vehicle records

    while True:
        print("\n--- Cryptography & Blockchain Fundamentals ---")
        print("1. Generate SHA-256 Hash")
        print("2. Digital Signature (Sign & Verify)")
        print("3. Register Vehicle")
        print("4. Retrieve Vehicle Details")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            message = input("Enter the message to hash: ")
            hash_result = generate_hash(message)
            print(f"\nSHA-256 Hash:\n{hash_result}")
            
        elif choice == '2':
            # Generate public and private keys (512-bit for speed in this simple app)
            print("\nGenerating Public/Private key pair...")
            public_key, private_key = rsa.newkeys(512)
            print("Keys generated successfully!")
            
            message = input("Enter the message to sign: ")
            
            # Sign the message with the private key
            signature = rsa.sign(message.encode(), private_key, 'SHA-256')
            print("\nMessage signed using Private Key.")
            
            # Verify the message with the public key
            try:
                print("Verifying signature using Public Key...")
                rsa.verify(message.encode(), signature, public_key)
                print("Result: ✅ Signature is VALID and authentic.")
            except rsa.VerificationError:
                print("Result: ❌ Signature is INVALID or tampered.")
                
        elif choice == '3':
            number_plate = input("Enter Vehicle Number Plate: ").strip().upper()
            
            # Input validation: No duplicate plates allowed
            if number_plate in vehicles:
                print("Error: Duplicate Car Number Plate. This vehicle is already registered.")
            else:
                owner = input("Enter Owner Name: ")
                model = input("Enter Vehicle Model: ")
                
                # Store in dictionary
                vehicles[number_plate] = {
                    "owner": owner,
                    "model": model
                }
                print(f"Vehicle '{number_plate}' registered successfully!")
                
        elif choice == '4':
            number_plate = input("Enter Vehicle Number Plate to search: ").strip().upper()
            
            if number_plate in vehicles:
                vehicle_data = vehicles[number_plate]
                print(f"\n--- Details for {number_plate} ---")
                print(f"Owner Name: {vehicle_data['owner']}")
                print(f"Vehicle Model: {vehicle_data['model']}")
                print("------------------------------")
            else:
                print("Error: Vehicle Number Plate not found.")
                
        elif choice == '5':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
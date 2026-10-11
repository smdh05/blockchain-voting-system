import hashlib

# --- Entities ---
class Voter:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False

class Candidate:
    def __init__(self, candidate_id, name):
        self.candidate_id = candidate_id
        self.name = name

class Block:
    def __init__(self, index, transaction, previous_hash):
        self.index = index
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combine block data to create a unique hash
        block_string = f"{self.index}{self.transaction}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
        
    def create_genesis_block(self):
        # The first block in the chain has no previous hash
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)
        
    def add_block(self, transaction):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transaction, previous_block.hash)
        self.chain.append(new_block)
        
    def validate_chain(self):
        # Loop through the chain to ensure no hashes have been tampered with
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's hash is accurate
            if current_block.hash != current_block.calculate_hash():
                return False
            # Check if it properly links to the previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# --- Main Console Application ---
def main():
    blockchain = Blockchain()
    voters = {}
    candidates = {}

    while True:
        # Display the menu loop
        print("\n--- Voting Management System ---")
        print("1. Add Candidate")
        print("2. Add Voter")
        print("3. Cast Vote")
        print("4. Print Blockchain")
        print("5. Validate Chain")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            c_id = input("Enter Candidate ID: ")
            if c_id in candidates:
                print("Error: Candidate ID already exists.") # Validation: No duplicate candidate IDs
            else:
                name = input("Enter Candidate Name: ")
                candidates[c_id] = Candidate(c_id, name)
                print("Candidate added successfully!")
                
        elif choice == '2':
            v_id = input("Enter Voter ID: ")
            if v_id in voters:
                print("Error: Voter ID already exists.") # Validation: No duplicate voter IDs
            else:
                name = input("Enter Voter Name: ")
                voters[v_id] = Voter(v_id, name)
                print("Voter added successfully!")
                
        elif choice == '3':
            v_id = input("Enter Voter ID: ")
            c_id = input("Enter Candidate ID: ")
            
            if v_id not in voters:
                print("Error: Voter not found.")
            elif voters[v_id].has_voted:
                print("Error: Voter has already cast their vote.") # Validation: No double-voting
            elif c_id not in candidates:
                print("Error: Candidate not found.")
            else:
                # Valid vote process
                voters[v_id].has_voted = True
                transaction = f"Voter '{v_id}' voted for Candidate '{c_id}'"
                blockchain.add_block(transaction)
                print("Vote cast successfully!")
                
        elif choice == '4':
            print("\n--- Blockchain Contents ---")
            for block in blockchain.chain:
                print(f"Index: {block.index}")
                print(f"Transaction: {block.transaction}")
                print(f"Previous Hash: {block.previous_hash}")
                print(f"Hash: {block.hash}")
                print("-" * 30)
                
        elif choice == '5':
            if blockchain.validate_chain():
                print("Blockchain is VALID.")
            else:
                print("Blockchain is COMPROMISED!")
                
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
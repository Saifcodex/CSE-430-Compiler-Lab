class SymbolInfo:
    def __init__(self, name, type_, size, dimension, line, address):
        self.name = name
        self.type = type_
        self.size = size
        self.dimension = dimension
        self.line = line
        self.address = address
        self.next = None  

class SymbolTable:
    def __init__(self, max_size=10):
        self.MAX = max_size
        self.table = [None] * self.MAX

    def getHashKey(self, name):
        return sum(ord(ch) for ch in name) % self.MAX

    def insert(self, name, type_, size, dimension, line, address):
        key = self.getHashKey(name)
        head = self.table[key]

        current = head
        while current:
            if current.name == name:
                print(f"[Error] '{name}' already exists in the symbol table.")
                return
            current = current.next
            
        new_symbol = SymbolInfo(name, type_, size, dimension, line, address)
        new_symbol.next = head
        self.table[key] = new_symbol
        print(f"[OK] Inserted '{name}' into symbol table.")

    def search(self, name):
        key = self.getHashKey(name)
        current = self.table[key]
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def delete(self, name):
        key = self.getHashKey(name)
        current = self.table[key]
        prev = None

        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.table[key] = current.next
                print(f"[OK] '{name}' deleted from symbol table.")
                return
            prev = current
            current = current.next

        print(f"[Error] '{name}' not found for deletion.")

    def update(self, name, type_=None, size=None, dimension=None, line=None, address=None):
        symbol = self.search(name)
        if not symbol:
            print(f"[Error] '{name}' not found for update.")
            return

        if type_ is not None:
            symbol.type = type_
        if size is not None:
            symbol.size = size
        if dimension is not None:
            symbol.dimension = dimension
        if line is not None:
            symbol.line = line
        if address is not None:
            symbol.address = address

        print(f"[OK] '{name}' updated.")

    def show(self):
        print(f"{'Bucket':<7} {'Name':<10} {'Type':<10} {'Size':<6} {'Dim':<5} {'Line':<6} {'Address'}")
        print("-" * 60)
        for i, head in enumerate(self.table):
            current = head
            while current:
                print(f"{i:<7} {current.name:<10} {current.type:<10} {current.size:<6} {current.dimension:<5} {current.line:<6} {current.address}")
                current = current.next


def main():
    st = SymbolTable(max_size=10)

    while True:
        print("\nSymbol Table Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Update")
        print("5. Show All")
        print("6. Exit")
        choice = input("Choose ▶ ")

        if choice == "1":
            name = input("Enter name: ")
            type_ = input("Enter type: ")
            size = input("Enter size: ")
            dimension = input("Enter dimension: ")
            line = input("Enter line number: ")
            address = input("Enter address: ")
            st.insert(name, type_, size, dimension, line, address)

        elif choice == "2":
            name = input("Enter name to search: ")
            symbol = st.search(name)
            if symbol:
                print(f"Found: {symbol.name}, {symbol.type}, {symbol.size}, {symbol.dimension}, {symbol.line}, {symbol.address}")
            else:
                print(f"[Error] '{name}' not found.")

        elif choice == "3":
            name = input("Enter name to delete: ")
            st.delete(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            type_ = input("New type (leave empty to skip): ") or None
            size = input("New size (leave empty to skip): ") or None
            dimension = input("New dimension (leave empty to skip): ") or None
            line = input("New line (leave empty to skip): ") or None
            address = input("New address (leave empty to skip): ") or None
            st.update(name, type_, size, dimension, line, address)

        elif choice == "5":
            st.show()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("[Error] Invalid choice.")


if __name__ == "__main__":
    main()

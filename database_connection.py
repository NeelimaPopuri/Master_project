class DatabaseConnection:
    """Simulating a database connection with context management."""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        """Establish the connection."""
        self.connected = True
        print(f"Connected to the database '{self.db_name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the connection."""
        self.connected = False
        print(f"Disconnected from the database'{self.db_name}'.")
        # Handle any exceptions
        if exc_type:
            print(f"An Exception occured: {exc_value}")
            return True  # Suppresses excetions if they occur


with DatabaseConnection("ExampleDB") as db:
    print(f"Is connected? {db.connected}")

from .database import Database
from .github_storage import GitHubStorage
import hashlib
import os
import pandas as pd

class Auth:
    def __init__(self):
        self.db = Database()
        self.github_storage = GitHubStorage()
        self.users_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "users.csv")
        self._initialize_files()

    def _initialize_files(self):
        """Initialize necessary files if they don't exist"""
        data_dir = os.path.dirname(self.users_file)
        os.makedirs(data_dir, exist_ok=True)

        if not os.path.exists(self.users_file):
            df = pd.DataFrame(columns=['username', 'password', 'name', 'email'])
            df.to_csv(self.users_file, index=False)

    def _hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def login_user(self, username, password):
        """Authenticate user login"""
        try:
            # Input validation
            if not username or not password:
                return False, "Username and password are required"

            # Get user data from GitHub first
            try:
                github_users = self.github_storage.get_users_data()
                if github_users is not None:
                    users_df = github_users
                else:
                    users_df = pd.read_csv(self.users_file)
            except Exception:
                # Fallback to local file if GitHub fails
                users_df = pd.read_csv(self.users_file)

            # Check if user exists
            user = users_df[users_df['username'] == username]
            if user.empty:
                return False, "Invalid username or password"

            # Verify password
            hashed_password = self._hash_password(password)
            if user.iloc[0]['password'] != hashed_password:
                return False, "Invalid username or password"

            return True, "Login successful"

        except Exception as e:
            print(f"Login error: {str(e)}")
            return False, f"Login failed: {str(e)}"

    def register_user(self, username, password, name, email):
        """Register a new user"""
        try:
            # Input validation
            if not all([username, password, name, email]):
                return False, "All fields are required"
            
            # Check if user exists
            if self._user_exists(username):
                return False, "Username already exists"
            
            # Hash password
            hashed_password = self._hash_password(password)
            
            # Save locally first
            success_local = self.db.save_user(username, hashed_password, name, email)
            if not success_local:
                return False, "Failed to save user locally"
            
            # Try to save to GitHub
            try:
                success_github = self.github_storage.update_users_csv(
                    username, hashed_password, name, email
                )
                if not success_github:
                    print("Warning: Failed to save user to GitHub")
            except Exception as e:
                print(f"GitHub storage error: {str(e)}")
                # Continue even if GitHub save fails
                
            return True, "Registration successful"
            
        except Exception as e:
            print(f"Registration error: {str(e)}")
            return False, f"Registration failed: {str(e)}"

    def _user_exists(self, username):
        """Check if a user exists"""
        try:
            users_df = pd.read_csv(self.users_file)
            return username in users_df['username'].values
        except Exception:
            return False
import os
import pandas as pd
from datetime import datetime
from .github_storage import GitHubStorage

class Database:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.data_dir = os.path.join(self.base_dir, "data")
        
        # Define file paths
        self.users_file = os.path.join(self.data_dir, "users.csv")
        self.progress_file = os.path.join(self.data_dir, "progress.csv")
        self.stats_file = os.path.join(self.data_dir, "stats.csv")
        
        # Initialize database
        self._initialize_database()
        self.github_storage = GitHubStorage()

    def _initialize_database(self):
        """Create necessary directories and files"""
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Initialize users.csv
        if not os.path.exists(self.users_file):
            pd.DataFrame(columns=[
                'username', 'password', 'name', 'email'
            ]).to_csv(self.users_file, index=False)

    def save_user(self, username, hashed_password, name, email):
        """Save new user to database"""
        try:
            # Create DataFrame for new user
            new_user = pd.DataFrame({
                'username': [username],
                'password': [hashed_password],
                'name': [name],
                'email': [email]
            })
            
            # Check if users.csv exists and read it
            if os.path.exists(self.users_file):
                users_df = pd.read_csv(self.users_file)
                
                # Check if username already exists
                if username in users_df['username'].values:
                    print(f"Username {username} already exists")
                    return False
                    
                # Append new user
                users_df = pd.concat([users_df, new_user], ignore_index=True)
            else:
                users_df = new_user
            
            # Save to CSV
            users_df.to_csv(self.users_file, index=False)
            print(f"User {username} saved successfully")
            return True
            
        except Exception as e:
            print(f"Error saving user: {str(e)}")
            return False
import pandas as pd
import os
import json
from datetime import datetime

class Database:
    def __init__(self):
        """Initialize database with required files and directories"""
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.data_dir = os.path.join(self.base_dir, "data")
        
        # Define file paths
        self.users_file = os.path.join(self.data_dir, "users.csv")
        self.progress_file = os.path.join(self.data_dir, "progress.csv")
        self.stats_file = os.path.join(self.data_dir, "stats.csv")
        
        # Initialize database
        self._initialize_database()

    def _initialize_database(self):
        """Create necessary directories and files"""
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Initialize users.csv
        if not os.path.exists(self.users_file):
            pd.DataFrame(columns=[
                'username', 'password', 'name', 'email', 
                'created_at', 'last_login'
            ]).to_csv(self.users_file, index=False)
        
        # Initialize progress.csv
        if not os.path.exists(self.progress_file):
            pd.DataFrame(columns=[
                'username', 'feature', 'data', 'timestamp'
            ]).to_csv(self.progress_file, index=False)
        
        # Initialize stats.csv
        if not os.path.exists(self.stats_file):
            pd.DataFrame(columns=[
                'username', 'eco_score', 'carbon_saved', 
                'water_saved', 'energy_reduced', 'timestamp'
            ]).to_csv(self.stats_file, index=False)

    def save_user_progress(self, username, feature, data):
        """Save user progress for a specific feature"""
        try:
            progress_df = pd.read_csv(self.progress_file)
            new_progress = pd.DataFrame({
                'username': [username],
                'feature': [feature],
                'data': [json.dumps(data)],
                'timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            })
            progress_df = pd.concat([progress_df, new_progress], ignore_index=True)
            progress_df.to_csv(self.progress_file, index=False)
            return True
        except Exception as e:
            print(f"Error saving progress: {e}")
            return False

    def get_user_progress(self, username, feature=None):
        """Get user progress, optionally filtered by feature"""
        try:
            progress_df = pd.read_csv(self.progress_file)
            user_progress = progress_df[progress_df['username'] == username]
            
            if feature:
                user_progress = user_progress[user_progress['feature'] == feature]
            
            # Convert stored JSON strings back to dictionaries
            user_progress['data'] = user_progress['data'].apply(json.loads)
            return user_progress
        except Exception as e:
            print(f"Error retrieving progress: {e}")
            return pd.DataFrame()

    def update_user_stats(self, username, stats):
        """Update user statistics"""
        try:
            stats_df = pd.read_csv(self.stats_file)
            new_stats = pd.DataFrame({
                'username': [username],
                'eco_score': [stats.get('eco_score', 0)],
                'carbon_saved': [stats.get('carbon_saved', 0)],
                'water_saved': [stats.get('water_saved', 0)],
                'energy_reduced': [stats.get('energy_reduced', 0)],
                'timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            })
            stats_df = pd.concat([stats_df, new_stats], ignore_index=True)
            stats_df.to_csv(self.stats_file, index=False)
            return True
        except Exception as e:
            print(f"Error updating stats: {e}")
            return False

    def get_user_stats(self, username):
        """Get latest user statistics"""
        try:
            stats_df = pd.read_csv(self.stats_file)
            user_stats = stats_df[stats_df['username'] == username]
            if not user_stats.empty:
                return user_stats.iloc[-1].to_dict()
            return None
        except Exception as e:
            print(f"Error retrieving stats: {e}")
            return None

    def get_leaderboard(self, metric='eco_score', limit=10):
        """Get leaderboard for a specific metric"""
        try:
            stats_df = pd.read_csv(self.stats_file)
            latest_stats = stats_df.sort_values('timestamp').groupby('username').last()
            return latest_stats.nlargest(limit, metric)[metric].to_dict()
        except Exception as e:
            print(f"Error retrieving leaderboard: {e}")
            return {}
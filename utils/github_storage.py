import os
import pandas as pd
import io
from github import Github
import base64
from datetime import datetime
import streamlit as st

class GitHubStorage:
    def __init__(self):
        # GitHub personal access token
        self.token = "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"  # Replace with your token
        
        try:
            self.g = Github(self.token)
            self.g.get_user().login
            self.repo = self.g.get_repo("JwalPatel/IDAI107-2013409-Jwal-Patel-XYZ-Hemer-Pandya")
        except Exception as e:
            print(f"GitHub Authentication Error: {e}")
            self.g = None
            self.repo = None

    def update_csv_file(self, file_path, new_data, commit_message):
        """Generic method to update any CSV file in the repository"""
        if not self.repo:
            print("GitHub storage not initialized. Using local storage only.")
            return False
            
        try:
            # Get current file content
            file = self.repo.get_contents(file_path)
            content = base64.b64decode(file.content).decode()
            
            # Read existing CSV
            df = pd.read_csv(io.StringIO(content))
            
            # Append new data
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            
            # Convert back to CSV
            new_content = df.to_csv(index=False)
            
            # Update file in repository
            self.repo.update_file(
                path=file_path,
                message=commit_message,
                content=new_content,
                sha=file.sha
            )
            return True
        except Exception as e:
            print(f"Error updating GitHub file: {e}")
            return False

    def update_users_csv(self, username, hashed_password, name, email):
        """Update users.csv"""
        new_user = {
            'username': username,
            'password': hashed_password,
            'name': name,
            'email': email
        }
        return self.update_csv_file(
            "data/users.csv",
            new_user,
            f"Add new user: {username}"
        )

    def update_progress_csv(self, username, feature, data, timestamp):
        """Update progress.csv"""
        new_progress = {
            'username': username,
            'feature': feature,
            'data': data,
            'timestamp': timestamp
        }
        return self.update_csv_file(
            "data/progress.csv",
            new_progress,
            f"Update progress for {username} in {feature}"
        )

    def update_stats_csv(self, username, eco_score, carbon_saved, water_saved, energy_reduced):
        """Update stats.csv"""
        new_stats = {
            'username': username,
            'eco_score': eco_score,
            'carbon_saved': carbon_saved,
            'water_saved': water_saved,
            'energy_reduced': energy_reduced,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return self.update_csv_file(
            "data/stats.csv",
            new_stats,
            f"Update stats for {username}"
        )

    def update_eco_metrics_csv(self, username, eco_score, carbon_saved, water_saved, energy_saved):
        """Update eco_metrics.csv"""
        new_metrics = {
            'username': username,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'eco_score': eco_score,
            'carbon_saved': carbon_saved,
            'water_saved': water_saved,
            'energy_saved': energy_saved
        }
        return self.update_csv_file(
            "data/eco_metrics.csv",
            new_metrics,
            f"Update eco metrics for {username}"
        )
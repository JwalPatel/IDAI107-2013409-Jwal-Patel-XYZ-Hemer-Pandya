def _initialize_csv_files(self):
    """Initialize all required CSV files with their headers"""
    csv_files = {
        'users.csv': ['username', 'password', 'name', 'email'],
        'stats.csv': ['username', 'eco_score', 'carbon_saved', 'water_saved', 'energy_reduced', 'timestamp'],
        'progress.csv': ['username', 'feature', 'data', 'timestamp'],
        'transportation_data.csv': ['username', 'timestamp', 'data'],
        'energy_data.csv': ['username', 'timestamp', 'data'],
        'water_data.csv': ['username', 'timestamp', 'data'],
        'food_data.csv': ['username', 'timestamp', 'data'],
        'waste_data.csv': ['username', 'timestamp', 'data'],
        'eco_metrics.csv': ['username', 'timestamp', 'eco_score', 'carbon_saved', 'water_saved', 'energy_saved']
    }
    
    for filename, headers in csv_files.items():
        filepath = os.path.join(self.data_dir, filename)
        if not os.path.exists(filepath):
            df = pd.DataFrame(columns=headers)
            df.to_csv(filepath, index=False)

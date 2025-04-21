# EcoWise Living Platform 🌍

## Project Title and Description
**EcoWise Living** (also referred to as "Eco Action") is a comprehensive web application designed to help users track, measure, and improve their environmental impact. The platform enables individuals to make more sustainable choices across multiple domains of daily life by providing personalized insights, progress tracking, and actionable recommendations.

**Project Objectives:**
- Raise awareness about individual environmental impact
- Provide tools to measure and reduce carbon footprint
- Encourage sustainable habits through progress tracking
- Offer personalized recommendations for eco-friendly living

## Features
- **User Authentication System**
  - Secure user registration and login
  - User profile management
  - Progress tracking across sessions

- **Interactive Dashboard**
  - Consolidated view of sustainability metrics
  - Progress visualization across all domains
  - Key performance indicators (Eco Score, Carbon Saved, Water Saved, Energy Reduced)

- **Multi-domain Sustainability Tracking**
  - **Transportation Module:** 
    - Track commute methods and distances
    - Calculate carbon emissions from various travel modes
    - Set and monitor sustainable transportation goals
  
  - **Energy Module:**
    - Monitor household energy consumption
    - Identify energy-saving opportunities
    - Track renewable energy usage
  
  - **Water Module:**
    - Log water consumption habits
    - Receive water conservation tips
    - Visualize water usage patterns
  
  - **Food Module:**
    - Track dietary choices and their environmental impact
    - Calculate food miles and associated emissions
    - Suggestions for more sustainable food options
  
  - **Waste Module:**
    - Monitor waste generation
    - Track recycling efforts
    - Tips for waste reduction

- **Progress Metrics and Gamification**
  - Feature completion tracking
  - Achievement milestones
  - Visual progress indicators

## Technologies Used

### Frontend
- **Streamlit** - Python-based web application framework for creating interactive dashboards
- **HTML/CSS** - For custom styling and enhanced UI elements

### Backend
- **Python** - Core programming language
- **Streamlit** - Serving as both frontend and backend framework

### Data Processing & Analysis
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing and data processing
- **Scikit-learn** - Machine learning algorithms for predictions and recommendations

### Data Visualization
- **Matplotlib** - Static, animated, and interactive visualizations
- **Plotly** - Interactive graphs and charts
- **Plotly Express** - High-level interface for Plotly
- **Seaborn** - Statistical data visualization

### AI Integration
- **Google Generative AI** - For personalized recommendations and insights

### Other Libraries
- **Pillow** - Image processing capabilities
- **python-dotenv** - Environment variable management
- **requests** - HTTP requests handling

## Installation Instructions

### Prerequisites
- Python 3.9 or higher
- Git (for cloning the repository)
- Internet connection (for API access)

### Step 1: Clone the Repository
```bash
git clone https://github.com/JwalPatel/IDAI107-2013409-Jwal-Patel-XYZ-Hemer-Pandya.git
cd IDAI107-2013409-Jwal-Patel-XYZ-Hemer-Pandya
```

### Step 2: Set Up Virtual Environment (Recommended)
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory with any necessary API keys:
```
# Example:
GOOGLE_API_KEY=your_api_key_here
```

### Step 5: Run the Application
```bash
streamlit run main.py
```
The application should now be running at `http://localhost:8501`

## Usage Instructions

### 1. Getting Started
- Create a new account via the "Create Account" button on the login page
- Fill in your details (username, password, name, email)
- Login with your credentials

### 2. Navigation
- Use the sidebar menu to navigate between different modules:
  - Dashboard (home screen)
  - Transportation
  - Energy
  - Water
  - Food
  - Waste

### 3. Dashboard Usage
- View your overall sustainability metrics
- Check progress across all features
- See improvements over time in eco score, carbon savings, etc.

### 4. Using Individual Modules
- **Transportation:**
  - Log your daily commutes and travel methods
  - Set sustainable transportation goals
  - View your transportation carbon footprint

- **Energy:**
  - Input your energy consumption data
  - Get recommendations for reducing energy usage
  - Track progress in energy efficiency

- **Water:**
  - Record water usage activities
  - Receive water-saving tips
  - Monitor improvements in water conservation

- **Food:**
  - Track your diet's environmental impact
  - Get suggestions for more sustainable food choices
  - Learn about local and seasonal options

- **Waste:**
  - Log waste generation and recycling efforts
  - Get personalized waste reduction strategies
  - Track progress toward zero-waste goals

### 5. Logging Out
- Click the "Logout" button in the sidebar when finished

## Contribution Guidelines

We welcome contributions to improve the EcoWise Living Platform! Here's how you can contribute:

### 1. Fork the Repository
Create your own fork of the project on GitHub.

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Commit Your Changes
```bash
git commit -am 'Add some feature or improvement'
```

### 4. Push to the Branch
```bash
git push origin feature/your-feature-name
```

### 5. Submit a Pull Request
- Go to the original repository on GitHub
- Click on "New Pull Request"
- Select your feature branch from your forked repository
- Submit the pull request with a clear description of the changes

### Coding Guidelines
- Follow PEP 8 style guidelines for Python code
- Include comments for complex logic
- Write tests for new features when applicable
- Ensure the application runs without errors

## Screenshots/Demos

### Login Screen
![Login Screen](https://via.placeholder.com/800x450?text=EcoWise+Login+Screen)

### Main Dashboard
![Dashboard](https://via.placeholder.com/800x450?text=EcoWise+Dashboard)

### Transportation Module
![Transportation Module](https://via.placeholder.com/800x450?text=Transportation+Module)

### Energy Tracking
![Energy Module](https://via.placeholder.com/800x450?text=Energy+Tracking+Interface)

### Water Conservation
![Water Module](https://via.placeholder.com/800x450?text=Water+Conservation+Tracking)

*Note: Replace these placeholder images with actual screenshots of your application.*

## Acknowledgments

- **Course IDAI107** for providing the project framework and requirements
- **Jwal Patel and Hemer Pandya** for the development and implementation of this platform
- **Streamlit Community** for the excellent documentation and examples
- **Open-source libraries** used in this project for making development more efficient
- All the **testers and early users** who provided valuable feedback during development

## Live Demo
Experience the EcoWise Living Platform: [Live Application](https://idai107-2013409-jwal-patel-xyz-hemer-pandya-mbm6cxjya8dudcqnfa.streamlit.app/)

## Contact Information
- **GitHub Repository**: [https://github.com/JwalPatel/IDAI107-2013409-Jwal-Patel-XYZ-Hemer-Pandya](https://github.com/JwalPatel/IDAI107-2013409-Jwal-Patel-XYZ-Hemer-Pandya)
- **Developer**: Jwal Patel - [GitHub Profile](https://github.com/JwalPatel)

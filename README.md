# LinkedIn Job Filter & Automator

This Python project automates the job application process on LinkedIn by filtering job posts based on user preferences and automatically applying for relevant positions. It logs into the user's LinkedIn account, navigates to the job postings, filters them according to specified criteria, fills out job application forms, attaches the resume, and submits the applications. 

## Features

- **LinkedIn Automation**: Automates the job application process on LinkedIn.
- **Login Authentication**: Logs into the user's LinkedIn account securely.
- **Job Post Filtering**: Filters job posts based on user-defined criteria such as location, industry, experience level, etc.
- **Job Application Automation**: Automatically fills out job application forms with user-provided information.
- **Resume Attachment**: Attaches the user's resume to job applications.
- **Error Handling**: Handles errors gracefully and provides informative error messages.

## Technologies Used

- **Python Libraries**:
  - `selenium` for web automation
  - `BeautifulSoup` for web scraping (optional)
  - `requests` for making HTTP requests (optional)
- **Web Automation Tools**:
  - `WebDriver` for browser automation (e.g., Chrome WebDriver, GeckoDriver for Firefox)
- **LinkedIn API (Optional)**:
  - Utilizes LinkedIn's API for accessing job postings and submitting applications (if available).

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/linkedin-job-filter.git`
2. Navigate to the project directory: `cd linkedin-job-filter`
3. Install dependencies: `pip install -r requirements.txt`
4. Download the appropriate WebDriver for your preferred browser and ensure it is added to your system's PATH.
5. Optionally, sign up for LinkedIn's API and obtain necessary credentials if available.

## Usage

1. Configure the program by providing your LinkedIn login credentials, job preferences, and other necessary information.
2. Run the main Python script: `python main.py`.
3. The program will log into your LinkedIn account, navigate to the job postings, and apply filters based on your preferences.
4. It will automatically apply for relevant job positions, fill out application forms, attach your resume, and submit applications.
5. Monitor the program's output for any errors or status updates.



# Simple Login Web Application

This is a basic Flask application that demonstrates a simple login functionality. It includes a login form where users can enter their username and password.

## Getting Started

### Prerequisites

- Python 3.12
- Chrome browser (for automated testing)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/dveersingh/automated_test_script.git
   
#### Install the required Python packages:

            pip install Flask selenium

2.  Download and install ChromeDriver (ensure it's in your system's PATH).


# Usage
1.  Run the Flask application:
       
        python app.py
 
###### The application will start and be accessible at http://localhost:5000.

2.  Open a browser and navigate to http://localhost:5000 to access the login page.
3.  Use the following credentials for login:

- Username: admin
- Password: admin


## Automated Testing
###### Automated testing for the login process has been implemented using Selenium. To run the automated test:
        python test_login.py
Make sure you have ChromeDriver installed and in your system's PATH.

# Expedia Flight Search Automation

This project automates the process of searching for flights on Expedia using Selenium WebDriver. It interacts with the web page to change regional settings, select flight options, and capture screenshots at various stages, making the flight booking process faster and more efficient.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)
- [Screenshots](#screenshots)
- [Log Output](#log-output)
- [License](#license)

## Features

- Automatically changes language and region settings to "India" and "English".
- Searches for one-way flights from Kolkata to Hyderabad.
- Selects a specific departure date.
- Allows specification of the number of travelers.
- Captures screenshots of key steps in the process.
- Logs actions and errors for clear output.

## Requirements

- Python 3.x
- Selenium package
- Chrome WebDriver
- Google Chrome browser
- An internet connection

## Setup

1. **Install Python**: Ensure Python is installed on your machine. Download from [python.org](https://www.python.org/downloads/).

2. **Install Selenium**: Install the Selenium package via pip:
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**: Download the appropriate ChromeDriver version for your version of Chrome from [ChromeDriver](https://chromedriver.chromium.org/downloads).

4. **Set Up Chrome Profile**: Create a custom directory for your Chrome profile. Update the path in the script accordingly.

## Usage

1. Clone the repository or create a Python file and copy the provided scripts into it.
2. Update the ChromeDriver path and custom directory in the script to match your environment.
3. Run the main script to execute the automation:
   ```bash
   python expediaComFlightAutomation.py
   ```

## Project Structure

```
chromedriver-64/
customDir/
2.region_changed.png
3.flight_tab.png
4.one_way.png
5.depart_city.png
6.dest_city.png
7.date_selection.png
8.travellers.png
9.first_flight.png
10.flight_selected.png
create_custom_directory.py
expediaComFlightAutomation.py
output.txt
README.md
```

- **chromedriver-64/**: Contains the ChromeDriver executable.
- **customDir/**: Directory for custom Chrome profile data.
- **Screenshots**: Captured images from various steps of the flight search process.
- **create_custom_directory.py**: Script for initializing Chrome with a custom profile directory.
- **expediaComFlightAutomation.py**: Main script to automate the flight search process.
- **output.txt**: File which logs actions and errors during execution.
- **README.md**: Documentation for the project.

## Code Explanation

### Functionality Overview

- **Automation Setup**: Initializes the Chrome WebDriver with user profile settings.
- **Web Interactions**: Automates clicks and data entries for flight selection on the Expedia website.
- **Error Handling**: Robust logging of actions helps trace any issues during execution.

## Screenshots

The script captures screenshots at critical steps, allowing users to visually confirm actions taken during the automation process.

## Log Output

At the end of the execution, a log file named `output.txt` is created, containing all logged messages for review.

## License

This project is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for details.

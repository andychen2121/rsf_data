
# RSF Occupancy Tracker

## Overview

This repository hosts the RSF Occupancy Tracker, a project designed to collect and monitor occupancy data from the University of California, Berkeley's Recreational Sports Facility (RSF). The goal is to provide users with current and historical data on how full the gym is at various times, aiding in planning visits to the facility. The data collection is automated through a combination of Beautiful Soup 4 (BS4), Selenium with Chromedriver (version 122.0.6261.94), and a scheduled cron job to run every 5 minutes.

## Features

- **Authentication Token Scraping**: Utilizes BS4 and Selenium for navigating and extracting occupancy data from the RSF's official website in `scrape.py`. Look for _"Authorization": Bearer shr__
- **Automated Data Collection**: A cron job schedules `main.py` to run every 5 minutes, ensuring up-to-date occupancy information.
- **Data Storage**: Occupancy data is stored and updated in a CSV file (`rsf_data.csv`), facilitating easy access and analysis.

## Requirements

- Python 3.6+
- Beautiful Soup 4
- Selenium
- Chromedriver (version 122.0.6261.94)
- Requests (for sending HTTP requests in `main.py`)

## Usage

1. **Configure Chromedriver**

   Ensure that Chromedriver (version 122.0.6261.94) is installed and its path is correctly set in `scrape.py`.

2. **Set up Environment Variables**

   Create a .env file with the following parameters:
   - AUTH_KEY= Scraped authorization key for CURL requests
   - EXECUTABLE_PATH= Local Chromedriver path
   - DATA_PATH= Data CSV path

4. **Run the Scraper**

   ```bash
   python scrape.py
   ```

   This script retrieves the necessary auth key and triggers `main.py` to send a request for occupancy data.

5. **Automate Data Collection with Cron**

   Edit your crontab to run `main.py` every 5 minutes:

   ```bash
   crontab -e
   ```

   Add the following line:

   ```bash
   */5 8-23 * * * /path/to/python3 /path/to/rsf-occupancy-tracker/main.py
   ```

   Replace `/path/to/python3` and `/path/to/rsf-occupancy-tracker/main.py` with the appropriate paths on your system. This Cron instruction updates data every 5 minutes during the RSF's hours of operations.

## Contributing

Interested in contributing? Great! Please contact `andychen2121 at berkeley dot edu` for access and further instructions.

## Disclaimer

This project is not affiliated with, endorsed by, or sponsored by UC Berkeley or any of its affiliates. Use this tool responsibly and in accordance with the RSF's website terms and conditions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

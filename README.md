# INEC Polling Unit Data Scraper

This repository contains a Selenium-based web scraper for polling unit data from the [INEC Nigeria Website](https://www.inecnigeria.org/?page_id=2526). The scraper collects polling unit details for **Lagos State**(this can be chnaged within the script) and saves them into a CSV file for easy analysis.

## Features

- Automatically navigates to the INEC polling unit page.
- Selects **Lagos** as the state and iterates through all Local Government Areas (LGAs) and wards.
- Retrieves polling unit data, including:
  - Polling Unit ID
  - Polling Unit Name
  - Remarks
  - Ward
  - LGA
- Saves the data into a CSV file.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- Browser-specific WebDriver (e.g., GeckoDriver for Firefox)

### Install Required Libraries

You can install the required libraries using pip:

```bash
pip install selenium

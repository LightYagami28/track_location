# Phone Number Tracker

A simple Python application that allows users to track the location and carrier of a phone number using the `phonenumbers`, `opencage`, and `folium` libraries. The application provides an interactive map displaying the location associated with the entered phone number.

## Features

- Parse and validate phone numbers.
- Retrieve the country and carrier information.
- Display the location on an interactive map.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)

## Installation

To install the required packages, run the following command in your terminal:

```bash
pip install phonenumbers opencage folium
```

## Usage

1. Clone the repository or download the source code.
2. Replace the placeholder in the code with your OpenCage API key.
3. Run the application:

```bash
python your_script_name.py
```

4. Enter a phone number in the input field and click the search button.
5. The application will display the country and carrier information, and generate a map showing the location associated with the phone number.
6. Click the "Location" button to open the generated map in your web browser.

## Screenshots

![Phone Number Tracker](search.png)  
## Acknowledgments

- [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) - Library for parsing, formatting, and validating phone numbers.
- [OpenCage Geocoder](https://opencagedata.com/) - Geocoding API for converting location names into geographic coordinates.
- [Folium](https://python-visualization.github.io/folium/) - Library for creating interactive maps.
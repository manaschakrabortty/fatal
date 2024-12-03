
#Currency Converter in Python 🏦💱
This project is a real-time currency converter built using Python with Tkinter for GUI, Requests for fetching data, and BeautifulSoup for web scraping.

Features ✨
   Simple User Interface with intuitive design.
   Supports popular currencies like USD, INR, EUR, and more.
   Real-time currency conversion using exchange rates fetched online.
   Reset and Exit functionalities for convenience.
   Displays current date automatically.
Prerequisites 🛠️
  Make sure you have the following libraries installed:

> tkinter
> requests
> bs4 (BeautifulSoup)
You can install any missing libraries with:
  pip install requests beautifulsoup4

How It Works 🤔
  Select the base currency (e.g., USD) and the target currency (e.g., INR).
  Enter the amount in the input field.
  Click Convert Currency to see the converted value.
  Use the Reset button to clear all fields.
  Exit the application using the Exit button.

Created with Tkinter:
    >Frames to organize sections.
    >Entry, Labels, and Buttons for input/output and actions.
    >Scales to visually represent amounts.
    >Key Functions:

  value_converted(): Fetches the exchange rate and calculates the converted value.
  reset_all(): Resets all inputs and outputs.
  exit_window(): Closes the application safely.


How to Run ▶️
Copy the code into a Python file, e.g., currency_converter.py.
Run the file:
  python currency_converter.py

Use the GUI to perform real-time currency conversions.

Limitations 🚧
    Internet connection is required for fetching exchange rates.
    Exchange rates are dependent on the source website and may not update instantly.

Option Pricing Model using Black-Scholes
This project involves implementing an Option Pricing Model using the Black-Scholes formula. The model is applied to real market data to estimate option prices and analyze their deviations from the theoretical values.

Project Overview
The goal of this project is to:

Implement the Black-Scholes formula for option pricing.
Read and process market data from CSV files.
Calculate the theoretical price of options using the Black-Scholes formula.
Compare these calculated prices with actual market prices to assess accuracy.
Perform analysis on deviations and generate visualizations to understand pricing discrepancies.
Features
Black-Scholes Calculation: Implements the Black-Scholes formula to calculate the theoretical price of call options.
Data Processing: Reads market data from CSV files, processes the data, and prepares it for analysis.
Deviation Analysis: Compares the calculated Black-Scholes price with actual market prices and analyzes the standard deviation.
Visualization: Plots the deviation of calculated prices from actual prices to visually analyze the model's performance.
Project Structure
bs.py: The main Python script containing the implementation of the Black-Scholes option pricing model, data processing functions, and analysis methods.
Input Files: The project expects market data in CSV format with specific columns that the script reads and processes.
Dependencies
Python 3.x
Required Libraries:
csv
datetime
math
scipy
matplotlib
You can install the required libraries using pip:

sh
Copy code
pip install scipy matplotlib
Usage
Prepare Input Data: Ensure your CSV files are formatted correctly. The script processes the following columns:

Symbol: The stock symbol.
Strike Price: The strike price of the option.
Expiration Date: The expiration date of the option.
Underlying Price: The current price of the underlying asset.
Option Prices: A series of option prices.
Run the Script: Execute the bs.py script to perform the option pricing calculation and analysis.

sh
Copy code
python bs.py
Analyze Results: The script outputs the standard deviation of the calculated prices from actual prices and visualizes the deviation using scatter plots.

Example
The script is designed to work with multiple CSV files. The provided example includes four files: NIFTY 15500 JAN-MAR.csv, NIFTY 15000 JAN-MAR.csv, NIFTY 14500 JAN-MAR.csv, NIFTY 14000 JAN-MAR.csv. Modify the file_list variable to include your own data files.

Conclusion
This project serves as a basic implementation of the Black-Scholes option pricing model and provides insights into the performance of the model when applied to real-world market data. The analysis and visualizations help understand the discrepancies between theoretical and actual market prices, aiding in better financial decision-making.

License
This project is licensed under the MIT License - see the LICENSE file for details.


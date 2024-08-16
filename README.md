# Option Pricing Model using Black-Scholes

This project involves implementing an Option Pricing Model using the Black-Scholes formula. The model is applied to real market data to estimate option prices and analyze their deviations from the theoretical values.

## Project Overview

The goal of this project is to:
- Implement the Black-Scholes formula for option pricing.
- Read and process market data from CSV files.
- Calculate the theoretical price of options using the Black-Scholes formula.
- Compare these calculated prices with actual market prices to assess accuracy.
- Perform analysis on deviations and generate visualizations to understand pricing discrepancies.

## Features

- **Black-Scholes Calculation**: Implements the Black-Scholes formula to calculate the theoretical price of call options.
- **Data Processing**: Reads market data from CSV files, processes the data, and prepares it for analysis.
- **Deviation Analysis**: Compares the calculated Black-Scholes price with actual market prices and analyzes the standard deviation.
- **Visualization**: Plots the deviation of calculated prices from actual prices to visually analyze the model's performance.

## Project Structure

- `bs.py`: The main Python script containing the implementation of the Black-Scholes option pricing model, data processing functions, and analysis methods.
- **Input Files**: The project expects market data in CSV format with specific columns that the script reads and processes.

## Dependencies

- Python 3.x
- Required Libraries:
  - `csv`
  - `datetime`
  - `math`
  - `scipy`
  - `matplotlib`

You can install the required libraries using pip:
```sh
pip install scipy matplotlib

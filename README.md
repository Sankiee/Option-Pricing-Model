# Option Pricing Models using Black-Scholes

## 1. Importing Required Libraries
The script starts by importing the necessary Python libraries:

- **`csv`**: To read the market data from CSV files.
- **`datetime`**: To handle date differences for calculating time to expiration.
- **`math`**: For mathematical functions like exponentiation, logarithms, and square roots.
- **`scipy.stats`**: To calculate the cumulative distribution function (CDF) for a standard normal distribution.
- **`matplotlib.pyplot`**: For plotting and visualizing the results.

## 2. Defining Constants and Global Variables
The script defines some key constants:

- **`root2pi`**: The square root of \(2\pi\), used in the normal distribution function.
- **`r`**: The risk-free interest rate, set to 3%.
- **`v`**: The volatility of the underlying asset, set to 18%.

## 3. Black-Scholes Call Option Pricing Function
The function `bs_ce(s, k, t)` calculates the theoretical price of a call option using the Black-Scholes formula:

- **Inputs**:
  - `s`: Current stock price (underlying asset).
  - `k`: Strike price of the option.
  - `t`: Time to expiration (in years).
- **Outputs**:
  - `c`: The calculated price of the call option.

## 4. Helper Functions
- **`normal(x)`**: Computes the normal distribution probability density function.
- **`date_diff(date1, date2)`**: Calculates the difference in days between two dates provided in the format `DD-MMM-YYYY`.

## 5. Reading and Processing Data
The function `read(file)` reads a CSV file and processes the data to extract relevant information for option pricing:

- The function skips rows with missing data or low volume.
- It calculates the time to expiration in days, converts it to years, and computes the option price using the Black-Scholes formula.
- The processed data is stored for further analysis.

## 6. Analyzing the Data
The function `analysis(data)` performs statistical analysis on the processed data:

- It calculates the standard deviation of the deviations between the Black-Scholes calculated prices and the market prices.
- It distinguishes between options that are out-of-the-money (OTM) and in-the-money (ITM).
- The function also tracks the maximum deviation observed.

## 7. Visualization
The script uses `matplotlib` to scatter plot the deviations for each option. This helps in visually assessing the accuracy of the Black-Scholes model.

## 8. Main Execution
The script processes multiple CSV files, performs the analysis for each, and prints the results:

- **`file_list`**: A list of CSV filenames that the script will process.
- The script outputs the standard deviation of deviations for all options, OTM options, and ITM options, along with the maximum deviation.

## 9. Results Interpretation
The printed results and scatter plots provide insight into:

- The overall accuracy of the Black-Scholes model for the given market data.
- The model's performance for OTM and ITM options separately.
- The most significant deviations where the model might have under- or over-estimated the option prices.

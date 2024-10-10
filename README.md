

# Statistical Analysis of Stock Price and Risk

This project performs various statistical tests and analyses on stock price returns for a selection of tech companies: **Apple (AAPL)**, **Microsoft (MSFT)**, **Google (GOOGL)**, **Amazon (AMZN)**, and **Meta (META)**. The code uses financial data from Yahoo Finance and applies statistical methods such as t-tests, correlation, F-tests, ANOVA, ARCH tests, and ADF tests to evaluate relationships, variances, and volatility in stock returns.

## Project Overview

This project:
1. Downloads historical stock data for several companies.
2. Computes daily returns for each stock.
3. Applies statistical tests to understand return distributions, relationships, and volatility patterns.
4. Visualizes the results using matplotlib and seaborn for deeper insights.

### Steps Implemented:
1. **Data Collection** using `yfinance`.
2. **Mean and Variance Testing** with t-tests.
3. **Correlation, F-test, ANOVA, ARCH, and ADF** statistical tests.
4. **Visualization** of stock returns, correlation heatmap, volatility, and stationarity checks.

---

## Table of Contents

- [Installation](#installation)
- [Data Collection](#data-collection)
- [Statistical Tests](#statistical-tests)
  - [One-Sample t-test](#one-sample-t-test)
  - [Pearson Correlation](#pearson-correlation)
  - [F-test](#f-test)
  - [ANOVA](#anova)
  - [ARCH Test](#arch-test)
  - [ADF Test](#adf-test)
- [Visualization](#visualization)
- [Results Interpretation](#results-interpretation)
- [Conclusion](#conclusion)
- [License](#license)

---

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your_username/stock-statistical-analysis.git
   cd stock-statistical-analysis
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include:
   - `yfinance`
   - `pandas`
   - `scipy`
   - `matplotlib`
   - `seaborn`
   - `statsmodels`

---

## Data Collection

The historical stock data is collected from Yahoo Finance using the `yfinance` package. We analyze five major tech companies:
- **Apple (AAPL)**
- **Microsoft (MSFT)**
- **Google (GOOGL)**
- **Amazon (AMZN)**
- **Meta (META)**

```python
import yfinance as yf

# Download stock data
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
df = yf.download(stocks, start='2015-01-01', end='2024-01-01')['Adj Close']
```

---

## Statistical Tests

The project applies several statistical tests on the daily returns of the stock data to extract insights about their relationships and volatility.

### One-Sample t-test
**Goal:** Test whether the mean return of Apple (AAPL) stock is significantly different from a threshold (0.1% daily return).
```python
from scipy import stats

# Perform a t-test for AAPL
t_stat, p_value = stats.ttest_1samp(aapl_returns, threshold)
```

### Pearson Correlation
**Goal:** Measure the correlation between Apple (AAPL) and Microsoft (MSFT) daily returns.
```python
corr, p_value = stats.pearsonr(returns['AAPL'], returns['MSFT'])
```

### F-test
**Goal:** Compare the variance of Apple (AAPL) and Amazon (AMZN) returns to determine if they have significantly different volatilities.
```python
f_stat, p_value = stats.levene(returns['AAPL'], returns['AMZN'])
```

### ANOVA
**Goal:** Check if the means of the returns of multiple stocks (AAPL, MSFT, GOOGL, AMZN, META) are statistically different.
```python
f_stat, p_value = stats.f_oneway(returns['AAPL'], returns['MSFT'], returns['GOOGL'], returns['AMZN'], returns['META'])
```

### ARCH Test
**Goal:** Test for the presence of volatility clustering in AAPL returns.
```python
from statsmodels.stats.diagnostic import het_arch

arch_test = het_arch(returns['AAPL'])
```

### ADF Test
**Goal:** Test for stationarity of the Apple (AAPL) returns using the Augmented Dickey-Fuller test.
```python
from statsmodels.tsa.stattools import adfuller

adf_test = adfuller(returns['AAPL'])
```

---

## Visualization

### Daily Returns Plot
The following plot shows the daily returns of all five stocks:
```python
returns[['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META']].plot(figsize=(14, 7))
plt.title('Daily Returns of AAPL, MSFT, AMZN, GOOGL, META')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.show()
```

### Correlation Heatmap
To visualize the relationships between the returns of the stocks, we use a heatmap:
```python
import seaborn as sns

corr_matrix = returns.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Stock Returns')
plt.show()
```

### Boxplot for F-test (Variance Comparison)
```python
sns.boxplot(data=returns[['AAPL', 'AMZN']])
plt.title('Comparison of Volatility (Variance) Between AAPL and AMZN')
plt.show()
```

### Squared Returns for Volatility Clustering (ARCH)
```python
plt.plot(returns['AAPL']**2)
plt.title('Squared Returns of AAPL (Volatility Clustering)')
plt.show()
```

### Rolling Mean Plot for ADF Test (Stationarity Check)
```python
plt.plot(returns['AAPL'], label='AAPL Returns')
plt.plot(returns['AAPL'].rolling(window=50).mean(), label='50-Day Rolling Mean', color='orange')
plt.title('AAPL Returns and Rolling Mean')
plt.legend()
plt.show()
```

---

## Results Interpretation

### Statistical Test Results:

- **One-Sample t-test**: The t-statistic (0.206) and p-value (0.837) suggest that AAPL's mean daily return is not significantly different from 0.1%.
- **Pearson Correlation**: The Pearson correlation coefficient (0.696) shows a strong positive correlation between AAPL and MSFT, and the p-value (0.0) confirms that this is statistically significant.
- **F-test**: The F-statistic (14.77) and p-value (0.0001) indicate that the variances of AAPL and AMZN are significantly different.
- **ANOVA**: The ANOVA test suggests that there are no significant differences in mean returns across AAPL, MSFT, GOOGL, AMZN, and META.
- **ARCH Test**: A significant p-value (4.5e-72) indicates the presence of volatility clustering in AAPL returns.
- **ADF Test**: The ADF statistic (-14.81) and p-value (2.04e-27) suggest that AAPL returns are stationary, which is essential for time series modeling.

---

## Conclusion

This project demonstrates how to perform a range of statistical tests on stock market data, providing valuable insights into the relationships between stocks, volatility clustering, and stationarity. The tests are useful in financial research to understand stock behavior, making them key tools for investors and analysts.

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

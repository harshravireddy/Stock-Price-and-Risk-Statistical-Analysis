# Step-1: data collection.

import yfinance as yf
import pandas as pd

# Download stock data
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
df = yf.download(stocks, start='2015-01-01', end='2024-01-01')['Adj Close']

# Preview the data
print(df.head())
df.to_csv('stock_data.csv')

# Step-2 : Mean and Variance test for returns.

from scipy import stats

# Calculate daily returns
returns = df.pct_change().dropna()

# Set a threshold (0.1% daily return)
threshold = 0.001

# Perform a t-test for AAPL
aapl_returns = returns['AAPL']
t_stat, p_value = stats.ttest_1samp(aapl_returns, threshold)

print(f'T-statistic: {t_stat}, P-value: {p_value}')

# Step-3 : Correlation, F-test, ANOVA, ARCH test, ADF test.

# Calculate correlation
corr, p_value = stats.pearsonr(returns['AAPL'], returns['MSFT'])

print(f'Pearson Correlation: {corr}, P-value: {p_value}')

# Perform F-test
f_stat, p_value = stats.levene(returns['AAPL'], returns['AMZN'])

print(f'F-statistic: {f_stat}, P-value: {p_value}')

# Perform one-way ANOVA

f_stat, p_value = stats.f_oneway(returns['AAPL'], returns['MSFT'], returns['GOOGL'], returns['AMZN'], returns['META'])

print(f'ANOVA F-statistic: {f_stat}, P-value: {p_value}')


# Perform ARCH test for AAPL

from statsmodels.stats.diagnostic import het_arch

arch_test = het_arch(returns['AAPL'])

print(f'ARCH Test Statistic: {arch_test[0]}, P-value: {arch_test[1]}')



# Perform ADF test on AAPL returns

from statsmodels.tsa.stattools import adfuller

adf_test = adfuller(returns['AAPL'])

print(f'ADF Statistic: {adf_test[0]}, P-value: {adf_test[1]}')

# Step-4 : Visualize results

# Visualize Stock returns
import matplotlib.pyplot as plt

# Plot daily returns of stocks
returns[['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META']].plot(figsize=(14, 7))
plt.title('Daily Returns of AAPL, MSFT, AMZN, GOOGL, META')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.show()

#Visualize Correlation Heatmap
import seaborn as sns

# Correlation matrix
corr_matrix = returns.corr()

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Stock Returns')
plt.show()

#F-test Visualization (Boxplot of AAPL vs. MSFT)
# Boxplot to compare variances of AAPL and MSFT
plt.figure(figsize=(8, 6))
sns.boxplot(data=returns[['AAPL', 'AMZN']])
plt.title('Comparison of Volatility (Variance) Between AAPL and AMZN')
plt.ylabel('Daily Returns')
plt.show()
# Visualization of Volatility Clustering (ARCH Test)
# Plot squared returns to visualize volatility clustering
plt.figure(figsize=(14, 7))
plt.plot(returns['AAPL']**2)
plt.title('Squared Returns of AAPL (Volatility Clustering)')
plt.xlabel('Date')
plt.ylabel('Squared Returns')
plt.show()
# visualization of Stationarity Check (ADF Test)

# Plot AAPL returns and rolling mean
plt.figure(figsize=(14, 7))
plt.plot(returns['AAPL'], label='AAPL Returns')
plt.plot(returns['AAPL'].rolling(window=50).mean(), label='50-Day Rolling Mean', color='orange')
plt.title('AAPL Returns and Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.show()

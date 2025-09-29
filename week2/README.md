# Week 2: Grain Sales by Hour

This assignment adapts the Chapter 10 “Tuples” exercise from *Python for Everybody*.  
Instead of analyzing email timestamps, we use agricultural sales data to calculate the distribution of sales by **hour of the day**.

## Why this matters
In agricultural economics, understanding sales activity by time of day can help farmers, traders, and co-ops optimize when they release grain to the market or monitor peak trading activity.

## Example Input (grain_prices.csv)
```csv
Date,Time,Grain,Price
2025-09-01,09:14:16,Wheat,6.20
2025-09-01,10:45:02,Corn,5.80
2025-09-01,14:12:34,Soybeans,11.40
2025-09-01,15:20:12,Wheat,6.25
2025-09-01,18:05:55,Corn,5.75

## Example Output
```text
09 2
10 1
14 1
15 1
18 1

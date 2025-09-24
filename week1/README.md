# Week 1: Agricultural Water Compliance Checker

This Python script reads annual farm water usage data from a text file 
and checks each farm against the **4.0 acre-feet per acre water regulation**.  
It prints whether each farm is **Compliant** or in **Violation**, and gives 
a summary at the end.

---

## Why this matters
Water regulation compliance is a critical issue in sustainable agriculture 
and agricultural economics. By tracking usage programmatically, farmers 
and regulators can make better decisions about resource management.

---

## Example File
'SunnyFields 3.7'
'GreenValley 4.2'
'DesertBloom 2.9'
'RiverBend 4.5'

## Example Output
'SunnyFields Compliant'
'GreenValley Violation'
'DesertBloom Compliant'
'RiverBend Violation'
Summary
Compliant farms: 2
Violations: 2

## How to Run
1. Save your farm data in a text file (e.g., `farms.txt`).
2. Run the script:
3. When prompted, enter the file name (e.g., `farms.txt`).

## Program 1: [Water Compliance Checker](wateruse.py)

---

## Program 2: Sales Log Analyzer
This program reads a sales log file where each line contains: YYYY-MM-DD FARM CROP QTY_KG PRICE_PER_KG

It calculates:
- Total quantity sold per crop  
- Total revenue per farm  
- The farm with the highest revenue  

### Example Input
```text
2025-05-03 SunnyFields tomatoes 180 1.80
2025-05-03 SunnyFields peppers 75 2.20
2025-05-04 GreenValley tomatoes 120 1.70
2025-05-04 RiverBend lettuce 90 1.20
2025-05-05 GreenValley peppers 60 2.50
2025-05-06 DesertBloom tomatoes 200 1.60
```
###Example Output
tomatoes 500.0
peppers 135.0
lettuce 90.0
SunnyFields 489.0

## Program 2: [Sales Log Analyzer](sales_analyzer.py)


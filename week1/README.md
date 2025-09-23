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

## Example Input File
```text
SunnyFields 3.7
GreenValley 4.2
DesertBloom 2.9
RiverBend 4.5

## Example Output File

SunnyFields Compliant
GreenValley Violation
DesertBloom Compliant
RiverBend Violation

Summary:
Compliant farms: 2
Violations: 2

## How to Run
1. Save your farm data in a text file (e.g., farms.txt).
2. Run the script: 3. When prompted, enter the file name (e.g., farms.txt).

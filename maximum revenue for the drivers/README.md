# Statistical Analysis: Card vs. Cash Samples

## Overview

This project performs a **two-sample t-test** to compare the means of two different payment methods: **card** and **cash**. The goal is to determine if there is a statistically significant difference between the two payment methods, analyzing whether they differ in terms of some specific feature (e.g., transaction amount, frequency, etc.).

### Key Results:
- **t-statistic**: 169.21
- **p-value**: 0.0

The analysis reveals a significant difference between the means of the two samples, with an extremely low p-value, indicating strong evidence against the null hypothesis.

---

## Contents

- `data/`: Contains the sample data (card and cash transactions).
- `scripts/`: Python scripts used for data analysis, including the t-test calculation.
- `results/`: Output files, including the t-test results and visualizations.

## Interpretation of Results

- **t-statistic**: The t-statistic is 169.21, indicating a large difference between the two sample means.
- **p-value**: A p-value of 0.0 (or extremely close to 0) suggests very strong evidence against the null hypothesis, meaning there is a statistically significant difference between the card and cash samples.

import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action="ignore")

# --------------------- Simulating Click Data For A/B Testing ---------------------------
N_exp = 10000
N_con = 10000

np.random.seed(seed=1111)
# Generating Click Data
click_exp = pd.Series(data=np.random.binomial(n=1, p=0.4, size=N_exp))
click_con = pd.Series(data=np.random.binomial(n=1, p=0.2, size=N_con))

# Generate Group Identifier
exp_id = pd.Series(data=np.repeat(a="exp", repeats=N_exp))
con_id = pd.Series(data=np.repeat(a="con", repeats=N_con))


df_exp = pd.concat([click_exp, exp_id], axis=1)
df_con = pd.concat([click_con, con_id], axis=1)

df_exp.columns = ["click", "group"]
df_con.columns = ["click", "group"]

df_ab_testing = pd.concat([df_exp, df_con], axis=0).reset_index(drop=True)

start = pd.Timestamp(datetime.now())

df_ab_testing["timestamp"] = pd.date_range(start=start, periods=len(df_ab_testing), freq="H")
df_ab_testing["timestamp"] = df_ab_testing["timestamp"].dt.strftime(date_format='%Y-%m-%d %I:%M:%S %p')



X_con = df_ab_testing.groupby("group").sum().loc["con"]
x_exp = df_ab_testing.groupby("group").sum().loc["exp"]

p_con_hat = X_con.loc["click"] / N_con
p_exp_hat = x_exp.loc["click"] / N_exp

print("\n\n", f"probability in control group: {p_con_hat}\nprobability \
in the experimental group: {p_exp_hat:.2f}".title(), sep="")

p_pooled_hat = (p_exp_hat + p_con_hat) / (N_con + N_exp)
pooled_variance = p_pooled_hat * (1 - p_pooled_hat) * (1 / N_con + 1 / N_exp)

print(f"probability of pooled hat : {p_pooled_hat:.15f}\n\
probability of pooled variance: {pooled_variance:.15f}".title())

SE = np.sqrt(pooled_variance)
print(f"standard Error (Standard deviation of the sample) : {SE:.5f}")


alpha = 0.05
half_alpha = alpha / 2
print(f"level of significant : {alpha}\nTwo tail alpha: {half_alpha}")

z_critical = np.round(stats.norm.ppf(1 - half_alpha), 3)
test_stats = (p_con_hat- p_exp_hat) / SE
print(z_critical)

p_value = stats.norm.sf(abs(test_stats)) * 2

print(f"p-value: {p_value:2f}")
print("test test:",test_stats)


# plt.figure(figsize=(12, 7))

# Create Normal Distribution

# X = np.linspace(start= -4, stop= 4, num= 1000)
# Y = stats.norm.pdf(x=X)

# plt.plot(X, Y, color="blue", label="normal distribution".upper())

# fill_the_middle = (X >= -z_critical) & (X <= z_critical)

# plt.fill_between(X, 0, Y, where=fill_the_middle, alpha=0.5, label=f"Acceptance region")
# plt.fill_between(X, 0, Y, where=(X <= -z_critical), color="red", alpha=0.5, label=f"Rejection region: (α/2: {half_alpha})")
# plt.fill_between(X, 0, Y, where=(X >= z_critical), color="red", alpha=0.5)

# plt.axvline(x=z_critical, linestyle="--", color="black", label=f"z-critical: {z_critical}")
# plt.axvline(x=-z_critical, linestyle="--", color="black", label=f"-z-critical: {-z_critical}")

# plt.tight_layout()
# plt.legend()
# plt.show()
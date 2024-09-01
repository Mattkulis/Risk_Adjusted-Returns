# TP2 Python Code:
# Program includes adjustments for taxes on realized gains.

# Variables
R_p = 0.12        # Portfolio's annualized return
R_b = 0.11        # Benchmark's annualized return
RFR = 0.05        # Nominal risk-free rate (quantifiable opportunity cost)
M2_change = 1     # Change in M2 money supply over lookback period
M2_initial = 20   # Initial M2 money supply at beginning of lookback period
D_max = 0.20      # Maximum allowed drawdown (risk budget)
D_realized = 0.03 # Realized drawdown over lookback period
B_drawdown = 0.15 # Benchmark's drawdown (Ex: S&P500)

# Ensure non-negative realized drawdown
D_realized = max(D_realized, 0)

# Step 1: Calculate the real risk-free rate
RFR_real = RFR - (M2_change / M2_initial)

# Step 2: Calculate portfolio's alpha relative to the benchmark
alpha_p = R_p - (R_b + RFR_real)

# Step 3: Adjust portfolio's alpha for realized drawdown
if D_realized == 0:
    # Handle zero drawdown case
    alpha_adj = alpha_p / 1e-10  # Use a very small denominator to simulate a large adjustment
else:
    alpha_adj = alpha_p / (D_realized / D_max) # D_realized / D_max calculates drawdown as a fraction of the risk budget

# Step 4: Adjust for monetary debasement using M2
alpha_deb = alpha_adj - (M2_change / M2_initial)

# Step 5: Calculate the benchmark's risk-adjusted alpha
alpha_b_adj = (R_b - RFR_real) / B_drawdown

# Step 6: Calculate the final metric
# Handle potential division by zero if alpha_b_adj is zero
if alpha_b_adj == 0:
    final_metric = float('inf') if alpha_deb > 0 else float('-inf')
else:
    final_metric = alpha_deb / alpha_b_adj

# Output the final metric
print(f"Risk-Adjusted Performance Metric: {final_metric:.4f}")

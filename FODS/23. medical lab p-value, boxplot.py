import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
placebo_group = np.array([68, 72, 65, 70, 71, 67, 73, 69, 70, 66])
treatment_group = np.array([60, 64, 55, 62, 58, 61, 59, 57, 63, 56])
# Perform t-test (two-sample independent t-test)
t_statistic, p_value = stats.ttest_ind(placebo_group, treatment_group)

print(f"t-statistic: {t_statistic:.2f}")
print(f"p-value: {p_value:.10f}")  

# Determine if the p-value is statistically significant (common threshold is 0.05)
if p_value < 0.05:
    print("has a statistically significant effect.")
else:
    print("has no statistically significant effect.")

plt.figure(figsize=(8, 6))
plt.boxplot([placebo_group, treatment_group], labels=['Placebo', 'Treatment'])
plt.title('Boxplot of Placebo vs. Treatment')
plt.ylabel('Response')
plt.show()

'''sample output
t-statistic: 7.61
p-value: 0.0000004999
has a statistically significant effect.
'''

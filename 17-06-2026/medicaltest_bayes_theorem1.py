# Medical Test Problem using Bayes' Theorem

# Given probabilities
prevalence = 0.01      # P(D)
sensitivity = 0.99     # P(Pos|D)
specificity = 0.95     # P(Neg|No Disease)

# False Positive Rate
false_positive_rate = 1 - specificity  # P(Pos|No Disease)

# Bayes' Theorem
numerator = sensitivity * prevalence

denominator = numerator + (false_positive_rate * (1 - prevalence))

posterior_probability = numerator / denominator

print("Probability of actually having the disease")
print("given a positive test result =", round(posterior_probability * 100, 2), "%")
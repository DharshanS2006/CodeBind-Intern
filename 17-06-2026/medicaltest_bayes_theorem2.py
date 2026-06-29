# Medical Test Problem using Bayes' Theorem

P_disease = float(input("Enter disease prevalence: "))
P_pos_given_dis = float(input("Enter true positive rate: "))
P_pos_given_no = float(input("Enter false positive rate: "))

P_no_disease = 1 - P_disease

# Total probability of positive test
P_positive = (P_pos_given_dis * P_disease +
              P_pos_given_no * P_no_disease)

# Bayes' Theorem
P_disease_given_pos = (P_pos_given_dis * P_disease) / P_positive

print("\nResults")
print("P(No Disease) =", round(P_no_disease, 4))
print("P(Positive Test) =", round(P_positive, 4))
print("P(Disease | Positive) =", round(P_disease_given_pos, 4))
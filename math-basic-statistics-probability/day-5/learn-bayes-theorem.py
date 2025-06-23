# 🔸 Bayes’ Theorem
# Bayes’ Theorem helps you find the probability of an event given that another event has already occurred.
# especially when information is indirect.

# formula :-
# P(A|B)=(P(B|A) * P(A))/P(B)

# where :- 
# P(A|B) --> Probability of A given B
# P(B|A) --> Probability of B given A
# P(A) --> Probability of A 
# P(B) --> Probability of B

# 🔸 Real-world example: Medical Diagnosis
# Let’s say:
# 1% of people have a rare disease → P(D) = 0.01
# The test detects the disease correctly 99% of the time → P(Positive|D) = 0.99
# False positive rate = 5% → P(Positive|No D)=0.05

# 👉 What is the probability a person actually has the disease if the test is positive?

# 🧠 Apply Bayes’ Formula:
# P(D|Positive)=(P(Positive|D) * P(D))/P(Positive)
# P(Positive) = (P(Positive|D) * P(D)) + (P(Positive|No D) * P(No D))
# =(0.99)(0.01)+(0.05)(0.99)=0.0099+0.0495=0.0594
# P(D|Positive) = 0.0099/0.0594 ≈ 0.1667
# ✅ So, only ~16.7% of people who test positive actually have the disease, due to low base rate and false positives.

# Bayes' Theorem implementation
P_D = 0.01
P_Pos_given_D = 0.99
P_Pos_given_NoD = 0.05
P_NoD = 1 - P_D

P_Pos = (P_Pos_given_D * P_D) + (P_Pos_given_NoD * P_NoD)
P_D_given_Pos = (P_Pos_given_D * P_D) / P_Pos

print("P(Disease | Positive Test):", round(P_D_given_Pos, 4))
# P(Disease | Positive Test): 0.1667

# 🔹 1. Conditional Probability: P(A|B)

# Conditional probability is the probability of event A occurring given that event B has already occurred.

# P(A|B) = (P(A ∩ B))/P(B) (if P(B) != 0)

# P(A ∩ B) is the probability of both A and B happening.
# P(B) is the probability of event B.
# So we "restrict" our universe to event B and then ask: what's the chance of A within that?

# Q: In a class of 50 students:
# 30 like Python (A)
# 20 like JavaScript (B)
# 10 like both

# What is P(A|B) 
# that means --> Probability a student likes Python given they like JavaScript?

# P(A ∩ B) = 10/50 , P(B) =20/50
# P(A|B) = (10/50)/(20/50) =0.5

# Given: A ∩ B = 10, B = 20, total = 50

P_A_and_B = 10 / 50
P_B = 20 / 50

P_A_given_B = P_A_and_B / P_B

print("P(A|B):", P_A_given_B)
# P(A|B): 0.5

# 🔹 1. Basic Probability Rules
# Probability measures how likely an event is to happen.

# P(E) = (Number of favorable outcomes)/(Total number of possible outcomes)

# 🔸 Key Rules:
# 0 <= P(E) <= 1 --> Probability is always between 0 and 1
# P(certain event) = 1 --> An event that always happens
# P(impossible event) = 0 --> An event that never happens
# P(not E) = 1 - P(E) --> Probability of event not happening
# P(E1 U E2) = P(E1) + P(E2) --> For mutually exclusive events (can’t happen together)

# eg:- 
# Q: What's the probability of rolling a 4 on a standard 6-sided die?
# Favorable outcomes = 1 (only one 4)
# Total outcomes = 6
# P(4) = 1/6 ≈ 0.1667

favorable = 1
total = 6
probability = favorable / total

print("Probability of rolling a 4:", probability)
# Probability of rolling a 4: 0.1667

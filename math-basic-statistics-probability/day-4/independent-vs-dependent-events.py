# 🔹 2. Independent vs Dependent Events

# ✅ Independent Events:
# Two events A and B are independent if: P(A ∩ B)=P(A).P(B)

# This means:
# 👉 The outcome of one does not affect the other.

# eg:-
# Tossing a coin and rolling a die.
# Drawing a card with replacement and then drawing another.

# ✅ Dependent Events:
# Two events A and B are dependent if: P(A ∩ B)!=P(A).P(B)

# This means:
# 👉 The outcome of one affects the other.

# eg:- 
# Drawing two cards without replacement.
# Selecting a ball from a bag, keeping it, then selecting another.

# Independent events: Rolling two dice
P_A = 1/6  # rolling a 3 on first die
P_B = 1/6  # rolling a 4 on second die

P_A_and_B = P_A * P_B
print("Independent (P(3 and 4)):", P_A_and_B)

# Dependent events: Drawing 2 cards without replacement
P_ace_first = 4 / 52
P_ace_second_given_first = 3 / 51

P_both_aces = P_ace_first * P_ace_second_given_first
print("Dependent (Both aces without replacement):", P_both_aces)

# Independent (P(3 and 4)): 0.027777...
# Dependent (Both aces): ~0.0045

# 🔍 How to Check Independence (Theoretical):

# To check if two events A and B are independent:
# Find:
    # P(A ∩ B)
    # P(A).P(B)
# If both are equal, → Independent
# If not, → Dependent
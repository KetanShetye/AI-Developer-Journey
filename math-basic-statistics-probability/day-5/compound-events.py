# 🔸 1. Compound Events
# A compound event is formed when two or more events happen together. There are two main types:
# Union (OR) — event A or B occurs
    # P(A U B) = P(A) + P(B) - P(A ∩ B)
# Intersection (AND) — event A and B both occur
    # P(A ∩ B) =P(A) x P(B) (if A and B are independent)

# 🔹 Types of Events:
# | Event Type             | Description                                                                  |
# | ---------------------- | ---------------------------------------------------------------------------- |
# | **Mutually Exclusive** | Events can't happen together (e.g., getting 3 **or** 5 on a single die roll) |
# | **Independent**        | One event does **not** affect the other                                      |
# | **Dependent**          | One event **does** affect the other                                          |

# eg:-
# 🧮 Example 1: Union (OR)
# Roll a die. What's the probability of getting a 2 or 4?
# P(2∪4)=P(2)+P(4) = 1/6 + 1/6 = 2/6 =0.333

# 🧮 Example 2: Intersection (AND — Independent)
# Draw 1 card from each of 2 decks. What's the probability both are kings?
# P(K1 ∩ K2) = 4/52 x 4/52 = 1/169

import itertools

outcomes = list(itertools.product(["H", "T"], repeat=2))
favorable = [outcome for outcome in outcomes if "H" in outcome]

probability = len(favorable) / len(outcomes)

print("P(at least one Head in two tosses):", probability)

# P(at least one Head in two tosses): 0.75
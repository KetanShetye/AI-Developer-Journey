# 🔹 Outcome
# A single possible result of a random experiment.
# Example: Rolling a die → outcome could be 4.

# 🔹 Sample Space (S)
# The set of all possible outcomes.
# eg:- 
# for a 6-sided die S={1,2,3,4,5,6}
# for 2 tossed coins S={HH, HT, TH, TT}

# 🔹 Event
# A subset of the sample space.
# It contains one or more outcomes you're interested in.
# eg:- 
    # Rolling an even number → Event = {2, 4, 6}
    # Getting heads → Event = {H}

# 🧠 Understanding:
# Let’s say you roll a 6-sided die.
sample_space = [1, 2, 3, 4, 5, 6]
event_even = [x for x in sample_space if x % 2 == 0]

print("Sample Space:", sample_space)
print("Event - Even Numbers:", event_even)
print("P(Even):", len(event_even) / len(sample_space))

# Sample Space: [1, 2, 3, 4, 5, 6]
# Event - Even Numbers: [2, 4, 6]
# P(Even): 0.5

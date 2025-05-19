#EIGHT

def candidate_elimination(data):
    specific_hypothesis = data[0].copy()[: -1]
    general_hypothesis = ['?']*(len(data[0]) -1)
    for example in data:
        if example[-1] == "Positive":
            for i in range(len(specific_hypothesis)):
                if specific_hypothesis[i] != example[i]:
                    specific_hypothesis[i] = "?"
        elif example[-1] == "Negative":
            for i in range(len(general_hypothesis)):
                if general_hypothesis[i] != example[i]:
                    general_hypothesis[i] = "?"
    return specific_hypothesis, general_hypothesis

data = [
    ['Sunny', 'Warm', 'High', 'Strong', 'Positive'],
    ['Sunny', 'Warm', 'High', 'Weak', 'Negative'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Positive'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Negative'],
    ['Sunny', 'Warm', 'Low', 'Strong', 'Positive']
    ]

specific, general = candidate_elimination(data)
print("Candidate Elimination Specific Hypothesis:" , specific)
print("Candidate Elimination General Hypothesis:" , general)
#FOUR

def find_s(data):
    hypothesis = data[0].copy()[: -1]
    for example in data:
        if example[-1] == "Positive":
            for i in range(len(hypothesis) -1):
                if hypothesis[i] != example[i]:
                    hypothesis[i] = "?"
    return hypothesis

data = [
    ['Sunny', 'Warm', 'High', 'Strong', 'Positive'],
    ['Sunny', 'Warm', 'High', 'Weak', 'Negative'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Positive'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Negative'],
    ['Sunny', 'Warm', 'Low', 'Strong', 'Positive']
    ]

result = find_s(data)
print("Find-S Hypothesis:", result)
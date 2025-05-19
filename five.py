#FIVE

def id3(data, attributes):
    labels = [row[-1] for row in data]
    return labels[0] if len(set(labels)) == 1 else {attributes[0]: {v: id3([r[1:] for r in data if r[0] == v], attributes[1:]) for v in set(r[0] for r in data)}}

attributes = ["Size", "Cost"]
mapping = {("Small", "Low"): "Hatchback", ("Medium", "Medium"): "Compact SUV", ("Big", "High"): "SUV"}

data = []
for _ in range(int(input("Enter number of records: "))): 
    size, cost = input("Enter Size, Cost: ").split(",")
    data.append([size, cost, mapping.get((size, cost), "Unknown")])

tree = id3(data, attributes)
print("\n Decision Tree:", tree)

def predict(tree, attributes, user_input):
    if not isinstance(tree, dict): return tree
    attr = next(iter(tree))
    return predict(tree[attr].get(user_input[attributes.index(attr)], "Unknown"), attributes, user_input)

user_input = input("\n Enter Size, Cost: ").split(",")
print("\n Predicted Car Type:", predict(tree, attributes, user_input)) 
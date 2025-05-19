#THREE

people = {}

def add_person():
    name = input("Enter name: ")
    income = input("Enter income level (low/medium/high): ")
    credit_score = input("Enter credit score (poor/good): ")
    employment = input("Are they employed? (yes/no): ")
    people[name] = {"income": income, "credit_score": credit_score, "employment": employment}
    
def is_eligible(name, data):
    person = data.get(name, {})
    return (person.get("income") == "high" or (person.get("credit_score") == "good" and person.get("employement") == "yes"))

total_people = int(input("Enter number of people: "))
for _ in range(total_people):
    add_person()
for person in people:
    print(f"{person} is elegible for loan: {is_eligible(person, people)}")
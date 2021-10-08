import pickle

#객체하나 불어오기
with open('object.bin', 'rb') as f:
    p1 = pickle.load(f)
print(p1)
print(p1.name)
print(p1.color)

#객체여러게 불어오기
with open('objects.bin', 'rb') as f:
    people = pickle.load(f)
# print(people)       #[<person.Person object at 0x0000020AEE158F70>, <person.Person object at 0x0000020AEE0FC6D0>]
# print(people[0])
# print(people[1])
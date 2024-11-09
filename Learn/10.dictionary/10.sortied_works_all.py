"""
 Note: sort works for list only, But sorted works for anything
"""

marks = {
    "physics": 90,
    "chemistry": 80,
    "maths": 70,
    "english": 60,
}

print(marks)

result = sorted(marks.items(), key=lambda x: x[1])
result1 = dict(sorted(marks.items(), key=lambda x: x[1]))

# sorted is used in case of anything not sort, it requires two parameters(iterables, key=<on basis of what>)
# it returns list always with tuples, we can change the output type
print(result)
print(result1)

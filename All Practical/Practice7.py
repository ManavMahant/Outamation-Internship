# JSON
"""
import json
x = {"Name" : "Manav",
     "Age" : 22,
     "Country" : "India"}
y = json.dumps(x)
print(y)"""

"""
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x)
print(json.dumps(x, indent=4, separators=(". ", " = ")))
"""

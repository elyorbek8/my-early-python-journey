# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:23:25 2024

@author: Elyorbek
"""

# indroduction to JSON
import json

# x = 18
# x_json = json.dumps(x)

# info = True
# info_json = json.dumps(info)


# nums = list(range(1,10))

# with open('nums.json', 'w') as file:
#     json.dump(nums,file)

# with open('nums.json') as file:
#     nums2 = json.load(file)
# print(nums2)


student = {
    "full_name": "alibekov sardor",
    "age": 20,
    "university": "stanford",
    "major": "CS",
    "subjects": [
        "algebra", "calculs", "physics", "electronics", "philosophy"
        ]
    }

student_json = json.dumps(student, indent=5)

with open('student.json', 'w') as file:
    json.dump(student,file)

with open("student.json") as f:
    student2 = json.load(f)

print(student2)













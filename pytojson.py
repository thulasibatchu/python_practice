import json
emp={
    'eid':101,
    'ename':'rg',
    'avail':True,
    'loc': None
}

print(type(emp))

emp_json=json.dumps(emp)
print(emp_json)
print(type(emp_json))
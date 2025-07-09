contacts = [{'name': 'mike', 'age': 40}, {'name': 'matt', 'age': 45}]
print(list(filter(lambda x: x['name'] == 'mike', contacts)))

print(list(sorted(contacts, key=lambda x: x['age'], reverse=True)))

contacts = {'mike': {'age': 40}, 'matt': {'age': 45}}
print(contacts['mike'])


import json

with open('file_1.json', 'w') as file:
    json.dump([{'id': i, 'name': f'test {i}'} for i in range(1, 11)] +
              [{'id': i, 'name': f'test {i}'} for i in range(31, 41)],
              file)

with open('file_2.json', 'w') as file:
    json.dump([{'id': i, 'name': f'test {i}'} for i in range(11, 21)] +
              [{'id': i, 'name': f'test {i}'} for i in range(41, 51)],
              file)

with open('file_3.json', 'w') as file:
    json.dump([{'id': i, 'name': f'test {i}'} for i in range(21, 31)] +
              [{'id': i, 'name': f'test {i}'} for i in range(51, 61)],
              file)



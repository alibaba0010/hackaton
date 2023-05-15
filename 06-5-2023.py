#  Python Code 
runners = [
    {'name': 'John', 'speed': 10, 'run_time': 6, 'rest_time': 20},
    {'name': 'James', 'speed': 8, 'run_time': 8, 'rest_time': 25},
    {'name': 'Jenna', 'speed': 12, 'run_time': 5, 'rest_time': 16},
    {'name': 'Josh', 'speed': 7, 'run_time': 7, 'rest_time': 23},
    {'name': 'Jacob', 'speed': 9, 'run_time': 4, 'rest_time': 32},
    {'name': 'Jerry', 'speed': 5, 'run_time': 9, 'rest_time': 18},
]
distances = {}
for runner in runners:
     distances[runner['name']] = 0
for sec in range(1234):
    for runner in runners:
          if sec % (runner['run_time'] + runner['rest_time']) < runner['run_time']:
            # Runner is running
            distances[runner['name']] += runner['speed']
            
winner = max(distances, key=distances.get)

for runner in runners:
    print(runner['name'], "covered", distances[runner['name']], "meters.")
print("The winning runner is", winner, "with a distance of", distances[winner], "meters.")

import json
with open("graph.json", "r") as file:
    graph = json.load(file)


starting_word = input("enter a four letter word: ")

visited = []

queue = [starting_word]

predecessors = {}

while queue:
	origin_word = queue.pop(0)
	
	for word in graph[origin_word]:
		if word=="POOP":
			predecessors[word] = origin_word
			queue = []
			break

		if word in visited:
			continue
		else:
			queue.append(word)
		
		predecessors[word] = origin_word
	
	visited.append(origin_word)

optimal_path = ["POOP"]

last_word = "POOP"

while predecessors[last_word] != starting_word:
	optimal_path.append(predecessors[last_word])
	last_word = predecessors[last_word]

optimal_path.reverse()

print(optimal_path)
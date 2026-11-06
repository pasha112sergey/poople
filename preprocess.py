from collections import defaultdict
import json

def is_neighbor(w1, w2):
    diff_count = 0

    for l1, l2 in zip(w1, w2):
        if l1 != l2 and diff_count > 0:
            return False
        
        elif l1 != l2 and diff_count == 0:
            diff_count += 1

    return True

def preprocess():

    words = []
    with open("word_list.txt", "r", encoding="utf-8") as file:
        for line in file:
            words.append(line.strip())

    graph = defaultdict(list)

    for start_word in words:
        for potential_connection in words:
            
            if start_word == potential_connection:
                continue

            if is_neighbor(start_word, potential_connection):
                graph[start_word].append(potential_connection)
            
    with open("graph.json", "w") as out:
        json.dump(graph, out, indent=4)




if __name__ == "__main__":
    preprocess()
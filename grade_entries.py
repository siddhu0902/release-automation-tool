#grade_entries
def build_gradebook(grade_entries):
    gradebook = {}
    for entry in grade_entries:
        name = entry['name']
        score = entry['score']
        if name in gradebook:
            gradebook[name].append(score)
        else:
            gradebook[name] = [score]
    return gradebook

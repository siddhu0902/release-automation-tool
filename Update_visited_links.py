#updated visited links
def update_visited_links(visited_links_set, new_links_list):
    initial_count = len(visited_links_set)
    for link in new_links_list:
        visited_links_set.add(link)
    new_count = len(visited_links_set)
    truly_new_links_added = new_count - initial_count
    return visited_links_set, truly_new_links_added

visited = {'http://example.com', 'http://google.com', 'http://test.com'}
new_links = ['http://google.com', 'http://python.org', 'http://example.com/about', 'http://test.com']

updated_visited, new_links_added = update_visited_links(visited, new_links)
print(updated_visited)
print(new_links_added)

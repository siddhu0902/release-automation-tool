#distribute_tasks
def distribute_task(server_load,new_tasks):
    for _ in range(new_tasks):
        min_index = server_load.index(min(server_load))
        server_load[min_index] += 1
    return server_load

server_load = [10,5,2,8]
new_tasks = 5
print(distribute_task(server_load,new_tasks))
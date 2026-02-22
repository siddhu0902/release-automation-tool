#Find_duplicate_packets
# A list of packet sequence numbers captures form the network
def packet_list(L):
    D = {}
    for x in L:
        if (L.count()>=2):
            D[x] = L.count(x)
    L = eval(input("Enter a list of packets: "),end='/n')
    packet_list(L)
    print(D)    
packet_list([1001,1002,1003,1002,1004,1005,1001,1003,1002])

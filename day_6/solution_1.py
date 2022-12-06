def find_first_four_unique_chars(packet):
    limit = 14
    for pos, i in enumerate(packet):
        verification_packet = packet[pos : pos + limit]
        if len([*set(verification_packet)]) == limit:
            return pos


begin_of_packets = []
with open("input") as communication_file:
    for packet in communication_file:
        # print(packet)
        begin_of_packets.append(find_first_four_unique_chars(packet) + 14)

print(begin_of_packets)

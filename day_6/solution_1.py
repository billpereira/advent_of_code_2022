def find_first_unique_chars(packet, limit):
    for pos, i in enumerate(packet):
        verification_packet = packet[pos : pos + limit]
        if len([*set(verification_packet)]) == limit:
            return pos


def main():
    limit = 14
    begin_of_packets = []
    with open("input") as communication_file:
        for packet in communication_file:
            begin_of_packets.append(
                find_first_unique_chars(packet, limit) + limit
            )

    print(begin_of_packets)


main()

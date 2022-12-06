from helper_funcs import find_marker


def main():
    # Part 1
    start_of_packet_marker = find_marker(sequence_length=4)
    print(f'Packet marker complete after {start_of_packet_marker} characters')

    # Part 2
    start_of_message_marker = find_marker(sequence_length=14)
    print(f'Message marker complete after {start_of_message_marker} characters')


if __name__ == "__main__":
    main()

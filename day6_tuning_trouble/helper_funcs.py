def find_marker(sequence_length: int):
    with open('datastream.txt') as data:
        text = data.readline()
        for i, _ in enumerate(text):
            if len(set(text[i:i+sequence_length])) == sequence_length:
                marker = text[i:i+sequence_length]
                return text.index(marker) + sequence_length

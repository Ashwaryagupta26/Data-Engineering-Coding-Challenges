import csv

def read_spec(spec_file):
    with open(spec_file, 'r') as f:
        spec = f.readlines()
    fields = []
    for line in spec:
        name, length = line.split(':')
        fields.append((name, int(length)))
    return fields

def parse_fixed_width_file(input_file, spec):
    parsed_data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            record = []
            position = 0
            for field_name, field_length in spec:
                record.append(line[position:position+field_length].strip())
                position += field_length
            parsed_data.append(record)
    return parsed_data


def write_csv(output_file, data, spec):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([field[0] for field in spec])
        writer.writerows(data)

def main(spec_file, input_file, output_file):
    spec = read_spec(spec_file)
    data = parse_fixed_width_file(input_file, spec)
    write_csv(output_file, data, spec)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python script.py <spec_file> <input_file> <output_file>")
    else:
        spec_file = sys.argv[1]
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        main(spec_file, input_file, output_file)

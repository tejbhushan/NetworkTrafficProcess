import csv
from collections import defaultdict

# Function to load the tag lookup table from a CSV file
def load_tag_lookup_table(lookup_file):
    tag_lookup = {}
    with open(lookup_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            dstport, protocol, tag = row
            protocol = protocol.lower()
            tag_lookup[(dstport, protocol)] = tag
    return tag_lookup

# Function to parse the flow log data and map to tags
def parse_flow_logs(log_file, tag_lookup):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    protocol_map = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp'
    }

    untagged_count = 0

    with open(log_file, 'r') as file:
        for line in file:
            components = line.strip().split()

            if not components:
                continue

            # Extract dstport (7th column) and protocol (8th column)
            dstport = components[6]
            protocol_num = components[7]
            
            protocol = "unknown"
            if protocol_num in protocol_map:
                protocol = protocol_map[protocol_num]
            
            tag = tag_lookup.get((dstport, protocol), "Untagged")
            if (dstport, protocol) in tag_lookup:
                tag_counts[tag] += 1
            else:
                untagged_count += 1

            port_protocol_counts[(dstport, protocol)] += 1

    return tag_counts, port_protocol_counts, untagged_count

# Function to write the output to a file
def write_output(output_file, tag_counts, port_protocol_counts, untagged_count):
    with open(output_file, 'w') as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        file.write(f"Untagged,{untagged_count}\n\n")

        file.write("Port/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

# Main function to execute the script
def main():
    log_file = 'flow_logs.txt'
    lookup_file = 'tag_lookup_table.csv'
    output_file = 'output.csv'

    try:
        tag_lookup = load_tag_lookup_table(lookup_file)
        tag_counts, port_protocol_counts, untagged_count = parse_flow_logs(log_file, tag_lookup)
        write_output(output_file, tag_counts, port_protocol_counts, untagged_count)
        print("Ready Outfile", output_file)
    except Exception as e:
        print(f"error {e}")

if __name__ == "__main__":
    main()

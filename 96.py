def count_hours_in_file(filenamne):
    hours_count = {}

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                parts = line.split()
                if len(parts) > 5:  # To ensure there's a time part
                    time = parts[5]
                    hour = time.split(':')[0]
                    hours_count[hour] = hours_count.get(hour, 0) + 1

    return hours_count

# Replace 'yourfile.txt' with your filename
filename = ('mbox-short.txt')
hour_distribution = count_hours_in_file(filename)

for hour, count in sorted(hour_distribution.items()):
    print(hour, count)

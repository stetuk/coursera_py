
def average(numbers):
    if len(numbers) == 0:
        return 0  # Avoid division by zero
    return sum(numbers) / len(numbers)
fname = input("Enter file name: ")
with open(fname, 'r') as fh:
    numbers = []
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            try:
                start = line.find('0')  # Assuming the number starts with '0'
                number = float(line[start:])
                numbers.append(number)
            except ValueError:
                print('Error: Invalid floating point number found.')
                continue

    avg = average(numbers)
    print("Average spam confidence:", avg)

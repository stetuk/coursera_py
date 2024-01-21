fname = ('mbox-short.txt')#input("Enter file name: ")
with open(fname, 'r') as fn:

    email_appearances = dict()

    for line in fn:
        if not line.startswith('From '):  # Check if the line is relevant
            continue

        words = line.split()
        if len(words) < 2:  # Skip lines with no email address
            continue

        email = words[1]  # The email address is the second word

        # Count appearances of each email
        email_appearances[email] = email_appearances.get(email, 0) + 1

# Find the email with the highest number of appearances
max_email = max(email_appearances, key=email_appearances.get)
max_appearances = email_appearances[max_email]

print(max_email, max_appearances)

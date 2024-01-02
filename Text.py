# Open the file
# Use words.txt as the file name
fname = input("Enter file name: ")
f = open(fname, 'r')  
    # Read the contents
fn=f.read()
cap=fn.upper()
 # Print the contents
print(cap.strip())

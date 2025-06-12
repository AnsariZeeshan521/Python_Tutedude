try:
    with open("sample.txt",'r') as file1:
        lines = file1.readlines()
        for i in range(len(lines)):
            print("Line ",i+1,": "+lines[i].strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
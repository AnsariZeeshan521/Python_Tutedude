with open("output.txt",'w') as file1:
    userinput1 = input("Enter text to write to the file: ")
    file1.writelines(userinput1+"\n")
    print("Data successfully written to output.txt\n")

with open("output.txt",'a') as file1:
    userinput2 = input("Enter additional text to append: ")
    file1.writelines(userinput2)
    print("Data successfully appended\n")
    file1.close()

with open("output.txt",'r') as file1:
    print("Final content of the output.txt:")
    print(file1.read())

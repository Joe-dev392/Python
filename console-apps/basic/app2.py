file1 = file2 = file3 = ""

print("Welcome User, kindly enter 3 file names (15 chars at least) and I will print out the extensions as well as the char count")

l1 = "true"
while(l1 == 'true'):
    file1 = input("Enter the first filename\t")
    if len(file1) >= 15:
        l1 = 'false'
    else:
        print("The filename is less than 15 characters")

l2 = "true"
while(l2 == 'true'):
    file2 = input("Enter the second filename\t")
    if len(file2) >= 15:
        l2 = 'false'
    else:
        print("The filename is less than 15 characters")

l3 = "true"
while(l3 == 'true'):
    file3 = input("Enter the third filename\t")
    if len(file3) >= 15:
        l3 = 'false'
    else:
        print("The filename is less than 15 characters")
print("Thanks for your inputs. Kindly find my output below as I've promised")
print(f"\nFile 1 extension: '{file1[-4:]}' | File 1 char-count: {len(file1)} | Ext char-count {len(file1[-4:])}".format(file1[-4:]),len(file1), len(file1[-4:]))
print(f"\nFile 2 extension: '{file2[-4:]}' | File 2 char-count: {len(file2)} | Ext char-count {len(file2[-4:])}".format(file2[-4:]),len(file2), len(file2[-4:]))
print(f"\nFile 3 extension: '{file3[-4:]}' | File 3 char-count: {len(file3)} | Ext char-count {len(file3[-4:])}".format(file3[-4:]),len(file3), len(file3[-4:]))
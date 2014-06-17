"""
out_file=open('C:/Python Projects/mydata.txt', 'w')
out_file.write('Hello\n')
out_file.write('world\n')

weekends = ['Saturday', 'Sunday']
out_file.writelines(weekends)
out_file.writelines(weekends)
out_file.flush()
out_file.close()



in_file=open('C:/Python Projects/mydata.txt' ,'r')
first=in_file.read(1)
second=in_file.read()

print (first)
print (second)

print(in_file.readlines())


out_file=('C:/Python Projects/mydata.txt', 'a')
out_file.write('\nGoodbye')


out_file2=open('C:/Python Projects/mydata2.txt', 'w')
out_file2.write('First Line\n')
out_file2.write('Second Line')
out_file2.flush()
out_file2.close()


in_file2=open('C:/Python Projects/mydata2.txt', 'r+')
print(in_file2.read(1))
print(in_file2.tell())

print(in_file2.readline())
in_file2.seek(0)
print(in_file2.readline())
in_file2.seek(0)
in_file2.write('hi')
in_file2.seek(0)
print(in_file2.readline())





# pickle example

import pickle
outfile=open('C:/Python Projects/mydata2.txt', 'wb')
letters=['a', 'b', 'c']
pickle.dump(letters, outfile)
outfile.close()

in_file = open('C:/Python Projects/mydata2.txt', 'rb')
file_data = pickle.load(in_file)
in_file.close()
print(file_data)




import pickle
letters=['a', 'b', 'c']
pickled_letters=pickle.dumps(letters)
print(pickled_letters)
unpickled_letters=pickle.loads(pickled_letters)
print(unpickled_letters)

"""


import shelve
db_file=shelve.open('C:/Python Projects/letters.txt', 'c')
db_file ['vowels'] =['a', 'e', 'i', 'o', 'u']
db_file['end'] = ['x', 'y', 'z']
db_file.close()

db_file=shelve.open('C:/Python Projects/letters.txt', 'c')
print(list(db_file.keys()))
print('vowels' in db_file)
del db_file['vowels']

print('vowels' in db_file)
db_file.sync() # similar to flush, it writes data to files right away
db_file.close()










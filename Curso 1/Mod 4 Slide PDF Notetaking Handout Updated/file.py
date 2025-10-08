def open_read_file(file):
    """Open the given file, reads each line and prints to the console.
    Closes the given file.
    """

    #open the given file in read mode
    f = open(file, 'r')
    print(type(f))

    cnt = 0
    line = f.readline()

    while line:
        print(line, end='')
        line = f.readline()

        cnt += 1

    print('')
    print('the are', cnt, 'lines in the file')

    f.close()

def open_read_append_new_file(file1, file2):
    """Open the first file,and reads all lines into a list.
    Reverses the lines, and appends then to the scond file.
    """

    #open the first file in read mode
    with open(file1) as fin:

        #read all lines into a list
        lst = fin.readlines()

        #reverse the list
        lst.reverse()

        #oppenn second file for appending
        fout = open(file2, 'a')

        #write reversed lines to second file
        fout.writelines(lst)

        #close the second file
        fout.close()

def open_read_appennd_same_file(file):
    """
    Opens the given file and reads all lines as a list,
    Appends lines to same file.
    """

    #open the file for reading and writing
    f = open(file, 'r+')

    #read all lines into a list
    lst = f.readlines()

    lst.insert(0, '\n')
    lst.insert(0, 'here is some new text')
    lst.insert(0, '\n')

    #append the lines back to same file
    f.writelines(lst)

    #close file
    f.close()

def open_read_write_new_file(file1, file2):
    """Opens the first file and reads all text as a string
    Copies or wirte all text to tje second file"""

    #open the fist for reading
    with open(file1) as fin:

        #reads all lines as a single string
        text = fin.read()

        #open second file in write mode
        fout  = open(file2, 'w')

        #write single string to second file
        fout.write(text)

        #close second file
        fout.close()

def main():
    #open_read_file('news.txt')
    #open_read_append_new_file('news.txt', 'news_out.txt')
    #open_read_appennd_same_file('news.txt')
    open_read_write_new_file('news.txt','news_copy.txt')

if __name__ == '__main__':
    main()
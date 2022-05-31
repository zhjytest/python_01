

lst = ['hello','abc']
for x in lst:
    if 'hell' in x:
        print(x)



def from_file_get_data(file_name):
    f = open(file_name,'r')
    line = f.readline()
    user_data = eval(line)
    return user_data



if __name__ == '__main__':
    from_file_get_data('user_data.txt')
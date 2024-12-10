def get_shelfs_book(numbers):
    for number in range(numbers): 
        book_format = {'author':None, 'name':None}
        lines = int(input('На какую полку добавить книгу?:'))
        book_format['name'] = input('Введите название книги:')
        book_format['author'] = input('Введите автора книги:')
        shelf = 'Shelf_{} : {}'.format(lines,book_format)
        with open("Library.txt", "a") as f:
            f.write(f'\n{shelf}')
    return "Книги добавлены"


def  read_file_library():
    with open('Library.txt','r') as f:
        for line in f:
            print(line.strip('\n')) 


def main():
    numbers_books = int(input('Сколько книг надо?:'))
    print(get_shelfs_book(numbers_books))
    read_file_library()

    
if __name__ == '__main__':
    main()
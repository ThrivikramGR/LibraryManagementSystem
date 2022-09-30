from random import randint
import mysql.connector as mysc

def manage(csr):
    '''Management Controls'''
    
    print()
    print('MANAGEMENT CONTROLS:')
    print()    
    
    while True:
        print('1. View All Books')
        print('2. Add Book')
        print('3. Delete Book')
        print('4. Choose Language')
        print('5. Choose Genre')
        print('6. Book Search')
        print('7. Back')
        
        minp=input("Enter required option:")
        print()
        print('*****************************')
    
        '''Each option calls the necessary function'''
    
        if minp=='1':
            viewall(csr)
                
        elif minp=='2':
            add(csr)
    
        elif minp=='3':
           delt(csr)
    
        elif minp == '4':
            lang(csr)
   
        elif minp == '5':
            gen(csr)
   
        elif minp == '6':
            src(csr)

        elif minp == '7':
            break

        else:
            print()
            print('Enter a Valid Choice!')
            print()
            print('*****************************')
            print() 

    return


def read(csr):
    '''Reader Controls'''
    
    print('How can I help?')

    while True:
        print('1. View all Books')
        print('2. Choose Language')
        print('3. Choose Genre')
        print('4. Book Search')
        print('5. Retrive Book')
        print('6. Return Book')
        print('7. Back')
    
        rinp=input("Enter required option:")
        print()
        print('*****************************')

        '''Each option calls the necessary function'''
   
        if rinp == '1':
            viewall(csr)
    
        elif rinp=='2':
            lang(csr)
    
        elif rinp=='3':
            gen(csr)
    
        elif rinp=='4':
            src(csr)
    
        elif rinp=='5':
            retv(csr)
        
        elif rinp=='6': 
            retn(csr)
       
        elif rinp=='7':
            break
    
        else:
            print('Enter a Valid Choice!')
            print()
            print('*****************************')
            print() 
    
    return


def viewall(csr):
    '''Function to View the entire collection of books'''
    
    csr.execute("SELECT * FROM  MainShelf ORDER BY Serial")
    print()
    h=csr.fetchall()
    print()
    print('Total Books:', csr.rowcount)
    print()
            
            
    if h==[]:
        print()
        print('****No Books!****')
        print()
        input('Press Enter to continue...')
        print()
        print('*****************************')
        print()
    else:
        print()
        print('SERIAL | ID | NAME | LANG | GENRE | SHELF | STATUS | READER')
        print()
        for i in h:
            print(i)
        print()
        input("Press Enter to continue...")
        print()
        print('*****************************')
        print()
        
    return


def add(csr):
    '''Function to Add books to all the corresponding tables'''
    
    while True:
        print()
        print("                            BOOK ADDITION")
        print()
        
        bname=(input("Enter Book Name:")).capitalize()
        blang=(input("Enter Book Language (Eng / Hin / Tam) :")).capitalize()
        bgenre=(input("Enter Book Genre (Novel / Ref / Poem ) :")).capitalize()
        print()
        
        rid=randint(1,99999)     #To Assign a random ID to the books
        rshelf=randint(1,25)     #To Decide the shelf number randomly
    
        ins="INSERT INTO MainShelf(ID, Name, Language, Genre, Shelf, Status, Reader) VALUES({}, '{}', '{}', '{}', {}, 'Available', '-')".format(rid, bname.capitalize(), blang.capitalize(), bgenre.capitalize(), rshelf)
        csr.execute(ins)
        cobj.commit()    
    
        if blang=='Eng':  
            ins="INSERT INTO English(ID, Name, Language, Genre, Shelf) VALUES({}, '{}', '{}', '{}', {})".format(rid, bname, blang, bgenre, rshelf)
            csr.execute(ins)
            cobj.commit()

        if blang=='Hin':  
            ins="INSERT INTO Hindi(ID, Name, Language, Genre, Shelf) VALUES({}, '{}', '{}', '{}', {})".format(rid, bname, blang, bgenre, rshelf)
            csr.execute(ins)
            cobj.commit()
        
        if blang=='Tam':  
            ins="INSERT INTO Tamil(ID, Name, Language, Genre, Shelf) VALUES({}, '{}', '{}', '{}', {})".format(rid, bname, blang, bgenre, rshelf)
            csr.execute(ins)
            cobj.commit()
        
        if bgenre=='Novel':  
            ins="INSERT INTO Novels(ID, Name, Language, Genre, Shelf) VALUES({}, '{}', '{}', '{}', {})".format(rid, bname, blang, bgenre, rshelf)
            csr.execute(ins)
            cobj.commit()
        
        if bgenre=='Reference':  
            ins="INSERT INTO Reference(ID, Name, Language, Genre, Shelf) VALUES({}, '{}', '{}', '{}', {})".format(rid, bname, blang, bgenre, rshelf)
            csr.execute(ins)
            cobj.commit()
        
        if bgenre=='Poem':  
            ins="INSERT INTO Poems(ID, Name, Language, Genre, Shelf) VALUES({}, '{}', '{}', '{}', {})".format(rid, bname, blang, bgenre, rshelf)
            csr.execute(ins)
            cobj.commit()
    
        print()
        print('Book Added Successfully!')
        print('Unique ID of the Book is:', rid)
        print('The book is to be placed at shelf:', rshelf)
        print()
        b=input('Add another book? [y/n] :')
        print()
        print()
        
        if b=='n':
            print()
            print('*****************************')
            print()
            break
        
        else:
            print()
            print('*****************************')
            print()
            continue
    
    return    


def delt(csr):
    '''Function to delete book from all the corresponding tables'''

    print()
    print("BOOK DELETION")
    
    while True:
        a=input("Enter Book ID to be deleted (Enter 'b' to go back) :")
        if a=='b':
            print()
            print('*****************************')
            print()
            break
        
        csr.execute('DELETE FROM MainShelf WHERE ID={}'.format(int(a)))  
        cobj.commit()
        
        '''Deleting from main table deletes from
        all other related tables using foreign key relation'''
        
        print()
        print('Book Deleted Successfully!')
        print()
        b=input('Delete another book? [y/n] :')
        print()
        print()
        
        if b=='n':
            print()
            print('*****************************')
            print()
            break
        else:
            print()
            print('*****************************')
            print()
            continue
    
    return


def lang(csr):     
    '''Function to Display the required language books'''
    
    a=input('Enter required language ( Eng / Hin / Tam ) :').capitalize()
    
    if a == 'Eng':    
        csr.execute("SELECT * FROM English ORDER BY Serial")
        print()
        h=csr.fetchall()
        print()
        print('Total Books:', csr.rowcount)
        print()
                    
        if h==[]:
            print()
            print('****No Books!****')
            print()
            input('Press Enter to continue...')
            print()
            print('*****************************')
            print()
    
        else:
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF')
            print()
            for i in h:
                print(i)
            print()
            input("Press Enter to continue...")
            print()
            print('*****************************')
            print()
        
    elif a == 'Tam':    
        csr.execute("SELECT * FROM Tamil ORDER BY Serial")
        print()
        h=csr.fetchall()
        print()
        print('Total Books:', csr.rowcount)
        print()
                    
        if h==[]:
            print()
            print('****No Books!****')
            print()
            input('Press Enter to continue...')
            print()
            print('*****************************')
            print()
    
        else:
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF')
            print()
            for i in h:
                print(i)
            print()
            input("Press Enter to continue...")
            print()
            print('*****************************')
            print()        
        
    elif a == 'Hin':    
        csr.execute("SELECT * FROM Hindi ORDER BY Serial")
        print()
        h=csr.fetchall()
        print()
        print('Total Books:', csr.rowcount)
        print()
                    
        if h==[]:
            print()
            print('****No Books!****')
            print()
            input('Press Enter to continue...')
            print()
            print('*****************************')
            print()
    
        else:
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF')
            print()
            for i in h:
                print(i)
            print()
            input("Press Enter to continue...")
            print()
            print('*****************************')
            print()
    
    else:
        return
    
    return    


def gen(csr):
    '''Function to Display the required genre books'''
    
    a=input("Enter Book Genre ( Novels / Ref / Poems ) :").capitalize()
    
    if a == 'Novels':    
        csr.execute("SELECT * FROM Novels ORDER BY Serial")
        print()
        h=csr.fetchall()
        print()
        print('Total Books:', csr.rowcount)
        print()
                    
        if h==[]:
            print()
            print('****No Books!****')
            print()
            input('Press Enter to continue...')
            print()
            print('*****************************')
            print()
    
        else:
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF')
            print()
            for i in h:
                print(i)
            print()
            input("Press Enter to continue...")
            print()
            print('*****************************')
            print()
        
    elif a == 'Ref':    
        csr.execute("SELECT * FROM Reference ORDER BY Serial")
        print()
        h=csr.fetchall()
        print()
        print('Total Books:', csr.rowcount)
        print()
                    
        if h==[]:
            print()
            print('****No Books!****')
            print()
            input('Press Enter to continue...')
            print()
            print('*****************************')
            print()
    
        else:
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF')
            print()
            for i in h:
                print(i)
            print()
            input("Press Enter to continue...")
            print()
            print('*****************************')
            print()        
        
    elif a == 'Poems':    
        csr.execute("SELECT * FROM Poems ORDER BY Serial")
        print()
        h=csr.fetchall()
        print()
        print('Total Books:', csr.rowcount)
        print()
                    
        if h==[]:
            print()
            print('****No Books!****')
            print()
            input('Press Enter to continue...')
            print()
            print('*****************************')
            print()
    
        else:
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF')
            print()
            for i in h:
                print(i)
            print()
            input("Press Enter to continue...")
            print()
            print('*****************************')
            print()
    
    else:
        return
    
    return


def src(csr):
    '''Function to Search any required book'''
    
    while True:
        c=input("Do you want to search by Book ID (id) or Book Name (name) [Enter 'b' to go back'] : ").capitalize()
    
        if c=='Name':
            '''Search by Name'''
            
            a=input("Enter partial or full book name :").capitalize()
            csr.execute("SELECT * FROM MainShelf WHERE Name LIKE '{}' ORDER BY Serial".format(a+'%'))
            h=csr.fetchall()
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF | STATUS | READER')
            print()
            for i in h:
                print(i)
            print()
       
        elif c=='Id':
            '''Search by ID'''
            
            b=int(input("Enter Book ID:"))
            csr.execute("SELECT * FROM MainShelf WHERE ID = {}".format(b))
            print()
            print()
            print('SERIAL | ID | NAME | LANG | GENRE | SHELF | STATUS | READER')
            print()
            print(csr.fetchone())
            print()
        
        else:
            break
        
        l=input("Do you want to search another book? [y/n] :")
        print()
        print()
        
        if l=='n':
            print()
            print('*****************************')
            print()
            break
        
        else:
            print()
            print('*****************************')
            print()
            continue
            
    return


def retv(csr):
    '''Function to update retrival status of any book along with retriver's name'''
    
    a=int(input("Enter ID of book retrived ( View all books to check availability ):"))
    b=input("Enter reader name:")
    csr.execute("UPDATE MainShelf SET Status = 'In Use', Reader = '{}' WHERE ID = {}".format(b,a))
    cobj.commit()
    
    print()
    print("Retrival Recorded!")
    print()
    input('Press Enter to continue...')
    print()
    print('*****************************')
    print()
    
    return


def retn(csr):
    '''Function to update book return status for retrived books''' 
    
    a=int(input("Enter Book ID to be returned:"))
    csr.execute("UPDATE MainShelf SET Status='Available', Reader = '-' WHERE ID = {}".format(a))
    cobj.commit()
    
    print()
    print("Return Recorded!")
    print()
    input('Press Enter to continue...')
    print()
    print('*****************************')
    print()
    
    return     


"""MAIN"""

cobj=mysc.connect(host='localhost', user='root', passwd='4321', database='LibProject')
csr=cobj.cursor()


print()
print('                   SARATHA INTERNATIONAL SCHOOL')
print()
print('                        LIBRARY MANAGEMENT') 
print()

while True:
    ctrl=input("            Do you want to Manage(m), Read(r) or Exit(e):")
    print()
    
    '''Each option calls the necessary function'''
    
    if ctrl=='m':
        manage(csr)

    elif ctrl=='r':
        read(csr)

    elif ctrl=='e':
        break
    
    else:
        print('Enter valid choice!')
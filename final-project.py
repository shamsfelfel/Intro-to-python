# initiate file
import os

# ترتيب العناصر في السجل
nem_index = 0
Type_index = 1
number_index = 2

# خيارات القائمة الرئيسية
Add_contact = "1"
Search_name = "2"
Search_number = "3"
Delete_name = "4"
Delete_numder = "5"
Show_all= "6"
Exit= "7"

# ل التعرف على الفروق الطفيفة با الاسماء 
def is_similar(name1,name2):

    if abs(len(name1) - len(name2)) > 2:
        return False
    
    if len(name1) > len(name2):
        lang=name1.lower()
        shart=name2.lower()
    else:
        lang=name2.lower()
        shart=name1.lower()
    
    daf=0
    for i in range(len(shart)):
        if lang[i] != shart[i]:
            daf += 1
            
     
    if daf >2:
         return False
    else:
         return True

def has_number(numbers , number):
    for valey in numbers:
        if valey == number:
            return True
    return False

def new_number(number):
    new = True
    for contact in contacts:
        if has_number(contact[number_index], number):
            new = False
            break
    return new
       
# قراة عدد غير محدد من الارقام في قائمة
def get_numbers():
    numbers=[]
    while True :
        number=int(input("Enter number or 0 to end: "))
        if number == 0:
            break
        else:
            if new_number(number):
                numbers.append(number)
            else:
                print("is not new number.")
                input("press enter to continue ..") 
                
                
    return numbers



# طباعة عنصر واحد من جهات الاتصال
def print_contact(contact) :
    print(f"Name: {contact[nem_index]}, Type: {contact[Type_index]}, Numbers: {contact[number_index]}") 

# طباعة لوحة التبديل الرئيسية
def menu():
    
    os.system("cls")
    
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║  Welcome to our Address book,please to find what you want            ║")
    print("╠══════════════════════════════════════════════════════════════════════╣") 
    print("║      1.Add new contact.                                              ║")
    print("║      2.Search by name.                                               ║")
    print("║      3.Search by number.                                             ║")
    print("║      4.Delete contact by name.                                       ║")
    print("║      5.Delete contact by number.                                     ║")
    print("║      6.Show all contacts.                                            ║")
    print("║      7.Exit.                                                         ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    return input("Enter your choice(1,7) :")

# البحث بدلالة الرقم
def find_by_number(number):
    
    found = False 
    for contac in contacts:
        if has_number(contac[number_index],number):
            found = True
            break
    
    if found:
        return  contac  
    else:
        return("Not found")
 
 # اضافة حهة اتصال       

# اضافة جهة اتصال
def add_new_contact():
    name= input("name: ")
    type= input("type: ")
    if type not in ["Family", "Personal", "Work", "Other"]:
        type = "Other"

    number =  get_numbers()
    exist = find_by_number(number)
    if exist=="Not found":
        contacts.append([name , type ,number])      
    else:
        print("Error! numder is found")
        input("press enter to continue ..")       

# طباعة كل جهات الاتصال
def show_All_contacts():
    if len(contacts)==0:
        print("No contacts stored yet")
    else: 
        for contact in contacts:
            print_contact(contact)
       
# البحث بدلالة الاسم
def find_by_name(name):
    
    found = False 


    for contact in contacts:
        if is_similar(contact[nem_index] , name):
            found = True
            break
    
    if found:
        return  contact  
    else:
        return("Not found") 
 
    
# قائمة جهات الاتصال            
contacts=[]
 
# البرنامج الرئيسي         
while True:
    
    choice = menu()
    # اذا تم اختيار الخيار 7 يتم انهاء البرنامج
    if choice==Exit:
        print("Good bye")
        break
    # اذا تم اختيلر الخيار رقم 1 يضيف جهة اتصال
    elif choice == Add_contact:
        add_new_contact()
        
# اذا تم اختيار الخيار رقم 3 يبحث بدلالة الرقم
    elif choice == Search_number :
        mobile=int(input("Search by Number: "))
        exist=find_by_number(mobile)
        
        if  exist=="Not found":
            print("Not found")
            input("press enter to continue ..")   
        else:
            print_contact(exist) 
            input("press enter to continue ..")
    
 # اذا تم اختيار خيار رقم 6 يتم طباعة جهة الاتصال
    elif  choice == Show_all:
         show_All_contacts()
         input("press enter to continue ..")
         
 #  اذا تم اختيار الخيار رقم 2 يتم البحث بلالة الاسم
    elif choice ==  Search_name:
        search_name=input("Search by name: ")
        exist=find_by_name(search_name)
        
        if  exist=="Not found":
            print("Not found")
            input("press enter to continue ..")   
        else:
            print_contact(exist) 

            input("press enter to continue ..")
            
 # اذا تم اختيار الخيار رقم 4 ستم حذف جهة الاتصال بدلالة الاسم
    elif choice == Delete_name:
        name_to_Delete=input("name to Delete: ")
        exist=find_by_name(name_to_Delete)
        
        if  exist=="Not found":
            print("Not found")
            input("press enter to continue ..")   
        else:
            contacts.remove(exist)
            print(contacts) 
            input("press enter to continue ..")
            
 # اذا تم اختيا الخيار رقم  5 يتم حذف جهة اتصال بدلالة الرقم
    elif choice == Delete_numder:
        number_to_Delete= int(input(" number to Delete: "))
        exist=find_by_number(number_to_Delete)
        
        if  exist=="Not found":
            print("Not found")
            input("press enter to continue ..")   
        else:
            contacts.remove(exist)
            print(contacts) 
            input("press enter to continue ..")
            
            
# اذا تم اختيار خيار غير موجود با القائمة  يطبع       
    else:
        print("Invalid choice, please try again.")

        input("press enter to continue ..")  
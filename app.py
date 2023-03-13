import csv 
import datetime
import os
from create_menu_file import create_menu


#Pizza üst sınıfı
class Pizza:
    def __init__(self, name, description, price):
        self.__name = name
        self.__description = description
        self.__price = price

    def get_description(self):
        return self.__description

    def get_cost(self):
        return self.__price


#Pizza sınıfının alt sınıfları
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", "Classic Italian pizza topped with tomato sauce, mozzarella cheese and basil leaves", 20)

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", "One of the most popular types of Italian pizza, topped with tomato sauce, mozzarella cheese and basil leaves", 25)

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", "It is a type of pizza from Turkish cuisine and is topped with sausage, cheddar cheese, tomatoes and peppers.", 30)

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", "The most popular pizza from an international pizza chain, with a variety of toppings", 35)



# Decorator sınıfı, tüm sosların üst sınıfı yani süper sınıfı
class Decorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description()

    def get_cost(self):
        return self._pizza.get_cost()


#Soslar, alt sınıflar
class TomatoSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Tomato Sauce"
        self.__price = 5

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price


class Cheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Cheddar Cheese"
        self.__price = 10

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price


class Mushroom(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Mushroom"
        self.__price = 8

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price

class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Olive"
        self.__price = 6

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price

class MushroomSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Mushroom Sauce"
        self.__price = 7

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price

class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Goat Cheese"
        self.__price = 9

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price

class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Meat Sauce"
        self.__price = 12

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price

class Onion(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Onion Sauce"
        self.__price = 5

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price

class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.__description = "Corn"
        self.__price = 4

    def get_description(self):
        return self._pizza.get_description() + f", {self.__description}"

    def get_cost(self):
        return self._pizza.get_cost() + self.__price


#Ödeme yapma fonksiyonu
def make_payment(cc_number, cc_password):
    # Burada kredi kartı numarası ve şifresinin doğru olduğunu kontrol edeceğiz.
    # Amount eklenebilir.
    # İşlem başarılıysa True döndüreceğiz, aksi halde False.
        if len(cc_number) == 10 and cc_password == "1234":
            #ödeme  
            return True
        else:
            return False

# Verileri csv dosyasına kaydeden fonksiyon
def save_order(name, surname, tc_id, credit_card_number, credit_card_password, order_description, order_time, payment, total_cost):
        folder_name = "Log_Documents"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

        file_name = "{}/Orders_Database.csv".format(folder_name)
        headers = ["Name","Surname","ID","Credit Card Number","Credit Card Password","Description","Time","Payment","Total Cost"]

        with open(file_name, mode="a", newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(headers)
            writer.writerow([name,surname,tc_id,credit_card_number,credit_card_password,order_description,order_time,payment, total_cost])


#Main fonksiyonu 
if __name__ == '__main__':
    #Menü içerikleri txt uzantılı dosyaya yazdırır ve kapatır.
    create_menu() 
    # Menüyü ekrana yazdır
    print("Welcome! Please choose a pizza and sauce from the menu: \n-----------------------------------------------\n1. Classic Pizza\n2. Margherita Pizza\n3. Turkish Pizza\n4. Dominos Pizza\n-----------------------------------------------\nSauces:\n1. Olive Sosu\n2. Mushroom Sosu\n3. Goat Cheese\n4. Meat Sauce\n5. Onion\n6. Corn\n-----------------------------------------------")

    pizzas = []
    total_cost = 0
    while True:
        #Kullanıcıyı doğru veri tipi ile seçim yaptırmaya zorlamak için döngü
        #Integer veri tipi girilmediği sürece döngü sonlanmayacak.
        # Kullanıcının pizza seçimi
        while True:
            try:        
                pizza_choice = int(input("Choose pizza (1-4), or 0 to finish: "))
                break
            except ValueError:
                print("Incorrect data type. Please try again.")

        if pizza_choice == 0:
            break
        elif pizza_choice == 1:
            pizza = ClassicPizza()
        elif pizza_choice == 2:
            pizza = MargheritaPizza()
        elif pizza_choice == 3:
            pizza = TurkishPizza()
        elif pizza_choice == 4:
            pizza = DominosPizza()
        else:
            print("Invalid selection!")         
        
        #Kullanıcının sos seçimi
        while True:
            try:
                sos_choice = int(input("Choose sauce (1-6), or 0 to finish: "))
                break
            except ValueError:
                print("Incorrect data type. Please try again.")
        

        # Seçilen sosu oluştur ve pizzaya ekle
        if sos_choice == 0:
            break
        elif sos_choice == 1:
            sos = Olive(pizza)
        elif sos_choice == 2:
            sos = MushroomSauce(pizza)
        elif sos_choice == 3:
            sos = GoatCheese(pizza)
        elif sos_choice == 4:
            sos = Meat(pizza)
        elif sos_choice == 5:
            sos = Onion(pizza)
        elif sos_choice == 6:
            sos = Corn(pizza)
        else:
            print("Invalid selection!")
            # Toplam fiyatı hesapla
        cost = sos.get_cost()
        pizzas.append(cost)
        for i in pizzas:
            total_cost += i 
        

    # Kullanıcı bilgilerini al
    name = input("Name : ").capitalize()
    surname = input("Surname: ").capitalize()
    tc_id = input("Identity Number: ")
    credit_card_number = input("Credit Card Number: ")
    credit_card_password = input("Credit Card Password: ")
    order_description = sos.get_description()
    order_time = datetime.datetime.now()
    payment = "Successful"

    # Ödeme işlemini tamamla
    payment_successful = make_payment(credit_card_number, credit_card_password)


    if payment_successful:
        # Sipariş onayını yazdır
        print("Payment {}! Your order is being prepared...\nOrder details: \nTime: {}:{}\nPizza: {}\nTotal: $ {}\nName Surname: {} {}\nIdentity Number: {}".format(payment,order_time.hour, order_time.minute,order_description,total_cost,name,surname,tc_id))
    else:
        print("The checkout process failed. Please check your credit card details.")
        payment = "Failed"
        total_cost = 0

    # Verileri csv dosyasına kaydet
    save_order(name=name,surname=surname,tc_id=tc_id,credit_card_number=credit_card_number,credit_card_password=credit_card_password,order_description=order_description,order_time=order_time, payment=payment,total_cost=total_cost)

        


       


    
    



    











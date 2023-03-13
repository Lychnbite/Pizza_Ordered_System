import os 

data = """
* Lütfen Bir Pizza Tabanı Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza
* ve seçeceğiniz sos:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan
16: Mısır
* Teşekkür ederiz!
"""

folder_name = "Log_Documents"
file_name = "Menu.txt"
file_path = os.path.join(folder_name, file_name)



if not os.path.exists(folder_name):
    os.mkdir(folder_name)



def create_menu():
    with open(file_path,"w") as file:
        file.writelines(data)


if __name__ == '__main__':
    create_menu()
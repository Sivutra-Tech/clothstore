import time
import csv

class warehouse:
    storageShirt = {}
    storagePant = {}
    storageShoe = {}
    def __init__(self):
        with open("access_log.txt","a") as file:
                file.write(f"{warehouse.__access_logging()}\n")
        with open("items.csv") as file: 
            reader = csv.DictReader(file)
            for colum in reader:
                if colum["Catergory"] == "Shoe":
                    finalStrippedID = colum["ID"].replace(",","")
                    warehouse.storageShoe[finalStrippedID] = list([colum["Name"],colum["Price"],colum["Stock"]])
                elif colum["Catergory"] == "Shirt":
                    finalStrippedID = colum["ID"].replace(",","")
                    warehouse.storageShirt[finalStrippedID] = list([colum["Name"],colum["Price"],colum["Stock"]])
                elif colum["Catergory"] == "Pant":
                    finalStrippedID = colum["ID"].replace(",","")
                    warehouse.storagePant[finalStrippedID] = list([colum["Name"],colum["Price"],colum["Stock"]])
                elif colum["Catergory"] == "":
                    break
    def __access_logging():
        return f"Access Granted At {time.ctime()}"
    def __payment_logging(Price):
        with open("payment_log.txt","a") as file:
            file.write(f"${Price} has been paid\n")
    def __stock_logging(ID):
        with open("stock_log.txt","a") as file:
            file.write(f"Item with ID ({ID}) stock has been reduced as it has been sold\n")
    def purchase_log(self,ID,price):
        warehouse.__stock_logging(ID)
        warehouse.__payment_logging(price)
    def print(self,whichStorage):
        if whichStorage.lower() == "shoe":
            print("ID : Price : Name : In Stock")
            for key,value in self.storageShoe.items():
                print(f"{key} : ${value[1]} : {value[0]} : {value[2]}")              
        elif whichStorage.lower() == "pant":
            print("ID : Price : Name")
            for key,value in self.storagePant.items():
                print(f"{key} : ${value[1]} : {value[0]} : {value[2]}")      
        elif whichStorage.lower() == "shirt":
            print("ID : Price : Name")
            for key,value in self.storageShirt.items():
                print(f"{key} : ${value[1]} : {value[0]} : {value[2]}")
        else:
            raise Exception("Failed in accessing storages")
    def get_shoe_price(self,ID):
        for key,value in self.storageShoe.items():
            if int(key) == int(ID):
                return value[1]
    def get_pant_price(self,ID):
        for key,value in self.storagePant.items():
            if int(key) == int(ID):
                return value[1]
    def get_shirt_price(self,ID):
        for key,value in self.storageShirt.items():
            if int(key) == int(ID):
                return value[1]
    def check_ID(self,ID,whichStorage):
        if whichStorage.lower() == "shoe":
            for key,value in self.storageShoe.items():
                if int(key) == int(ID):
                    return True
        elif whichStorage.lower() == "pant":
            for key,value in self.storagePant.items():
                if int(key) == int(ID):
                    return True   
        elif whichStorage.lower() == "shirt":
            for key,value in self.storageShirt.items():
                if int(key) == int(ID):
                    return True
        else:
            return False
        
    ## below functions are broken!!! cool idea, but can not do it yet
    #-------
    def add_storageShoe(self,ID):
        for key,value in self.storageShoe.items():
            if int(key) == int(ID):
                value[2] = int(value[2])
                value[2] += 1
                with open("items.csv","") as file:
                    #MANUALL
                    colums = ["Catergory","ID","Name","Price","Stock"]
                    warehouse.__access_logging()
                    writer = csv.DictWriter(file,fieldnames=colums)
                    writer.writeheader()
                    writer.writerows(self.storageShoe)                  
    def add_storagePant(self,ID):
        for key,value in self.storagePant.items():
            if int(key) == int(ID):
                value[2] = int(value[2])
                value[2] += 1
    def add_storageShirt(self,ID):
        for key,value in self.storageShirt.items():
            if int(key) == int(ID):
                value[2] = int(value[2])
                value[2] += 1
    #--------










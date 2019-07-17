class Car():
    def __init__(self,paizi,xinghao,year):
        self.paizi=paizi
        self.xinghao=xinghao
        self.year=year
        self.lucheng=0
    def descriptive(self):
        long_name=str(self.year)+' '+self.paizi+' '+self.xinghao

        print(long_name)
    def read_lucheng(self):
        print("The car has run "+str(self.lucheng)+' miles.')
    def update_lucheng(self,miles):
        if miles>=self.lucheng:
            self.lucheng=miles
        elif miles<self.lucheng:
            print("You can't roll back")

class Electric(Car):
    def __init__(self,paizi,xinghao,year):
        super().__init__(paizi,xinghao,year)
        self.battery_size=100
    def describe_battery(self):
        print("The car has a "+str(self.battery_size)+" -kwh battery.")
my_tesla=Electric('tesla','model',2013)
my_tesla.descriptive()
my_tesla.describe_battery()
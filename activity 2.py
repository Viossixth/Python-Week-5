class car:
    def __init__(self,model="991.2 GT2 RS",name="Hellhound", color="silver",package="Weissach Package",model_year="2018",price="R8 Million"):
            self.model = model
            self.name = name
            self.color = color 
            self.package = package
            self.model_year = model_year
            self.price = price

    def move(self):
         return "drive"

    def show_name(self):
        print(f"Hello I am {self.name}")

    def show_color(self):
        print(f"{self.name} is {self.color}")

    def show_model(self):
        print(f"I am a {self.model}")

    def show_package(self):
        print(f"{self.name} has a {self.package}")

    def show_price(self):
        print(f"{self.name} is for sale for {self.price}")

#Activity 2

class airplane:
     def move(self):
          return "fly"
     
for transport in [airplane(),car()]:
    print(transport.move())
         





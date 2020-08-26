from Chess_Board import Properies
from Chess_Board import AuxiliarClass
from Chess_Board import messages
from Chess_Board import values_of_chips
# This class contain all the movemets in the chips and attack

# messages.next_position()
# messages.next_position()


class chips_of_game(AuxiliarClass):
    def attack(self, eaten, attaker):
        self.eat_in_chess(eaten, attaker)

    def update_chip_position(self, new_value):
        self.new_value = new_value
        counter = 0
        self.search_of_chips(self.entry_2)
        if self.chip_position[0] == messages.entry_1[0] and self.position_y == messages.entry_1[1]:
            for x in values_of_chips[self.color][self.chip_type]:
                if self.value == x:
                    values_of_chips[self.color][self.chip_type][counter] = self.new_value
                counter += 1


#chips_on_game = chips_of_game(9, 9, 'red')


class play(AuxiliarClass):
    def case_1(self, value_1):
        self.value_1 = value_1
        self.play()
        self.colors(self.value_1)
        self.search_of_chips(self.entry_1) #Esto busca si hay una ficha en la ingresada
        self.next_position() #Te pide la posicion
        self.dont_eat_your_team(self.entry_2)
        self.auxiliar_function() #Me permite agregar manejar mejor el rango del movimiento de la ficha
        self.movements_chips()  
        print(self.count)
        print(self.color)
        print(self.value_range)
        print( self.rules_for_chips(self.chip_position,self.value_range)       )            #Reglas de las fichas si se mueve
        self.cop_1 = int(self.chip_position[0])
        self.cop_2 = self.chip_position[1]
        print(self.cop_1,self.cop_2)
      #  self.operating_system() #Limpia la consola cada cierto tiempo
       # self.search_of_chips(self.entry_2) 
        
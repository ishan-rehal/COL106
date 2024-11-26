'''
    Python file to implement the class CrewMate
'''
from heap import Heap
from treasure import Treasure
class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.load = 0
        # min_id_comparator = lambda x, y: x.id < y.id
        self.treasures = []
        self.completion_time = 0
        
    def add_treasure(self,treasure):
        self.treasures.append(treasure)
        if(treasure.arrival_time>=self.completion_time):
            self.completion_time = treasure.arrival_time + treasure.size
        else:
            self.completion_time += treasure.size
    pass
    
    def deep_copy(self):
        # Create a new instance of CrewMate
        new_crewmate = CrewMate()
        
        # Copy all attributes from self to new_crewmate
        new_crewmate.load = self.load
        
        # Deep copy each treasure in the treasures list
        new_crewmate.treasures = [treasure.deep_copy() for treasure in self.treasures]
        
        # Copy other attributes as needed
        # ...
        
        return new_crewmate
    
    # Add more methods if required
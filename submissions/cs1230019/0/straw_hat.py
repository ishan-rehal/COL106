'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        temp = []
        for i in range(m):
            temp.append(CrewMate())
        min_completion_time_comparator = lambda x, y: x.completion_time < y.completion_time
        self.crew = Heap(min_completion_time_comparator, temp)
        
        min_id_comparator = lambda x, y: x.id < y.id
        self.treasures = Heap(min_id_comparator,[])
        self.working_crew = []
        
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        temp_crewmate = self.crew.extract()
        if(temp_crewmate.completion_time==0):
            self.working_crew.append(temp_crewmate)
        temp_crewmate.add_treasure(treasure)
        self.crew.insert(temp_crewmate)
        self.treasures.insert(treasure)
        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        temp = self.treasures.to_sorted_list()
        for i in temp:
            i.completion_time = None
        # Make a deep copy of self.working_crew without using copy module
        deep_copy_of_working_crew = [crewmate.deep_copy() for crewmate in self.working_crew]
        
        def priority_comparator(x, y):
            if x.arrival_time + x.size < y.arrival_time + y.size:
                return True
            elif x.arrival_time + x.size > y.arrival_time + y.size:
                return False
            else:
                return x.id < y.id
            
        ans=[]
        
        for crewmate in deep_copy_of_working_crew:
            for i in range(len(crewmate.treasures)):
                ans.append(crewmate.treasures[i])
        
        for crewmate in deep_copy_of_working_crew:
            temp_treasures = Heap(priority_comparator, [crewmate.treasures.pop(0)])
            simulation_time = temp_treasures.top().arrival_time
            counter=0
            
            while(temp_treasures.size>0): 
                # if(counter==10):
                #     break
                # counter+=1
                # print("simulation_time",simulation_time)
                # temp = sorted(ans, key=lambda treasure: treasure.id)
                # for i in temp:
                #     print(i.id,i.arrival_time,i.size,i.completion_time)
                
                cur_treasure = temp_treasures.extract()
                if(len(crewmate.treasures)>0):
                    if(cur_treasure.arrival_time>simulation_time):
                        simulation_time=cur_treasure.arrival_time
                    if(crewmate.treasures[0].arrival_time >= simulation_time + cur_treasure.size):
                        cur_treasure.completion_time = simulation_time + cur_treasure.size 
                        simulation_time += cur_treasure.size
                        # cur_treasure.size = 0 
                        temp_treasures.insert(crewmate.treasures.pop(0)) 
                    else:
                        cur_treasure.size = cur_treasure.size - (crewmate.treasures[0].arrival_time - simulation_time)
                        simulation_time = crewmate.treasures[0].arrival_time
                        temp_treasures.insert(cur_treasure)
                        temp_treasures.insert(crewmate.treasures.pop(0))
                        
                else:
                    if(cur_treasure.arrival_time>simulation_time):
                        simulation_time=cur_treasure.arrival_time
                    cur_treasure.completion_time = simulation_time + cur_treasure.size
                     
                    simulation_time += cur_treasure.size 
                    # cur_treasure.size = 0
                    
        ans = sorted(ans, key=lambda treasure: treasure.id)
        return ans
        pass
    
    
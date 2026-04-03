class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # in order to solve this problem we have to keep in mind one very intuitive formula
        # speed=distance/time 
        # distance = end_position(target)- starting_position(position[i])
        # it's done !
        #we calculate the time to reach the target for each of the cars, if two cars have the same time 
        #they are part of the same fleet
        # this means we need to sort the cars by time_to_reach_target
        # we need to keep track of the actual positions of the cars as well
        # so we create a new  array in which we store =(position[i], time_to_target[i])
        # we sort this array by time_to_target
        # every group of cars with the same time_to_target is a fleet 
        
        n=len(position)
        time=[]

        for p,s in zip(position,speed):
            t=(target-p)/s
            time.append((p,t))
        
        # we compute time but now who is in front of who + which car should i compare first
        
        time.sort(key=lambda x: x[0], reverse=True)
        
        # target=12
        # position=[10,8,0,5,3]
        # speed=[2,4,1,1,3]
        #[(10, 1.0), (8, 1.0),(0, 12.0), (5, 7.0), (3, 3.0)]
        #sort by position 
        #[(0, 12.0),(3, 3.0),(5, 7.0),(8, 1.0),(10, 1.0)]

        current_fleet_time=0
        fleets=0
        for p,t in time:
            if t>current_fleet_time:
                fleets+=1
                current_fleet_time=t
            else:
                continue
        return fleets
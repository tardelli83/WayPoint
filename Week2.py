from abc import ABC, abstractmethod

class Distance:
    def __init__(self, magnitude, unit):
        if magnitude < 0:
            raise ValueError("Magnitude cannot be negative.")
        self.magnitude =magnitude
        self.unit =unit


    def convert(self, target_unit):
        if target_unit == self.unit:
            return Distance(self.magnitude, target_unit)
        elif self.unit == 'km':
            new_magnitude=self.magnitude/1.60934
            return Distance(new_magnitude, target_unit)
        elif self.unit == 'mi':
            new_magnitude=self.magnitude*1.60934
            return Distance(new_magnitude, target_unit)
        else:
            raise ValueError("Unit must be 'mi' or 'km'.")

    def __str__(self):
        return f'{self.magnitude:.2f} {self.unit}'

    def __repr__(self):
        return f"Distance {self.magnitude} {self.unit}"

    def __add__(self, other):
        if(self.unit==other.unit):
            new_magnitude=self.magnitude + other.magnitude
        else:
            converted_other=other.convert(self.unit)
            new_magnitude=self.magnitude+converted_other.magnitude
        return Distance(new_magnitude, self.unit)

    def __sub__(self, other):
        if(self.unit==other.unit):
            new_magnitude=self.magnitude - other.magnitude
        else:
            converted_other=other.convert(self.unit)
            new_magnitude=self.magnitude-converted_other.magnitude
        return Distance(new_magnitude, self.unit)

    def __eq__(self, other):
        converted_other=other.convert(self.unit)
        return self.magnitude==converted_other.magnitude

    def __lt__(self, other):
        converted_other=other.convert(self.unit)
        return self.magnitude<converted_other.magnitude

class Trail:
    default_unit = 'km'

    def __init__(self,id,name,distance,elevation_gain_m,difficulty):
        self.id = id
        self.name = name

        if isinstance(distance, (int, float)):
            self.distance = Distance(distance, Trail.default_unit)
        else:
            self.distance = distance

        self.elevation_gain_m = elevation_gain_m
        self.set_difficulty(difficulty)

    def get_difficulty(self):
        return self._difficulty

    def set_difficulty(self,difficulty):
        if difficulty not in ['easy', 'moderate', 'hard']:
            raise ValueError("Unit must be 'easy' or 'moderate' or 'hard'.")
        self._difficulty = difficulty

    @classmethod
    def set_default_unit(cls, new_unit):
        if new_unit not in ['km', 'mi']:
            raise ValueError("Unit must be 'mi' or 'km'.")
        cls.default_unit = new_unit

    @classmethod
    def from_dict(cls,data):
        return cls(
            data['id'],
            data['name'],
            data['distance'],
            data['elevation_gain_m'],
            data['difficulty']
        )

    @staticmethod
    def validator(difficulty):
        if difficulty.lower() not in {'easy', 'moderate', 'hard'}:
            raise ValueError("Difficulty must be 'easy' or 'moderate' or 'hard'.")
        return True

    def __eq__(self, other):
        return self.id==other.id

    @abstractmethod
    def estimated_time(self):
        pass

    @abstractmethod
    def summary(self):
        pass



class DayHike(Trail):
    def __init__(self,id,name,distance,elevation_gain_m,difficulty):
        super().__init__(id,name,distance,elevation_gain_m,difficulty)

    def estimated_time(self):
        '''
        I assume an average pace of 4 Km/h and I assume that every 100 m of elevation gain are
        equivalent to 1000 m of plane hiking
        '''
        return (self.distance.magnitude + (self.elevation_gain_m/100)/4)

    def summary(self):
        print(f"The DayHike {self.name} Trial is {self.distance.magnitude:.2f} Km long."
              f"The difficulty is {self._difficulty} and "
              f"the estimated time to complete is {self.estimated_time()}"
              )


class BackpackingRoute(Trail):
    def __init__(self,id,name,distance,elevation_gain_m,difficulty):
        super().__init__(id,name,distance,elevation_gain_m,difficulty)

    def estimated_time(self):
        '''
        I assume an average pace of 3 Km/h due to the weight of the backpack.
         I assume also that every 100 m of elevation gain are
        equivalent to 1500 m of plane hiking
        '''
        return (self.distance.magnitude + ((self.elevation_gain_m*1.5)/100))/3

    def summary(self):
        print(f"The BackpackingRoute {self.name} Trial is {self.distance.magnitude:.2f} Km long."
              f"The difficulty is {self._difficulty} and "
              f"the estimated time to complete is {self.estimated_time()}"
              )

class TrailRun(Trail):
    def __init__(self,id,name,distance,elevation_gain_m,difficulty):
        super.__init__(id,name,distance,elevation_gain_m,difficulty)

    def estimated_time(self):
        '''
        I assume an average pace of 8 Km/h because they run.
         I assume also that every 100 m of elevation gain are
        equivalent to 1000 m of plane running
        '''
        return (self.distance.magnitude + ((self.elevation_gain_m)/100))/8

    def summary(self):
        print(f"The BackpackingRoute {self.name} Trial is {self.distance.magnitude:.2f} Km long."
              f"The difficulty is {self._difficulty} and "
              f"the estimated time to complete is {self.estimated_time()}"
              )

class GuidedDayHaike(DayHike):
    def __init__(self,id,name,distance,elevation_gain_m,difficulty, guide_name):
        super().__init__(id,name,distance,elevation_gain_m,difficulty)
        self.guide_name = guide_name

    def summary(self):
        print(f"The BackpackingRoute {self.name} Trial is {self.distance.magnitude:.2f} Km long."
              f"The difficulty is {self._difficulty} and "
              f"the estimated time to complete is {self.estimated_time()}. "
              f"The Guide name is {self.guide_name}"
              )


class Itinerary():
    def __init__(self, trials=None):
        self.trials = list(trials) if trials else []

    def add_trial(self, trial):
        self.trials.append(trial)

    def total_distance(self):
        if len(self.trials) == 0:
            return Distance(0, 'km')
        else:
            new_unit = self.trials[0].distance.unit
            total_distance = 0
            for t in self.trials:
                converted_dist = t.distance.convert(new_unit)
                total_distance += converted_dist.magnitude
        return Distance(total_distance, self.trials[0].distance.unit)


def main():
    d1=GuidedDayHaike(1,'Bello',5,100,'easy','Aldo')
    d1.summary()






if __name__ == '__main__':
    main()


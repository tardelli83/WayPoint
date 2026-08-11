from abc import ABC, abstractmethod

class ElevationMixin:
    def grade_percentage(self):
        '''
               Function name: grade_percentage()
               Developer Name: Emilio Palermo
               Date: 11th August 2026

               The function is used to calculate the average percentage slope of the trail

               Parameters: Nothing
               :return: A float number that indicates the average percentage slope

        '''
        distance_meters = self.distance.convert('km').magnitude * 1000
        if distance_meters == 0:
            return 0.0
        return (self.elevation_gain_m / distance_meters) * 100

class RatingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._rating = None

    def set_rating(self, stars):
        '''Function
        name: grade_percentage()
        Developer
        Name: Emilio Palermo
        Date: 11th August 2026

        The function is used to set and validate the rating of the trail

        Parameters: Nothing
        :return: Nothing
        '''

        if not (1 <= stars <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self._rating = stars

    def get_rating(self):
        '''
        Function
        name: grade_percentage()
        Developer
        Name: Emilio Palermo
        Date: 11th August 2026

        The function is used to return rating of the trail if the trail is properly rated

        Parameters: Nothing
        :return: a number that indicates the rating of the trail
        '''
        return self._rating if self._rating else 'Not rated'

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

    def __gt__(self, other):
        converted_other=other.convert(self.unit)
        return self.magnitude>converted_other.magnitude

class Trail(ABC):
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
        Function name: estimated_time()
        Developer Name: Emilio Palermo
        Date: 10th August 2026

        Overrides Trail.estimated_time.

        The function is used to calculate the estimated time of completion of the trial.
        For the calculation, I assume an average pace of 4 Km/h and I assume that every 100 m
        of elevation gain are equivalent to 1000 m of plane hiking

        Parameters: Nothing
        :return: A float number that indicates the estimated time

        '''
        return (self.distance.magnitude + (self.elevation_gain_m/100)/4)

    def summary(self):
        '''
                Function name: summary
                Developer Name: Emilio Palermo
                Date: 10th August 2026

                Overrides Trail.summary.

                The function is used to return a summary of the main information of the trial

                Parameters: Nothing
                :return: A string that indicates name, distance, difficulty and estimated time
        '''
        return (f"The {self.name} is {self.distance}. "
                f"The difficulty is {self._difficulty} "
                f"and the estimated time to complete is {self.estimated_time()}.")


class BackpackingRoute(Trail):
    def __init__(self,id,name,distance,elevation_gain_m,difficulty):
        super().__init__(id,name,distance,elevation_gain_m,difficulty)

    def estimated_time(self):
        '''
        Function name: estimated_time()
        Developer Name: Emilio Palermo
        Date: 10th August 2026

        Overrides the parent class estimated_time method.

        This function is used for calculating the estimated time.

        I assume an average pace of 3 Km/h due to the weight of the backpack.
        I assume also that every 100 m of elevation gain are equivalent to 1500 m of plane hiking
        '''
        return (self.distance.magnitude + ((self.elevation_gain_m*1.5)/100))/3

    def summary(self):
        '''
        Function name: summary()
        Developer Name: Emilio Palermo
        Date: 10th August 2026

        Overrides the parent class summary method.

        The function is used to return a summary of the main information of the trial

        Parameters: Nothing
        :return: A string that indicates name, distance, difficulty and estimated time
        '''
        return(f"The Backpacking Route {self.name} Trial is {self.distance.magnitude:.2f} Km long."
              f"The difficulty is {self._difficulty} and "
              f"the estimated time to complete is {self.estimated_time()}"
              )

class TrailRun(Trail):
    def __init__(self,id,name,distance,elevation_gain_m,difficulty):
        super().__init__(id,name,distance,elevation_gain_m,difficulty)

    def estimated_time(self):
        '''
        I assume an average pace of 8 Km/h because they run.
         I assume also that every 100 m of elevation gain are
        equivalent to 1000 m of plane running
        '''
        return (self.distance.magnitude + ((self.elevation_gain_m)/100))/8

    def summary(self):
        return(f"The Trial Run {self.name} is {self.distance.magnitude:.2f} Km long."
              f"The difficulty is {self._difficulty} and "
              f"the estimated time to complete is {self.estimated_time()}"
              )

class GuidedDayHike(ElevationMixin, RatingMixin, DayHike):
    def __init__(self,id,name,distance,elevation_gain_m,difficulty, guide_name):
        super().__init__(id,name,distance,elevation_gain_m,difficulty)
        self.guide_name = guide_name

    def summary(self):
        base_summary=super().summary()
        rating_info=f"Rating: {self.get_rating()} stars." if self._rating else ""
        return f"{base_summary}. The Guide name is {self.guide_name}.{rating_info}"


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
            total_distance = Distance(0,new_unit)
            for t in self.trials:
                total_distance += t.distance
        return total_distance

class FakeTrail:
    def __init__(self,name,hours):
        self.name = name
        self.hours = hours

    def estimated_time(self):
        return self.hours


def main():
    #Print MRO for GuidedDayHike as a testing
    print("MRO for GuidedDayHike:")

    for cls in GuidedDayHike.__mro__:
        print(cls.__name__)
    print("-" * 30)

    #Calculate the estimated time for different trials as a test
    hike=DayHike(1,'Day Hike1',5,100,'easy')
    backpack=BackpackingRoute(2,'Back Pack1',10,500,'hard')
    fake=FakeTrail('Fake Trail',3.5)

    mixed_trials=[hike,backpack,fake]

    total_time=0

    for trial in mixed_trials:
        total_time+=trial.estimated_time()
    print(f"Total time to complete is {total_time:.2f}")

    #distance tests
    print(f'The total distance of the mixed_trials is {hike.distance+backpack.distance}')
    if(Distance(2,'km')+Distance(3,'km')==Distance(5,'km')):
        print('The Distance test was successful')
    else:
        print('The Distance test was not successful')

    #test invalid Trial is successful and gives TypeError







if __name__ == '__main__':
    main()


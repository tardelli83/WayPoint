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

class Trial:
    default_unit = 'km'

    def __init__(self,id,name,distance,elevation_gain_m,difficulty):
        self.id = id
        self.name = name

        if isinstance(distance, (int, float)):
            self.distance = Distance(distance, Trial.default_unit)
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

class Itinerary():
    def __init__(self,trials=None):
        self.trials = list (trials) if trials else []

    def add_trial(self,trial):
        self.trials.append(trial)

    def total_distance(self):
        if len(self.trials)==0:
            return Distance(0, 'km')
        else:
            new_unit=self.trials[0].distance.unit
            total_distance=0
            for t in self.trials:
                converted_dist=t.distance.convert(new_unit)
                total_distance+=converted_dist.magnitude
        return Distance(total_distance, self.trials[0].distance.unit)






def main():
    d1 = Distance(10,'km')
    d2 = Distance(20,'km')
    d3 = Distance(30,'km')

    t1=Trial(1,'nord',d1, 100,'moderate')
    t2=Trial(2,'sud',d2, 100,'moderate')
    t3=Trial(3,'est',d3, 100,'moderate')

    it1 = Itinerary([t1])
    it1.add_trial(t2)


    print(it1.total_distance())




if __name__ == '__main__':
    main()


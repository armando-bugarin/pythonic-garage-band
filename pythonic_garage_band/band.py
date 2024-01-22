class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    def __str__(self):
        return f"Band: {self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        raise NotImplementedError("Subclasses must implement this method")

    def play_solo(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __repr__(self):
        raise NotImplementedError("Subclasses must implement this method")

class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

class Bassist(Musician):
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

class Drummer(Musician):
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

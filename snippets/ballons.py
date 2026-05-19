class Balloon:
    
    def __init__(self, id_code):
        self._altitude = 0
        self._status = 'Grounded'
        self.id_code = id_code
        
    def launch(self):
        self._status = 'Launched'
        self._altitude = 5
    
    def report_status(self):
        return self._status
    
    def get_altitude(self):
        return self._altitude
    
    def add_altitude(self, delta):
        if self._altitude + delta >= 0:
            self._altitude += delta
        else:
            self._altitude = 0
    
    def set_status(self, status):
        self._status = status
    
    def __eq__(self, other):
        return self.id_code == other.id_code
    
    def __lt__(self, other):
        return self._altitude < other._altitude
    
    def __lte__(self, other):
        return self._altitude <= other._altitude
        
    def __repr__(self):
        return f"Balloon {self.id_code} at {self._altitude}m, status: {self.report_status()}"
        

class DataBalloon(Balloon):
    def __init__(self, id_code, sensor_type):
        super().__init__(id_code)
        self.sensor_type = sensor_type
    
    def report_status(self):
        return "Lots of Numbers " + super().report_status()
        

class CameraBalloon(Balloon):
    def __init__(self, id_code, camera_resolution):
        super().__init__(id_code)
        self.sensor_type = camera_resolution

    def report_status(self):
        return "Click, Click " + super().report_status()

my_balloon = DataBalloon(1, "Temperature")
second_balloon = CameraBalloon(2, "10MP")
print(type(my_balloon))
print(type("Hello"), type(1.5), type([1,2,3]))
if type(my_balloon) is Balloon:
    print("I'm a Balloon")

if type(my_balloon) is DataBalloon:
    print("I like numbers")

if isinstance(my_balloon, Balloon):
    print("This is a Balloon")

balloon_list = []
for i in range(4):
    id = input("Enter balloon ID: ")
    type = input("Enter balloon type (D)ata or (C)amera: ")
    if type == "D":
        sensor = input("Enter sensor type:")
        balloon = DataBalloon(id, sensor)
    elif type == "C":
        res = input("Enter camera resolution:")
        balloon = CameraBalloon(id, res)
    balloon_list.append(balloon)

balloon_list[1].launch()
balloon_list[2].launch()
balloon_list[2].add_altitude(10)    
print(balloon_list)
    

print(f"Status: {my_balloon.report_status()}, Altitude: {my_balloon.get_altitude()}")

print("Launching")

my_balloon.launch()

print(f"Status: {my_balloon.report_status()}, Altitude: {my_balloon.get_altitude()}")
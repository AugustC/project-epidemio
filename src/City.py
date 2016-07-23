class City:
    """Class of cities"""
    
    def __init__(self, cityname, disease_frequency, population):
        self.name = cityname
        self.frequency = disease_frequency
        self.population = population
        self.outbreaks = self.find_outbreaks()

    def find_outbreaks(self):
        # Function that creates a boolean array with value true where an epidemic outbreak occurs
        # Outbreak: Infected people surpass 300 per thousand of habitants
        outbreak = [(self.frequency[i]/self.population) >= 0.3 for i in range(len(self.frequency)) ]
        return outbreak

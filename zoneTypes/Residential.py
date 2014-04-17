import ZoneRCI

class Residential:
  zoneType = "res"
  population = 0
  populationMax = 0
  
  def __refreshStats(self):
    self.populationMax = self.density * 10
    super().__refreshStats()
  
  def produce():
    
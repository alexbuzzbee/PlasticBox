import Zone

class ZoneRCI(Zone):
  """The base class for the Residential, Commercial, and Industrial zones."""
  happiness = 0
  happyTime = 0 # How many turns in a row this zone has had 90+ happiness.
  density = 0
  flagWantsToIncreaseDensity = False;
  
  # Private
  
  def __refreshFlags(self):
    if all( self.age > 8, self.happyTime > 2, self.density < 10 ):
      self.flagWantsToIncreaseDensity = True
    else:
      self.flagWantsToIncreaseDensity = False
    super().__refreshFlags()
  
  def __refreshStats(self):
    if self.happiness >= 90:
      self.happyTime = self.happyTime + 1
    else:
      self.happyTime = 0
      super().__refreshStats()
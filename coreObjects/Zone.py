import random

class Zone(object):
  """The base class for simulation zones, which power the economy and provide resources."""
  age = 0;
  agents = [ None ]; # The agents in this zone.
  powerNeed = 0;
  power = 0;
  waterNeed = 0;
  water = 0;
  spaceAvailable = 0;
  spaceUsed = 0;
  flagNeedsPower = False;
  flagNeedsWater = False;
  
  def __init__(self):
    self.spaceAvailable = random.randint(500, 1000);
  
  def __refreshFlags(self):
    if all( self.age > 8, self.happyTime > 2, self.density < 10 ):
      self.flagWantsToIncreaseDensity = True;
    else:
      self.flagWantsToIncreaseDensity = False;
    if self.powerNeed > self.power:
      self.flagNeedsPower = True;
    else:
      self.flagNeedsPower = False;
    if self.waterNeed > self.water:
      self.flagNeedsWater = True;
    else:
      self.flagNeedsWater = False;
  
  def __refreshStats(self):
    self.age = self.age + 1;
    self.power = 0;
    self.water = 0;
    self.powerNeed = self.density * 10;
    self.waterNeed = self.density * 10;
    if self.happiness >= 90:
      self.happyTime = self.happyTime + 1;
    else:
      self.happyTime = 0;
  
  def refresh(self):
    """Refresh the status of this zone. Should be run every turn."""
    self.__refreshStats();
    self.__refreshFlags();
  
  def destroyAgent(self, index):
    """Destroy the agent in this zone at 'index'."""
    self.agents[index].destroy();
    del self.agents[index];
  
class ZoneRCI:
  """The base class for the Residential, Commercial, and Industrial zones."""
  happiness = 0;
  happyTime = 0; # How many turns in a row this zone has had 90+ happiness.
  density = 0;
  flagWantsToIncreaseDensity = False;
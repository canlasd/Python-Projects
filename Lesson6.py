class Time:
  """ Blueprint for a Time object"""
  def __init__(self):
     self.__hour = 0
     self.__minute = 0
     self.__second = 0


  def tick (self):
      
      self.__second=self.__second+1
      if (self.__second==60):
          self.__second=0
          self.__minute=self.__minute+1
          
      elif (self.__minute==60):
            self.minute=0
            self.__hour=self.__hour+1
      elif (self.__hour==24):
            self.__hour=0

      
      """
      for self.__second in range(0,60):
          if (self.__second==60):
              self.__second=0
              self.__minute=self.__minute+1
      

              for self.__minute in range(0,60):
                if (self.__minute==60):
                  self.__minute=0
                  self.__hour=self.__hour+1

              
                  for self.__hour in range(0,24):
                    if (self.__hour==24):
                        self.__hour=0
          
  
      
  
  def tick(self):
          self.__second=self.__second+1
          if (self.__second==60):
              self.__second=0
              self.__minute=self.__minute+1
              if (self.__minute==60):
                  self.__minute=0
                  self.__hour=self.__hour+1
                  if (self.__hour==24):
                      self.__hour=0

  """
      

  def set_time(self, hour, minute, second):
     self.set_hour(hour)
     self.set_minute(minute)
     self.set_second(second)

  def print_time(self):
     print (self.__hour, ":", self.__minute, ":", self.__minute)

  def set_second(self, second):
      if (second>=0 and second<=60):
         self.__second=second
      else:
         self.__second=0

  def get_second(self):
      return self.__second


  def set_minute(self, minute):
      if (minute>=0 and minute<=60):
         self.__minute=minute
      else:
         self.__minute=0

  def get_minute(self):
      return self.__minute


  def set_hour(self, hour):
      if (hour>=0 and hour<=24):
         self.__hour=hour
      else:
         self.__hour=0

  def get_hour(self):
      return self.__hour


        

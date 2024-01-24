def add_time(start, duration, day = None):

  week_days = {"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
  start_time = start.split(':')
  start_hour = int(start_time[0])
  start_minute = int(start_time[1].split()[0])
  start_meridiem = start_time[1].split()[1]  
  number_days = 0
  new_day = ""

  if start_meridiem == 'PM' and start_hour != 12:
    start_hour +=12

  if start_meridiem == 'AM' and start_hour == 12:
    start_hour -= 12

  duration_time = duration.split(':')
  duration_hour = int(duration_time[0])
  duration_minute = int(duration_time[1])

  new_minute = start_minute + duration_minute

  if new_minute >= 60:
    duration_hour +=1
    new_minute -= 60

  if duration_hour >= 24:
    number_days = int(duration_hour/24)

  new_hour = start_hour + (duration_hour%24)

  if new_hour >= 24:
    number_days +=1
    new_hour -=24

  if new_hour == 0:
    new_hour +=12
    new_meridiem = 'AM'
  elif new_hour == 12:
    new_meridiem = 'PM'
  elif new_hour >= 1 and new_hour <=11:
    new_meridiem = 'AM'
  else:
    new_hour -= 12
    new_meridiem = 'PM'

  if day is not None:
    new_day_number = (week_days[day.lower()] + number_days)%7
  
    if new_day_number == 0:
      new_day = list(week_days.keys())[list(week_days.values()).index(7)]
    else:
      new_day = list(week_days.keys())[list(week_days.values()).index(new_day_number)]

  if day is None:

    if number_days == 0:
      return (str(new_hour)+":"+str(new_minute).rjust(2,'0')+" "+new_meridiem)
    elif number_days == 1:
      return (str(new_hour)+":"+str(new_minute).rjust(2,'0')+" "+new_meridiem+" (next day)")
    else:
      return (str(new_hour)+":"+str(new_minute).rjust(2,'0')+" "+new_meridiem+" ("+str(number_days)+" days later)")

  else:
    if number_days == 0:
      return (str(new_hour)+":"+str(new_minute).rjust(2,'0')+" "+new_meridiem+", "+day)
    elif number_days == 1:
      return (str(new_hour)+":"+str(new_minute).rjust(2,'0')+" "+new_meridiem+", "+new_day.capitalize()+" (next day)")
    else:
      return (str(new_hour)+":"+str(new_minute).rjust(2,'0')+" "+new_meridiem+", "+new_day.capitalize()+" ("+str(number_days)+" days later)")

    


    

  
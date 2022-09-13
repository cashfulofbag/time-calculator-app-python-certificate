def add_time(start, duration, day = False):

  week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  week_days_l = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  days = 0
  
  s1 = start.split(" ")
  start_time = s1[0]
  ending = s1[1]
  s2 = start_time.split(":")
  start_hour = int(s2[0])
  start_minute = int(s2[1])
  s3 = duration.split(":")
  dur_hour = int(s3[0])
  dur_minute = int(s3[1])

  new_minute = start_minute + dur_minute
  if(new_minute > 60):
    start_hour = start_hour + 1
    new_minute = new_minute - 60
  
  if(new_minute < 10):
    new_minute = "0" + str(new_minute)
  
  new_hour = start_hour + dur_hour
        
  while(new_hour > 12):
    if(ending == "AM"):
      ending = "PM"
      if(new_hour > 12):
        new_hour = new_hour - 12
    else:
      ending = "AM"
      if(new_hour > 12):
        new_hour = new_hour - 12
        days = days + 1

  if(new_hour == 12):
    if(ending == "AM"):
      ending = "PM"
    else:
      ending = "AM"
      days = days + 1

  if(day):
    day = day.lower()
    for x in range(len(week_days_l)):
      if(day == week_days_l[x]):
        y = (days + x) % 7
        day = week_days[y]
        break
        
  
  
  
  if(day):
    if(days > 1):
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending + ", " + day + " (" + str(days) + " days later)"
    elif(days == 1):
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending + ", " + day + " (next day)"
    else:
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending + ", " + day
  else:
    if(days > 1):
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending + " (" + str(days) + " days later)"
    elif(days == 1):
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending + " (next day)"
    else:
      new_time = str(new_hour) + ":" + str(new_minute) + " " + ending
  


  return new_time
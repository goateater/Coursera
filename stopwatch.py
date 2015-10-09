# template for "Stopwatch: The Game"

import simplegui

# define global variables
# ==================================
position = [60, 85] # position of watch
counter_position = [175,25] # position of counter
time = 0
interval = 10
reset = 0
stopwatch_running = True
stopwatch_stopped = False
successful_stops = 0
total_stops = 0
# ==================================

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t // 600 # whole minutes
    b = t // 100 % 6 # tens of whole seconds
    c = (t // 10) % 10 # seconds
    d = t % 10 # tenths of seconds
    return '%d:%d%d.%d' % (a,b,c,d)  
 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startup():
    timer.start()
    

def pauseit():
    global successful_stops,total_stops
    if stopwatch_running:
        timer.stop()
        total_stops += 1
        if time % 10 == 0:
            successful_stops += 1
            counter()
        

def reset():
    timer.stop()
    global time
    time = 0
    global successful_stops
    successful_stops = 0
    global total_stops
    total_stops = 0
     

def counter():
    global successful_stops
    global total_stops
    return successful_stops, total_stops
  
    

# define event handler for timer with 0.1 sec interval
def time_handler():
    global time
    global position
    time = time + 1
    return time    



# define draw handler
def draw_handler(canvas):
    global time
    global position
    canvas.draw_text(str(format(time)),position,36,"White", "serif")
    canvas.draw_text(str(counter()),counter_position,14,"White", "serif")

    
    
# create frame
frame = simplegui.create_frame("StopWatch!", 250, 150)    
button1 = frame.add_button("Start", startup)
button2 = frame.add_button("Stop",pauseit)
button3 = frame.add_button("Reset", reset)
timer = simplegui.create_timer(interval,time_handler)




# register event handlers



# start frame
frame.start()
frame.set_draw_handler(draw_handler)
# Please remember to review the grading rubric

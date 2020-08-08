import simplegui
import random


width = 800
height = 400
ball_radius = 20
score = 0
paddle_vel = 0
paddle_pos = width / 2

ball_pos = [width / 2 , height / 2]

gravity = 0.5

ball_vel = [0,0]
drift = 0

pad_width = 160

highscore = 0

def spawn_ball():
    global ball_pos, ball_vel, gravity, drift, paddle_pos 
    ball_pos = [width / 2, 180]
    gravity = 0.5
    ball_vel = [0,0]
    drift = random.choice([-0.1, -0.05, -0.07, -0.02, 0.1, 0.05, 0.07, 0.02])
    paddle_pos = 360
    
def new_game():
   
    global score  
    score = 0
    spawn_ball()

def draw(c):
    global score, paddle_pos, paddle_vel, ball_pos, ball_vel, gravity, drift, pad_width, highscore        
    # draw ball
    c.draw_circle(ball_pos,ball_radius, 2 ,"Blue","Cyan")
    # draw paddle
    c.draw_polygon([[paddle_pos, 350], [paddle_pos, 360], [paddle_pos + pad_width, 360], [paddle_pos + pad_width, 350]],1, 'Orange', 'Yellow')
    # Update paddle's horizontal position
    paddle_pos += paddle_vel
    # Update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    ball_vel[0] += drift
    ball_vel[1] += gravity
    #Test whether the ball touches/collides with the paddle
    if(ball_pos[1] == 330):
        if(paddle_pos <= ball_pos[0] <= paddle_pos + pad_width):
            ball_vel[1] *= -1
            ball_vel[1] += 0.5
            #Set a new drift direction
            drift = random.choice([-0.1, -0.05, -0.07, -0.02, 0.1, 0.05, 0.07, 0.02])
            #Increment Score
            score += 1  
    if ((ball_pos[0] + drift) < 0 or (ball_pos[0] + drift) > 800):
        ball_vel[0] *= -1
    # Start new game if ball is missed
    ball_pos[1] > 400
    if(ball_pos[1] > 380):
        if(score > highscore):
            highscore = score
        new_game()
    #Draw score
    c.draw_text('Score :', (300, 80), 44, 'Gray', 'serif')
    c.draw_text(str(score),[440,80],44,'Gray', 'serif')
    c.draw_text('High Score :', (620, 50), 24, 'Gray', 'serif')
    c.draw_text(str(highscore),[760,50],24,'Gray', 'serif')
    
    
def keydown(key):
    speed = 12
    global paddle_vel
    if key == simplegui.KEY_MAP["left"]:
        paddle_vel -= speed 
    elif key == simplegui.KEY_MAP["right"]:
        paddle_vel += speed   
        
def keyup(key):
    speed = 12
    global paddle_vel
    if key == simplegui.KEY_MAP["left"]:
        paddle_vel += speed 
    elif key == simplegui.KEY_MAP["right"]:
        paddle_vel -= speed

# create frame
frame = simplegui.create_frame("Bounce", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()

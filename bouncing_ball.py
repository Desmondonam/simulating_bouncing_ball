import turtle
# Set key parameters
gravity = -0.005  # pixels/(time of iteration)^2
y_velocity = 1  # pixels/(time of iteration)
x_velocity = 0.0  # pixels/(time of iteration)
cor = 0.546 # this is the energy loss or the coefficient of restitution
width = 600
height = 700
# Set window and ball
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)
ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")
# Main loop
while True:
    # Move ball
    ball.sety(ball.ycor() + y_velocity)
    ball.setx(ball.xcor() + x_velocity)
    # Acceleration due to gravity
    y_velocity += gravity
    # Bounce off the ground
    if ball.ycor() < -height / 2:
        y_velocity = -y_velocity * cor
        # Set ball to ground level to avoid it getting "stuck"
        ball.sety(-height / 2)
    # Bounce off the walls (left and right)
    if ball.xcor() > width / 2 or ball.xcor() < -width / 2:
        x_velocity = -x_velocity
    window.update()
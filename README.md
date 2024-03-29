# Simulating a bouncing ball

In this project, we are going to apply the concepts that are mathematical and scientific so that we are able to calculate and simulate the bouncing ball. 
We are to apply the laws of Science and Mathematics so that we are able to explain the bouncing Ball effect. 

# First Step
We are creating a game that has the bouncing ball to accept the bouncing ball effect 
This is done in tkinter so we are able to visualize how the effect of the bouncing ball has
Also we are put in place the environmental effects that it encounters in the process of the bouncing. 


# Abstract
This project describes the attempt to show you the magic of mathematics science and how it lies at the heart of everything in real life: from a bouncing ball to the limits of the universe! You will also meet with the most scientific programming language - Python. You will actually understand how difficult it is to recreate the behavior of a simple bouncy ball from the real world! Last but not least, we will mention the concepts of Ordinary Differential Equation, Newton's equations of motion with constant <b>acceleration, Coefficient of restitution, G force </b> and many other things in the world of mathematics.

# Introduction
Most physical phenomena are ultimately described by a relationship between changing quantities, resulting in differential equations. If such an equation only contains one independent variable (such as time) and hence only total derivatives (and no partial derivatives) we classify it as an ordinary differential equation (ODE). An ODE of order n contains no derivatives higher than the n-th derivative:

F(t,y,y(1),…,y(n))=0
 
The dependent variable  y=y(t)  is a function of the independent variable  t  and  y(n)=dnydtn  is the  n -th derivative with respect to  t . A linear ODE only contains first powers of  y  or its derivatives. A non-linear ODE may contain higher powers. There often exist methods to solve linear ODEs analytically but this is impossible for most non-linear ODEs. Solutions of an ODE are fixed by the initial conditions1, e.g.,  y0=y(t0)  and similar for all higher derivatives. For an ODE of order  n , exactly  n  initial conditions are needed.

Using ODE integration algorithms (integrators) we can solve linear and non-linear ODEs of any order numerically. The basic idea is to start with the initial conditions and then propagate  y  for a small step  h  to numerically compute  y(t0+h)  and all its derivatives. By repeating the process, one extrapolates from the initial condition to any "later" value of  t .

In this project we will use the simplest integrator, the Euler algorithm.

# Bouncing ball with the Euler integrator

In this project we are solving the problem of the bouncing ball with the simplest of all integrators: <b>the forward Euler scheme.</b>

We have to solve the second order ODE (Newton's equations of motion with constant acceleration)

d2ydt2=−g
 
where  g  is the constant acceleration due to gravity2 and  y(t)  is the position of the ball as a function of time (its trajectory).

The forward Euler scheme for any first order ODE

dydt=f(y,t)
 
is

y(t+h)=y(t)+hf(y(t),t).
 
In order to solve the original 2nd order equation of motion we make use of the fact that one  n -th order ODE can be written as  n  coupled first order ODEs, namely

dydtdvdt=v=−g.
 
Solve each of the first order ODEs with the Euler algorithm:

y(t+h)v(t+h)=y(t)+hv(t)=v(t)−hg.


# Coefficient of restitution

From what we have seen so far, we can see that the behavior of the ball is not what we would expect in the real world. The reasons for this are many, and one of them is called Coefficient of restitution (COR).

The COR, also denoted by ( e ), is the ratio of the final to initial relative velocity between two objects after they collide. It normally ranges from 0 to 1 where 1 would be a perfectly elastic collision. A perfectly inelastic collision has a coefficient of 0, but a 0 value does not have to be perfectly inelastic. It is measured in the Leeb rebound hardness test, expressed as 1000 times the COR, but it is only a valid COR for the test, not as a universal COR for the material being tested.

The value is almost always less than one due to initial translational kinetic energy being lost to rotational kinetic energy, plastic deformation, and heat. It can be more than 1 if there is an energy gain during the collision from a chemical reaction, a reduction in rotational energy, or another internal energy decrease that contributes to the post-collision velocity.

Coefficient of restitution (e)=Relative velocity after collision Relative velocity before collision
 
The coefficient is related to (relative) kinetic energy by  e=KE(after collision)KE(before collision)−−−−−−−−−−√ 
The mathematics were developed by Sir Isaac Newton in 1687. It is also known as Newton's experimental law.

Line of impact – It is the line along which e is defined or in absence of tangential reaction force between colliding surfaces, force of impact is shared along this line between bodies. During physical contact between bodies during impact its line along common normal to pair of surfaces in contact of colliding bodies. Hence e is defined as a dimensionless one-dimensional parameter.

Range of values for e – treated as a constant

ee  is usually a positive, real number between 0 and 1:

e=0e=0 : This is a perfectly inelastic collision. This means kinetic energy along the common normal is 0. Kinetic energy is converted to heat or work done in deforming the objects.

0<e<10<e<1 : This is a real-world inelastic collision, in which some kinetic energy is dissipated.

e=1e=1 : This is a perfectly elastic collision, in which no kinetic energy is dissipated, and the objects rebound from one another with the same relative speed with which they approached.

e<0e<0 : A COR less than zero would represent a collision in which the separation velocity of the objects has the same direction (sign) as the closing velocity, implying the objects passed through one another without fully engaging. This may also be thought of as an incomplete transfer of momentum. An example of this might be a small, dense object passing through a large, less dense one – e.g., a bullet passing through a target, or a motorcycle passing through a motor home or a wave tearing through a dam.

The COR of a basket ball is 0.546

e>1e>1 : This would represent a collision in which energy is released, for example, nitrocellulose billiard balls can literally explode at the point of impact. Also, some recent articles have described superelastic collisions in which it is argued that the COR can take a value greater than one in a special case of oblique collisions.456 These phenomena are due to the change of rebound trajectory caused by friction. In such collision kinetic energy is increased in a manner energy is released in some sort of explosion. It is possible that  e=∞  for a perfect explosion of a rigid system.

Maximum deformation phase – In any collision for  0<e≤1 , there is a condition when for short moment along line of impact colliding bodies have same velocity when its condition of kinetic energy is lost in maximum fraction as heat, sound and light with deformation potential energy. For this short duration this collision  e=0  and may be referred as inelastic phase.
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
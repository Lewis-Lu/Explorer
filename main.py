from Xspace import Xspace
from vehicle import lidar_car
import obstacle as Obs
from plotting import Plot as Plotter
import matplotlib.pyplot as plt

dim_range = (100, 100)
start = (10, 10)
end = (90, 90)
N_obs = 40

car_loc = (10, 20)
car_ori = 90

obstacles = Obs.random_obstacle_generate(dim_range, start, end, N_obs)
Space = Xspace(dim_range, obstacles)
Car = lidar_car(car_loc, car_ori)

# plot part
handle_plot = Plotter(Space)
ax = plt.gca()

ax = handle_plot.plot_2D(ax, obstacles, start, end)
ax = handle_plot.plot_2D_vehicle(ax, Car)

ax.axis('equal')
ax.grid()
plt.xlim([0, dim_range[0]]) 
plt.ylim([0, dim_range[1]])
plt.xlabel('x (m)') 
plt.ylabel('y (m)')
plt.show()
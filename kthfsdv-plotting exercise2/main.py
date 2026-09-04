import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

class Plotter:
    def __init__(self, start_t, end_t, num_points):
        self.start_t = start_t
        self.end_t = end_t
        self.num_points = num_points

        self.t = np.linspace(start_t, end_t, num_points)


    def lambda_func(self, t):
        return 5 * np.sin(2 * np.pi * t)

    def h_func(self, t):
        return 3 * np.pi * np.exp(-self.lambda_func(t))

class StaticPlotter(Plotter):
    def plot(self):
        h = self.h_func(self.t)

        plt.plot(self.t, h)

        plt.xlabel("t")
        plt.ylabel("h(t)")
        plt.title("h(t) = 3*pi*exp(-lambda[t])")

        plt.grid()
        plt.show()

class DynamicPlotter(Plotter):
    def __init__(self, start_time, end_time, num_points):
        super().__init__(start_time, end_time, num_points)

        self.paused = False
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        self.fig.subplots_adjust(bottom=0.15)


        # pause button
        pause_ax = self.fig.add_axes([0.8, 0.02, 0.1, 0.05])
        self.pause_button = Button(pause_ax, "Pause")
        self.pause_button.on_clicked(self.on_pause)

        #print button
        reset_ax = self.fig.add_axes([0.69, 0.02, 0.1, 0.05])
        self.reset_button = Button(reset_ax, "Reset")
        self.reset_button.on_clicked(self.on_reset)

    def on_pause(self, event):
        if self.paused:
            self.animation.event_source.start()
            self.pause_button.label.set_text("Pause")
        else:
            self.animation.event_source.stop()
            self.pause_button.label.set_text("Resume")

        self.paused = not self.paused

    def on_reset(self, event):
        self.animation.event_source.stop()
        self_paused = True
        self.pause_button.label.set_text("Start")

        self.line.set_data([],[])

        self.animation.frame_seq = self.animation.new_frame_seq()

        self.fig.canvas.draw_idle()




    def update(self, frame):
        curr_t = self.t[:frame + 1]
        curr_h = self.h_func(curr_t)

        self.line.set_data(curr_t, curr_h)

        self.ax.relim()
        self.ax.autoscale_view()

        return self.line

    def plot(self):
        self.animation = FuncAnimation(self.fig, self.update, frames = self.num_points, interval= 50)

        self.ax.set_xlabel("t")
        self.ax.set_ylabel("h(t)")
        self.ax.set_title("h(t) = 3*pi*exp(-lambda[t])")
        self.ax.grid()

        plt.show()

    
plotter = DynamicPlotter(0, 2, 500)
plotter.plot()
from manim import *


class Pith(Scene):
    def construct(self):
        sq = Square(side_length=5,stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.75)

        self.play(Create(sq), run_time=3)
        self.wait()




class Formula(Scene):
    def construct(self):
        text = MathTex(
            "I_D = I_{DSS}\left(1-\dfrac{V_{GS}}{V_P}\right)^2"
            )
        self.play(Write(text))



class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-10, 1], y_range=[-1, 17], axis_config={"include_tip": False},
            x_length=4,
            y_length=6,
            x_axis_config={"numbers_to_include": [-8,-4,-2.4,0]},
            y_axis_config={"numbers_to_include": np.arange(0, 17, 4)}

        )
        labels = ax.get_axis_labels(x_label="V (V)", y_label="I (mA)")


      

        t = ValueTracker(0)

        def func(x):
            return 16*(1+x/8)**2
        graph = ax.plot(func, color=BLUE)


        line_1 = ax.get_vertical_line(ax.input_to_graph_point(-4, graph), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(-2.4, graph), color=YELLOW)
        line_3 = ax.get_horizontal_line(ax.input_to_graph_point(4, graph), color=YELLOW)
        line_4 = ax.get_horizontal_line(ax.i2gp(8, graph), color=YELLOW)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[-8:] ,100)
        minimum_index = func(x_space).argmax()

        self.add(ax, labels, graph, line_1, line_2, line_3, line_4, dot)
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait()




class HW21(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 2, 1], y_range=[-1, 13, 1], axis_config={"include_tip": False},
            x_length=4, y_length=6,
            x_axis_config={"numbers_to_include": [-4,-2, -1.2, 0]},
            y_axis_config={"numbers_to_include": np.arange(0, 17, 4)}
        )
        # axes.to_edge(RIGHT, buff=0.5)
        axes_labels = axes.get_axis_labels(x_label="V (V)", y_label="I (mA)")

        #def func(x):
        #    return 10*(1+x/4)**2
        #graph = axes.plot(func, color=BLUE)

        graph = axes.plot(lambda x : 12*(1+x/4)**2, x_range = [-4,0], color=BLUE)

        line_1 = axes.get_vertical_line(axes.input_to_graph_point(-2, graph), color=YELLOW)
        line_2 = axes.get_vertical_line(axes.i2gp(-1.2, graph), color=YELLOW)
        line_3 = axes.get_horizontal_line(axes.c2p(-2, 3), color=YELLOW)
        line_4 = axes.get_horizontal_line(axes.c2p(-1.2, 6), color=YELLOW)


    
        # line_3 = Line(
        #     start = axes.c2p(0,graph.underlying_function(-2)),
        #     end = axes.c2p(-2,graph.underlying_function(-2)),
        #     stroke_color=YELLOW, stroke_width=1
        # )
        # line_4 = Line(
        #     start = axes.c2p(0,graph.underlying_function(-2)),
        #     end = axes.c2p(-1.2,graph.underlying_function(-2)),
        #     stroke_color=YELLOW, stroke_width=1
        # )

        graphing_stuff = VGroup(axes, graph, axes_labels, line_1, line_2, line_3, line_4)
        # graphing_stuff = VGroup(axes, graph, axes_labels, horiz_line)

        my_function = MathTex( "I_D = I_{DSS} ( 1-\dfrac{V_{GS}}{V_P} )^2 " ).next_to(axes, LEFT, buff=0.05)
        my_function_2 = MathTex( "I_D = 12 ( 1-\dfrac{V_{GS}}{-4} )^2 " ).next_to(axes, LEFT, buff=0.05)

        self.play(DrawBorderThenFill(axes), Write(axes_labels))
        self.play(Create(graph))
        self.play(Create(line_1), Create(line_2), Create(line_3), Create(line_4))
        self.play(graphing_stuff.animate.shift(RIGHT*1.75))
        self.play(Write(my_function))
        self.play(Transform(my_function, my_function_2))
        self.play(FadeOut(graphing_stuff))



        #self.add(axes, axes_labels, graph, line_1, line_2, line_3, line_4)
        #self.play(Write(axes))
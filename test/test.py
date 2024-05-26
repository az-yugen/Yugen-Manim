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
            y_axis_config={"numbers_to_include": np.arange(0, 13, 3)}
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


        # dot_1 = Dot(color = RED).shift(axes.c2p(-2,3))
        # coords = np.around(axes.point_to_coords(dot_1.get_right()), decimals=1)
        # label_1 = Text(coords[0], coords[1]).scale(0.7).next_to(dot_1, LEFT)

        dot_1 = Dot(axes.coords_to_point(-2,3), color=RED)
        lines_1 = axes.get_lines_to_point(axes.c2p(-2,3))
        dot_2 = Dot(axes.c2p(-1.2, 6), color=RED)
        lines_2 = axes.get_lines_to_point(axes.c2p(-1.2, 6))

    
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

        # graphing_stuff = VGroup(axes, graph, axes_labels, line_1, line_2, line_3, line_4, dot_1, label_1)
        # graphing_stuff = VGroup(axes, graph, axes_labels, horiz_line)
        graphing_stuff = VGroup(axes, graph, axes_labels, lines_1, dot_1)

        my_function = MathTex( "I_D = I_{DSS} ( 1-\dfrac{V_{GS}}{V_P} )^2 " ).next_to(axes, LEFT, buff=0)
        my_function_2 = MathTex( "I_D = 12 ( 1-\dfrac{V_{GS}}{-4} )^2 " ).next_to(axes, LEFT, buff=0)

        self.play(DrawBorderThenFill(axes), Write(axes_labels))
        self.play(Create(graph))
        # self.play(Create(line_1), Create(line_2), Create(line_3), Create(line_4))
        self.play(Create(lines_1))
        self.play(SpinInFromNothing(dot_1))
        self.play(graphing_stuff.animate.shift(RIGHT*1.75))
        self.play(Write(my_function))
        self.play(TransformMatchingShapes(my_function, my_function_2))
        self.play(FadeOut(graphing_stuff))



        #self.add(axes, axes_labels, graph, line_1, line_2, line_3, line_4)
        #self.play(Write(axes))



class HW22(Scene):
    def construct(self):

        eqn = MathTex( "I_D = I_{DSS} ( 1-\dfrac{V_{GS}}{V_P} )^2 " )
        given_I = MathTex( "I_{DSS}=12mA").next_to(eqn, DL)
        given_V = MathTex("V_P=-4V").next_to(eqn, DR)
        eqn_2 = MathTex( "I_D = 12 ( 1-\dfrac{V_{GS}}{-4} )^2 " )
        eqn_3 = MathTex( "I_D = 12 ( 1+\dfrac{V_{GS}}{4} )^2 " )

        self.play(Write(eqn))
        self.wait(1)
        self.play(Write(given_I), Write(given_V))
        self.wait(1)
        self.play(TransformMatchingTex(eqn, eqn_2), FadeOut(given_I), FadeOut(given_V))
        self.play(TransformMatchingTex(eqn_2, eqn_3))




        axes = Axes(
            x_range=[-5, 2, 0.1], y_range=[-1, 21, 0.1], axis_config={"include_tip": False},
            x_length=3.5, y_length=5.5,
            x_axis_config={"numbers_to_include": [-4,-2, -1.2, 0, 1], "font_size": 20, "include_ticks": False},
            y_axis_config={"numbers_to_include": np.arange(0, 21, 4), "font_size": 20, "include_ticks": False}
        ).shift(RIGHT*1.75)
        axes_labels = axes.get_axis_labels(x_label="V_{GS} (V)", y_label="I_D (mA)").shift(RIGHT*1.1)


        graphing_stuff = VGroup(axes, axes_labels)




        eqn_plot_11 = MathTex( "I_D = 12 ( 1+\dfrac{0}{4} )^2 " )
        eqn_plot_12 = MathTex( "I_D = 12" )
        dot_1 = Dot(axes.coords_to_point(0,12), color=RED)



        eqn_plot_21 = MathTex( "I_D = 12 ( 1+\dfrac{-4}{4} )^2 " )
        eqn_plot_22 = MathTex( "I_D = 0" )
        dot_2 = Dot(axes.coords_to_point(-4,0), color=RED)



        group_eqn = VGroup(eqn, eqn_2, eqn_3, eqn_plot_11, eqn_plot_12, eqn_plot_21, eqn_plot_22)

        self.play(eqn_3.animate.shift(LEFT*3))



        self.play(DrawBorderThenFill(axes), Write(axes_labels))


        self.play(TransformMatchingTex(eqn_3, eqn_plot_11.shift(LEFT*3)))
        self.play(TransformMatchingTex(eqn_plot_11, eqn_plot_12.shift(LEFT*3)))
        self.play(SpinInFromNothing(dot_1))



        self.play(TransformMatchingTex(eqn_plot_12, eqn_plot_21.shift(LEFT*3)))
        self.play(TransformMatchingTex(eqn_plot_21, eqn_plot_22.shift(LEFT*3)))
        self.play(SpinInFromNothing(dot_2))





        dot_3 = Dot(axes.coords_to_point(-2,3), color=RED)
        lines_3 = axes.get_lines_to_point(axes.c2p(-2,3))
        dot_4 = Dot(axes.c2p(-1.2, 6), color=RED)
        lines_4 = axes.get_lines_to_point(axes.c2p(-1.2, 6))

        lines_5 = axes.get_lines_to_point(axes.c2p(1, (12*(1+1/4)**2)))
        dot_5 = Dot(axes.c2p(1, (12*(1+1/4)**2)), color=RED)

        self.play(Create(lines_3))
        self.play(SpinInFromNothing(dot_3))
        self.play(Create(lines_4))
        self.play(SpinInFromNothing(dot_4))
        self.play(Create(lines_5))
        self.play(SpinInFromNothing(dot_5))
        self.wait(1)




        graph = axes.plot(lambda x : 12*(1+x/4)**2, x_range = [-4,1], color=BLUE)

        self.play(Create(graph))
        self.wait(3)



        # self.play(FadeOut(graphing_stuff))





class HW24(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-5, 2, 0.1], y_range=[-1, 21, 0.1], axis_config={"include_tip": False},
            x_length=4, y_length=7,
            x_axis_config={"numbers_to_include": [-4,-2, -1.2, 0, 1], "font_size": 20, "include_ticks": False},
            y_axis_config={"numbers_to_include": np.arange(0, 21, 3), "font_size": 20, "include_ticks": False}
        )
        axes_labels = axes.get_axis_labels(x_label="V_{GS} (V)", y_label="I_D (mA)")    



        dot_1 = Dot(axes.coords_to_point(0,12), color=RED)
        dot_2 = Dot(axes.coords_to_point(-4,0), color=RED)
        dot_3 = Dot(axes.coords_to_point(-2,3), color=RED)
        lines_3 = axes.get_lines_to_point(axes.c2p(-2,3))
        dot_4 = Dot(axes.c2p(-1.2, 6), color=RED)
        lines_4 = axes.get_lines_to_point(axes.c2p(-1.2, 6))
        lines_5 = axes.get_lines_to_point(axes.c2p(1, (12*(1+1/4)**2)))
        dot_5 = Dot(axes.c2p(1, (12*(1+1/4)**2)), color=RED)


        graph = axes.plot(lambda x : 12*(1+x/4)**2, x_range = [-4,1], color=BLUE)



        area_d = axes.get_area(graph, [-4, 0], color=ORANGE, opacity=0.2)
        area_e = axes.get_area(graph, [0, 1], color=GREEN, opacity=0.2)



        self.play(DrawBorderThenFill(axes), Write(axes_labels))

        self.play(SpinInFromNothing(dot_1))
        self.play(SpinInFromNothing(dot_2))
        self.play(Create(lines_3))
        self.play(SpinInFromNothing(dot_3))
        self.play(Create(lines_4))
        self.play(SpinInFromNothing(dot_4))
        self.play(Create(lines_5))
        self.play(SpinInFromNothing(dot_5))

        self.play(Create(graph))
        self.play(FadeIn(area_d), FadeIn(area_e))
        self.wait(3)












class HW23(Scene):
    def construct(self):


        axes = Axes(
            x_range=[-1, 4.5, 0.1], y_range=[-2, 15, 0.1], axis_config={"include_tip": True},
            x_length=9, y_length=6,
            x_axis_config={"numbers_to_include": np.arange(0, 4.5, 1), "font_size": 20, "include_ticks": False},
            y_axis_config={"numbers_to_include": np.arange(0, 15, 1), "font_size": 20, "include_ticks": False}
        )
        axes_labels = axes.get_axis_labels(x_label="V_{GS} (V)", y_label="I_D (mA)")


        graph_straight = axes.plot(lambda x: 0, x_range=[0,2], color=BLUE)
        graph = axes.plot(lambda x : 3*(x-2)**2, x_range = [2,4.1], color=BLUE)



        graphing_stuff = VGroup(axes, axes_labels)




        dot_1 = Dot(axes.coords_to_point(2,0), color=RED)
        dot_2 = Dot(axes.coords_to_point(3,(3*(3-2)**2)), color=RED)
        dot_3 = Dot(axes.coords_to_point(4,(3*(4-2)**2)), color=RED)

        lines_2 = axes.get_lines_to_point(axes.c2p(3,(3*(3-2)**2)))
        lines_3 = axes.get_lines_to_point(axes.c2p(4,(3*(4-2)**2)))



        self.play(DrawBorderThenFill(axes), Write(axes_labels))
        self.play(SpinInFromNothing(dot_1))
        self.play(Create(lines_2), SpinInFromNothing(dot_2))
        self.play(Create(lines_3), SpinInFromNothing(dot_3))

        self.play(Create(graph_straight))
        self.play(Create(graph), run_time=2)
        self.wait(3)
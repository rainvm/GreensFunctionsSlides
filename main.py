# manim
import numpy
from manim import *
from manim_editor import PresentationSectionType
# math
from sympy import *
import numpy as np

config["background_color"] = WHITE

axes = NumberPlane(x_range=[0, 2 * PI, 1], x_length=5, y_range=[-2, 4, 1], y_length=5).add_coordinates().shift(
    LEFT * 3.5)
axes.x_axis.set_color(BLACK)
axes.y_axis.set_color(BLACK)

fontsize = 35

titleDot = Dot()
titleDot.set_y(3.2)
titleDot.set_x(-6)


class Title(Scene):
    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        pos = 2
        dist = 1
        dot = Dot(color=WHITE)
        self.play(Create(dot))
        title = Text("The Method of Green's Functions", font_size=36, should_center=True, color='#38248a',
                     font="Tenorite")
        title.set_y(pos)
        byline = Text("Ryan Coyne", font_size=20, should_center=False, color=BLACK, font="Tenorite")
        byline.set_y(pos - dist)
        byline.set_x(0)
        inst = Text("NHTI - Concord's Community College", font_size=20, should_center=False, color=BLACK,
                    font="Tenorite")
        inst.set_y(pos - 2 * dist)
        inst.set_x(0)
        date = Text("5/5/2023", font_size=20, should_center=False, color=BLACK, font="Tenorite")
        date.set_x(0)
        date.set_y(pos - 3 * dist)
        self.add(byline, title, inst, date)
        self.wait()


class Limit(Scene):
    def construct(self):
        axes = NumberPlane(x_range=[0, 4, 1], x_length=5, y_range=[0, 4, 1], y_length=5).add_coordinates().shift(
            LEFT * 3.5)
        axes.x_axis.set_color(BLACK)
        axes.y_axis.set_color(BLACK)
        self.next_section(type=PresentationSectionType.NORMAL)
        title = Text("Limits", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)
        limf = axes.plot(
            lambda t: t,
            color=BLACK,
            x_range=[0, 4]
        )
        limitFunctionText = MathTex(r"f(x)=\frac{x^2-2\cdot x}{x-2}", color=BLACK, font_size=fontsize)
        limitFunctionText.set_x(1)
        vert = axes.plot_implicit_curve(lambda x, y: x - 1, color=BLACK)
        vert.y_range = {0, 2}
        hole = Dot(radius=0.001)
        holePos = axes.coords_to_point(2, 2)
        hole.set_x(holePos[0])
        hole.set_y(holePos[1])
        self.add(limitFunctionText, title)
        self.add(axes)
        self.play(Create(limf))
        self.next_section(type=PresentationSectionType.NORMAL)
        group = VGroup(MathTex(r"2^2-2\cdot2"), MathTex(r"2-2"))
        undefined1 = MathTex(r"f(2)=", r"\frac{2^2-2\cdot2}{2-2}", color=BLACK, font_size=fontsize).set_x(1)
        self.play(TransformMatchingTex(limitFunctionText, undefined1))
        self.next_section(type=PresentationSectionType.NORMAL)
        undefined2 = MathTex(r"f(2)=", r"\frac{0}{0}", color=BLACK, font_size=fontsize).set_x(1)
        self.play(TransformMatchingTex(undefined1, undefined2))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(hole)
        self.play(hole.animate.scale(50))


class Derivative(Scene):
    @staticmethod
    def functionInterval(inv_f, tracker, Df):
        a = 0.8
        if -a < Df < a:
            x1 = 0
        elif inv_f(4, tracker) < 0:
            x1 = 0
        elif inv_f(4, tracker) > 6:
            x1 = 6
        else:
            x1 = inv_f(4, tracker)

        if -a < Df < a:
            x2 = 6
        elif inv_f(-2, tracker) < 0:
            x2 = 0
        elif inv_f(-2, tracker) > 6:
            x2 = 6
        else:
            x2 = inv_f(-2, tracker)

        return min(x1, x2), max(x1, x2)

    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        title = Text("The Derivative", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)

        # defs
        h = Symbol('a')
        tracker = ValueTracker(1.3)
        x = Symbol('x')
        y = x ** 3 - 9 * x ** 2 + 25 * x - 19
        Dy = y.diff(x)
        f = lambdify(x, y, 'numpy')
        Df = lambdify(x, Dy, 'numpy')
        tanLine = lambdify([x, h], Df(h) * (x - h) + f(h), 'numpy')
        inv_f = lambdify([x, h], (x - f(h)) / Df(h) + h, 'numpy')

        function = axes.plot(
            lambda t: f(t),
            color=PURPLE_C,
            x_range=[1, 4.8]
        )

        tanPlot = always_redraw(
            lambda: axes.plot(lambda x: tanLine(x, tracker.get_value()),
                              color=GREEN_E,
                              x_range=self.functionInterval(inv_f, tracker.get_value(), Df(tracker.get_value()))
                              ))

        slopeText = always_redraw(
            lambda: MathTex(r"f'(%.2f)= %.2f" % (tracker.get_value(), Df(tracker.get_value())),
                            color=GREEN_E,
                            font_size=fontsize)
            .shift(DOWN).shift(RIGHT)
        )

        functionText = MathTex(r"f(x)=x^3-9x^2+25x-19", color=PURPLE_C, font_size=fontsize)
        functionText.shift(2 * UP)
        functionText.shift(2 * RIGHT)

        derivText = MathTex(r"\frac{df}{dx}=3x^2-18x+25", color=GREEN_E, font_size=fontsize).shift(RIGHT * 1.8)
        altderivText = MathTex(r"f'(x)=3x^2-18x+25", color=GREEN_E, font_size=fontsize).shift(RIGHT * 1.8)
        self.add(axes, tracker, title)
        self.next_section()
        self.play(Create(function), Create(functionText))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(derivText))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Transform(derivText, altderivText))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(tanPlot), Create(slopeText))
        self.next_section(type=PresentationSectionType.NORMAL)
        moveTangent = lambda mobject, dt: mobject.increment_value(dt)
        tracker.add_updater(moveTangent)
        self.wait(1.5)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.wait(1.03)
        tracker.remove_updater(moveTangent)


class Integral(Scene):
    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        self.next_section(type=PresentationSectionType.NORMAL)
        title = Text("The Integral", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)

        # defs
        vg = VGroup()
        h = Symbol('a')
        x = Symbol('x')
        y = sin(x)
        Dy = y.diff(x)
        f = lambdify(x, y, 'numpy')
        Df = lambdify(x, Dy, 'numpy')
        # tanLine = lambdify([x, h], Df(h) * (x - h) + f(h), 'sympy')
        # inv_tan = lambdify([x, h], (x - f(h)) / Df(h) + h, 'numpy')

        function = axes.plot(
            lambda t: f(t),
            color=PURPLE_C,
            x_range=[0, 2 * PI]
        )
        width = ValueTracker(0.01)

        area = always_redraw(lambda: axes.get_area(graph=function, x_range=(0, width.get_value()),
                                                   color=DARK_BLUE, opacity=0.5))

        functionText = MathTex(r"f(x)=\sin x", color=PURPLE_C, font_size=fontsize)
        functionText.shift(DOWN).shift(2 * RIGHT)

        antiDeriv0A = MathTex(r"=", color=RED_E, font_size=fontsize).shift(2 * UP).shift(2 * RIGHT)
        antiDeriv0B = MathTex(r"\int f'(x) dx", color=RED_E, font_size=fontsize).next_to(antiDeriv0A, LEFT)
        antiDeriv0C = MathTex(r"f(x)", color=RED_E, font_size=fontsize).next_to(antiDeriv0A, RIGHT)

        antiDeriv1A = MathTex(r" = ", color=RED_E, font_size=fontsize).shift(2 * UP).shift(2 * RIGHT)
        antiDeriv1B = MathTex(r"\int f(x) dx ", color=RED_E, font_size=fontsize).next_to(antiDeriv1A, LEFT)
        antiDeriv1C = MathTex(r"F(x)", color=RED_E, font_size=fontsize).next_to(antiDeriv1A, RIGHT)

        # antiDeriv2 = MathTex(r"\int \sin x dx = -\cos x", color=PURPLE_C).shift(2*RIGHT).shift(DOWN)

        integral0B = MathTex(r" = ", color=DARK_BLUE, font_size=fontsize).shift(0.5 * UP).shift(2 * RIGHT)
        integral0A = MathTex(r"\int_a^b f(x) dx", color=DARK_BLUE, font_size=fontsize).next_to(integral0B, LEFT)
        integral0C = MathTex(r" F(b)-F(a)", color=DARK_BLUE, font_size=fontsize).shift(UP).next_to(integral0B, RIGHT)
        integral1B = always_redraw(lambda: MathTex(r" = ",
                                                   color=DARK_BLUE, font_size=fontsize).shift(0.5 * UP).shift(
            2 * RIGHT))
        integral1A = always_redraw(lambda: MathTex(r"\int_0^{%.2f} \sin x dx"
                                                   % (width.get_value()),
                                                   color=DARK_BLUE, font_size=fontsize).next_to(integral1B, LEFT))
        integral1C = always_redraw(lambda: MathTex(r"-\cos(%.2f)+\cos(0)"
                                                   % (width.get_value()),
                                                   color=DARK_BLUE, font_size=fontsize).next_to(integral1B, RIGHT))

        areaValueA = MathTex("= ", color=DARK_BLUE, font_size=fontsize).shift(2 * RIGHT)
        areaValueB = always_redraw(lambda: MathTex("%.2f" % (-cos(width.get_value()) + 1), color=DARK_BLUE,
                                                   font_size=fontsize).next_to(areaValueA, RIGHT))

        # initialize
        self.add(axes, width, title)
        # draw antiderivatives
        self.play(Create(antiDeriv0A), Create(antiDeriv0B), Create(antiDeriv0C))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Transform(antiDeriv0A, antiDeriv1A), Transform(antiDeriv0B, antiDeriv1B),
                  Transform(antiDeriv0C, antiDeriv1C))
        # draw integral
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(integral0A), Create(integral0B), Create(integral0C))
        # draw function text
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(function), Create(functionText))
        # convert integral
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Transform(integral0A, integral1A), Transform(integral0B, integral1B),
                  Transform(integral0C, integral1C))
        self.add(integral1A, integral1C)
        self.remove(integral0A, integral0C)
        # draw area
        self.next_section(type=PresentationSectionType.NORMAL)
        self.play(Create(area))
        self.next_section(type=PresentationSectionType.NORMAL)
        self.add(areaValueA, areaValueB)
        width.add_updater(lambda mobject, dt: mobject.increment_value(2 * dt))
        self.wait(PI / 4)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.wait(PI / 4)
        self.next_section(type=PresentationSectionType.NORMAL)
        self.wait(PI / 4)


class DiffEQ(Scene):
    def construct(self):
        axes = NumberPlane(x_range=[-1.5, 2 * PI, 1], x_length=5, y_range=[-2, 4, 1],
                           y_length=5).add_coordinates().shift(
            LEFT * 3.5)
        axes.background_lines.set_opacity(0)
        axes.x_axis.set_color(BLACK)
        axes.y_axis.set_color(BLACK)
        bullet1 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(1.6*UP)
        bullet2 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(0.8*UP)
        bullet3 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6)
        bullet4 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(1.6*DOWN)
        line1 = Tex("One or more derivatives of a function", color=BLACK, font_size=40).next_to(bullet1, RIGHT)
        line3 = Tex("Often very difficult or impossible to solve", color=BLACK, font_size=40).next_to(bullet3, RIGHT)
        line2 = Tex("Used to model many physical phenomena", color=BLACK, font_size=40).next_to(bullet2, RIGHT)
        line4 = Tex(r"Differential operator ", color=BLACK, font_size=40).next_to(bullet4, RIGHT)

        operator2 = MathTex(r"= ", color=BLACK, font_size=40).next_to(line4, 2*DOWN).shift(LEFT)
        operator1 = MathTex(r"\mathbf{L} ", color=BLACK, font_size=40).next_to(operator2, LEFT)
        operator3 = MathTex(r"\frac{d^2}{dt^2} + b \frac{d}{dt} + k", color=BLACK, font_size=40).next_to(operator2, RIGHT)
        opeq1 = MathTex(r"= ", color=BLACK, font_size=40).next_to(operator2, 3*DOWN)
        opeq2 = MathTex(r"\mathbf{L} x ", color=BLACK, font_size=40).next_to(opeq1, LEFT)
        opeq3 = MathTex(r"f(t)", color=BLACK, font_size=40).next_to(opeq1, RIGHT)

        spring = ImageMobject("spring-mass.png").shift(4 * RIGHT)
        spring.scale(0.25)
        navier_stokes = MathTex(r"\frac{\partial \textbf{u}}{\partial t} + (\textbf{u}\cdot \nabla)\textbf{u}"
                                r"-\nu \nabla^2\textbf{u}=-\frac{1}{\rho}\nabla p + g", color=BLACK,
                                font_size=30).next_to(line3, DOWN)
        spring_mass = MathTex(r"m \frac{d^2x}{dt^2} + b \frac{dx}{dt} + kx = f(t).", color=BLACK, font_size=30).next_to(
            spring, UP * 2)
        title = Text("Differential Equations", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)
        self.add(titleDot, title)
        self.add(spring, bullet1, line1, navier_stokes, bullet2, line2, bullet3, spring_mass, line3, line4, bullet4, operator1, operator2, operator3, opeq1, opeq2, opeq3)
        self.wait(1)


class springPlot(Scene):
    def construct(self):
        title = Text("Differential Equations", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)
        axes = NumberPlane(
            axis_config={"color": BLACK},
            x_range=[0, 2 * PI, 1],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=6
        ).add_coordinates().shift(DOWN)

        axes.x_axis.set_color(BLACK)
        axes.y_axis.set_color(BLACK)
        f = axes.plot(
            lambda x: np.exp(-x) * np.cos(8 * x),
            color=BLUE_E,
            x_range=[0, 2 * PI]
        )
        self.add(title, axes)
        self.play(Create(f))


class Adjoint(Scene):
    def construct(self):
        self.next_section(type = PresentationSectionType.NORMAL)
        title = Text("The Adjoint Operator", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)
        bullet1 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(UP)
        bullet2 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(DOWN)
        bullet3 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(2*DOWN)
        bullet4 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(3*DOWN)
        line1 = Tex(r"Repeated integration by parts", color=BLACK, font_size=40).next_to(bullet1, RIGHT)
        intByParts = MathTex(r"\int_\mathrm{a}^\mathrm{b} v \mathbf{L} u dx = [ \cdots]\biggr\rvert_\mathrm{a}^\mathrm{b} + \int_\mathrm{a}^\mathrm{b} u\mathbf{L^*}  v dx", color=BLACK, font_size=40).next_to(line1, DOWN)
        table = ImageMobject("tabular.png").shift(4*RIGHT).scale(0.4)
        line3 = Tex(r"Example: \(a(x)\frac{d^2}{dx^2}+b(x)\frac{d}{dx}+c(x)\)", color=BLACK, font_size=40).next_to(bullet3, RIGHT)
        line2 = Tex(r"Self adjoint if \( \mathbf{L} = \mathbf{L^*} \)", color=BLACK, font_size=40).next_to(bullet2, RIGHT)
        line4 = Tex(r"Second order linear: self adjoint if \(a'=b\)", color=BLACK, font_size=40).next_to(bullet4, RIGHT)
        self.add(title, bullet1, line1, intByParts, table, line3, line2, bullet3, bullet2, line4, bullet4)
        self.wait()


class Delta(Scene):
    def construct(self):
        self.next_section(type = PresentationSectionType.NORMAL)
        title = Text("The Dirac Delta Function", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)
        bullet1 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(UP)
        bullet2 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6)
        bullet3 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(DOWN)
        bullet4 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(2 * DOWN)
        line1 = Tex(r"Unit point mass", color=BLACK, font_size=40).next_to(bullet1, RIGHT)
        line2 = Tex(r"", color=BLACK, font_size=40).next_to(bullet2, RIGHT)
        line3 = Tex(r"Point mass", color=BLACK, font_size=40).next_to(bullet3, RIGHT)
        line4 = Tex(r"Point mass", color=BLACK, font_size=40).next_to(bullet4, RIGHT)

        self.add(title)



class George(Scene):
    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        title = Text("The Method of Green's Functions", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)
        bullet1 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(2 * UP)
        bullet2 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(UP)
        bullet3 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6)
        bullet4 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(DOWN)
        bullet5 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(2*DOWN)
        bullet6 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(3*DOWN)
        line1 = Tex(r"Son of a baker with only one year of schooling as a child",
                    color=BLACK, font_size=40).next_to(bullet1, RIGHT)
        line2 = Tex(r"Disliked the bakery work", color=BLACK, font_size=40).next_to(bullet2, RIGHT)
        line3 = Tex(r"His father bought a windmill because of rising hostility toward bakers", color=BLACK, font_size=40).next_to(bullet3, RIGHT)
        line4 = Tex(r"Also disliked milling", color=BLACK, font_size=40).next_to(bullet4, RIGHT)
        line5 = Tex(r"Published an essay on Electricity and Magnetism in 1828", color=BLACK, font_size=40).next_to(bullet5, RIGHT)
        line6 = Tex(r"Inherited from his father and studied mathematics at Cambridge", color=BLACK, font_size=40).next_to(bullet6, RIGHT)

        self.add(title, bullet1, bullet4, bullet3, bullet2, line1, line2, line3, line4, line5, bullet5, bullet6, line6)
        self.wait(1)

class GreensFunctions(Scene):
    def construct(self):
        self.next_section(type=PresentationSectionType.NORMAL)
        title = Text("The Method of Green's Functions", color=BLACK)
        title.align_to(titleDot, LEFT)
        title.align_to(titleDot, UP)
        bullet1 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(2 * UP)
        bullet2 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6)
        bullet3 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift( DOWN)
        bullet4 = Dot(radius=0.05, color=BLACK).shift(LEFT * 6).shift(2 * DOWN)
        line1 = Tex(r"Find solutions to linear differential equations of the form", color=BLACK, font_size=40).next_to(bullet1, RIGHT)
        diffeq = MathTex(r" \mathbf{L}u=\phi ", color=BLACK, font_size=40).next_to(line1,DOWN)
        line1cont = Tex(r"over the interval a \(\leq x \leq\) b.", color=BLACK, font_size=40).next_to(line1, DOWN*3).align_to(line1, LEFT)
        line2 = Tex(r"Determine the ajoint, \(\mathbf{L^*}\)", color=BLACK, font_size=40).next_to(bullet2, RIGHT)
        line3 = Tex(r"Let \(\mathbf{L^*}G = \delta \)", color=BLACK, font_size=40).next_to(bullet3, RIGHT)
        line4 = Tex(r"Solving the differential equation becomes a problem of integration", color=BLACK, font_size=40).next_to(bullet4, RIGHT)

        self.add(title, bullet1, line1, diffeq, line1cont, bullet2, line2, bullet3, bullet4, line3, line4)
        self.wait(1)

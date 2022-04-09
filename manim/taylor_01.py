from manimlib.imports import *

class BeginAnimation(Scene):

    def construct(self):
        sentence01 = TextMobject("我想在本次视频开头让你对本期内容有一些直观上的理解，", color = BLUE).scale(0.8)
        sentence02 = TextMobject("如果你此前没有听过或是对泰勒公式不熟悉也没有关系也不要害怕，", color = BLUE).scale(0.8)
        sentence03 = TextMobject("我将尽可能的减少公式的推导，所以一起来看这次的内容吧！", color = BLUE).scale(0.8)
        sentence01.shift(UP)
        sentence03.shift(DOWN)
        group = VGroup(sentence01, sentence02, sentence03)
        self.play(Write(sentence01, run_time = 2))
        self.play(Write(sentence02, run_time = 2))
        self.play(Write(sentence03, run_time = 2))
        self.wait(2)
        word = TextMobject("泰勒公式", color = RED).scale(1.5)
        equation = TextMobject("$$f(x)=\\sum_{n=0}^N\\displaystyle\\frac{f^{(n)}(a)}{n!}(x-a)^n+R_N(x)$$", color = BLUE).scale(1.5)
        self.play(ReplacementTransform(group, word, run_time = 2))
        self.wait(2)
        self.play(ReplacementTransform(word, equation, run_time = 2))
        self.wait(2)
        self.play(FadeOut(equation, run_time = 2))
        self.wait()

class Part01(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "y_min": -2,
        "y_max": 2,
        "x_axis_width": 14,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
        "graph_origin": ORIGIN+DOWN*0.5,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-3, 3, 1),
        "y_labeled_nums": range(-2, 2, 1)
    }

    def construct(self):
        sentence01 = TextMobject("思考这样一个问题：", color = BLUE).to_edge(UP).scale(0.8)
        sentence02 = TextMobject("对一个给定的函数，我们能否使用任意次的多项式函数来近似？", color = RED).to_edge(UP).shift(DOWN).scale(0.8)
        self.play(Write(sentence01, run_time = 2))
        self.play(Write(sentence02, run_time = 2))
        equation = TextMobject("$$f(x)=a_0+a_1x+a_2x^2+a_3x^3+a_4x^4+a_5x^5+a_6x^6\\cdots$$").to_edge(UP).shift(DOWN*2).scale(0.8)
        a_list = TextMobject("$$a_0=$$", "$$a_1=$$", "$$a_2=$$", "$$a_3=$$", "$$a_4=$$", "$$a_5=$$", "$$a_6=$$").scale(0.6).to_edge(UR).shift(LEFT)
        self.play(Write(equation, run_time = 2))
        self.wait(2)
        self.play(sentence01.scale, 0.6, sentence01.shift, LEFT*4, sentence02.scale, 0.6, sentence02.shift, LEFT*3.5+UP*0.5,
                  equation.scale, 0.6, equation.shift, LEFT*4+UP)
        self.play(Write(a_list, run_time = 4))
        self.setup_axes(animate=True)
        func = [
            lambda x: x,
            lambda x: 1+x+x**5,
            lambda x: 1+x+x**2+x**5/5,
            lambda x: 1-x**2/2+x**4/math.factorial(4),
            lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6)
        ]
        group = [
            TextMobject("$$0$$", "$$1$$", "$$0$$", "$$0$$", "$$0$$", "$$0$$", "$$0$$"),
            TextMobject("$$1$$", "$$1$$", "$$0$$", "$$0$$", "$$0$$", "$$1$$", "$$0$$"),
            TextMobject("$$1$$", "$$1$$", "$$1$$", "$$0$$", "$$0$$", "$$\\frac{1}{5}$$", "$$0$$"),
            TextMobject("$$1$$", "$$0$$", "$$-\\frac{1}{2}$$", "$$0$$", "$$\\frac{1}{4!}$$", "$$0$$", "$$0$$"),
            TextMobject("$$1$$", "$$0$$", "$$-\\frac{1}{2}$$", "$$0$$", "$$\\frac{1}{4!}$$", "$$0$$", "$$-\\frac{1}{6!}$$")
        ]

        for f in group:
            f.set_color(BLUE).scale(0.4)
            for i in range(0, 7):
                f[i].next_to(a_list[i].get_corner(RIGHT), RIGHT)
        func_graph = [
            self.get_graph(
                f,
                color = BLUE
            )
            for f in func
        ]
        for i in range(0, 5):
            self.wait(3)
            if i == 0:
                self.play(ShowCreation(func_graph[0],run_time=1), Write(group[0], run_time = 3))
            else:
                self.play(ReplacementTransform(func_graph[i-1], func_graph[i], run_time = 1), ReplacementTransform(group[i-1], group[i], run_time = 1))
        self.wait(2)
        group = VGroup(sentence01, sentence02, self.axes, func_graph[4], equation, group[4], a_list)
        self.play(FadeOut(group, run_time = 2))
        self.wait(2)
        self.wait()

class Part02(Scene):
    CONFIG = {
        'ML': 'ML.png',
        'Regression': 'PolyRegression.png'
    }
    def construct(self):
        sentence01 = TextMobject("如果你对机器学习有些了解，你一定会对上面的问题有一些自己的想法，", "甚至对于特定的函数会提出新的拟合方式", color = RED).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("但是这并不是我们今天想讨论的重点", color = BLUE).scale(0.8).next_to(sentence01.get_corner(DOWN), DOWN)
        ML = ImageMobject(self.ML)
        ML.set_height(4)
        Regression = ImageMobject(self.Regression)
        Regression.set_height(4)
        ML.shift(DOWN+LEFT*4)

        Regression.next_to(ML, RIGHT)
        self.play(Write(sentence01[0], run_time = 1))
        self.play(FadeInFromLarge(ML), run_time = 1.5)
        self.play(Write(sentence01[1]), run_time =1)
        self.play(FadeInFromLarge(Regression), run_time = 1.5)
        self.wait(2)

        self.play(Write(sentence02), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence01), FadeOut(sentence02), FadeOut(ML), FadeOut(Regression), run_time = 1)
        self.wait()

class Part03(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -10,
        "y_max": 10,
        "x_axis_width": 14,
        "y_axis_height": 8,
        "x_labeled_nums": range(-5, 5, 1),
        "y_labeled_nums": range(-10, 10, 2),
        "graph_origin": ORIGIN + DOWN * 1.2,
        "function_color": RED,
        "axes_color": WHITE
    }

    def construct(self):
        sentence01 = TextMobject("对一个给定的函数，我们能否使用任意次的多项式函数来近似？", color=BLUE).to_edge(UP).scale(0.8)
        self.play(Write(sentence01), run_time = 1)
        self.wait(2)
        sentence02 = TextMobject("想要实现这个问题我们需要理解如何正确地使用这些零件：$x^n$", color=BLUE).next_to(sentence01, DOWN).scale(0.8)
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        sentence03 = TextMobject("我们试一试先将$x$与$x^2$相加起来", color = RED).next_to(sentence02, DOWN).scale(0.8)
        self.play(Write(sentence03), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence01), FadeOut(sentence02), run_time = 1)
        self.play(sentence03.scale, 0.6, sentence03.to_edge, UL)
        self.setup_axes(animate=True)
        func_graph_1 = self.get_graph(lambda x:x, color = GREEN)
        func_lab_1 = self.get_graph_label(func_graph_1, label="y=x", x_val=4)
        func_graph_2 = self.get_graph(lambda x:x**2, color = GREEN)
        func_lab_2 = self.get_graph_label(func_graph_2, label="y=x^2", x_val=-2)
        func_graph_3 = self.get_graph(lambda x:x+x**2, color = RED)
        func_lab_3 = self.get_graph_label(func_graph_3, label="y=x+x^2", x_val = 2)
        self.play(ShowCreation(func_graph_1), ShowCreation(func_lab_1), run_time=1.5)
        self.play(ShowCreation(func_graph_2), ShowCreation(func_lab_2), run_time=1.5)
        self.play(ShowCreation(func_graph_3), ShowCreation(func_lab_3), run_time=1.5)

        sentence04 = TextMobject("我们看到他们相处得还算融洽，也就是说并没有出现明显压制对方的情况", color = BLUE).next_to(sentence03, DOWN).shift(1.2*RIGHT).scale(0.4)
        sentence05 = TextMobject("二者的特性依旧能在和函数中体现出来，但是更高次的$x^2$已经占据了主导", color = BLUE).next_to(sentence04, DOWN).scale(0.4)
        self.play(Write(sentence04), run_time = 1)
        self.wait(2)
        self.play(Write(sentence05), run_time = 1)
        self.wait(2)
        group = VGroup(sentence03, sentence04, sentence05, func_graph_1, func_graph_3, func_lab_1, func_lab_3)
        self.play(FadeOut(group), run_time = 1)
        self.wait(1)
        self.wait()

class Part04(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -10,
        "y_max": 10,
        "x_axis_width": 14,
        "y_axis_height": 8,
        "x_labeled_nums": range(-5, 5, 1),
        "y_labeled_nums": range(-10, 10, 2),
        "graph_origin": ORIGIN + DOWN * 1.2,
        "function_color": RED,
        "axes_color": WHITE
    }

    def construct(self):
        self.setup_axes(animate=False)
        func_graph_1 = self.get_graph(lambda x: x**2, color = GREEN)
        func_lab_1 = self.get_graph_label(func_graph_1, label="y=x^2", x_val=-2)
        self.add(func_lab_1, func_graph_1)
        sentence01 = TextMobject("那我们试一试将$x^7$与$x^2$相加起来",color = BLUE).scale(0.4).to_edge(UL)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        func_graph_2 = self.get_graph(lambda x: x**7, color = BLUE)
        func_lab_2 = self.get_graph_label(func_graph_2, label = "y=x^7", x_val = -1.2).shift(LEFT)
        self.play(ShowCreation(func_graph_2), Write(func_lab_2), run_time = 1.5)
        self.wait(1)
        func_graph_3 = self.get_graph(lambda x:x**2+x**7, self.function_color)
        func_lab_3 = self.get_graph_label(func_graph_3, label = "y=x^2+x^7", x_val = 1)
        self.play(ShowCreation(func_graph_3), Write(func_lab_3), run_time = 1.5)
        self.wait(2)
        sentence02 = TextMobject("我们可以看到此时几乎已经体现不出$x^2$的特性！", color = BLUE).scale(0.4).next_to(sentence01, DOWN).shift(RIGHT*0.5)
        self.play(Write(sentence02), run_time = 1.5)
        self.wait(2)
        sentence03 = TextMobject("此时你一定会思考如何去控制使得和函数可以同时体现二者的特性", color = RED).scale(0.4).next_to(sentence02, DOWN)
        self.play(Write(sentence03), run_time = 1.5)
        self.wait(1)
        sentence04 = TextMobject("让我们试着在每一项的分母上加上它的幂次", color = BLUE).scale(0.4).next_to(sentence03, DOWN)
        self.play(Write(sentence04), run_time = 1.5)
        self.wait(1)
        group = VGroup(sentence01, sentence02, sentence03)
        self.play(FadeOut(group), sentence04.to_edge, UL, run_time = 1.5)
        func_graph_4 = self.get_graph(lambda x:x**2/2+x**7/7, color = RED)
        func_lab_4 = self.get_graph_label(func_graph_4, label = "y=\\displaystyle\\frac{x^2}{2}+\\frac{x^7}{7}", x_val = 1)
        self.play(ReplacementTransform(func_graph_3, func_graph_4), ReplacementTransform(func_lab_3, func_lab_4), run_time =1.5)
        self.wait(2)
        sentence05 = TextMobject("我们看到此时情况已经发现了一些改善，但效果仍然不够好，那么我们如果将分母换为幂次的阶乘将会发生什么呢？", color = BLUE).next_to(sentence04, DOWN).scale(0.4)
        self.play(Write(sentence05), run_time = 1.5)
        self.wait(2)
        func_graph_5 = self.get_graph(lambda x: x**2/2+x**7/math.factorial(7), color = RED)
        func_lab_5 = self.get_graph_label(func_graph_5, label = "y=\\displaystyle\\frac{x^2}{2!}+\\frac{x^7}{7!}", x_val = 1).shift(DOWN)
        self.play(ReplacementTransform(func_graph_4, func_graph_5), ReplacementTransform(func_lab_4, func_lab_5), run_time =1.5)
        self.wait(2)
        sentence06 = TextMobject("这时曲线已经在零点附近体现出了$x^2$的特性，让我们调整坐标轴看一看大范围内的情况", color = RED).next_to(sentence05, DOWN).scale(0.4).shift(RIGHT*0.5)
        self.play(Write(sentence06), run_time = 1.5)
        self.wait(1)
        group_1 = VGroup(self.axes, sentence04, sentence05, sentence06, func_lab_1, func_lab_2, func_lab_5, func_graph_1, func_graph_2, func_graph_5)
        self.play(FadeOut(group_1), run_time = 1)
        self.wait(2)
        self.wait()

class Part05(Scene):
    CONFIG = {
        'GeoGebra':'GeoGebra.png'
    }

    def construct(self):
        GeoGebra = ImageMobject(self.GeoGebra).set_height(6).shift(DOWN)
        sentence01 = TextMobject("由于发现使用manim画大范围的图效果并不好，贴上一张GeoGebra的图~", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("所以我们看到阶乘帮助我们很好地调和了高次项和低次项", color = RED).scale(0.8).next_to(sentence01, DOWN)
        sentence03 = TextMobject("最后我将用$y=e^x$和$y=\\sin x$为例，再次直观体会多项式拟合函数", color = RED).scale(0.8).next_to(sentence02, DOWN)
        sentence04 = TextMobject("下期视频我们将更深入地去解释泰勒公式，大家不见不散哟~", color = BLUE).scale(0.8).next_to(sentence03, DOWN).shift(DOWN)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(FadeInFromLarge(GeoGebra))
        self.wait(5)
        self.play(FadeOut(GeoGebra))
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03), run_time = 1)
        self.wait(1)
        self.play(Write(sentence04), run_time = 1)
        self.wait(2)
        group = VGroup(sentence01, sentence02, sentence03, sentence04)
        self.play(FadeOut(group), run_time = 1.5)
        self.wait(1)
        self.wait()





class ExponentielFunction(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 75,
        "x_axis_width": 14,
        "y_axis_height": 6,
        "y_tick_frequency": 15,
        "graph_origin": ORIGIN + DOWN * 2.5,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 5, 1),
        "y_labeled_nums": range(0, 75, 15)
    }
    def construct(self):

        self.setup_axes(animate=True)
        sentence01 = TextMobject("注：坐标轴经过伸缩处理以方便演示", color = BLUE).to_edge(DOWN).scale(0.8)
        self.play(Write(sentence01))
        func_graph = self.get_graph(lambda x : np.exp(x), self.function_color)
        func_lab = self.get_graph_label(func_graph, label="y=e^x", x_val = 4).shift(LEFT)

        poly = []
        for i in range(1, 9):
            poly.append(lambda x, i=i: x**i/math.factorial(i))

        poly_graph = [
            self.get_graph(
                f,
                color = GREEN
            )
            for f in poly
        ]

        taylor = [
            lambda x: 1,
            lambda x: 1+x,
            lambda x: 1+x+x**2/math.factorial(2),
            lambda x: 1+x+x**2/math.factorial(2)+x**3/math.factorial(3),
            lambda x: 1+x+x**2/math.factorial(2)+x**3/math.factorial(3)+x**4/math.factorial(4),
            lambda x: 1+x+x**2/math.factorial(2)+x**3/math.factorial(3)+x**4/math.factorial(4)+x**5/math.factorial(5),
            lambda x: 1+x+x**2/math.factorial(2)+x**3/math.factorial(3)+x**4/math.factorial(4)+x**5/math.factorial(5)+x**6/math.factorial(6),
            lambda x: 1+x+x**2/math.factorial(2)+x**3/math.factorial(3)+x**4/math.factorial(4)+x**5/math.factorial(5)+x**6/math.factorial(6)+x**7/math.factorial(7),
            lambda x: 1+x+x**2/math.factorial(2)+x**3/math.factorial(3)+x**4/math.factorial(4)+x**5/math.factorial(5)+x**6/math.factorial(6)+x**7/math.factorial(7)+x**8/math.factorial(8)
        ]
        taylor_label= TextMobject(
            "$y=1$",
            "$y=1+x$",
            "$y=1+x+\\displaystyle\\frac{1}{2!}x^2$",
            "$$y=1+x+\\displaystyle\\frac{1}{2!}x^2+\\frac{1}{3!}x^3$$",
            "$$y=1+x+\\displaystyle\\frac{1}{2!}x^2+\\frac{1}{3!}x^3+\\frac{1}{4!}x^4$$",
            "$$y=1+x+\\displaystyle\\frac{1}{2!}x^2+\\frac{1}{3!}x^3+\\cdots+\\frac{1}{5!}x^5$$",
            "$$y=1+x+\\displaystyle\\frac{1}{2!}x^2+\\frac{1}{3!}x^3+\\cdots+\\frac{1}{6!}x^6$$",
            "$$y=1+x+\\displaystyle\\frac{1}{2!}x^2+\\frac{1}{3!}x^3+\\cdots+\\frac{1}{7!}x^7$$",
            "$$y=1+x+\\displaystyle\\frac{1}{2!}x^2+\\frac{1}{3!}x^3+\\cdots+\\frac{1}{8!}x^8$$",
            color = BLUE
        ).to_edge(UL).scale(0.6)
        poly_label = TextMobject(
            "$y=x$",
            "$y=\\displaystyle\\frac{1}{2!}x^2$",
            "$y=\\displaystyle\\frac{1}{3!}x^3$",
            "$y=\\displaystyle\\frac{1}{4!}x^4$",
            "$y=\\displaystyle\\frac{1}{5!}x^5$",
            "$y=\\displaystyle\\frac{1}{6!}x^6$",
            "$y=\\displaystyle\\frac{1}{7!}x^7$",
            "$y=\\displaystyle\\frac{1}{8!}x^8$",
            color = GREEN
        ).scale(0.6)
        taylor_graph = [
            self.get_graph(
                f,
                color = BLUE
            )
            for f in taylor
        ]

        group = [
            VGroup(poly_graph[i], taylor_graph[i])
            for i in range(0, 8)
        ]

        taylor_label[0].to_edge(UL)
        self.play(ShowCreation(func_graph), ShowCreation(func_lab))
        self.wait(2)
        self.play(ShowCreation(taylor_graph[0]), Write(taylor_label[0]))
        for i in range(0, 8):
            self.wait(2)
            taylor_label[i+1].to_edge(UL)
            poly_label[i].to_edge(UL).shift(DOWN)
            self.play(ShowCreation(poly_graph[i]), Write(poly_label[i]))
            self.wait(2)
            self.play(ReplacementTransform(group[i], taylor_graph[i+1]), FadeOut(taylor_graph[i]), ReplacementTransform(taylor_label[i], taylor_label[i+1]), FadeOut(poly_label[i]))
        sentence02 = TextMobject("我们看到此时的多项式函数已经与指数函数拟合得很不错了！", color = BLUE).scale(0.6).to_edge(UL).shift(DOWN)
        self.play(Write(sentence02))
        self.wait(1)
        group1 = VGroup(self.axes, sentence01, sentence02, func_graph, func_lab, taylor_graph[8], taylor_label[8])
        self.play(FadeOut(group1, run_time = 2))
        self.wait(1)
        self.wait()


class SineFunction(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -1.2,
        "y_max": 1.2,
        "x_axis_width": 14,
        "y_axis_height": 7,
        "y_tick_frequency": 0.4,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 5, 1),
        "y_labeled_nums": [-1, 1]
    }
    def construct(self):

        self.setup_axes(animate=False)
        sentence01 = TextMobject("注：坐标轴经过伸缩处理以方便演示", color=BLUE).to_edge(DOWN).scale(0.8)
        self.play(Write(sentence01))
        func_graph = self.get_graph(lambda x : np.sin(x), self.function_color)
        func_lab = self.get_graph_label(func_graph, label="y=\\sin x", x_val=4).shift(LEFT)

        poly = []
        for i in range(2, 8):
            poly.append(lambda x, i=i: (-1)**(i+1)*i*x**(2*i-1)/math.factorial(2*i-1))

        poly_graph = [
            self.get_graph(
                f,
                color = GREEN
            )
            for f in poly
        ]

        taylor = [
            lambda x: x,
            lambda x: x - x**3/math.factorial(3),
            lambda x: x - x**3/math.factorial(3)+x**5/math.factorial(5),
            lambda x: x - x**3/math.factorial(3)+x**5/math.factorial(5)-x**7/math.factorial(7),
            lambda x: x - x**3/math.factorial(3)+x**5/math.factorial(5)-x**7/math.factorial(7)+x**9/math.factorial(9),
            lambda x: x - x**3/math.factorial(3)+x**5/math.factorial(5)-x**7/math.factorial(7)+x**9/math.factorial(9)-x**11/math.factorial(11),
            lambda x: x - x**3/math.factorial(3)+x**5/math.factorial(5)-x**7/math.factorial(7)+x**9/math.factorial(9)-x**11/math.factorial(11)+x**13/math.factorial(13)
        ]

        taylor_label = TextMobject(
            "$$y=x$$",
            "$$y=x-\\displaystyle\\frac{x^3}{3!}$$",
            "$$y=x-\\displaystyle\\frac{x^3}{3!}+\\frac{x^5}{5!}$$",
            "$$y=x-\\displaystyle\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}$$",
            "$$y=x-\\displaystyle\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}+\\frac{x^9}{9!}$$",
            "$$y=x-\\displaystyle\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}+\\frac{x^9}{9!}-\\frac{x^{11}}{11!}$$",
            "$$y=x-\\displaystyle\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\frac{x^7}{7!}+\\frac{x^9}{9!}-\\frac{x^{11}}{11!}+\\frac{x^{13}}{13!}$$",
            color = BLUE
        ).to_edge(UL).scale(0.6)
        poly_label = TextMobject(
            "$$y=-\\displaystyle\\frac{x^3}{3!}$$",
            "$$y=\\displaystyle\\frac{x^5}{5!}$$",
            "$$y=-\\displaystyle\\frac{x^7}{7!}$$",
            "$$y=\\displaystyle\\frac{x^9}{9!}$$",
            "$$y=-\\displaystyle\\frac{x^{11}}{11!}$$",
            "$$y=\\displaystyle\\frac{x^{13}}{13!}$$",
            color = GREEN
        ).scale(0.6)
        taylor_graph = [
            self.get_graph(
                f,
                color = BLUE
            )
            for f in taylor
        ]

        group = [
            VGroup(poly_graph[i], taylor_graph[i])
            for i in range(0, 6)
        ]

        taylor_label[0].to_edge(UL)
        self.play(ShowCreation(func_graph), ShowCreation(func_lab))
        self.wait(2)
        self.play(ShowCreation(taylor_graph[0]), Write(taylor_label[0]))
        for i in range(0, 6):
            self.wait(2)
            taylor_label[i+1].to_edge(UL)
            poly_label[i].to_edge(UL).shift(DOWN)
            self.play(ShowCreation(poly_graph[i]), Write(poly_label[i]))
            self.wait(2)
            self.play(ReplacementTransform(group[i], taylor_graph[i + 1]), FadeOut(taylor_graph[i]),
                      ReplacementTransform(taylor_label[i], taylor_label[i + 1]), FadeOut(poly_label[i]))
        sentence02 = TextMobject("我们看到多项式函数与正弦函数同样拟合得不错！", color = BLUE).scale(0.6).to_edge(UL).shift(DOWN)
        sentence03 = TextMobject("而且细心的你一定发现我们只使用了奇数次幂！", color = PINK).scale(0.6).to_edge(UL).shift(DOWN*1.4)
        self.play(Write(sentence02), run_time = 1)
        self.play(Write(sentence03), run_time = 1)
        self.wait(2)
        group = VGroup(taylor_label[6], self.axes, sentence02, sentence03, sentence01, func_lab
                       ,func_graph, taylor_graph[6])
        self.play(FadeOut(group))
        self.wait()






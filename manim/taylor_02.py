from manimlib.imports import *

class BeginPart(GraphScene):
    CONFIG = {
        "x_min": -4,
        "x_max": 4,
        "y_min": -1.2,
        "y_max": 1.2,
        "x_axis_width": 8,
        "y_axis_height": 4,
        "y_tick_frequency": 0.4,
        "graph_origin": ORIGIN+DOWN*1.8,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-4, 4, 1),
        "y_labeled_nums": [-1, 1]
    }
    def construct(self):

        equation = TextMobject("$f(x)=\\sum_{n=0}^N$","$\\displaystyle\\frac{f^{(n)}(a)}{n!}$","$(x-a)^n+$","$R_N(x)$", color = RED).scale(1.5)
        sentence01 = TextMobject("在上一期视频中我们初步认识了泰勒公式", color = BLUE).scale(0.8).to_edge(UP).shift(DOWN*2)
        sentence02 = TextMobject("我们直观地感受了多项式函数拟合函数的魅力", color = BLUE).scale(0.8).next_to(sentence01, DOWN)
        sentence03 = TextMobject("不过还没有解释泰勒公式的这些符号代表着什么", color = GREEN).scale(0.8).next_to(sentence02, DOWN)
        sentence04 = TextMobject("依然不要害怕，在本期我仍然尽可能直观地去解释泰勒公式",color = GREEN).scale(0.8).next_to(sentence03, DOWN)
        sentence05 = TextMobject("有小伙伴已经在上期的评论区剧透了一种理解泰勒公式的思路！", color = GREEN).scale(0.8).next_to(sentence04, DOWN)
        group = VGroup(equation, sentence01, sentence02, sentence03, sentence04)

        self.play(DrawBorderThenFill(equation))
        self.play(equation.to_edge, UP, equation.scale, 0.8)
        self.wait(1)
        self.play(Write(sentence01), run_time = 1)
        self.wait(0.5)
        self.play(Write(sentence02), run_time = 2)
        self.setup_axes(animate=True)
        taylor = [
            lambda x: x,
            lambda x: x - x ** 3 / math.factorial(3),
            lambda x: x - x ** 3 / math.factorial(3) + x ** 5 / math.factorial(5),
            lambda x: x - x ** 3 / math.factorial(3) + x ** 5 / math.factorial(5) - x ** 7 / math.factorial(7),
            lambda x: x - x ** 3 / math.factorial(3) + x ** 5 / math.factorial(5) - x ** 7 / math.factorial(
                7) + x ** 9 / math.factorial(9),
            lambda x: x - x ** 3 / math.factorial(3) + x ** 5 / math.factorial(5) - x ** 7 / math.factorial(
                7) + x ** 9 / math.factorial(9) - x ** 11 / math.factorial(11),
            lambda x: x - x ** 3 / math.factorial(3) + x ** 5 / math.factorial(5) - x ** 7 / math.factorial(
                7) + x ** 9 / math.factorial(9) - x ** 11 / math.factorial(11) + x ** 13 / math.factorial(13)
        ]
        taylor_graph = [
            self.get_graph(
                f,
                color=GREEN
            )
            for f in taylor
        ]
        self.play(ShowCreation(taylor_graph[0]))
        for i in range(0, 6):
            self.wait(1)
            self.play(ReplacementTransform(taylor_graph[i], taylor_graph[i+1]))
        self.wait(2)
        self.play(FadeOut(self.axes), FadeOut(taylor_graph[6]))
        self.play(Write(sentence03), Indicate(equation[1]), Indicate(equation[3]), run_time = 2)
        self.wait(1)
        self.play(Write(sentence04), run_time = 1)
        self.wait(2)
        self.play(Write(sentence05), run_time = 1)
        self.wait(1)
        self.play(FadeOut(sentence05))
        self.wait(2)
        self.play(FadeOut(group), run_time=1.5)
        self.wait()

class Part01(Scene):

    def construct(self):
        sentence01 = TextMobject("我们首先跳到物理领域来认识另一个概念", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("在高中物理中我们学习过两种运动：匀速直线运动和匀加速直线运动").scale(0.8).next_to(sentence01, DOWN)
        sentence03 = TextMobject("现在我们来考虑这样一个问题，一质点以$a_0$的初速度，从$s_0$处正向运动，求$ts$时走过的路程S", color = RED).scale(0.8).next_to(sentence02, DOWN)
        equation01 = TextMobject("$S=s_0+a_0t$",color = BLUE).scale(0.8).next_to(sentence02, DOWN)
        sentence04 = TextMobject("这并不难你会很自然地得出：").scale(0.6).next_to(sentence02, DOWN*0.8)
        sentence05 = TextMobject("如果我们再加一个附加条件，质点的加速度是$a_1$", color = RED).scale(0.8).next_to(equation01, DOWN)
        sentence06 = TextMobject("这个问题也并不难：").scale(0.6).next_to(sentence05, DOWN*0.8)
        equation02 = TextMobject("$S=s_0+a_0t+\\displaystyle\\frac{1}{2}a_1t^2$",color = BLUE).scale(0.8).next_to(sentence05, DOWN)
        sentence07 = TextMobject("如果我们再加上一个条件，质点的加加速度是$a_2$", color = RED).scale(0.8).next_to(equation02, DOWN)
        sentence08 = TextMobject("这时你可能会感觉到困惑，加加速度是什么？").scale(0.6).next_to(sentence07, DOWN*0.8)
        sentence09 = TextMobject("加速度是用来描述速度的变化，加加速度自然是用来描述加速度的变化", color = GREEN).scale(0.6).next_to(sentence08, DOWN*0.8)
        sentence10 = TextMobject("在数学中用来描述函数变化的术语叫做导数，为了帮助大家更清楚地了解接下来的内容，我将用一些时间来讲一下导数", color = GREEN).scale(0.6).next_to(sentence09, DOWN*0.8)
        sentence11 = TextMobject("什么是导数？", color = BLUE).shift(UP*0.5)
        sentence12 = TextMobject("What is the derivative?", color = BLUE).shift(DOWN*0.5)

        group = VGroup(sentence01, sentence02)
        group1 = VGroup(sentence03, sentence05, sentence07, sentence08, sentence09, sentence10, equation01, equation02)
        group2 = VGroup(sentence11, sentence12)

        self.play(Write(sentence01), run_time = 1)
        self.wait(2)
        self.play(Write(sentence02), run_time = 1.5)
        self.wait(1)
        self.play(Write(sentence03), run_time = 2)
        self.wait(2)
        self.play(FadeOut(group), sentence03.to_edge, UL, run_time = 1)
        self.wait(2)
        self.play(Write(sentence04), run_time = 1)
        self.wait(1)
        self.play(FadeOut(sentence04))
        self.wait(1)
        self.play(Write(equation01), run_time = 1)
        self.wait(2)
        self.play(Write(sentence05), run_time = 1)
        self.wait(1)
        self.play(Write(sentence06), run_time = 1)
        self.wait(1)
        self.play(FadeOut(sentence06))
        self.wait(1)
        self.play(Write(equation02), run_time = 1)
        self.wait(2)
        self.play(Write(sentence07), run_time = 1)
        self.wait(1)
        self.play(Write(sentence08), run_time = 1)
        self.wait(1)
        self.play(Write(sentence09), run_time = 1)
        self.wait(1)
        self.play(Write(sentence10), run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(group1, group2), run_time = 1.5)
        self.wait(1)
        self.play(FadeOut(group2))
        self.wait()


class Derivative(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 25,
        "y_tick_frequency": 5,
        "y_labeled_nums": range(0, 25, 5),
        "exclude_zero_label": False,

        "y_axis_height": 6,
        "x_axis_width": 12,
        "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "func": lambda x: (x**2-4*x+5)/2
    }

    def construct(self):

        sentence01 = TextMobject("如何去描述一个函数在某点的变化？", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("其实我们在生活中经常会提到变化的问题，比如我们每天都会关注新冠疫情确诊人数的变化，"
                                 "我们此时将时间以天为单位去描述变化，也就是一些离散的点", color = BLUE).scale(0.6).next_to(sentence01, DOWN)

        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(sentence02), run_time = 2)
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color=RED)
        point = [
            self.input_to_graph_point(i, graph)
            for i in range(1, 9)
        ]
        dot = [
          Dot(p, color = BLUE)
          for p in point
        ]
        for i in range(0, 8):
            self.play(ShowCreation(dot[i]))
            self.wait(0.25)
        self.wait(2)
        group1 = VGroup(sentence01, sentence02)
        sentence04 = TextMobject("但对于一个函数并不是离散的点，而是连续的曲线", color = BLUE).scale(0.6).to_edge(UP)
        self.play(ReplacementTransform(group1, sentence04))
        self.play(ShowCreation(graph), run_time = 1.5)
        sentence05 = TextMobject("按照上面的思想，我们只需要将这个单位缩小得足够小，描述的变化也会足够精确", color = BLUE).scale(0.6).next_to(sentence04, DOWN)
        self.play(Write(sentence05), run_time = 1)
        slop1 = self.get_secant_slope_group(6, graph, dx=1, dx_label="dx = 1", df_label="\\frac{dy}{dx}")
        slop2 = self.get_secant_slope_group(6, graph, dx=0.5, dx_label="dx = 0.5", df_label="\\frac{dy}{dx}")
        slop3 = self.get_secant_slope_group(6, graph, dx=0.1, dx_label="dx = 0.1", df_label="\\frac{dy}{dx}")

        self.play(ShowCreation(slop1))
        self.wait(1)
        self.play(ReplacementTransform(slop1, slop2))
        self.wait(1)
        self.play(ReplacementTransform(slop2, slop3))
        self.wait(1)
        group2 = VGroup(sentence04, sentence05)
        self.play(FadeOut(group2, UP), run_time = 1)
        self.wait(1)
        sentence06 = TextMobject("当我们的单位足够小时，也就是导数的定义", color = BLUE).scale(0.6).to_edge(UP)
        self.play(Write(sentence06), run_time = 1)
        self.wait(1)
        equation01 = TextMobject("$$f'(x)=\\lim\\limits_{\\Delta x\\rightarrow 0}\\displaystyle\\frac{\\Delta y}{\\Delta x}$$", color = RED).scale(0.8).next_to(sentence06, DOWN)
        self.play(DrawBorderThenFill(equation01), run_time = 1)
        self.wait(1)
        sentence07 = TextMobject("我们通常用$f'(x)$来代表$f(x)$的导数，用$\\Delta$来代表一个量的变化量", color = GREEN).scale(0.6).next_to(equation01, DOWN*0.6)
        self.play(Write(sentence07), run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(sentence07))
        sentence08 = TextMobject("当我们将这个概念带回物理领域更加清晰", color = BLUE).scale(0.8).to_edge(UP)
        self.play(ReplacementTransform(sentence06, sentence08), run_time = 1 )
        self.wait(1)
        equation02 = TextMobject("$$v=\\lim\\limits_{\\Delta t\\rightarrow 0}\\displaystyle\\frac{\\Delta s}{\\Delta t}$$", color = RED).scale(0.8).next_to(sentence08, DOWN)
        self.play(ReplacementTransform(equation01, equation02),run_time = 1)
        self.play(Indicate(equation02),run_time = 1)
        self.wait(1)
        sentence09 = TextMobject("这也正是速度的定义，也就是在某一点的斜率", color = GREEN).scale(0.6).next_to(equation02, DOWN)
        self.play(Write(sentence09), run_time = 1)
        self.wait(1)
        sentence10 = TextMobject("同样加速度、加加速度我们都会定义", color = GREEN).scale(0.6).next_to(equation02, DOWN)
        self.play(ReplacementTransform(sentence09, sentence10), run_time = 1)
        self.wait(1)
        equation03 = TextMobject("$$a=\\lim\\limits_{\\Delta t\\rightarrow 0}\\displaystyle\\frac{\\Delta v}{\\Delta t}$$", color = RED).scale(0.8).next_to(sentence08, DOWN)
        self.play(ReplacementTransform(equation02, equation03), run_time = 1)
        self.wait(1)
        equation04 = TextMobject("$$a'=\\lim\\limits_{\\Delta t\\rightarrow 0}\\displaystyle\\frac{\\Delta a}{\\Delta t}$$", color = RED).scale(0.8).next_to(sentence08, DOWN)
        self.play(ReplacementTransform(equation03, equation04), run_time = 1)
        self.wait(2)
        self.play(FadeOut(equation04), FadeOut(sentence08), FadeOut(sentence10), FadeOut(slop3), FadeOut(dot[0]), FadeOut(dot[1]), FadeOut(dot[2]), FadeOut(dot[3]),
                  FadeOut(dot[4]), FadeOut(dot[5]), FadeOut(dot[6]), FadeOut(dot[7]), run_time = 1.5)
        self.wait(1)
        sentence11 = TextMobject("值得一提的是当我们对位移做一次求导运算，得到的是速度", color = BLUE).scale(0.8).to_edge(UP)
        sentence12 = TextMobject("当我们做两次求导运算自然就是加速度，同理加加速度就是三阶导数", color = BLUE).scale(0.8).next_to(sentence11, DOWN)
        deriv = self.get_derivative_graph(graph, color = BLUE)
        de_deriv = self.get_derivative_graph(deriv, color = GREEN)
        self.play(Write(sentence11), ShowCreation(deriv), run_time = 1.5)
        self.wait(2)
        self.play(Write(sentence12), ShowCreation(de_deriv), run_time =1.5)
        self.wait(3)
        self.play(FadeOut(sentence11), FadeOut(sentence12), run_time = 1.5)
        sentence13 = TextMobject("对于以上这些概念，我不希望你死记硬背下来，我想让你直观地去感受与理解", color = BLUE).scale(0.6).to_edge(UP)
        self.add(dot[0])
        self.play(DrawBorderThenFill(sentence13), MoveAlongPath(dot[0], graph), run_time = 5)
        self.wait(1)
        sentence14 = TextMobject("当然我并没有提到求导是如何运算的，如果你没有学过这部分知识，我建议你不妨在看完这期视频后去自己学习一下，我相信你一定会很有收获的", color = BLUE).scale(0.6).next_to(sentence13, DOWN)
        self.play(Write(sentence14), run_time = 2)
        self.wait(2)
        group3 = VGroup(sentence13, sentence14, deriv, de_deriv, graph, dot[0])
        self.play(FadeOut(group3), FadeOut(self.axes), run_time = 1.5)
        self.wait(1)
        self.wait()

class Part02(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 25,
        "y_tick_frequency": 5,
        "y_labeled_nums": range(0, 25, 5),
        "exclude_zero_label": False,

        "y_axis_height": 6,
        "x_axis_width": 12,
        "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "func": lambda x: (x**2-4*x+5)/2
    }

    def construct(self):
        sentence01 = TextMobject("让我们回到前面的问题", color = BLUE).scale(0.8).to_edge(UP)
        self.play(Write(sentence01), run_time = 1)
        equation01 = TextMobject("$S=s_0+a_0t$", color = RED).scale(0.8).next_to(sentence01, DOWN)
        self.play(Write(equation01), run_time = 1)
        equation02 = TextMobject("$S=s_0+a_0t+\\displaystyle\\frac{a_1}{2}t^2$",color = RED).scale(0.8).next_to(equation01, DOWN)
        self.play(Write(equation02), run_time = 1)
        self.wait(1)
        sentence02 = TextMobject("现在给定了加加速度$a_2$，我们只需要让$S$的三阶导数等于它就可以了", color = GREEN).scale(0.6).next_to(equation02, 0.8*DOWN)
        self.play(Write(sentence02, run_time = 1))
        self.wait(1)
        self.play(FadeOut(sentence02))
        sentence03 = TextMobject("$S^{(3)}=a_2$（对于高阶导数我们用$^{(n)}$来代表它的阶数）", color = GREEN).scale(0.8).next_to(equation02, DOWN)
        self.play(Write(sentence03), run_time = 1)
        self.wait(1)
        self.play(FadeOut(sentence03))
        self.wait(1)
        equation03 = TextMobject("$S=s_0+a_0t+\\displaystyle\\frac{a_1}{2}t^2+\\frac{a_2}{6}t^3$",color = RED).scale(0.8).next_to(equation02, DOWN)
        self.play(Write(equation03), run_time = 2)
        self.wait(1)
        sentence04 = TextMobject("你可以通过求导来验证这个结果的合理性", color = GREEN).scale(0.8).next_to(equation03, DOWN*0.8)
        self.play(Write(sentence04), run_time = 1)
        self.wait(2)
        group1 = VGroup(sentence01, equation01, equation02, equation03)
        self.play(FadeOut(group1), FadeOut(sentence04), run_time = 1)
        self.wait(1)
        sentence05 = TextMobject("如果你想系统地求出$S$，这就涉及到求导的逆运算：积分$\\int$", color = GREEN).scale(0.8).to_edge(UP)
        self.play(Write(sentence05), run_time = 1)
        self.wait(1)
        sentence06 = TextMobject("正如导数对应的是曲线的斜率，积分对应的就是曲线的面积", color = GREEN).scale(0.6).next_to(sentence05, DOWN*0.8)
        sentence07 = TextMobject("高中物理中就已经提到$v-t$图像的面积对应的正是位移，这是可以理解的，位移正是速度在时间上的积累", color = BLUE).scale(0.6).next_to(sentence06, DOWN*0.8)
        sentence08 = TextMobject("这并不是我们本次讨论的重点，所以还是只给你一些直观感受", color = GREEN).scale(0.6).next_to(sentence07, DOWN*0.8)
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color = RED)
        area = self.get_area(graph, 2, 8)
        self.play(Write(sentence06), run_time = 1)
        self.play(ShowCreation(graph), run_time = 1)
        self.play(ShowCreation(area), run_time = 1)
        self.wait(1)
        self.play(Write(sentence07), run_time = 1)
        self.wait(1)
        self.play(Write(sentence08),run_time = 1)
        self.wait(2)
        group2 = VGroup(sentence05, sentence06, sentence07, sentence08, graph, area)
        self.play(FadeOut(group2),FadeOut(self.axes), run_time = 1)
        self.wait(1)
        self.play(FadeIn(group1))
        self.wait(1)
        sentence09 = TextMobject("我们可以依次自然地写出", color = GREEN).scale(0.6).next_to(equation03, DOWN*0.8)
        self.play(Write(sentence09), run_time = 1)
        self.wait(1)
        self.play(FadeOut(sentence09))
        equation04 = TextMobject("$S=s_0+a_0t+\\displaystyle\\frac{a_1}{2}t^2+\\frac{a_2}{6}t^3+\\frac{a_3}{24}t^4$", color = RED).scale(0.8).next_to(equation03, DOWN)
        equation05 = TextMobject("$S=s_0+a_0t+\\displaystyle\\frac{a_1}{2}t^2+\\frac{a_2}{6}t^3+\\frac{a_3}{24}t^4+\\frac{a_4}{120}t^5$", color = RED).scale(0.8).next_to(equation04, DOWN)
        self.play(Write(equation04),run_time = 1)
        self.play(Write(equation05),run_time = 1)
        sentence10 = TextMobject("是否感觉到很熟悉呢？我们将速度、加速度等写成$S$的导数形式", color = GREEN).scale(0.6).next_to(equation05, DOWN*0.8)
        self.play(Write(sentence10))
        self.wait(1)
        self.play(FadeOut(sentence10))
        equation06 = TextMobject("$S=s_0+s'(0)t+\\displaystyle\\frac{s^{(2)}(0)}{2!}t^2+\\frac{s^{(3)}(0)}{3!}t^3+\\frac{s^{(4)}(0)}{4!}t^4+\\cdots$", color = RED).scale(0.8).next_to(equation05, DOWN)
        self.play(Write(equation06),run_time = 2)
        self.wait(2)
        group3 = VGroup(group1, equation04, equation05)
        self.play(FadeOut(group3))

        equation06.generate_target()
        equation06.target.scale(1).to_edge(UP).set_color(BLUE)

        self.play(MoveToTarget(equation06))
        self.wait(2)
        self.wait()

class Part03(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$t$",
        "y_axis_label": "$S$",
        "y_min": 0,
        "y_max": 25,
        "y_tick_frequency": 5,
        "y_labeled_nums": range(0, 25, 5),
        "exclude_zero_label": False,

        "y_axis_height": 6,
        "x_axis_width": 12,
        "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "func": lambda x: (x ** 2 - 4 * x + 5) / 2,
        "sine": lambda x: np.sin(x),
    }
    def construct(self):
        equation = TextMobject("$S=s_0+s'(0)t+\\displaystyle\\frac{s^{(2)}(0)}{2!}t^2+\\frac{s^{(3)}(0)}{3!}t^3+\\frac{s^{(4)}(0)}{4!}t^4+\\cdots$", color = BLUE).scale(0.8).to_edge(UP)
        self.add(equation)
        sentence01 = TextMobject("这个式子告诉我们如果我们给一个质点足够多的初始条件，那么就可以实现对其$S-t$曲线的精确控制，仿佛有一只无形的手在控制着它", color = GREEN).scale(0.6).next_to(equation, DOWN*0.8)
        self.play(Write(sentence01),run_time = 2)
        self.setup_axes(animate=True)
        func = self.get_graph(self.func, color = RED)
        point = self.input_to_graph_point(0, func)
        dot = Dot(point, color = YELLOW)
        self.play(ShowCreation(dot))
        self.wait(1)
        path1 = TracedPath(dot.get_center, stroke_width = 6, stroke_color = RED)
        self.play(ShowCreation(path1), MoveAlongPath(dot, func), run_time = 5)
        self.wait(1)
        sentence02 = TextMobject("注意刚刚运动的这个点的轨迹并不是真实的轨迹，只是$S-t$图像上的点", color = GREEN).scale(0.6).next_to(equation, DOWN*0.8)
        self.play(ReplacementTransform(sentence01, sentence02))
        self.wait(1)
        self.play(FadeOut(sentence02))
        self.wait(1)
        sentence03 = TextMobject("换句话来说，我们可以构造这样一个多项式，使其的$n$阶导数在给定函数的某一个点与该函数的对应阶导数都相等，如果这一点带给我们的信息足够多（$n$足够大），我们就可以完成从局部逼近到全局逼近", color = BLUE).scale(0.6).next_to(equation, DOWN*0.8)
        self.play(Write(sentence03), run_time = 3)
        self.wait(2)
        self.play(FadeOut(sentence03), run_time = 1)
        self.wait(1)
        sentence04 = TextMobject("我们取的这样一个点一直是零点，当然也可以取其他的点，如果这个质点是在$t=t_0$时出发，上式就会变成这样的形式", color = BLUE).scale(0.6).next_to(equation, DOWN*0.8)
        self.play(Write(sentence04), run_time = 1.5)
        self.wait(1)
        equation02 = TextMobject("$S=s_0+s'(t_0)t+\\displaystyle\\frac{s^{(2)}t_0}{2!}(t-t_0)^2+\\frac{s^{(3)}t_0}{3!}(t-t_0)^3+\\cdots$", color = BLUE).scale(0.8).to_edge(UP)
        self.play(ReplacementTransform(equation, equation02),run_time = 1)
        self.wait(3)
        group = VGroup(equation02, sentence04, path1)
        self.play(FadeOut(group), FadeOut(self.axes), run_time = 1)
        self.wait(1)
        self.wait()

class Part04(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 1,
        "y_labeled_nums": range(0, 1, 2),
        "exclude_zero_label": False,

        "y_axis_height": 6,
        "x_axis_width": 12,
        "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "func": lambda x: np.exp(-1/x**2),
        "sine": lambda x: np.sin(x),
    }
    def construct(self):
        sentence01 = TextMobject("以上提供了一种从运动角度去理解泰勒公式的方法", color = BLUE).scale(0.8).to_edge(UP)
        equation = TextMobject("$f(x)=\\sum_{n=0}^N$", "$\\displaystyle\\frac{f^{(n)}(a)}{n!}$", "$(x-a)^n+$",
                               "$R_N(x)$", color=RED).to_edge(UP)
        sentence02 = TextMobject("现在我们还没有解释这个$R_n(x)$的含义", color = BLUE).scale(0.6).next_to(equation, DOWN)
        sentence03 = TextMobject("实际上，你可将它理解为一种误差，那么如果多项式足够逼近给定函数，应该满足$n$足够大时，$R_n(x)\\rightarrow 0$", color = BLUE).scale(0.6).next_to(sentence02, DOWN)
        sentence04 = TextMobject("并不是所有函数的经过泰勒公式计算后都可以很好地逼近它自己，让我们看这样一个函数", color = GREEN).scale(0.6).next_to(equation, DOWN*0.8)
        function_tex = TextMobject("$$f(x)=\\begin{cases} e^{-\\frac{1}{x^2}} & x\\neq 0 \\\\ 0 &x=0 \\end{cases}$$", color = BLUE).scale(0.7).next_to(equation, DOWN)
        sentence05 = TextMobject("可以证明$f^{(n)}=0$，显然用泰勒公式得到的多项式并不逼近于函数本身", color = GREEN).scale(0.6).next_to(function_tex, DOWN*0.8)

        self.play(Write(sentence01), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence01))
        self.play(Write(equation), run_time = 1)
        self.wait(2)
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03), run_time = 2)
        self.wait(2)
        self.play(FadeOut(sentence02), FadeOut(sentence03), run_time = 1)
        self.wait(1)
        self.play(Write(sentence04), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(sentence04, function_tex), run_time = 2)
        self.wait(2)
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color = BLUE)
        self.play(ShowCreation(graph), run_time = 1)
        self.wait(1)
        self.play(Write(sentence05), run_time = 1)
        self.wait(2)
        group = VGroup(equation, function_tex, sentence05, graph)
        self.play(FadeOut(group), FadeOut(self.axes), run_time = 1)
        self.wait(1)
        self.wait()

class Part05(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position":{
            "phi": 65*DEGREES,
            "theta": 60*DEGREES,
            "distance":50,
            "gamma":0,
        },
    }

    def construct(self):
        sentence01 = TextMobject("当然我们还有许多细节没有讨论，包括函数是否可导等等，但是就像我一直强调的那样，我希望带给你的是直观地去触碰与理解它！", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("在上期的评论区中有小伙伴提到了多元泰勒公式，也就是自变量由一个变为了两个甚至更多，同样在本期结尾，我也尝试做了一下三维空间中泰勒公式的拟合，"
                                 "由于自己能力有限，可能效果并没有二维的那么好，如果大家有思路欢迎可以一起交流！", color = RED).scale(0.8).next_to(sentence01, DOWN)
        self.play(Write(sentence01), run_time = 2)
        self.wait(2)
        self.play(Write(sentence02), run_time = 3)
        self.wait(2)
        self.play(FadeOut(sentence01), FadeOut(sentence02))
        self.wait(1)

        self.set_camera_to_default_position()
        axes = self.get_axes()
        self.add(axes)
        self.wait(2)
        surface = ParametricSurface(lambda u, v: np.array([u, v, np.sin(v+u)]),
                                     u_min = -4, u_max = 4, v_min = -4, v_max = 4, checkerboard_colors = None, fill_color = BLUE, fill_opacity=0.8, stroke_color = WHITE, stroke_width = 2.5)
        self.play(ShowCreation(surface), run_time = 2)
        surface1 = ParametricSurface(lambda u, v:np.array([u,v,u+v]),
                                    u_min=-4,u_max=4,v_min=-4,v_max=4, checkerboard_colors = None, fill_color = YELLOW_D, fill_opacity=0.8, stroke_color = WHITE, stroke_width = 2.5)
        surface2 = ParametricSurface(lambda u,v:np.array([u,v,u+v-1/math.factorial(3)*(u+v)**3]),
                                    u_min=-4,u_max=4,v_min=-4,v_max=4, checkerboard_colors = None, fill_color = YELLOW_D, fill_opacity=0.8, stroke_color = WHITE, stroke_width = 2.5)
        surface3 = ParametricSurface(lambda u, v: np.array([u,v, u+v-1/math.factorial(3)*(u+v)**3+1/math.factorial(5)*(u+v)**5]),
                                    u_min = -4, u_max = 4, v_min = -4, v_max = 4, checkerboard_colors = None,fill_color = YELLOW_D,fill_opacity=0.8, stroke_color = WHITE, stroke_width = 2.5)
        surface4 = ParametricSurface(lambda u, v: np.array([u,v, u+v-1/math.factorial(3)*(u+v)**3+1/math.factorial(5)*(u+v)**5-1/math.factorial(7)*(u+v)**7]),
                                     u_min=-4, u_max=4, v_min=-4, v_max=4, checkerboard_colors = None, fill_color=YELLOW_D, fill_opacity=0.8, stroke_color = WHITE, stroke_width = 2.5)
        surface5 = ParametricSurface(lambda u, v: np.array([u, v, u + v - 1 / math.factorial(3) * (u + v) ** 3 + 1 / math.factorial(5) * (u + v) ** 5 - 1 / math.factorial(7) * (u + v) ** 7+1/math.factorial(9)*(u+v)**9]),
                                     u_min=-4, u_max=4, v_min=-4, v_max=4, checkerboard_colors=None,
                                     fill_color=YELLOW_D, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2.5)
        surface6 = ParametricSurface(lambda u, v: np.array([u, v, u + v - 1 / math.factorial(3) * (u + v) ** 3 + 1 / math.factorial(5) * (u + v) ** 5 - 1 / math.factorial(7) * (u + v) ** 7+1/math.factorial(9)*(u+v)**9-1/math.factorial(11)*(u+v)**11]),
                                     u_min=-4, u_max=4, v_min=-4, v_max=4, checkerboard_colors=None,
                                     fill_color=YELLOW_D, fill_opacity=0.8, stroke_color=WHITE, stroke_width=2.5)
        self.play(ShowCreation(surface1), run_time = 1)
        dt = 1/15
        theta_0 = 60*DEGREES
        for i in range(30):
            theta_0 += 3 * DEGREES
            self.set_camera_orientation(phi=65 * DEGREES, theta=theta_0)
            self.wait(dt)
        self.play(ReplacementTransform(surface1, surface2), run_time = 2)
        for i in range(30):
            theta_0 += 3*DEGREES
            self.set_camera_orientation(phi = 65*DEGREES, theta=theta_0)
            self.wait(dt)
        self.play(ReplacementTransform(surface2, surface3), run_time = 2)
        for i in range(30):
            theta_0 += 3*DEGREES
            self.set_camera_orientation(phi= 65*DEGREES, theta=theta_0)
            self.wait(dt)
        self.play(ReplacementTransform(surface3, surface4), run_time = 2)
        for i in range(30):
            theta_0 += 3*DEGREES
            self.set_camera_orientation(phi= 65*DEGREES , theta=theta_0)
            self.wait(dt)
        self.play(ReplacementTransform(surface4, surface5), run_time = 2)
        for i in range(30):
            theta_0 += 3*DEGREES
            self.set_camera_orientation(phi= 65*DEGREES , theta=theta_0)
            self.wait(dt)
        self.play(ReplacementTransform(surface5, surface6), run_time = 2)
        for i in range(30):
            theta_0 += 3*DEGREES
            self.set_camera_orientation(phi= 65*DEGREES , theta=theta_0)
            self.wait(dt)
        self.wait(1)
        self.wait()
from manimlib.imports import *

class Part01(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 5,
        "x_axis_label": "$x$",
        "y_min": 0,
        "y_max": 6,
        "exclude_zero_label": False,
        "y_axis_height": 3,
        "x_axis_width": 6,
        "graph_origin": UP*0.5,
        "func": lambda x: (x ** 2 - 4 * x + 5) / 2
    }
    def construct(self):
        sen1 = TextMobject("今天我们来讨论一下定积分的一些问题").scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("事实上，主要是一点定理的直观展示").scale(0.8).shift(DOWN*3.5)
        sen3 = TextMobject("定积分在我之前的视频已经出现过几次了").scale(0.8).shift(DOWN*3.5)
        sen4 = TextMobject("定积分一个很重要的思想在于理解从离散到连续").scale(0.8).shift(DOWN*3.5)

        word1 = TextMobject("$\\textsl{Definite Integral}$",color = BLUE).scale(1.5).shift(LEFT*4+UP*2)

        self.play(Write(sen1))
        self.play(DrawBorderThenFill(word1))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.wait(2)
        self.play(Transform(sen1,sen3))
        self.wait(2)
        self.play(Transform(sen1,sen4))
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color=RED)
        area = self.get_area(graph, 1, 4)
        self.play(ShowCreation(graph))
        self.play(ShowCreation(area))
        self.wait(3)

        sen5 = TextMobject("还有一个概念的问题需要说明").scale(0.8).shift(DOWN*3.5)
        sen6 = TextMobject("经常出现的另一个名词叫做不定积分").scale(0.8).shift(DOWN*3.5)
        sen7 = TextMobject("英语中它也叫作$antiderivative$").scale(0.8).shift(DOWN*3.5)
        sen8 = TextMobject("你们都知道$anti$是一个表示反对的前缀").scale(0.8).shift(DOWN*3.5)
        word2 = TextMobject("$\\textsl{Indefinite Integral}$",color = BLUE).scale(1.5).shift(DOWN*2).align_to(word1,LEFT)
        word3 = TextMobject("$\\textsl{Antiderivative}$",color = BLUE).scale(1.5).shift(DOWN*1.5).align_to(word1,LEFT)
        note = TextMobject("别忘记加$C$~",color = YELLOW).scale(0.8).shift(DOWN*3.5)

        eq = TextMobject("$\\displaystyle\\int f'(x)dx=f(x)$","$+C$",color = BLUE).shift(RIGHT*3+DOWN*2)
        eq[1].set_color(YELLOW)

        self.play(Transform(sen1,sen5))
        self.wait(2)
        self.play(Transform(sen1,sen6))
        self.play(DrawBorderThenFill(word2))
        self.wait(2)
        self.play(Transform(sen1,sen7))
        self.wait(2)
        self.play(Transform(sen1,sen8))
        self.play(Transform(word2,word3))
        self.wait(2)
        self.play(Write(eq[0]))
        self.play(Transform(sen1,note))
        self.play(FadeIn(eq[1]))
        self.wait(2)

        sen9 = TextMobject("在收敛的情况下，定积分的结果通常是一个数",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen10 = TextMobject("而不定积分是导数的逆运算，得到的同样是函数",color = BLUE).scale(0.8).shift(DOWN*3.5)

        bg_rec1 = SurroundingRectangle(word1)
        bg_rec2 = SurroundingRectangle(word2)

        self.play(Transform(sen1,sen9))
        self.play(ShowCreation(bg_rec1))
        self.play(ApplyWave(area))
        self.wait(3)
        self.play(Transform(sen1,sen10))
        self.play(ShowCreation(bg_rec2))
        self.play(ApplyWave(eq))
        self.wait(3)

class Part02(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 6,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "y_min": 0,
        "y_max": 6,
        "exclude_zero_label": False,
        "y_axis_height": 5,
        "x_axis_width": 12,
        "graph_origin": DOWN*2.5+LEFT*6,
        "func": lambda x: (x ** 2 - 4 * x + 5) / 2
    }
    def construct(self):
        sen1 = TextMobject("让我们来看看这个变上限积分的公式").scale(0.8).shift(DOWN*3.5)
        eq = TextMobject("$(\\int_{a}^{x}f(t)dt)'=f(x)$", color = BLUE).to_edge(UP)
        sen2 = TextMobject("你需要知道这里的$'$是对变量$x$求导").scale(0.8).shift(DOWN*3.5)
        sen3 = TextMobject("弄清是哪一个量在变化是非常重要的").scale(0.8).shift(DOWN*3.5)

        eq1 = TextMobject("$\\Phi(x)=\\int_{a}^{x}f(t)dt$",color = BLUE).to_edge(UP).shift(RIGHT*3)

        self.play(Write(sen1))
        self.wait(1)
        self.play(Write(eq))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.wait(2)
        self.play(Transform(sen1,sen3))
        self.play(eq.shift,LEFT*3)
        self.play(Write(eq1))
        self.wait(2)

        sen4 = TextMobject("根据定积分的几何意义，$\\Phi(x)$表示从定值$a$到变量$x$函数所围成的面积").scale(0.8).shift(DOWN*3.5)
        sen5 = TextMobject("$t$只是一个用于表示的中间变量，并不会在$\\Phi(x)$中得到直接体现").scale(0.8).shift(DOWN*3.5)
        sen6 = TextMobject("让我们来看看具体是怎样变化的").scale(0.8).shift(DOWN*3.5)

        self.play(Transform(sen1,sen4),run_time = 1.5)

        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color=RED)
        area = self.get_area(graph, 1, 3)
        x_line = Line(np.array([0,-3,0]),np.array([0,2,0]),color = BLUE)
        x_label = TextMobject("$x$",color = BLUE).scale(0.8).move_to(np.array([0,-2.7,0])).shift(DOWN*0.5+RIGHT*0.5)

        self.play(ShowCreation(graph))
        self.play(ShowCreation(x_line))
        self.play(ShowCreation(area))
        self.play(ShowCreation(x_label))
        self.wait(2.5)

        self.play(Transform(sen1,sen5))
        self.play(ApplyWave(self.x_axis_label_mob))
        self.wait(2.5)
        self.play(Transform(sen1,sen6))
        self.wait(1)

        self.t = 0
        dec = DecimalNumber(0)
        dec1 = DecimalNumber(0)

        def func(x):
            return 1/6*x**3-x**2+5/2*x-5/3

        dec.add_updater(lambda a:a.set_value(func(self.t/4 + 3)))
        dec1.add_updater(lambda a:a.set_value(3 + self.t/4))

        x_para = TextMobject("$x=$",color = BLUE).shift(UP*2.5).shift(LEFT*5)
        dec1.next_to(x_para,RIGHT*0.7)
        phi_label = TextMobject("$\\Phi(x)=$",color = BLUE).shift(UP*2.5).shift(LEFT*2.5)
        dec.next_to(phi_label,RIGHT*0.7)
        group = VGroup(x_para,dec1,phi_label,dec)
        self.play(ShowCreation(x_para),ShowCreation(phi_label),ShowCreation(dec),ShowCreation(dec1))
        self.wait(2)

        def anim(obj1, dt):
            obj1.shift(RIGHT*dt)
            self.t += dt
        obj = VGroup(x_label,x_line)
        obj.save_state()
        x_label.add_updater(anim)
        x_line.add_updater(anim)
        self.wait(3)
        self.play(FadeOut(group),FadeOut(obj))
        area1 = self.get_area(graph,1,5)
        self.play(Transform(area,area1))
        self.wait(2)

        sen7 = TextMobject("当$x$变化时，积分上限就随之变化相等的量").scale(0.8).shift(DOWN*3.5)
        xx = TextMobject("$x'=x+dx$",color = RED).shift(UP*2.5).align_to(eq,LEFT)
        d = TextMobject("$dx$",color = RED).scale(0.8).move_to(np.array([4.5,-2.7,0]))
        de = TextMobject(
            "$$y'=\\lim\\limits_{\\Delta x\\rightarrow 0}\\displaystyle\\frac{\\Delta y}{\\Delta x}$$",
            color=RED).scale(0.8).shift(UP*2.5).align_to(eq1,LEFT)

        self.play(Transform(sen1,sen7))
        self.wait(2)
        self.play(Write(xx))
        self.wait(2)
        area2 = self.get_area(graph,5,5.2).set_color(RED)
        self.play(ShowCreation(d),ShowCreation(area2))
        self.wait(2)

        sen8 = TextMobject("现在回忆一下导数的定义").scale(0.8).shift(DOWN*3.5)
        self.play(Transform(sen1,sen8))
        self.play(Write(de))
        self.wait(2)

        sen9 = TextMobject("由$x$变化引起的$\\Phi (x)$变化正是面积的变化",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen10 = TextMobject("当考虑极限情况时，增加的矩形面积与$dx$之比也就正是$f(x)$！",color = BLUE).scale(0.8).shift(DOWN*3.5)

        self.play(Transform(sen1,sen9))
        self.wait(2.5)
        fx = TextMobject("$f(x)$",color = YELLOW).move_to(self.input_to_graph_point(5,graph)).shift(LEFT*0.5)
        area3 = self.get_area(graph,5,5.05).set_color(RED)
        self.play(Transform(sen1,sen10))
        self.wait(1)
        self.play(Transform(area2,area3))
        self.play(ShowCreation(fx))
        self.wait(4)

class Part03(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 6,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "y_min": 0,
        "y_max": 6,
        "exclude_zero_label": False,
        "y_axis_height": 5,
        "x_axis_width": 12,
        "graph_origin": DOWN*2.5+LEFT*6,
        "func": lambda x: (x ** 2 - 4 * x + 5) / 2
    }
    def construct(self):
        sen1 = TextMobject("有时我们的积分上限并不是$x$，而是关于$x$的函数").scale(0.8).shift(DOWN*3.5)
        sen2 = TextMobject("别紧张，回忆刚才的过程你会发现几乎是一样的原理").scale(0.8).shift(DOWN*3.5)
        sen3 = TextMobject("再次强调这里的变化均是由$x$变化所引起的",color = RED).scale(0.8).shift(DOWN*3.5)
        sen4 = TextMobject("所以当$x$变化一点点时，积分上限的变化变成$dp(x)$").scale(0.8).shift(DOWN*3.5)

        self.setup_axes(animate=False)
        x_line = Line(np.array([4, -3, 0]), np.array([4, 3, 0]), color=BLUE)
        x_label = TextMobject("$p(x)$", color=BLUE).scale(0.8).move_to(np.array([4, -2.7, 0])).shift(
            DOWN * 0.5 + RIGHT * 0.5)
        graph = self.get_graph(self.func)
        area = self.get_area(graph,1,5)
        fx = TextMobject("$f(p(x))$", color=RED).move_to(self.input_to_graph_point(5, graph)).shift(LEFT * 0.5)
        self.add(x_line)
        self.add(graph)
        self.add(area)
        eq1 = TextMobject("$\\Phi(x)=\\int_{a}^{p(x)}f(t)dt$",color = BLUE).to_edge(UP)
        eq2 = TextMobject("$\\Phi(x)=\\int_{q(x)}^{p(x)}f(t)dt$",color = BLUE).to_edge(UP)
        eq3 = TextMobject("$\\Phi'(x)=$","$f(p(x))p'(x)$",color = BLUE).next_to(eq1,DOWN)
        eq4 = TextMobject("$\\Phi'(x)=$","$f(p(x))p'(x)-f(q(x))q'(x)$",color = BLUE).next_to(eq1,DOWN)
        self.play(Write(sen1))
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.play(Write(x_label))
        self.wait(2)
        self.play(Transform(sen1,sen3))
        self.wait(3)
        self.play(Transform(sen1,sen4))
        self.wait(2)
        d = TextMobject("$dp(x)$",color = RED).scale(0.8).move_to(np.array([4.5,-2.7,0]))
        dd = TextMobject("$p'(x)$","$dx$",color = RED).scale(0.8).move_to(np.array([4.5,-2.7,0]))
        area1 = self.get_area(graph, 5, 5.2).set_color(RED)
        self.play(ShowCreation(d), ShowCreation(area1),ShowCreation(fx))
        self.wait(2)

        sen5 = TextMobject("你知道$dp(x)$等于什么的，就和求导一样").scale(0.8).shift(DOWN*3.5)
        area2 = self.get_area(graph, 5, 5.05).set_color(RED)
        self.play(Transform(sen1,sen5))
        self.play(Transform(area1,area2))
        self.play(Transform(d,dd))
        self.wait(2.5)

        sen6 = TextMobject("那么当你再次回忆导数的定义，你就会很自然地得出").scale(0.8).shift(DOWN*3.5)
        self.play(Transform(sen1,sen6))
        self.play(Write(eq3[0]))
        self.wait(2)
        group = VGroup(dd[0],fx)
        self.play(ReplacementTransform(group,eq3[1]))
        self.wait(2)
        sen7 = TextMobject("就像$p(x)$对施了一点点魔法一样，Right？").scale(0.8).shift(DOWN*3.5)
        self.play(Transform(sen1,sen7))
        self.wait(3)

        sen7 = TextMobject("类似的，积分下限同样可以变成函数",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen8 = TextMobject("你可以想想此时的结论应该是怎样的？",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen9 = TextMobject("我在这里将直接给出结论",color = BLUE).scale(0.8).shift(DOWN*3.5)
        sen10 = TextMobject("你可以思考一下这为什么是减号，就留作思考题啦~",color = BLUE).scale(0.8).shift(DOWN*3.5)

        self.play(Transform(sen1,sen7))
        self.play(Transform(eq1,eq2))
        self.wait(2)
        self.play(Transform(sen1,sen8))
        self.wait(3)
        self.play(Transform(sen1,sen9))
        self.wait(1)
        self.play(Transform(eq3,eq4))
        self.wait(2)
        self.play(Transform(sen1,sen10))
        self.play(ApplyWave(eq3[1]))
        self.wait(3)
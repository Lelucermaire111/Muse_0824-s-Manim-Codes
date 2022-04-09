# for name in [s for s in list(COLOR_MAP.keys()) if s.endswith("_C")]:
#     locals()[name.replace("_C", "")] = locals()[name
from manimlib.imports import *

class BeginAnimation(Scene):
    CONFIG = {
        'Hadamard': 'Hadamard.jpg'
    }
    def construct(self):

        sentence01 = TextMobject("在实数域中，连接两个真理的最短的路径是通过复数域。", color = BLUE).shift(UP*1.5)
        author = TextMobject("——雅克·阿达马", color = RED).next_to(sentence01, DR).shift(LEFT*4).scale(0.9)
        self.play(Write(sentence01), run_time = 1.5)
        self.wait(1)
        Hadamard = ImageMobject(self.Hadamard)
        Hadamard.set_height(4)
        Hadamard.shift(LEFT*5+DOWN*1.5)
        self.play(FadeIn(Hadamard), Write(author), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence01),FadeOut(author), FadeOut(Hadamard), run_time = 1)
        self.wait()

class Part01(Scene):
    def construct(self):

        sentence01 = TextMobject("你对复数是怎样的印象呢？", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("当我在课本中第一次接触到复数的时候，当时觉得只是提供了$i$这种符号以及一些计算，看起来只是像数学家的一个小把戏", color = BLUE).scale(0.8).to_edge(UP).next_to(sentence01, DOWN)
        sentence03 = TextMobject("随着学习的深入，我必须要为当时的想法道歉，因为复数真的很精妙！", color = BLUE).next_to(sentence02, DOWN).scale(0.8)
        equation01 = TextMobject("$\\sqrt{-1} = i, z=a+bi$", color = RED).next_to(sentence03, DOWN)
        sentence04 = TextMobject("Only a trick???", color = RED).next_to(sentence03, DOWN)
        cross_04 = Cross(sentence04).set_color(YELLOW)

        self.play(Write(sentence01), run_time = 1)
        self.wait(1.5)
        self.play(Write(sentence02), DrawBorderThenFill(equation01), run_time = 2)
        self.wait(0.5)
        self.play(ReplacementTransform(equation01, sentence04), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03), run_time = 1)
        self.play(ShowCreation(cross_04), run_time = 0.5)
        self.wait(1)
        group = VGroup(sentence01, sentence02, sentence03, sentence04, cross_04)
        t = ValueTracker(0)
        cir = Circle(radius = 2).shift(LEFT*5).set_color(BLUE)
        dot_p = Dot().add_updater(lambda a:a.move_to(
            np.array([-5+2*np.cos(t.get_value()), 2*np.sin(t.get_value()),0])))
        dot_q = Dot().add_updater(lambda a:a.move_to(
            np.array([-2, 2*np.sin(t.get_value()), 0])))
        l_pq = DashedLine().add_updater(lambda a:a.put_start_and_end_on(
            dot_p.get_center(), dot_q.get_center()))

        label = TextMobject("$e^{it}$", color = RED).scale(1.5).next_to(cir, UP)
        path = TracedPath(dot_q.get_center, stroke_wifth=6,stroke_color= YELLOW)
        path.add_updater(lambda a:a.shift(RIGHT*0.04))
        self.play(ReplacementTransform(group, cir), run_time = 1)
        self.play(Write(label), run_time = 1)
        self.add(dot_q, dot_p, l_pq, path)
        self.play(t.set_value, 2*TAU, run_time = 8, rate_func = linear)
        group1 = VGroup(cir, dot_q, dot_p, l_pq, path, label)
        sentence05 = TextMobject("复数是什么？", color = BLUE).scale(1.5)
        self.play(FadeOut(group1),run_time = 0.1)
        self.wait(1)
        self.play(DrawBorderThenFill(sentence05), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence05), run_time = 1)
        self.wait(1)


class Part02(Scene):

    def construct(self):

        sentence01 = TextMobject("当我们第一次接触", "数", "的时候，通常是这样:\\\\", "然后我们补充了负数的概念，这样整数的认识完整了", color = BLUE).to_edge(UP).scale(0.8)
        sentence01[1].set_color(RED)
        equation01 = TextMobject("$0,8,24,2020,$", "$-1,-2,-9$", color = RED)
        equation01[1].set_color(GREEN)
        sentence02 = TextMobject("然后我们认识了有理数，", "与之对应的是无理数", color = BLUE).to_edge(UP).scale(0.8)
        equation02 = TextMobject("$0.5,963.4057,\\displaystyle\\frac{5}{7},$", "$\\pi,e,\\sqrt{2}$", color = RED).next_to(equation01, DOWN)
        equation02[1].set_color(GREEN)
        sentence03 = TextMobject("对数认识到这里，我们就可以画出这样一条数轴！", color = BLUE).to_edge(UP)
        sentence04 = TextMobject("我们将以上提到的这些数归为实数域", color = GREEN).next_to(sentence03, DOWN)
        sentence05 = TextMobject("问题来到复数域，我们可以在一维数轴上表示复数吗？", color = RED).shift(DOWN*1.5)
        self.play(Write(sentence01[0]), Write(sentence01[1]), Write(sentence01[2]), run_time = 1.5)
        self.play(Indicate(sentence01[1]), run_time = 1)
        self.wait(1)
        self.play(Write(equation01[0]), run_time = 1)
        self.wait(1)
        self.play(Write(sentence01[3]), run_time = 1)
        self.wait(1)
        self.play(Write(equation01[1]), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(sentence01, sentence02[0]), run_time = 1)
        self.play(Write(equation02[0]))
        self.wait(2)
        self.play(Write(sentence02[1]), Write(equation02[1]), run_time = 1)
        self.wait(2)
        group1 = VGroup(equation01, equation02)
        numline = NumberLine(x_min = -7, x_max = 7, include_tip = True)
        self.play(ReplacementTransform(sentence02, sentence03), run_time = 1)
        self.play(ReplacementTransform(group1, numline), run_time = 1)
        t = ValueTracker(0)
        triangle = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).rotate(PI).move_to(
            np.array([-2, 0.5, 0]))
        dec = DecimalNumber(0)
        triangle.add_updater(lambda a: a.move_to(
            np.array([t.get_value(), 0.5, 0])))
        dec.add_updater(lambda a: a.set_value(t.get_value()))
        dec.add_updater(lambda a: a.next_to(triangle, UP))
        self.play(ShowCreation(triangle), ShowCreation(dec))
        self.play(t.set_value, 6, rate_func=there_and_back, run_time=3)
        self.play(t.set_value, -6, rate_func=there_and_back, run_time=3)
        self.play(Write(sentence04), run_time = 1)
        self.wait(1)
        self.play(Write(sentence05), run_time = 1)
        self.wait(2)
        group2 = VGroup(dec, numline, triangle,sentence03, sentence04, sentence05)
        self.play(FadeOut(group2), run_time = 1)
        self.wait()

class Part03(Scene):

    def construct(self):
        sentence01 = TextMobject("让我们来回顾一下复数的概念，形如$z=$", "$x$", "$+iy$", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("我们将$x$称为实部，记作$x=Re\\,z$，", "$y$称为虚部，记作$y=lm\\,z$", color = RED).scale(0.8)
        tip = TextMobject("注意虚部并没有$i$哦！", color = GREEN).scale(0.6).next_to(sentence02[1], DOWN*0.8)
        sentence03 = TextMobject("然后是关于复数的计算：", color = BLUE).scale(0.8).next_to(sentence01, DOWN)
        equation01 = TextMobject("$z_1\\pm z_2=(a_1+b_1i)\\pm (a_2+b_2i)=(a_1+a_2)\\pm (b_1+b_2)i$\\\\",
                                 "$z_1z_2=(a_1+b_1i)(a_2+b_2i)=(a_1a_2-b_1b_2)+(a_1b_2+a_2b_1)i$\\\\",
                                 "$\\displaystyle\\frac{z_1}{z_2}=\\frac{a_1+b_1i}{a_2+b_2i}=\\frac{(a_1+b_1i)(a_2-b_2i)}{a_2^2+b_2^2}(a_2b_2\\neq 0)$", color = BLUE).scale(0.8).next_to(sentence02, DOWN)
        sentence04 = TextMobject("emmm我的目的并不是想向你展示这些看起来有些吓人的公式(也没有那么吓人啦），如果你不熟悉复数的运算，也没有关系，在后面我们将看到更直观的理解", color = GREEN)\
            .scale(0.6).to_edge(UP)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(sentence02[0]), Indicate(sentence01[1]), run_time = 1)
        self.wait(1)
        self.play(Write(sentence02[1]), Indicate(sentence01[2]), run_time = 1)
        self.wait(1)
        self.play(Write(tip))
        self.wait(1)
        self.play(FadeOut(tip))
        self.wait(0.5)
        self.play(Write(sentence03), run_time = 1)
        self.wait(1)
        self.play(Write(equation01), run_time = 6)
        self.wait(3)
        self.play(ReplacementTransform(sentence01, sentence04), FadeOut(sentence02), FadeOut(sentence03), run_time = 1)
        self.wait(2)
        sentence05 = TextMobject("但我们还是可以从这些计算看到，实部与虚部在计算中并没有发生合并", color = RED).scale(0.6).next_to(sentence04, DOWN)
        sentence06 = TextMobject("这就意味着我们难以通过一维坐标系来表示复数，这就需要复数坐标系的出场！", color = RED).scale(0.6).next_to(sentence05, DOWN).shift(DOWN)
        arrow = Arrow(sentence05.get_corner(DOWN), sentence06.get_corner(UP))
        self.play(Write(sentence05), run_time = 1)
        self.wait(1)
        self.play(ShowCreation(arrow), run_time = 1)
        self.play(Write(sentence06), run_time = 1)
        self.wait(2)
        group1 = VGroup(sentence05, sentence06, sentence04, equation01, arrow)
        self.play(FadeOut(group1), run_time = 1)
        self.wait()

class Part04(Scene):

    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        grid.add_coordinates()
        self.play(ShowCreation(grid), run_time = 2)
        self.wait(1)
        vector1 = Vector(np.array([1,2,0])).set_color(RED)
        vector2 = Vector(np.array([2,1,0])).set_color(GREEN)
        vector3 = Vector(np.array([3,3,0])).set_color(YELLOW)
        sentence01 = TextMobject("让我们在复数坐标系看一看复数的表示以及一些运算").scale(0.6).set_color(RED).to_edge(UL)
        self.play(ShowCreation(sentence01))
        self.wait(1.5)
        self.play(FadeOut(sentence01))
        label1 = TextMobject("$1+2i$", color = RED).scale(0.6).next_to(vector1, LEFT)
        label2 = TextMobject("$2+i$", color = GREEN).scale(0.6).next_to(vector2, RIGHT)
        label3 = TextMobject("$3+3i$", color = YELLOW).scale(0.6).next_to(vector3, DOWN).shift(UP*0.8)
        vec1 = VGroup(label1, vector1)
        vec2 = VGroup(label2, vector2)
        vec3 = VGroup(label3, vector3)
        self.play(ShowCreation(vec1), run_time = 1)
        self.play(ShowCreation(vec2), run_time = 1)
        self.wait(2)
        self.play(vec2.shift, 2*UP+RIGHT, run_time = 1)
        self.wait(1)
        self.play(ShowCreation(vec3), run_time = 1)
        sentence02 = TextMobject("所以看到这里有没有很眼熟呢？").set_color(RED).scale(0.6).to_edge(UL)
        sentence03 = TextMobject("向量！", "复数的加减法的确跟向量的运算很像").set_color(RED).scale(0.6).to_edge(UL)
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        self.play(ClockwiseTransform(sentence02, sentence03), run_time = 1)
        self.wait(0.5)
        self.play(Flash(sentence03[0], flash_radius = 0.6), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(sentence02))
        sentence04 = TextMobject("然而对于复数的乘除法，至少现在来看就没有这么直观了", color = RED).scale(0.6).to_edge(UL)
        tip = TextMobject("向量的点积、叉积和乘法是有区别的！", color = BLUE).scale(0.6).next_to(sentence04, DOWN)
        self.play(Write(sentence04), run_time = 1)
        self.wait(1)
        self.play(Write(tip), run_time = 1)
        self.play(Indicate(tip))
        self.wait(1)
        self.play(FadeOut(tip))
        self.wait(1)
        group = VGroup(vec2, vec3)
        self.play(FadeOut(group), run_time = 1)
        sentence05 = TextMobject("但是我们可以看一些更简单的情况，比如只和$i$相乘", color = RED).scale(0.6).to_edge(UL)
        self.wait(1)
        self.play(ClockwiseTransform(sentence04, sentence05), run_time = 1)
        self.wait(1)
        self.play(Rotating(vector1, radians=PI/2, about_point=np.array([0,0,0])), FadeOut(label1), run_time = 1.5)
        self.wait(1)
        newlabel1 = TextMobject("$-2+i$", color = RED).scale(0.6).shift(LEFT*2+UP*0.5)
        self.play(FadeIn(newlabel1))
        self.wait(1)
        self.play(FadeOut(sentence04))
        sentence06 = TextMobject("我们将复数在坐标轴中逆时针旋转了90度！", color = RED).scale(0.6).to_edge(UL)
        self.wait(1)
        self.play(Write(sentence06), run_time = 1)
        self.wait(1)
        sentence07 = TextMobject("这并不是什么突发的奇思妙想，$i^4=1$对应着旋转了360度，也就回到了它本身，这是非常融洽的", color = RED).scale(0.6).to_edge(UL)
        self.play(ReplacementTransform(sentence06, sentence07), run_time = 1)
        self.wait(1)
        self.play(Rotating(vector1, radians=2*PI, about_point=np.array([0,0,0])), run_time = 3)
        self.wait(1)
        sentence08 = TextMobject("所以现在你一定会思考我们如何去实现旋转任意角度呢？让我们引进新的数学工具", color = YELLOW).scale(0.6).to_edge(UL)
        self.play(ReplacementTransform(sentence07, sentence08), ru_time = 1)
        group1 = VGroup(grid, vector1, newlabel1, sentence08)
        self.wait(2)
        formula = TextMobject("$e^{ix}=\\cos x+i\\sin x$", color = BLUE).scale(1.5)
        self.play(ReplacementTransform(group1, formula), run_time = 2)
        self.wait(2)
        self.play(FadeOut(formula), run_time = 1)
        self.wait()


class Part05(Scene):

    def construct(self):
        sentence01 = TextMobject("如果你没有看到过刚才的欧拉公式，你也许会看到过“上帝公式”", color = RED).scale(0.8).to_edge(UP)
        formula1 = TextMobject("$e^{i\\pi}+1=0$", color = BLUE)
        sentence02 = TextMobject("这是欧拉公式将$\\pi$代入的特例", color = RED).scale(0.8).to_edge(UP)
        sentence03 = TextMobject("一个式子将自然对数、圆周率、虚数、1和0都包含了，非常美妙，Right?", color = RED).scale(0.8).to_edge(UP).next_to(sentence02, DOWN)
        formula2 = TextMobject("$e^{ix}=\\cos x+i\\sin x$", color = BLUE)
        sentence04 = TextMobject("让我们回到欧拉公式本身，我们可以试着去简单证明一下它，刚好会用到Up分享过的泰勒公式", color = RED).scale(0.8).to_edge(UP)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(formula1))
        self.wait(2)
        self.play(ReplacementTransform(sentence01, sentence02), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03), run_time = 2)
        self.wait(1)
        self.play(FadeOut(sentence02), FadeOut(sentence03), run_time = 1)
        self.wait(1)
        self.play(Write(sentence04), ClockwiseTransform(formula1, formula2), run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(formula1))
        self.wait(1)
        proof1 = TextMobject("$\\cos x=$", "$1-\\displaystyle\\frac{x^2}{2!}+\\frac{x^4}{4!}-\\cdots$", color = BLUE).scale(0.8).next_to(sentence04, DOWN)
        proof2 = TextMobject("$i\\sin x=$", "$ix-i\\displaystyle\\frac{(x)^3}{3!}+i\\frac{(x)^5}{5!}-\\cdots$",color = BLUE).scale(0.8).next_to(proof1, DOWN)
        proof1_right = TextMobject("$\\cos x=$","$1+\\displaystyle\\frac{(ix)^2}{2!}+\\frac{(ix)^4}{4!}+\\cdots$", color = BLUE).scale(0.8).next_to(sentence04,DOWN).shift(0.6*RIGHT)
        proof2_right = TextMobject("$i\\sin x=$","$ix+\\displaystyle\\frac{(ix)^3}{3!}+\\frac{(ix)^5}{5!}+\\cdots$", color = BLUE).scale(0.8).next_to(proof1, DOWN)
        proof3 = TextMobject("$\\cos x+i\\sin x$", "$=\\displaystyle 1+ix+\\frac{(ix)^2}{2!}+\\frac{(ix)^3}{3!}+\\frac{(ix)^4}{4!}+\\frac{(ix)^5}{5!}+\\cdots$", color = BLUE).scale(0.8).next_to(proof2, DOWN)
        proof4 = TextMobject("$e^x=1+x+\\displaystyle\\frac{x^2}{2!}+\\frac{x^3}{3!}+\\frac{x^4}{4!}+\\frac{x^5}{5!}+\\cdots$", color = RED).scale(0.8).next_to(proof3, DOWN)
        proof5 = TextMobject("$e^{ix}=\\cos x+i\\sin x$", color = YELLOW).next_to(proof4, DOWN*1.2)
        sentence05 = TextMobject("让我们利用$i$的乘方性质对式子进行一下变换", color = GREEN).scale(0.6).to_edge(DOWN)
        sentence06 = TextMobject("是不是很眼熟的形式？Bingo！", color = GREEN).scale(0.6).to_edge(DOWN)
        self.play(Write(proof1), run_time = 1.5)
        self.wait(1)
        self.play(Write(proof2), run_time = 1.5)
        self.wait(1)
        self.play(Write(sentence05), run_time = 1)
        self.wait(1)
        self.play(FadeOut(sentence05))
        self.play(ReplacementTransform(proof1[1], proof1_right[1]), run_time = 1)
        self.play(ReplacementTransform(proof2[1], proof2_right[1]), run_time = 1)
        self.wait(2)
        group = VGroup(proof1[0], proof1_right[1], proof2[0], proof2_right[1])
        self.play(TransformFromCopy(group, proof3), run_time = 2)
        self.wait(2)
        self.play(Write(sentence06), run_time = 1)
        self.wait(1)
        self.play(Write(proof4), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence06))
        self.play(DrawBorderThenFill(proof5), run_time = 1.5)
        self.wait(3)
        sentence07 = TextMobject("尽管这个证明过程还有一些细节没有讨论，不过对这个证明还是可以接受的", color = RED).scale(0.8).to_edge(UP)
        self.play(ReplacementTransform(sentence04, sentence07))
        self.wait(1)
        sentence08 = TextMobject("实际上，这个证明过程中也蕴含着非常漂亮的几何直观", color = RED).scale(0.8).to_edge(UP)
        self.play(ClockwiseTransform(sentence07, sentence08), run_time = 1)
        group1 = VGroup(proof1[0], proof1_right[1], proof2[0], proof2_right[1], proof3, proof4, proof5, sentence07)
        self.wait(2)
        self.play(FadeOut(group1))
        self.wait()

class Part06(Scene):

    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        self.play(ShowCreation(grid), run_time = 2)
        self.wait(1)
        sentence01 = TextMobject("根据我们以上的证明，我们有：" ,color = RED).scale(0.6).to_edge(UL)
        equation = TextMobject("$e^i=$","$1$","$+i$", "$+\\displaystyle\\frac{1}{2!}i^2$",
                               "$\\displaystyle+\\frac{1}{3!}i^3$",
                               "$\\displaystyle+\\frac{1}{4!}i^4$","$+\\cdots$", color = YELLOW).scale(0.8).to_edge(UL).shift(DOWN*0.8)
        tip = TextMobject("为了方便演示，这里将图形扩大了三倍~", color = YELLOW).scale(0.7).to_edge(DOWN).shift(DOWN*0.5)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(equation), run_time = 1)
        self.wait(1)
        cir = Circle(radius = 3, color = GREEN)
        self.play(ShowCreation(cir), run_time = 1)
        self.play(Write(tip))
        self.wait(2)
        vec1 = Vector(np.array([3,0,0])).set_color(RED)
        vec2 = Vector(np.array([0,3,0])).set_color(RED).shift(RIGHT*3)
        vec3 = Vector(np.array([-1.5,0,0])).set_color(RED).shift(RIGHT*3+UP*3)
        vec4 = Vector(np.array([0,-1/2,0])).set_color(RED).shift(RIGHT*1.5+UP*3)
        vec5 = Vector(np.array([1/8,0,0])).set_color(RED).shift(RIGHT*1.5+UP*2.5)
        self.play(ShowCreation(vec1), Indicate(equation[1]), run_time = 1)
        self.wait(1)
        self.play(ShowCreation(vec2), Indicate(equation[2]), run_time = 1)
        self.wait(1)
        self.play(ShowCreation(vec3), Indicate(equation[3]), run_time = 1)
        self.wait(1)
        self.play(ShowCreation(vec4), Indicate(equation[4]), run_time = 1)
        self.wait(1)
        self.play(ShowCreation(vec5), Indicate(equation[5]), run_time = 1)
        self.wait(1)
        sentence02 = TextMobject("看起来它们在以螺旋的方式逼近一个点！", color = RED).scale(0.6).to_edge(UL)
        self.play(ReplacementTransform(sentence01, sentence02))
        self.wait(1)
        line = Line(np.array([0,0,0]), np.array([3*np.cos(1), 3*np.sin(1), 0])).set_color(RED)
        arc = Arc(radius = 0.8, angle = 1).set_color(BLUE)
        self.play(ShowCreation(line),run_time = 1)
        self.play(ShowCreation(arc),run_time = 1)
        self.wait(1)
        sentence03 = TextMobject("这个点对应的正是模长为1，辐角为1弧度的复数：", "$e^i$", color = RED).scale(0.6).to_edge(UL)
        self.play(ReplacementTransform(sentence02, sentence03[0]), run_time = 1)
        self.wait(1)
        sentence03[1].set_color(YELLOW)
        self.play(Write(sentence03[1]), run_time = 1)
        self.play(Flash(sentence03[1], flash_radius = 0.6, run_time = 1))
        self.wait(2)
        sentence04 = TextMobject("接下来我们将以新的方式去认识复数！", color = PINK).scale(0.6).to_edge(UL).shift(DOWN*2)
        self.play(Write(sentence04))
        self.wait(1.5)
        group = VGroup(grid, tip, arc, cir, vec1, vec2, vec3, vec4, vec5, sentence03, equation, sentence04, line)
        self.play(FadeOut(group), run_time = 1)
        self.wait()

class Part07(Scene):

    def construct(self):
        sentence01 = TextMobject("根据刚才的演示，你已经可以想象对于$e^{i\\theta}$在复平面上的点的辐角就是$\\theta$，距离原点距离为1", color = RED).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("我们也可以在前面乘一个实数，来代表其距离原点的距离", color = RED).scale(0.8).next_to(sentence01, DOWN)
        sentence03 = TextMobject("现在我们可以将复数写成这样的形式", "$z=re^{i\\theta}$", color = RED).scale(0.8).next_to(sentence02, DOWN)
        sentence03[1].set_color(BLUE)
        self.play(Write(sentence01), run_time = 2)
        self.wait(1)
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03[0]), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03[1]), run_time = 1)
        tip = TextMobject("我们将$r$称为模长，$\\theta$称为辐角", color = GREEN).scale(0.8).next_to(sentence03, DOWN)
        self.play(ShowCreationThenFadeOut(tip), run_time = 4)
        sentence04 = TextMobject("一个更紧凑也更精妙的形式，Right？", color = GREEN).scale(0.6).next_to(sentence03, DOWN)
        self.wait(2)
        self.play(ShowCreationThenFadeOut(sentence04), run_time = 2.5)
        sentence05 = TextMobject("所以现在让我们再来看复数的乘除法", color = RED).scale(0.8).next_to(sentence03, DOWN)
        self.play(Write(sentence05), run_time = 1)
        self.wait(1)
        equation01 = TextMobject("$z_1z_2=r_1r_2e^{\\theta_1+\\theta_2}, \\displaystyle\\frac{z_1}{z_2}=\\frac{r_1}{r_2}e^{\\theta_1-\\theta_2}$", color = BLUE).scale(0.8).next_to(sentence05, DOWN)
        self.play(Write(equation01), run_time = 1)
        self.wait(2)
        sentence06 = TextMobject("让我们回到复平面！", color = GREEN).scale(0.6).next_to(equation01, DOWN)
        self.play(Write(sentence06), run_time = 1)
        self.wait(1)
        group = VGroup(sentence01, sentence02, sentence03, sentence05, sentence06)
        self.play(FadeOut(group))
        self.play(equation01.scale,0.8, equation01.to_edge, UL, equation01.set_color, RED, run_time = 2)
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        self.play(ShowCreation(grid), run_time=2)
        self.wait(1)
        vector1 = Vector(np.array([2**0.5, 2**0.5, 0]), color = RED)
        vector2 = Vector(np.array([-3**0.5, 1, 0]), color = GREEN)
        label1 = TextMobject("$z_1=2e^{i\\frac{\\pi}{4}}$", color = RED).scale(0.8).next_to(vector1, RIGHT)
        label2 = TextMobject("$z_2=2e^{i\\frac{5\\pi}{6}}$", color = GREEN).scale(0.8).next_to(vector2, LEFT)
        vec1 = VGroup(vector1, label1)
        vec2 = VGroup(vector2, label2)
        self.play(ShowCreation(vec1), run_time = 1)
        self.play(ShowCreation(vec2), run_time = 1)
        sentence07 = TextMobject("当我们现在来看复数乘除法的意义就更清晰了！", color = YELLOW).scale(0.6).next_to(equation01, DOWN)
        sentence08 = TextMobject("我们先伸长两倍，", "再逆时针旋转$\\displaystyle\\frac{5\\pi}{6}$", color = YELLOW).scale(0.6).next_to(equation01, DOWN)
        self.play(Write(sentence07), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence07))
        vector3 = Vector(np.array([2*2**0.5, 2*2**0.5,0]), color = YELLOW)
        self.play(ShowCreation(vector3), Write(sentence08[0]), run_time = 1.5)
        self.wait(1)
        self.play(Rotating(vector3, about_point=np.array([0,0,0]), radians = 5/12*TAU), Write(sentence08[1]), run_time = 1.5)
        label3 = TextMobject("$z_3=4e^{i\\frac{13\\pi}{12}}$", color = YELLOW).scale(0.8).next_to(vector3, RIGHT)
        self.play(FadeIn(label3))
        self.wait(2)
        vec3 = VGroup(vector3, label3)
        group = VGroup(vec1, vec2, vec3, equation01, sentence08)
        self.play(FadeOut(group))
        self.wait(1)
        sentence09 = TextMobject("我们来到复数的世界以后，有许多需要重新定义的概念，比如导数和积分", color = RED).scale(0.6).to_edge(UL)
        self.play(Write(sentence09, run_time = 1))
        self.wait(1)
        sentence10 = TextMobject("这就要涉及到很多复变函数的知识，emmm这并不是这期视频的重点", color = RED).scale(0.6).to_edge(UL).shift(DOWN)
        sentence11 = TextMobject("不过这并不妨碍我向你展示一些美妙的复数变换！", color = GREEN).scale(0.6).to_edge(UL).shift(DOWN*2)
        self.play(Write(sentence10), run_time = 1)
        self.wait(2)
        self.play(Write(sentence11), run_time = 1)
        self.wait(1)
        group1 = VGroup(sentence09, sentence10, sentence11)
        self.play(FadeOut(group1))

class ComplexTransform01(Scene):
    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        self.add(grid)
        label = TextMobject("$w=e^z$", color = RED).shift(RIGHT*3).shift(UP*2)
        self.play(Write(label), run_time = 1)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_complex_function,
            lambda z:np.exp(z),
            run_time = 3)
        self.wait(2)
        self.play(FadeOut(grid), FadeOut(label))
        self.wait()

class ComplexTransform02(Scene):
    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        self.play(ShowCreation(grid))
        label = TextMobject("$w=z^2$", color = RED).shift(RIGHT*3).shift(UP*2)
        self.play(Write(label), run_time = 1)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_complex_function,
            lambda z: z**2,
            run_time = 3)
        self.wait(2)
        self.play(FadeOut(grid), FadeOut(label))
        self.wait()

class ComplexTransform03(Scene):
    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}
        )
        self.play(ShowCreation(grid))
        label = TextMobject("$w=\\sin z$", color = RED).shift(RIGHT*3).shift(UP*2)
        self.play(Write(label), run_time = 1)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_complex_function,
            lambda z: np.sin(z),
            run_time = 3)
        self.wait(2)
        self.play(FadeOut(grid), FadeOut(label))
        self.wait()

class Part08(Scene):
    def construct(self):
        sentence01 = TextMobject("看起来的确很美妙，不过背后的原理并不是那么好理解", color = RED).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("That's Okay!当你有了一些直观感受，再去学习相关知识效果会更好！", color = RED).scale(0.8).to_edge(UP)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(ClockwiseTransform(sentence01, sentence02), run_time = 1)
        self.wait(1)
        self.play(FadeOut(sentence01))
        sentence03 = TextMobject("复数的出现再次扩充了对数的认识", color = RED).scale(0.8).to_edge(UP)
        sentence04 = TextMobject("欧拉公式的出现则让复数更加精妙！", color = RED).scale(0.8).next_to(sentence03, DOWN)
        sentence05 = TextMobject("复数的应用也非常非常广泛，例如在", "信号处理、", "电路分析、", "量子力学等等", color = RED).scale(0.8).next_to(sentence04, DOWN)
        formula1 = TextMobject("$x(t)=\\sum_{k=-\\infty}^{+\\infty}a_k e^{jk\\omega_0 t}$", color = BLUE).scale(0.8)
        formula2 = TextMobject("$C=\\displaystyle\\frac{1}{j\\omega C},L=j\\omega L$", color = BLUE).scale(0.8)
        formula3 = TextMobject("$$ \\hat H \\Psi = i \\hbar \\frac{\\partial \\Psi}{\\partial t} $$", color = BLUE).scale(0.8)
        self.play(Write(sentence03), run_time = 1)
        self.wait(1)
        self.play(Write(sentence04), run_time = 1)
        self.wait(2)
        self.play(Write(sentence05[0]), run_time = 1)
        self.play(Write(sentence05[1]), Write(formula1), run_time = 2)
        self.play(Indicate(formula1))
        self.wait(1)
        self.play(Write(sentence05[2]), ClockwiseTransform(formula1, formula2), run_time = 2)
        self.wait(1)
        self.play(Write(sentence05[3]), ClockwiseTransform(formula1, formula3), run_time = 2)
        self.wait(2)
        group = VGroup(sentence03, sentence04, sentence05, formula1)
        self.play(FadeOut(group), run_time = 1)
        self.wait(1)
        sentence06 = TextMobject("Life is complex. It has real and imaginary components.", color = BLUE)
        self.play(Write(sentence06))
        self.wait(3)
        self.play(FadeOut(sentence06))
        self.play()

class Part09(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position":{
            "phi":65 * DEGREES,
            "theta":-60 * DEGREES,
            "distance": 50,
            "gamma": 0,
        }
    }
    def construct(self):
        sentence01 = TextMobject("在视频的最后我想回到开头的那段动画", color = RED).scale(0.8).to_edge(UP)
        self.play(ShowCreationThenFadeOut(sentence01), run_time = 3)
        t = ValueTracker(0)
        cir = Circle(radius = 2).shift(LEFT*5).set_color(BLUE)
        dot_p = Dot().add_updater(lambda a:a.move_to(
            np.array([-5+2*np.cos(t.get_value()), 2*np.sin(t.get_value()),0])))
        dot_q = Dot().add_updater(lambda a:a.move_to(
            np.array([-2, 2*np.sin(t.get_value()), 0])))
        l_pq = DashedLine().add_updater(lambda a:a.put_start_and_end_on(
            dot_p.get_center(), dot_q.get_center()))
        path = TracedPath(dot_q.get_center, stroke_wifth=6, stroke_color= YELLOW)
        path.add_updater(lambda a:a.shift(RIGHT*0.04))
        self.play(ShowCreation(cir))
        self.add(dot_q, dot_p, l_pq, path)
        self.play(t.set_value, 2*TAU, run_time = 8, rate_func = linear)
        group1 = VGroup(cir, dot_q, dot_p, l_pq, path)
        self.play(FadeOut(group1))
        sentence02 = TextMobject("让我们将点的轨迹从z轴上观察一下", color = RED).scale(0.8).to_edge(UP)
        self.play(ShowCreationThenFadeOut(sentence02), run_time = 3)
        self.wait(1)
        self.set_camera_to_default_position()
        r = 2
        w = 4
        circle = ParametricFunction(lambda t:r*complex_to_R3(np.exp(1j*w*t)),
                                    t_min = 0, t_max = TAU*1.5, color = RED, stroke_width = 8)
        spiral_line = ParametricFunction(lambda t: r* complex_to_R3(np.exp(1j * w *t))+OUT * t,
                                         t_min=0, t_max = TAU*1.5,color = RED, stroke_width=8)
        circle.shift(IN*2.5), spiral_line.shift(IN*2.5)
        axes = ThreeDAxes(x_max = 8, x_min = -8, y_min = -8, y_max = 8, z_min = -5, z_max = 4)
        self.add(axes)
        self.play(ShowCreation(circle))
        self.wait(1)
        self.play(TransformFromCopy(circle, spiral_line, rate_func = linear), run_time = 4)
        self.wait(2)
        dt = 1/15
        phi_0 = 65*DEGREES
        theta_0 = -60*DEGREES
        phi = 90*DEGREES
        delta_phi = (phi-phi_0)/30
        delta_theta = 6*DEGREES
        for i in range(30):
            phi_0 += delta_phi
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        for i in range(60):
            theta_0 += delta_theta
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        self.wait(2)
        self.play(FadeOut(spiral_line),FadeOut(circle),FadeOut(axes), run_time = 1)

class Part10(Scene):

    def construct(self):
        sentence01 = TextMobject("让我们思考最后一件事，如果控制向量旋转的频率以及向量长度，再将它们组合起来我们会得到什么呢？", color = BLUE).scale(0.8).to_edge(UP)
        self.play(ShowCreationThenFadeOut(sentence01), run_time = 3)
        t = ValueTracker(0)
        dot_p = Dot().add_updater(lambda a:a.move_to(
            np.array([-5+2*np.cos(t.get_value()), 2*np.sin(t.get_value()),0])))
        dot_p1 = Dot().add_updater(lambda a:a.move_to(
            np.array([-5+2*np.cos(t.get_value())+2/3*np.cos(3*t.get_value()), 2*np.sin(t.get_value())+2/3*np.sin(3*t.get_value()),0])))
        dot_p2 = Dot().add_updater(lambda a:a.move_to(
            np.array([-5+2*np.cos(t.get_value())+2/3*np.cos(3*t.get_value())+2/5*np.cos(5*t.get_value()), 2*np.sin(t.get_value())+2/3*np.sin(3*t.get_value())+2/5*np.sin(5*t.get_value()),0])))
        dot_p3 = Dot().add_updater(lambda a:a.move_to(
            np.array([-5+2*np.cos(t.get_value())+2/3*np.cos(3*t.get_value())+2/5*np.cos(5*t.get_value())+2/7*np.cos(7*t.get_value()), 2*np.sin(t.get_value())+2/3*np.sin(3*t.get_value())+2/5*np.sin(5*t.get_value())+2/7*np.sin(7*t.get_value()),0])))
        dot_q = Dot().add_updater(lambda a:a.move_to(
            np.array([-2, 2*np.sin(t.get_value())+2/3*np.sin(3*t.get_value())+2/5*np.sin(5*t.get_value())+2/7*np.sin(7*t.get_value()), 0])))
        l_pq = DashedLine().add_updater(lambda a:a.put_start_and_end_on(
            dot_p.get_center(), dot_q.get_center()))
        l_p1 = Vector().add_updater(lambda a:a.put_start_and_end_on(
            dot_p.get_center(), dot_p1.get_center()))
        l_p2 = Vector().add_updater(lambda a:a.put_start_and_end_on(
            dot_p1.get_center(), dot_p2.get_center()))
        l_p3 = Vector().add_updater(lambda a:a.put_start_and_end_on(
            dot_p2.get_center(), dot_p3.get_center()))
        path = TracedPath(dot_q.get_center, stroke_width=6, stroke_color= YELLOW)
        path1 = TracedPath(dot_p.get_center,stroke_width=3, stroke_color= BLUE)
        path2 = TracedPath(dot_p1.get_center,stroke_width=3, stroke_color= BLUE)
        path3 = TracedPath(dot_p2.get_center,stroke_width=3, stroke_color= BLUE)
        path4 = TracedPath(dot_p3.get_center,stroke_width=3, stroke_color= BLUE)
        path.add_updater(lambda a:a.shift(RIGHT*0.02))
        self.add(dot_q, dot_p, dot_p1, dot_p2, dot_p3, l_pq, l_p1, l_p2,l_p3, path, path4)
        group = VGroup(dot_q, dot_p, dot_p1, dot_p2, dot_p3, l_pq, l_p1, l_p2,l_p3, path, path1, path2, path3, path4)
        self.play(t.set_value, 2*TAU, run_time = 16, rate_func = linear)
        self.play(FadeOut(group))
        self.wait()

class Part11(Scene):

    def construct(self):
        sentence01 = TextMobject("我们得到了一个近似的方波！", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("可以猜想只要我们控制的足够好，我们可以画出很多东西！", color = BLUE).scale(0.8).to_edge(UP).shift(DOWN)
        sentence03 = TextMobject("这背后的原理也就是","傅里叶分析","，但我相信你已经有了一些感受，Right？", color = BLUE).scale(0.8).to_edge(UP).shift(2*DOWN)
        self.play(Write(sentence01), run_time = 1)
        self.wait(2)
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03), run_time = 1.5)
        self.play(Indicate(sentence03[1]))
        self.wait(1.5)
        group = VGroup(sentence01, sentence02, sentence03)
        self.play(FadeOut(group))
        self.wait()



class Part12(Scene):
    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}

        )
        self.play(ShowCreation(grid))
        label = TextMobject("$w=-\\sqrt(z)-1$", color=RED).shift(RIGHT * 3).shift(UP * 2)
        self.play(Write(label), run_time=1)
        grid.prepare_for_nonlinear_transform()
        func = ParametricFunction(lambda t: np.array([np.cos(t)-1, np.sin(t), 0]), t_min=0, t_max=TAU).set_color(RED)
        self.play(
            func.apply_complex_function,
            lambda z: np.sqrt(z)*(-1) - 1,
            grid.apply_complex_function,
            lambda z: np.sqrt(z)*(-1) - 1,
            run_time=10)
        self.wait(2)
        self.wait()


class Part13(Scene):
    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}

        )
        self.play(ShowCreation(grid))
        label = TextMobject("$w=\\sqrt(z)-1$", color=RED).shift(RIGHT * 3).shift(UP * 2)
        self.play(Write(label), run_time=1)
        grid.prepare_for_nonlinear_transform()
        func = ParametricFunction(lambda t: np.array([np.cos(t)-1, np.sin(t), 0]), t_min=0, t_max=TAU).set_color(RED)
        self.play(
            func.apply_complex_function,
            lambda z: np.sqrt(z) - 1,
            grid.apply_complex_function,
            lambda z: np.sqrt(z)-1,
            run_time=10)
        self.wait(2)
        self.wait()

class AddedProof(Scene):

    def construct(self):
        sentence01 = TextMobject("在实数域上，我们有:",color = RED).scale(0.8).to_edge(UP)
        equation01 = TextMobject("$e^x=\\lim\\limits_{n\\rightarrow +\\infty}(1+\\displaystyle\\frac{x}{n})^n$", color = BLUE).to_edge(UP).shift(DOWN)
        sentence02 = TextMobject("这个定义也可以扩展到复数域上:", color = RED).scale(0.8).next_to(equation01, DOWN)
        equation02 = TextMobject("$e^{i\\theta}=\\lim\\limits_{n\\rightarrow +\\infty}(1+\\displaystyle\\frac{i\\theta}{n})^n$", color = BLUE).next_to(sentence02, DOWN)
        tip = TextMobject("你要相信这个扩展的确是合理且自洽的，我在这里想做的是它的直观展示", color = GREEN).scale(0.8).next_to(equation02 , DOWN)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(DrawBorderThenFill(equation01), run_time = 2)
        self.wait(2)
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        self.play(DrawBorderThenFill(equation02), run_time = 2)
        self.wait(2)
        self.play(FadeIn(tip), run_time = 1)
        self.wait(2)
        group = VGroup(sentence01, sentence02, equation02, equation01, tip)
        self.play(FadeOut(group), run_time = 1)
        self.wait()

class AddedProof1(Scene):

    def construct(self):
        grid = ComplexPlane(
            axis_config={"stroke_color": WHITE}

        )
        self.play(ShowCreation(grid))
        equation = TextMobject("$e^i=\\lim\\limits_{n \\to +\\infty}(1+\\displaystyle\\frac{i}{n})^n$", color = RED).scale(0.8).to_edge(UR)
        word3 = TextMobject("$n=3$", color = GREEN).scale(0.6).to_edge(UR).shift(1.6*DOWN)
        word7 = TextMobject("$n=7$", color = GREEN).scale(0.6).to_edge(UR).shift(1.6*DOWN)
        word_theta = TextMobject("$\\theta=1\\quad rad$", color = GREEN).scale(0.7).to_edge(UR).shift(DOWN)
        self.play(ShowCreation(equation), run_time = 2)
        self.wait(1)
        cir = Circle(radius = 3).set_color(BLUE)
        line = Line(np.array([0,0,0]), np.array([3*np.cos(1), 3*np.sin(1), 0]), color = BLUE)
        arc = Arc(radius=0.8, angle=1).set_color(RED)
        label = TextMobject("$\\theta$", color = RED).scale(0.6).next_to(arc, RIGHT*0.8)
        self.play(ShowCreation(cir))
        self.play(ShowCreation(arc), ShowCreation(line))
        self.play(Write(label))
        self.play(Write(word_theta))
        self.wait(1)
        self.play(Write(word3), run_time = 1)
        z1 = []
        for i in range(3):
            z1.append(3*(1+1j/3)**(i+1))
        Vec1 = VGroup()
        label_z1 = VGroup()
        Color = [RED, ORANGE, YELLOW, GREEN, TEAL, BLUE, PURPLE]
        for i in range(3):
            Vec1.add(Vector(grid.n2p(z1[i])).set_color(Color[i]))
        label_z1.add(TextMobject("$(1+\\frac{i}{3})^1$", color = Color[0]).scale(0.6).move_to(grid.n2p(z1[0]))).shift(RIGHT*0.5)
        label_z1.add(TextMobject("$(1+\\frac{i}{3})^2$", color = Color[1]).scale(0.6).move_to(grid.n2p(z1[1]))).shift(RIGHT*0.5)
        label_z1.add(TextMobject("$(1+\\frac{i}{3})^3$", color = Color[2]).scale(0.6).move_to(grid.n2p(z1[2]))).shift(RIGHT*0.5)
        for i in range(3):
            self.play(ShowCreation(Vec1[i]), ShowCreation(label_z1[i]), run_time = 1)
            self.wait(1)
        self.wait(2)
        self.play(FadeOut(Vec1), FadeOut(label_z1), run_time=2)
        self.play(ClockwiseTransform(word3, word7), run_time = 1)
        z2 = []
        for i in range(7):
            z2.append(3*(1+1j/7)**(i+1))
        Vec2 = VGroup()
        for i in range(7):
            Vec2.add(Vector(grid.n2p(z2[i])).set_color(Color[i]))
        for i in range(7):
            self.play(ShowCreation(Vec2[i]))
            self.wait(0.5)
        label_z2 = TextMobject("$(1+\\frac{i}{7})^7$", color = Color[6]).scale(0.6).move_to(grid.n2p(z2[6])).shift(RIGHT*0.5)
        self.play(ShowCreation(label_z2))
        self.wait(2)
        self.play(FadeOut(label_z2), FadeOut(Vec2), FadeOut(arc), FadeOut(line))
        self.wait(1)
        word_theta_2 = TextMobject("$\\theta=\\pi\\quad rad$", color = GREEN).scale(0.7).to_edge(UR).shift(DOWN)
        word50 = TextMobject("$n=50$", color = GREEN).scale(0.6).to_edge(UR).shift(1.6*DOWN)
        arc2 = Arc(radius = 0.8 ,angle = PI).set_color(RED)
        self.play(ShowCreation(arc2))
        equation2 = TextMobject("$e^{i\\pi}=\\lim\\limits_{n \\to +\\infty}(1+\\displaystyle\\frac{i\\pi}{n})^n$", color=RED).scale(0.8).to_edge(UR)
        self.play(ClockwiseTransform(word_theta, word_theta_2), ReplacementTransform(equation, equation2), run_time = 2)
        self.play(ClockwiseTransform(word3, word50))
        self.wait(2)
        z3 = []
        for i in range(50):
            z3.append(3*(1+PI*1j/50)**(i+1))
        Vec3 = VGroup()
        for i in range(50):
            Vec3.add(Vector(grid.n2p(z3[i])).set_color(Color[int(i/8)]))
        for i in range(50):
            self.play(ShowCreation(Vec3[i]), run_time = 0.2)
        label_z3 = TextMobject("$(1+\\frac{i\\pi}{50})^{50}$", color = Color[6]).scale(0.6).move_to(grid.n2p(z3[49])).shift(LEFT*0.8)
        self.play(Write(label_z3))
        self.wait(3)
        self.play(FadeOut(label_z3), FadeOut(Vec3))
        self.wait(1)
        word100 = TextMobject("$n=100$", color = GREEN).scale(0.6).to_edge(UR).shift(1.6*DOWN)
        self.play(ClockwiseTransform(word3, word100))
        z4 = []
        for i in range(100):
            z4.append(3*(1+PI*1j/100)**(i+1))
        Vec4 = VGroup()
        for i in range(100):
            Vec4.add(Vector(grid.n2p(z4[i])).set_color(Color[int(i/15)]))
        for i in range(100):
            self.play(ShowCreation(Vec4[i]), run_time = 0.1)
        label_z4 = TextMobject("$(1+\\frac{i\\pi}{100})^{100}$", color = Color[6]).scale(0.6).move_to(grid.n2p(z4[99])).shift(LEFT*0.8)
        self.play(Write(label_z4))
        self.wait(3)
        equation3 = TextMobject("$n\\rightarrow +\\infty, e^{i\\theta}=\\cos {\\theta}+i\\sin {\\theta}$", color = YELLOW).scale(0.8).to_edge(UP).shift(UP*0.5)
        sentence = TextMobject("很直观，Right？", color = YELLOW).move_to(np.array([0,-1,0]))
        self.play(Write(equation3))
        self.wait(2)
        self.play(ShowCreationThenFadeOut(sentence), run_time = 3)
        self.wait()





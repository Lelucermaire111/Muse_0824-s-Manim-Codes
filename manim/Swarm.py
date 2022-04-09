from manimlib.imports import *


class BeginAnimation(GraphScene):
    CONFIG = {
        "x_min":0,
        "x_max":3,
        "x_axis_width":6,
        "y_min":-1,
        "y_max":3,
        "y_axis_height":4,
    }
    def construct(self):
        sen1 = TextMobject("我们通常将求最值问题和导数的知识联系在一起").scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("但是这期视频我并不想用导数来讨论这个问题").scale(0.7).shift(DOWN*3.5)
        sen3 = TextMobject("毕竟想使用导数你总是需要一些熟练的数学知识").scale(0.7).shift(DOWN*3.5)
        sen4 = TextMobject("所以，你能否想到一些求解最优值的方法：").scale(0.7).shift(DOWN*3.5)
        sen5 = TextMobject("它们不需要过多的数学基础，而且很容易理解与编写").scale(0.7).shift(DOWN*3.5)
        sen6 = TextMobject("当然，你可以借助计算机编写程序来实现你的方法").scale(0.7).shift(DOWN*3.5)
        sen7 = TextMobject("除此之外，你也需要考虑我们面临的问题可能是更复杂的高维情况").scale(0.7).shift(DOWN*3.5)

        eq1 = TextMobject("$$\\displaystyle f'(x_0)=\\lim\\limits_{x\\rightarrow x_0}\\frac{f(x)-f(x_0)}{x-x_0}$$",color = BLUE).scale(0.8).shift(DOWN*1.5+RIGHT*3.5)
        word = TextMobject("No Derivative!",color = BLUE).shift(DOWN*2+LEFT*3)
        word1 = TextMobject("* Easy to Understand",color = RED).scale(0.8).shift(UP*3+RIGHT*3)
        word2 = TextMobject("* No much prior knowledge",color = RED).scale(0.8).shift(UP*2).align_to(word1,LEFT)
        word3 = TextMobject("* Easy to program",color = RED).scale(0.8).shift(UP).align_to(word2,LEFT)
        word4 = TextMobject("* High Dimension",color = BLUE).scale(0.8).align_to(word3,LEFT)
        computer = SVGMobject('Computer.svg',color = BLUE).shift(DOWN*2+RIGHT*3)

        self.play(Write(sen1),run_time = 2)
        self.wait(0.5)
        self.graph_origin = 6*LEFT+0.5*UP
        self.axes_color = RED
        self.setup_axes(animate=True)
        fg1 = self.get_graph(lambda x:x*np.log(x),GREEN,x_min = 0.001,x_max = 3)
        self.play(ShowCreation(fg1))
        self.wait(0.5)
        self.graph_origin = RIGHT+0.5*UP
        self.axes_color= BLUE
        self.setup_axes(animate=True)
        fg2 = self.get_graph(lambda x:np.log(x)+1,YELLOW,x_min=0.1,x_max = 3)
        self.play(ShowCreation(fg2))
        self.play(Write(eq1))
        self.wait(2)
        self.play(FadeOut(sen1))
        self.play(Write(sen2),run_time = 1.5)
        self.play(FadeOut(self.axes),FadeOut(fg2))
        self.play(ReplacementTransform(eq1,word),run_time = 1)
        self.wait(2)
        self.play(FadeOut(sen2))
        self.play(Write(sen3),run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(sen3))
        self.play(Write(sen4),run_time = 1.5)
        self.wait(1.5)
        self.play(FadeOut(sen4))
        self.play(Write(sen5),run_time = 1.5)
        self.play(Write(word1))
        self.play(Write(word2))
        self.wait(2)
        self.play(FadeOut(sen5))
        self.play(Write(sen6),run_time = 1.5)
        self.play(ShowCreation(computer))
        self.play(Write(word3))
        self.wait(0.5)
        self.play(Uncreate(computer))
        self.wait(2)
        self.play(FadeOut(sen6))
        self.play(Write(sen7),run_time = 1)
        self.play(Write(word4))
        self.wait(3)

class Part01(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 3,
        "x_axis_width": 6,
        "y_min": -1,
        "y_max": 3,
        "y_axis_height": 6,
    }
    def xlnx(self,t):
        return t*np.log(t)

    def construct(self):
        label = TextMobject("$$y=x\\ln x$$",color = BLUE).shift(UP*3).shift(LEFT*3)
        sen1 = TextMobject("认识函数取值最初的方式是怎样的？").scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("我们可以在一定范围内选取自变量的值然后代入得到函数值").scale(0.7).shift(DOWN*3.5)
        sen3 = TextMobject("如果我们选取了很多个点，我们就可以大致描述函数的图像").scale(0.7).shift(DOWN*3.5)
        sen4 = TextMobject("借助于现代计算机的帮助下，我们很容易选取大量的点").scale(0.7).shift(DOWN*3.5)
        sen5 = TextMobject("然后我们可以选取这些点中最优的函数值来作为近似的最优值").scale(0.7).shift(DOWN*3.5)
        sen6 = TextMobject("尽管具有不确定性，不过只要点足够多，还是有希望给出一个靠谱的答案").scale(0.7).shift(DOWN*3.5)
        sen7 = TextMobject("毕竟这几乎是一种朴素的随机猜的方式！").scale(0.7).shift(DOWN*3.5)

        self.play(Write(sen1),run_time = 1.5)
        self.graph_origin = 6*LEFT+DOWN*1
        self.axes_color = RED
        self.setup_axes(animate=True)
        fg1 = self.get_graph(lambda x:x*np.log(x),GREEN,x_min = 0.001,x_max = 3)
        self.play(DrawBorderThenFill(label))
        self.wait(1.5)
        self.play(ReplacementTransform(sen1,sen2),run_time = 1)
        y_min = 100
        x_min = 0
        rand = round(random.uniform(0, 3), 2)
        y_val = round(self.xlnx(rand), 2)
        if y_val < y_min:
            x_min = rand
            y_min = y_val
        label_x = TextMobject("$x=$" + str(rand),color = BLUE).scale(0.8).shift(UP*3+RIGHT*3)
        label_y = TextMobject("$y=$" + str(y_val),color = BLUE).scale(0.8).shift(UP*2+RIGHT*3)
        label_min = TextMobject("$y_{min}=$" + str(y_min),color = RED).scale(0.8).shift(UP+RIGHT*3)
        self.play(Write(label_x),run_time = 1)
        self.play(Write(label_y),run_time = 1)
        self.play(Write(label_min))
        dot = Dot(self.input_to_graph_point(rand,fg1),color = BLUE)
        self.play(ShowCreation(dot))
        self.wait(1.5)
        self.play(ReplacementTransform(sen2,sen3),run_time = 1)
        for i in range(0,3):
            rand = round(random.uniform(0,3),2)
            y_val = round(self.xlnx(rand),2)
            if y_val < y_min:
                x_min = rand
                y_min = y_val
            label_x1 = TextMobject("$x=$" + str(rand), color=BLUE).scale(0.8).shift(UP * 3 + RIGHT * 3)
            label_y1 = TextMobject("$y=$" + str(y_val), color=BLUE).scale(0.8).shift(UP * 2 + RIGHT * 3)
            label_min1 = TextMobject("$y_{min}=$" + str(y_min), color=RED).scale(0.8).shift(UP + RIGHT * 3)
            dot = Dot(self.input_to_graph_point(rand, fg1), color=BLUE)
            self.play(Transform(label_x,label_x1),run_time = 0.25)
            self.play(Transform(label_y,label_y1),run_time = 0.25)
            self.play(Transform(label_min,label_min1),run_time = 0.25)
            self.add(dot)

        self.wait(2)
        self.play(ReplacementTransform(sen3,sen4),run_time = 1)

        for i in range(1,50):
            rand = round(random.uniform(0,3),2)
            y_val = round(self.xlnx(rand),2)
            if y_val < y_min:
                x_min = rand
                y_min = y_val
            label_x1 = TextMobject("$x=$" + str(rand), color=BLUE).scale(0.8).shift(UP * 3 + RIGHT * 3)
            label_y1 = TextMobject("$y=$" + str(y_val), color=BLUE).scale(0.8).shift(UP * 2 + RIGHT * 3)
            label_min1 = TextMobject("$y_{min}=$" + str(y_min), color=RED).scale(0.8).shift(UP + RIGHT * 3)
            dot = Dot(self.input_to_graph_point(rand, fg1), color=BLUE)
            self.play(Transform(label_x,label_x1),run_time = 0.2/i)
            self.play(Transform(label_y,label_y1),run_time = 0.2/i)
            self.play(Transform(label_min,label_min1),run_time = 0.25/i)
            self.add(dot)
        self.wait(2)
        self.play(ReplacementTransform(sen4,sen5))
        dot = Dot(self.input_to_graph_point(x_min,fg1),color = RED)
        self.play(ShowCreation(dot),Indicate(label_min))
        self.wait(2)
        self.play(ReplacementTransform(sen5,sen6))
        self.wait(2)
        self.play(ReplacementTransform(sen6,sen7))
        self.wait(3)

class Part02(Scene):
    def construct(self):
        sen1 = TextMobject("实际上，刚刚的过程让我想到了一种基于概率的数学方法").scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("蒙特卡罗法",color = RED).scale(0.8).shift(DOWN*3.5)
        sen3 = TextMobject("这么说有一些抽象，让我们来看一个具体的例子").scale(0.7).shift(DOWN*3.5)

        word = TextMobject("Monte Carlo",color = BLUE).to_edge(UP)
        word1 = TextMobject("* 一种以概率统计理论为指导的数值计算方法",color = BLUE).scale(0.8).next_to(word,DOWN*0.8)
        word2 = TextMobject("* 使用随机数或伪随机数来解决问题", color = BLUE).scale(0.8).next_to(word1,DOWN*0.8).align_to(word1,LEFT)

        self.play(Write(sen1),run_time = 1.5)
        self.wait(1.5)
        self.play(Transform(sen1,sen2))
        self.play(Write(word))
        self.wait(1)
        self.play(Write(word1),run_time = 2)
        self.play(Write(word2), run_time = 2)
        self.wait(1.5)
        self.play(FadeOut(sen1))
        self.play(Write(sen3),run_time = 2)
        self.wait(2)

class Part03(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 1.1,
        "x_axis_width": 6.6,
        "y_min": 0,
        "y_max": 1.1,
        "y_axis_height": 6.6,
    }
    def construct(self):
        self.graph_origin = LEFT*5+DOWN*3
        self.setup_axes(animate=False)
        self.add(self.axes)
        cir = Arc(radius = 6).set_color(GREEN).shift(DOWN*3+LEFT*5)
        square = Square(side_length = 6).shift(LEFT*2)
        self.add(cir,square)
        sen1 = TextMobject("用蒙特卡罗法如何求圆周率呢？").scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("想象成往正方形内随机地撒一把豆子").scale(0.7).shift(DOWN*3.5)
        sen3 = TextMobject("撒的豆子足够多，落在四分之一圆内的豆子比例应该近似等于面积的比值").scale(0.7).shift(DOWN*3.5)
        sen4 = TextMobject("这是我模拟了100次的结果").scale(0.7).shift(DOWN*3.5)
        sen4_1 = TextMobject("这是我继续模拟了1000次的结果").scale(0.7).shift(DOWN*3.5)
        sen4_2 = TextMobject("这是我继续模拟了10000次的结果").scale(0.7).shift(DOWN*3.5)
        sen5 = TextMobject("你也可以用类似的方法去求一些定积分").scale(0.7).shift(DOWN*3.5)

        eq = TextMobject("$$\\displaystyle\\frac{S_{circle}}{S_{square}}=\\frac{\\pi}{4}=\\frac{Num_{inside}}{Num_{all}}$$",color = BLUE).scale(0.8).shift(UP*3+RIGHT*4.5)

        self.play(Write(sen1),run_time = 1)
        self.wait(2)
        self.play(Transform(sen1,sen2),run_time = 1)
        self.wait(2)
        self.play(Transform(sen1,sen3))
        self.wait(1)
        self.play(Write(eq),run_time = 3)

        rand1 = random.uniform(0, 1)
        rand2 = random.uniform(0, 1)
        sum = 0
        num_in = 0
        color = BLUE
        if rand1**2+rand2**2 <1:
            color = BLUE
            num_in = num_in + 1
        else:
            color = RED
        sum = sum + 1
        pi_val = round(4 * num_in / sum,5)
        dot = SmallDot(self.coords_to_point(rand1,rand2),color = color)
        self.play(ShowCreation(dot))
        self.wait(1)

        group1 = VGroup(dot)
        for i in range(1,100):
            rand1 = random.uniform(0, 1)
            rand2 = random.uniform(0, 1)
            if rand1 ** 2 + rand2 ** 2 < 1:
                color = BLUE
                num_in = num_in + 1
            else:
                color = RED
            sum = sum + 1
            pi_val = round(4 * num_in / sum, 5)
            dot = SmallDot(self.coords_to_point(rand1, rand2), color=color)
            group1.add(dot)
        self.play(ShowCreation(group1))
        pi_label = TextMobject("$\\pi=$" + str(pi_val)).shift(UP + RIGHT * 5)
        self.play(Write(pi_label), run_time=0.5)
        self.wait(1)
        self.play(Transform(sen1,sen4))
        self.wait(2)
        group2 = VGroup()
        for i in range(1,1000):
            rand1 = random.uniform(0, 1)
            rand2 = random.uniform(0, 1)
            if rand1 ** 2 + rand2 ** 2 < 1:
                color = BLUE
                num_in = num_in + 1
            else:
                color = RED
            sum = sum + 1
            pi_val = round(4 * num_in / sum, 5)
            dot = SmallDot(self.coords_to_point(rand1, rand2), color=color)
            group2.add(dot)
        self.play(ShowCreation(group2))
        pi_label_1 = TextMobject("$\\pi=$" + str(pi_val)).shift(UP + RIGHT * 5)
        self.play(Transform(pi_label,pi_label_1), run_time=0.5)
        self.wait(1)
        self.play(Transform(sen1,sen4_1))
        self.wait(2)
        group3 = VGroup()
        for i in range(1,10000):
            rand1 = random.uniform(0, 1)
            rand2 = random.uniform(0, 1)
            if rand1 ** 2 + rand2 ** 2 < 1:
                color = BLUE
                num_in = num_in + 1
            else:
                color = RED
            sum = sum + 1
            pi_val = round(4 * num_in / sum, 5)
            dot = SmallDot(self.coords_to_point(rand1, rand2), color=color)
            group3.add(dot)
        self.play(ShowCreation(group3))
        pi_label_1 = TextMobject("$\\pi=$" + str(pi_val)).shift(UP + RIGHT * 5)
        self.play(Transform(pi_label,pi_label_1), run_time=0.5)
        self.wait(1)
        self.play(Transform(sen1,sen4_2))
        self.wait(2)
        self.play(Transform(sen1,sen5))
        self.wait(3)

class Part04(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "x_axis_width": 6,
        "y_min": -5,
        "y_max": 5,
        "y_axis_height": 6,
        "cont":"Contour.png"
    }
    def func(self,x,y):
        return (x**2+y**2)/100-np.cos(x)*np.cos(y)+1
    def construct(self):
        cont = ImageMobject(self.cont).set_height(6).set_width(6).shift(LEFT*3)
        self.graph_origin = LEFT*3
        self.setup_axes(animate=False)
        sen1 = TextMobject("让我们回到前面的问题").scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("随机取值并不是一种高效的方法，让我们用一个高维函数来再次感受一下").scale(0.7).shift(DOWN*3.5)
        sen3 = TextMobject("这是一个非常特殊而有趣的函数，这里给出它的等高线图").scale(0.7).shift(DOWN*3.5)
        added = TextMobject("颜色越深代表其值越小").scale(0.7).shift(DOWN*3.5)
        sen4 = TextMobject("不过你很容易观察其最小值是$x=0,y=0$时为$0$").scale(0.7).shift(DOWN*3.5)
        sen5 = TextMobject("在进行了1000次模拟后，得到了这样的结果").scale(0.7).shift(DOWN*3.5)
        sen6 = TextMobject("不得不说这种方法比较低效而且成本高，不过确实很容易编写程序").scale(0.7).shift(DOWN*3.5)
        sen7 = TextMobject("你只需要掌握随机数random和for循环的用法就可以编写").scale(0.7).shift(DOWN*3.5)
        sen8 = TextMobject("但是我们仍需要去寻找更好的方法").scale(0.7).shift(DOWN*3.5)

        self.play(Write(sen1))
        self.wait(1)
        self.play(Transform(sen1,sen2))
        func = TextMobject("$$z=\\displaystyle\\frac{x^2+y^2}{100}-\\cos x\\cos y+1$$", color=BLUE).scale(0.7).to_edge(UP).shift(UP*0.5+RIGHT)
        self.play(Write(func), run_time = 2)
        self.wait(2)
        self.play(Transform(sen1,sen3),run_time = 1.5)
        self.play(FadeIn(cont))
        self.add(self.axes)
        self.wait(2)
        self.play(Transform(sen1,added))
        self.wait(2)
        self.play(Transform(sen1,sen4))
        self.wait(2)
        self.play(Transform(sen1,sen5))
        self.wait(2)
        x = 10
        y = 10
        val_min = 10
        group = VGroup()
        for i in range(1,1000):
            rand1 = random.uniform(-5, 5)
            rand2 = random.uniform(-5, 5)
            val = self.func(rand1,rand2)
            if val < val_min:
                val_min = round(val,5)
                x = round(rand1,5)
                y = round(rand2,5)
            dot = SmallDot(self.coords_to_point(rand1, rand2), color = BLUE)
            group.add(dot)
        self.play(ShowCreation(group))
        x_label = TextMobject("$x=$"+str(x),color = BLUE).shift(UP*2.5+RIGHT*4.5)
        y_label = TextMobject("$y=$"+str(y),color = BLUE).shift(UP*1.5).align_to(x_label,LEFT)
        z_label = TextMobject("$z_{min}=$"+str(val_min),color = RED).shift(0.5*UP).align_to(y_label,LEFT)

        word1 = TextMobject("* random",color = RED).shift(RIGHT*5+DOWN)
        word2 = TextMobject("* for",color = RED).shift(DOWN*2).align_to(word1,LEFT)
        self.play(Write(x_label))
        self.play(Write(y_label))
        self.play(Write(z_label))
        self.wait(2)
        self.play(Transform(sen1,sen6))
        self.wait(2)
        self.play(Transform(sen1,sen7))
        self.play(Write(word1),Write(word2))
        self.wait(1)
        self.play(Transform(sen1,sen8))
        self.wait(3)

class Part05(Scene):
    def construct(self):
        sen1 = TextMobject("随机取值提供给了我们一个基于概率模拟的思路").scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("接下来让我们从大自然汲取一下灵感").scale(0.7).shift(DOWN*3.5)
        sen3 = TextMobject("涌现体现的是个体组成的群体展现出远比其本身强大的智能").scale(0.7).shift(DOWN*3.5)
        sen = TextMobject("在复杂的自适应系统中，‘涌现’现象俯拾皆是：蚂蚁社群、神经网络、免疫系统、互联网乃至世界经济等。但凡一个过程的整体的行为远比构成它的部分复杂，皆可称为‘涌现’。",color = BLUE).scale(0.7).to_edge(UP)
        author = TextMobject("———约翰霍兰德",color = BLUE).scale(0.7).next_to(sen,DOWN).shift(RIGHT*4.5)
        self.play(Write(sen1))
        self.wait(1.5)
        self.play(Transform(sen1,sen2))
        self.wait(2)
        self.play(FadeOut(sen1))
        self.play(Write(sen),run_time = 3)
        self.play(Write(author))
        self.wait(2)
        self.play(Write(sen3))
        self.play(FadeOut(sen),FadeOut(author))

        group1 = VGroup()

        for i in range(0,900):
            rand1 = random.uniform(-3, 3)
            rand2 = random.uniform(-3, 3)
            dot = SmallDot(np.array([rand1, rand2, 0]), color=BLUE)
            group1.add(dot)

        self.play(ShowCreation(group1))

        self.wait(2)
        group2 = VGroup()
        for i in range(1,31):
            for j in range(1,31):
                dot = SmallDot(np.array([-3+i*0.2,-3+0.2*j,0]),color = BLUE)
                group2.add(dot)

        self.play(ReplacementTransform(group1,group2),run_time = 2)
        self.wait(3)

class Part06(Scene):
    def construct(self):
        sen1 = TextMobject("想象这样一个例子").scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("你是一个粒子在随机探索一个区域，你能够评估当前位置的优劣").scale(0.7).shift(DOWN*3.5)
        sen3 = TextMobject("所以你要如何寻找这个区域内最好的位置呢？").scale(0.7).shift(DOWN*3.5)
        sen4 = TextMobject("也许你会借助于惯性的前进($\\omega$代表惯性因子)").scale(0.7).shift(DOWN*3.5)
        sen5 = TextMobject("你或许还会借助于记忆中最好的位置").scale(0.7).shift(DOWN*3.5)
        sen6 = TextMobject("所以你下一时刻的速度应该是蓝色矢量").scale(0.7).shift(DOWN*3.5)

        d1 = TextMobject("$x_k$代表当前位置,","$v_k$代表上一时刻的速度",color = BLUE).scale(0.7).to_edge(UP)
        d2 = TextMobject("$p_k$代表记忆中最好的位置,","$g_k$代表种群到达过的最好位置",color= BLUE).scale(0.7).next_to(d1,DOWN*0.6).align_to(d1,LEFT)

        dot = Dot(np.array([-2,-3,0]),color = BLUE)
        lb1 = TextMobject("$x_k$",color = BLUE).scale(0.7).next_to(dot,0.8*LEFT)
        dot1 = Dot(np.array([2,1,0]),color = RED)
        lb2 = TextMobject("$p_k$",color = RED).scale(0.7).next_to(dot1,LEFT*0.8)
        arr = DashedLine(dot.get_center(),dot1.get_center(),color = RED)
        v2 = Line(np.array([1,-2,0]),np.array([3,0,0]),color = RED)
        v3 = Line(dot.get_center(),np.array([3,0,0]),color = BLUE)
        v1 = Line(dot.get_center(),np.array([1,-2,0]),color = GREEN)
        lb3 = TextMobject("$\\omega v_k$",color = GREEN,).scale(0.7).shift(DOWN*2)

        self.play(Write(sen1),run_time = 1)
        self.wait(1)
        self.play(FadeOut(sen1))
        self.play(Write(sen2),run_time = 2)
        self.play(ShowCreation(dot))
        self.wait(2)
        self.play(Transform(sen2,sen3))
        self.wait(1.5)
        self.play(Transform(sen2,sen4))
        self.play(Write(lb1))
        self.play(ShowCreation(v1),Write(lb3))
        self.wait(1)
        self.play(Write(d1))
        self.wait(1)
        self.play(Transform(sen2,sen5))
        self.play(ShowCreation(dot1),Write(lb2))
        self.wait(1)
        self.play(Write(d2[0]))
        self.play(ShowCreation(arr))
        self.wait(1)
        self.play(TransformFromCopy(arr,v2))
        self.wait(1)
        self.play(ShowCreation(v3))
        self.play(Transform(sen2,sen6))
        self.wait(2)

        sen7 = TextMobject("但是别忘了你还可以知道同伴们目前到达的最好位置",color = BLUE).scale(0.7).shift(DOWN*3.5)
        self.play(Transform(sen2,sen7))
        dot2 = Dot(np.array([-5,1,0]),color = YELLOW)
        lb4 = TextMobject("$g_k$",color = YELLOW).scale(0.7).next_to(dot2,LEFT)
        arr1 = DashedLine(dot.get_center(),dot2.get_center(),color = YELLOW)
        self.play(ShowCreation(dot2),Write(lb4))
        self.play(Write(d2[1]))
        self.wait(1)
        self.play(ShowCreation(arr1))
        self.wait(1)
        v4 = Line(np.array([3,0,0]),np.array([1.5,2,0]),color = YELLOW)
        self.play(TransformFromCopy(arr1,v4))
        self.wait(1)
        v5 = Line(dot.get_center(),np.array([1.5,2,0]),color = BLUE)
        lb5 = TextMobject("$v_{k+1}$",color = BLUE).scale(0.7).next_to(v5,LEFT*0.8).shift(RIGHT)
        self.play(ReplacementTransform(v3,v5))
        self.play(Write(lb5))
        self.wait(2)

        sen8 = TextMobject("一个看起来很合理的策略，让我们整理一下思路").scale(0.7).shift(DOWN*3.5)
        eq1 = TextMobject("$ v_{k+1}=$","$\\omega v_k$","$+$","$\\displaystyle c_1 r_1\\frac{p_k-x_k}{\\Delta t}$","$+$","$\\displaystyle c_2 r_2\\frac{g_k-x_k}{\\Delta t}$",color = BLUE).scale(0.8).to_edge(UP)
        eq2 = TextMobject("$x_{k+1}=x_k+v_{k+1}\\Delta t$",color = BLUE).scale(0.8).next_to(eq1,DOWN).align_to(eq1,LEFT)
        eq1[1].set_color(GREEN)
        eq1[3].set_color(RED)
        eq1[5].set_color(YELLOW)
        self.play(Transform(sen2,sen8))
        self.wait(2)
        self.play(FadeOut(d1),FadeOut(d2))
        self.play(Write(eq1),run_time = 4)
        self.play(Write(eq2))

        sen9 = TextMobject("其中$\\omega$是惯性因子").scale(0.7).shift(DOWN*3.5)
        sen10 = TextMobject("$c_1$代表对自己的相信程度").scale(0.7).shift(DOWN*3.5)
        sen11 = TextMobject("$c_2$代表对社群的相信程度").scale(0.7).shift(DOWN*3.5)
        sen12 = TextMobject("你可以通过控制这三个变量来控制群体演化的侧重方面").scale(0.7).shift(DOWN*3.5)
        sen13 = TextMobject("$r_1,r_2$是产生的随机数").scale(0.7).shift(DOWN*3.5)
        sen14 = TextMobject("对高维情况具有普遍性，很清晰直观，Right?",color = RED).scale(0.7).shift(DOWN*3.5)

        self.play(Transform(sen2,sen9))
        self.play(Indicate(eq1[1],color = GREEN))
        self.wait(2)
        self.play(Transform(sen2,sen10))
        self.play(Indicate(eq1[3],color = RED))
        self.wait(2)
        self.play(Transform(sen2,sen11))
        self.play(Indicate(eq1[5]))
        self.wait(2)
        self.play(Transform(sen2,sen12))
        self.wait(2)
        self.play(Transform(sen2,sen13))
        self.wait(2)
        self.play(Transform(sen2,sen14))
        self.wait(3)


import numpy as np
import matplotlib.pyplot as plt


class PSO(object):
    def __init__(self, population_size, max_steps):
        self.w = 0.6  # 惯性权重
        self.c1 = self.c2 = 2
        self.population_size = population_size  # 粒子群数量
        self.dim = 2  # 搜索空间的维度
        self.max_steps = max_steps  # 迭代次数
        self.x_bound = [-5, 5]  # 解空间范围
        self.x = np.random.uniform(self.x_bound[0], self.x_bound[1],
                                   (self.population_size, self.dim))  # 初始化粒子群位置
        self.v = np.random.rand(self.population_size, self.dim)  # 初始化粒子群速度
        fitness = self.calculate_fitness(self.x)
        self.p = self.x  # 个体的最佳位置
        self.pg = self.x[np.argmin(fitness)]  # 全局最佳位置
        self.individual_best_fitness = fitness  # 个体的最优适应度
        self.global_best_fitness = np.min(fitness)  # 全局最佳适应度

    def calculate_fitness(self, x):
        x1 = x[:, 0]
        x2 = x[:, 1]
        return np.sum(np.square(x) / 100, axis=1) + 1 - np.cos(x1) * np.cos(x2)

    def evolve(self):
        fig = plt.figure()
        for step in range(self.max_steps):
            r1 = np.random.rand(self.population_size, self.dim)
            r2 = np.random.rand(self.population_size, self.dim)
            # 更新速度和权重
            self.v = self.w * self.v + self.c1 * r1 * (self.p - self.x) + self.c2 * r2 * (self.pg - self.x)
            self.x = self.v + self.x
            plt.clf()
            plt.scatter(self.x[:, 0], self.x[:, 1], s=30, color='k')
            plt.xlim(self.x_bound[0], self.x_bound[1])
            plt.ylim(self.x_bound[0], self.x_bound[1])
            plt.pause(0.01)
            fitness = self.calculate_fitness(self.x)
            # 需要更新的个体
            update_id = np.greater(self.individual_best_fitness, fitness)
            self.p[update_id] = self.x[update_id]
            self.individual_best_fitness[update_id] = fitness[update_id]
            # 新一代出现了更小的fitness，所以更新全局最优fitness和位置
            if np.min(fitness) < self.global_best_fitness:
                self.pg = self.x[np.argmin(fitness)]
                self.global_best_fitness = np.min(fitness)
            print('best fitness: %.5f, mean fitness: %.5f' % (self.global_best_fitness, np.mean(fitness)))


class Part07(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "x_axis_width": 6,
        "y_min": -5,
        "y_max": 5,
        "y_axis_height": 6,
        "cont":"Contour.png"
    }
    def construct(self):
        sen1 = TextMobject("现在让我们来看看这个方法的效果怎么样",color = BLUE).scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("这里我取种群数量为20，运动次数为100",color = BLUE).scale(0.7).shift(DOWN*3.5)

        word1 = TextMobject("population size = $20$",color = BLUE).scale(0.8).shift(UP*2.7+RIGHT*4)
        word2 = TextMobject("run steps = $100$",color = BLUE).scale(0.8).shift(UP*1.9).align_to(word1,LEFT)

        cont = ImageMobject(self.cont).set_height(6).set_width(6).shift(LEFT * 3)
        self.graph_origin = LEFT * 3
        self.setup_axes(animate=False)
        self.play(FadeIn(cont))
        self.add(self.axes)
        self.play(Write(sen1))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.play(Write(word1))
        self.play(Write(word2))
        self.wait(2)
        self.play(FadeOut(sen1))
        pso = PSO(20,100)
        for step in range(pso.max_steps):
            r1 = np.random.rand(pso.population_size, pso.dim)
            r2 = np.random.rand(pso.population_size, pso.dim)
            # 更新速度和权重
            pso.v = pso.w * pso.v + pso.c1 * r1 * (pso.p - pso.x) + pso.c2 * r2 * (pso.pg - pso.x)
            pso.x = pso.v + pso.x
            group = VGroup()
            for i in pso.x:
                if abs(i[0])<=5 and abs(i[1])<=5:
                    dot = SmallDot(self.coords_to_point(i[0],i[1]),color = BLUE)
                    group.add(dot)
            self.add(group)
            self.wait(0.1)
            self.play(FadeOut(group),run_time = 0.05)
            fitness = pso.calculate_fitness(pso.x)
            # 需要更新的个体
            update_id = np.greater(pso.individual_best_fitness, fitness)
            pso.p[update_id] = pso.x[update_id]
            pso.individual_best_fitness[update_id] = fitness[update_id]
            # 新一代出现了更小的fitness，所以更新全局最优fitness和位置
            if np.min(fitness) < pso.global_best_fitness:
                pso.pg = pso.x[np.argmin(fitness)]
                pso.global_best_fitness = np.min(fitness)
        self.add(group)
        word3 = TextMobject("$x=$"+str(float(round(pso.pg[0],10))),color = BLUE).scale(0.8).shift(UP*1.1).align_to(word1,LEFT)
        word4 = TextMobject("$y=$"+str(float(round(pso.pg[1],10))),color = BLUE).scale(0.8).shift(UP*0.3).align_to(word1,LEFT)
        word5 = TextMobject("$z_{min}=$"+str(float(round(pso.global_best_fitness,10))),color = BLUE).scale(0.8).shift(DOWN*0.5).align_to(word1,LEFT)

        sen3 = TextMobject("最后的结果要改良很多，Right?").scale(0.7).shift(DOWN*3.5)
        sen4 = TextMobject("而且我们只用了20个粒子模拟了100次！").scale(0.7).shift(DOWN*3.5)
        sen5 = TextMobject("这种方法被称为粒子群算法，其本身体现了一种涌现的思想").scale(0.7).shift(DOWN*3.5)
        sen6 = TextMobject("当然对于特定的问题，你需要合理设置以上参数").scale(0.7).shift(DOWN*3.5)
        sen7 = TextMobject("比如如果我将惯性因子提高一点，你可以思考一下会发生什么").scale(0.7).shift(DOWN*3.5)
        title = TextMobject("Particle Swarm Optimization",color = RED).scale(0.8).shift(RIGHT).to_edge(UP)
        self.wait(1)
        self.play(Write(word3))
        self.play(Write(word4))
        self.play(Write(word5))

        self.wait(2)
        self.play(Write(sen3))
        self.wait(2)
        self.play(Transform(sen3,sen4))
        self.wait(2)
        self.play(Transform(sen3,sen5))
        self.play(Write(title))
        self.wait(2)
        self.play(Transform(sen3,sen6))
        self.play(FadeOut(group))
        self.wait(2)
        self.play(Transform(sen3,sen7))
        self.wait(3)
        pso = PSO(20, 100)
        pso.w = 0.8
        for step in range(pso.max_steps):
            r1 = np.random.rand(pso.population_size, pso.dim)
            r2 = np.random.rand(pso.population_size, pso.dim)
            # 更新速度和权重
            pso.v = pso.w * pso.v + pso.c1 * r1 * (pso.p - pso.x) + pso.c2 * r2 * (pso.pg - pso.x)
            pso.x = pso.v + pso.x
            group = VGroup()
            for i in pso.x:
                if abs(i[0]) <= 5 and abs(i[1]) <= 5:
                    dot = SmallDot(self.coords_to_point(i[0], i[1]), color=BLUE)
                    group.add(dot)
            self.add(group)
            self.wait(0.1)
            self.play(FadeOut(group), run_time=0.05)
            fitness = pso.calculate_fitness(pso.x)
            # 需要更新的个体
            update_id = np.greater(pso.individual_best_fitness, fitness)
            pso.p[update_id] = pso.x[update_id]
            pso.individual_best_fitness[update_id] = fitness[update_id]
            # 新一代出现了更小的fitness，所以更新全局最优fitness和位置
            if np.min(fitness) < pso.global_best_fitness:
                pso.pg = pso.x[np.argmin(fitness)]
                pso.global_best_fitness = np.min(fitness)
        self.add(group)
        word3_1 = TextMobject("$x=$" + str(float(round(pso.pg[0], 10))), color=BLUE).scale(0.8).shift(UP * 1.1).align_to(word1, LEFT)
        word4_1 = TextMobject("$y=$" + str(float(round(pso.pg[1], 10))), color=BLUE).scale(0.8).shift(UP * 0.3).align_to(word1, LEFT)
        word5_1 = TextMobject("$z_{min}=$" + str(float(round(pso.global_best_fitness, 10))), color=BLUE).scale(0.8).shift(DOWN * 0.5).align_to(word1, LEFT)
        self.play(Transform(word3,word3_1))
        self.play(Transform(word4,word4_1))
        self.play(Transform(word5,word5_1))
        self.wait(3)

class Part08(Scene):
    def construct(self):
        sen1 = TextMobject("我想通过这期视频给你一些启发",color = BLUE).scale(0.7).shift(DOWN*3.5)
        sen2 = TextMobject("即使抛开导数，我们仍然可以思考一些办法来解决问题",color = BLUE).scale(0.7).shift(DOWN*3.5)
        sen3 = TextMobject("这些办法往往很容易理解与实现",color = BLUE).scale(0.7).shift(DOWN*3.5)
        sen4 = TextMobject("如果你们喜欢相关内容，我可以将这个系列继续做下去",color = BLUE).scale(0.7).shift(DOWN*3.5)
        sen5 = TextMobject("希望本期视频有所帮助，感谢观看，Goodbye！",color = BLUE).scale(0.7).shift(DOWN*3.5)

        word1 = TextMobject("* Nelder Melder Simplex",color = RED).scale(0.8).shift(UP*3+LEFT*3)
        word2 = TextMobject("* Simulated Annealing",color = RED).scale(0.8).shift(UP*2.2).align_to(word1,LEFT)
        word3 = TextMobject("* Divided Rectangles",color = RED).scale(0.8).shift(UP*1.4).align_to(word1,LEFT)
        word4 = TextMobject("* Genetic Algorithms",color = RED).scale(0.8).shift(UP*0.6).align_to(word1,LEFT)
        word5 = TextMobject("* ......",color = RED).scale(0.8).shift(DOWN*0.2).align_to(word1,LEFT)

        self.play(Write(sen1))
        self.wait(2)
        self.play(Transform(sen1,sen2))
        self.wait(2)
        self.play(Write(word1))
        self.play(Write(word2))
        self.play(Write(word3))
        self.play(Write(word4))
        self.play(Write(word5))
        self.wait(2)
        self.play(Transform(sen1,sen3))
        self.wait(1.5)
        self.play(Transform(sen1,sen4))
        self.wait(1.5)
        self.play(Transform(sen1,sen5))
        self.wait(2)
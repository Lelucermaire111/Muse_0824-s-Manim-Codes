from manimlib.imports import *

class BeginAnimation(Scene):
    def construct(self):
        sentence01 = TextMobject("之前我们介绍过使复数变得非常精妙的欧拉公式：",color = BLUE).scale(0.8).to_edge(UP)
        equation1 = TextMobject("$$e^{ix}=\\cos x+i\\sin x$$", color = RED).next_to(sentence01, DOWN)
        sentence02 = TextMobject("今天让我们认识拓扑学里面的欧拉公式：", color = BLUE).scale(0.8).next_to(equation1, DOWN)
        equation2 = TextMobject("$$V+F-E=2$$", color = RED).next_to(sentence02, DOWN)
        self.play(Write(sentence01), run_time = 1.5)
        self.wait(1.5)
        self.play(Write(equation1), run_time = 1.5)
        self.wait(2)
        self.play(Write(sentence02), run_time = 1.5)
        self.wait(1.5)
        self.play(Write(equation2),run_time = 1.5)
        self.wait(2)
        sentence03 = TextMobject("对于一个多面体，它的顶点数$V$,面数$F$,棱数$E$，有着以上这样的关系", color = GREEN).scale(0.8).next_to(equation2, DOWN)
        sentence04 = TextMobject("如果你不相信，You can check it!", color = GREEN).scale(0.8).next_to(sentence03, DOWN)
        self.play(Write(sentence03), run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sentence04), run_time = 1.5)
        self.wait(1.5)



class ThreeD(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position":{
            "phi": 60*DEGREES,
            "theta": 90*DEGREES,
            "distance":50,
            "gamma":0,
        },
    }
    def construct(self):
        self.set_camera_to_default_position()
        self.wait(2)
        point1 = np.array([3,0,-1])
        point2 = np.array([-3,3,-1])
        point3 = np.array([-3,-3,-1])
        point4 = np.array([0,0,3])
        triangle1 = Polygon(point1, point2, point3,fill_color = BLUE, color = BLACK, fill_opacity = 0.5 )
        triangle2 = Polygon(point1, point2, point4,fill_color = BLUE, color = BLACK, fill_opacity = 0.5 )
        triangle3 = Polygon(point1, point3, point4,fill_color = BLUE, color = BLACK, fill_opacity = 0.5 )
        triangle4 = Polygon(point2, point3, point4,fill_color = BLUE, color = BLACK, fill_opacity = 0.5 )
        line1 = Line(point1, point2, color = WHITE)
        line2 = DashedLine(point1, point3, color = WHITE, dash_length = 0.3)
        line3 = Line(point1, point4, color = WHITE)
        line4 = Line(point2, point3, color = WHITE)
        line5 = Line(point2, point4, color = WHITE)
        line6 = Line(point3, point4, color = WHITE)
        added_line = Line(point1, point3, color = BLUE, fill_opacity = 0.5)
        pyramid = VGroup( triangle4, triangle2, triangle3, triangle1,added_line, line1, line2, line3, line4, line5, line6)
        self.play(ShowCreation(pyramid), run_time = 2)
        self.wait(3)
        self.play(FadeOut(pyramid))
        self.set_camera_orientation(theta = 120*DEGREES)
        cube = Cube(fill_color = BLUE, stroke_width = 2, stroke_color =WHITE, side_length = 4)
        self.play(ShowCreation(cube), run_time = 2)
        self.wait(3)
        self.play(FadeOut(cube))
        p1 = np.array([3,-3,-1])
        p2 = np.array([-3,3,-1])
        p3 = np.array([-3,-3,-1])
        p4 = np.array([3,3,-1])
        p5 = np.array([2,2,1])
        p6 = np.array([-2,2,1])
        p7 = np.array([2,-2,1])
        p8 = np.array([-2,-2,1])
        d1 = Sphere(fill_color = BLUE).scale(0.05).move_to(p1)
        d2 = Sphere(fill_color = BLUE).scale(0.05).move_to(p2)
        d3 = Sphere(fill_color = BLUE).scale(0.05).move_to(p3)
        d4 = Sphere(fill_color = BLUE).scale(0.05).move_to(p4)
        d5 = Sphere(fill_color = BLUE).scale(0.05).move_to(p5)
        d6 = Sphere(fill_color = BLUE).scale(0.05).move_to(p6)
        d7 = Sphere(fill_color = BLUE).scale(0.05).move_to(p7)
        d8 = Sphere(fill_color = BLUE).scale(0.05).move_to(p8)
        dot_group = VGroup(d1, d2, d3, d4, d5, d6, d7, d8)
        l1 = Line(p1,p4,color = BLUE)
        l2 = Line(p1,p3,color = BLUE)
        l3 = Line(p2,p3,color = BLUE)
        l4 = Line(p2,p4,color = BLUE)
        l5 = Line(p1,p7,color = BLUE)
        l6 = Line(p2,p6,color = BLUE)
        l7 = Line(p3,p8,color = BLUE)
        l8 = Line(p4,p5,color = BLUE)
        l9 = Line(p5,p6,color = BLUE)
        l10 = Line(p5,p7,color = BLUE)
        l11 = Line(p6,p8,color = BLUE)
        l12 = Line(p7,p8,color = BLUE)
        linegroup = VGroup(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12)
        lengtai = VGroup(dot_group, linegroup)
        self.play(ShowCreation(lengtai), run_time = 3)
        self.wait(3)
        self.play(FadeOut(lengtai), run_time = 2)

class Part01(Scene):

    def construct(self):
        sentence01 = TextMobject("我相信你自己已经验证了一些多面体，并发现欧拉公式是成立的", color = BLUE).scale(0.8).to_edge(UP)
        self.play(Write(sentence01), run_time = 1.5)
        self.wait(1.5)
        sentence02 = TextMobject("但是...","我们如何去证明它？", color = RED).scale(0.8).next_to(sentence01, DOWN)
        self.play(Write(sentence02[0]), run_time = 1)
        self.play(ShowIncreasingSubsets(sentence02[1]), run_time = 3)
        self.wait(2)
        sentence03 = TextMobject("不妨暂停下来想一想！", color = BLUE).scale(0.8).next_to(sentence02, DOWN)
        self.play(Write(sentence03), run_time = 1)
        self.wait(1.5)

class ThreeD_2(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position":{
            "phi": 60*DEGREES,
            "theta": 90*DEGREES,
            "distance":50,
            "gamma":0,
        },
    }
    def construct(self):
        self.set_camera_to_default_position()
        self.wait(2)
        point1 = np.array([3, 0, -1])
        point2 = np.array([-3, 3, -1])
        point3 = np.array([-3, -3, -1])
        point4 = np.array([0, 0, 3])
        line1 = Line(point1, point2, color = BLUE)
        line2 = Line(point1, point3, color = BLUE)
        line3 = Line(point1, point4, color = BLUE)
        line4 = Line(point2, point3, color = BLUE)
        line5 = Line(point2, point4, color = BLUE)
        line6 = Line(point3, point4, color = BLUE)
        pyramid = VGroup(line1,line2,line3,line4,line5,line6)
        self.play(ShowCreation(pyramid), run_time = 3)
        self.wait(1.5)
        for i in range(0,10):
            x = random.uniform(-5,5)
            y = random.uniform(-5,5)
            z = random.uniform(0,5)
            point4 = np.array([x,y,z])
            l3 = Line(point1, point4, color=BLUE)
            l5 = Line(point2, point4, color=BLUE)
            l6 = Line(point3, point4, color=BLUE)
            x = VGroup(line1, line2, l3, line4, l5, l6)
            self.play(ReplacementTransform(pyramid, x), run_time = 1)
            self.wait(0.3)
            pyramid = x
        self.play(FadeOut(pyramid))
        self.wait(1)

class Part02(ThreeDScene):
    CONFIG = {
        "default_angled_camera_position":{
            "phi": 60*DEGREES,
            "theta": -90*DEGREES,
            "distance":50,
            "gamma":0,
        },
    }
    def construct(self):
        sentence01 = TextMobject("看了刚才这段动画，不知道有没有激发一下你的灵感呢？", color = BLUE).scale(0.8).to_edge(UP)
        self.play(Write(sentence01), run_time = 1.5)
        self.wait(1)
        sentence02 = TextMobject("在刚才的动画中，多面体的顶点、棱、面的数量并未发生改变", color = BLUE).scale(0.8).next_to(sentence01, DOWN)
        sentence03 = TextMobject("也就是说，你可以将它想象成橡皮膜之类的东西，那么我们也自然可以", color = BLUE).scale(0.8).next_to(sentence02, DOWN)
        sentence04 = TextMobject("将它压到一个平面上！", color = RED).next_to(sentence03, DOWN)
        self.play(Write(sentence02), run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sentence03), run_time = 1.5)
        self.wait(1.5)
        self.play(ShowIncreasingSubsets(sentence04), run_time = 2)
        self.play(Indicate(sentence04, color = RED))
        self.wait(2)
        point1 = np.array([0,0,0])
        point2 = np.array([0,2,0])
        point3 = np.array([-2.1,-1.5, 0])
        point4 = np.array([2.1,-1.5,0])
        d1 = Dot(point1)
        d2 = Dot(point2)
        d3 = Dot(point3)
        d4 = Dot(point4)
        l1 = Line(point1, point2, color = BLUE)
        l2 = Line(point1, point3, color = BLUE)
        l3 = Line(point1, point4, color = BLUE)
        l4 = Line(point2, point3, color = BLUE)
        l5 = Line(point2, point4, color = BLUE)
        l6 = Line(point3, point4, color = BLUE)
        line_group = VGroup(l1,l2,l3,l4,l5,l6)
        dot_group = VGroup(d1,d2,d3,d4)
        tu = VGroup(dot_group,line_group)
        tu.shift(DOWN*2)
        self.play(ShowCreation(tu), run_time = 2)
        self.wait(3)
        text_group = VGroup(sentence01, sentence02, sentence03, sentence04)
        self.play(FadeOut(text_group))
        sentence05 = TextMobject("我们这样做并没有改变原有的顶点、棱、面之间的关系", color = BLUE).scale(0.8).to_edge(UP)
        sentence06 = TextMobject("顶点与棱可以很好地对应到平面上，","由于压到平面内，原有的面变成了平面图上线所构成的闭合区域", color = BLUE).scale(0.8).next_to(sentence05, DOWN)
        sentence07 = TextMobject("而区域的数目也要比面的数目少一个", color = BLUE).scale(0.8).next_to(sentence06, DOWN)
        ll1 = Line(point4, np.array([0,0,3]),color = RED)
        ll2 = Line(point2, np.array([0,0,3]), color = RED)
        ll3 = Line(point3, np.array([0,0,3]), color = RED)
        ll4 = Line(point4, point2, color = RED)
        ll5 = Line(point4, point3, color = RED)
        ll6 = Line(point3, point2, color = RED)
        tu2 = VGroup(ll1,ll2,ll3,ll4,ll5,ll6)
        tu2.shift(DOWN*2+LEFT*4)
        self.play(Write(sentence05), run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sentence06[0]), run_time = 1)
        self.wait(1.5)
        self.play(Write(sentence06[1]), run_time = 1.5)
        self.wait(1)
        dt = 1/15
        phi_0 = 0
        for i in range(30):
            phi_0 += 2 * DEGREES
            self.set_camera_orientation(phi = phi_0, theta = -90*DEGREES )
            self.wait(dt)
        self.wait(2)
        self.play(ShowCreation(tu2))
        self.wait(1)
        self.play(ReplacementTransform(tu2, tu), run_time = 2)
        self.wait(2)
        for i in range(30):
            phi_0 -= 2 * DEGREES
            self.set_camera_orientation(phi = phi_0, theta = -90*DEGREES )
            self.wait(dt)
        self.play(Write(sentence07), run_time = 1.5)
        self.wait(1.5)
        text_group2=VGroup(sentence05, sentence06,sentence07)
        self.play(FadeOut(text_group2), run_time = 1)
        sentence08 = TextMobject("让我们整理一下思路，所以现在我们的目标变成：", color = BLUE).scale(0.8).to_edge(UP)
        equation = TextMobject("$$V+K-E=1$$", color = RED).next_to(sentence08, DOWN)
        sentence09 = TextMobject("$K$为平面图中闭合区域的数量", color = BLUE).scale(0.8).next_to(equation, DOWN)
        self.play(Write(sentence08), run_time = 1.5)
        self.wait(1.5)
        self.play(DrawBorderThenFill(equation), run_time = 1.5)
        self.wait(1.5)
        self.play(Write(sentence09), run_time = 1.5)
        self.wait(2)
        text_group3=VGroup(sentence08,equation,sentence09)
        self.play(FadeOut(text_group3), run_time = 2)
        self.wait()

class Part03(Scene):

    def construct(self):
        point1 = np.array([0,0,0])
        point2 = np.array([0,2,0])
        point3 = np.array([-2.1,-1.5, 0])
        point4 = np.array([2.1,-1.5,0])
        d1 = Dot(point1)
        d2 = Dot(point2)
        d3 = Dot(point3)
        d4 = Dot(point4)
        l1 = Line(point1, point2, color = BLUE)
        l2 = Line(point1, point3, color = BLUE)
        l3 = Line(point1, point4, color = BLUE)
        l4 = Line(point2, point3, color = BLUE)
        l5 = Line(point2, point4, color = BLUE)
        l6 = Line(point3, point4, color = BLUE)
        line_group = VGroup(l1,l2,l3,l4,l5,l6)
        dot_group = VGroup(d1,d2,d3,d4)
        tu = VGroup(dot_group,line_group)
        tu.shift(DOWN*2)
        self.add(tu)
        sentence01 = TextMobject("思考这样一件事，拆掉一条线", color = BLUE).scale(0.8).to_edge(UP)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(FadeOut(l4), run_time = 1)
        self.wait(1)
        sentence02 = TextMobject("与此同时，我们消灭了一个区域", color = BLUE).scale(0.8).next_to(sentence01, DOWN)
        self.play(Write(sentence02), run_time = 1)
        self.wait(2)
        sentence03 = TextMobject("然后我们可以继续这样做下去，直到区域全部被消灭", color = BLUE).scale(0.8).next_to(sentence02, DOWN)
        self.play(Write(sentence03), run_time = 2)
        self.wait(1.5)
        self.play(FadeOut(l5),run_time = 1)
        self.play(FadeOut(l6),run_time = 1)
        self.wait(2)
        text_group = VGroup(sentence01, sentence02, sentence03)
        self.play(FadeOut(text_group), run_time = 1)
        sentence04 = TextMobject("这时还剩下几条线呢？","$V-1$", color = GREEN).scale(0.8).to_edge(UP)
        sentence04[1].set_color(RED)
        tip1 = TextMobject("也就是顶点数目减一", color = BLUE).scale(0.6).next_to(sentence04, 0.8*DOWN)
        sentence05 = TextMobject("我们消灭了几条线呢？","$K$", color = GREEN).scale(0.8).next_to(sentence04, DOWN)
        sentence05[1].set_color(RED)
        tip2 = TextMobject("也就是区域的数量", color = BLUE).scale(0.6).next_to(sentence05, 0.8*DOWN)
        sentence06 = TextMobject("原来一共有几条线呢？","$E$", color = GREEN).scale(0.8).next_to(sentence05,DOWN)
        sentence06[1].set_color(RED)
        tip3 = TextMobject("也就是棱的数量", color = BLUE).scale(0.6).next_to(sentence06,0.8*DOWN)
        self.play(Write(sentence04[0]),run_time = 1)
        self.wait(1)
        self.play(ShowPassingFlashAround(l1))
        self.play(ShowPassingFlashAround(l2))
        self.play(ShowPassingFlashAround(l3))
        self.play(ShowCreationThenFadeOut(tip1), run_time = 2)
        self.play(DrawBorderThenFill(sentence04[1]),run_time = 1)
        self.wait(1)
        self.play(Write(sentence05[0]),run_time = 1)
        self.wait(1)
        self.play(ShowCreationThenFadeOut(tip2), run_time = 2)
        self.play(DrawBorderThenFill(sentence05[1]),run_time = 1)
        self.wait(1)
        self.play(Write(sentence06[0]),run_time = 1)
        self.wait(1)
        self.play(ShowCreationThenFadeOut(tip3),run_time = 2)
        self.play(Write(sentence06[1]))
        self.wait(1)
        equation = TextMobject("So...","$E=V-1+K$", color = RED).next_to(sentence06,DOWN)
        self.play(Write(equation[0]), run_time = 1)
        self.wait(1)
        self.play(Write(equation[1]), run_time = 2)
        self.wait(1.5)
        sentence07 = TextMobject("BINGO!!!", color = BLUE).next_to(equation,DOWN)
        self.play(Write(sentence07), run_time = 1)
        self.wait(1.5)
        text_group2 = VGroup(sentence04,sentence05,sentence06,sentence07,equation)
        tu1 = VGroup(dot_group,l1,l2,l3)
        self.play(FadeOut(text_group2),FadeOut(tu1), run_time = 2)
        self.wait(1)

class Part04(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position":{
            "phi": 60*DEGREES,
            "theta": -70*DEGREES,
            "distance":50,
            "gamma":0,
        },
    }
    def construct(self):
        sentence01 = TextMobject("欧拉公式适用的多面体不可以无限推广", color = BLUE).scale(0.8).to_edge(UP)
        sentence02 = TextMobject("让我们来看这样一个例子", color = BLUE).scale(0.8).next_to(sentence01,DOWN)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(sentence02, run_time = 1))
        self.wait(1)
        self.play(FadeOut(sentence01),FadeOut(sentence02),run_time = 1)
        self.set_camera_to_default_position()
        cube_yellow = Cube(fill_color = YELLOW, stroke_width = 2, stroke_color = WHITE)
        cube_green = Cube(fill_color = YELLOW, stroke_width = 2).scale([0.5,0.5,0.5]).shift(OUT+UP)
        self.play(ShowCreation(cube_yellow),ShowCreation(cube_green), run_time = 2)
        self.wait(2)
        self.play(FadeOut(cube_yellow), FadeOut(cube_green))
        self.set_camera_orientation(phi = 0, theta = -90*DEGREES)
        sentence03 = TextMobject("你可以很容易地验证这个多面体并不满足欧拉公式", color = RED).scale(0.8).to_edge(UP)
        sentence04 = TextMobject("从刚才的证明过程中我们也看到要求各个顶点是由棱相连的", color = RED).scale(0.8).next_to(sentence03,DOWN)
        self.play(Write(sentence03), run_time = 1.5)
        self.wait(1)
        self.play(Write(sentence04, run_time = 1.5))
        self.wait(1)
        self.play(FadeOut(sentence03),FadeOut(sentence04),run_time = 1)
        sentence05 = TextMobject("事实上，我们刚才的证明已经用到了一些简单的图论的知识，比如连通图、树等概念", color = BLUE).scale(0.8).to_edge(UP)
        sentence06 = TextMobject("同时，也提醒我们不妨把问题转换一下再来看！", color = BLUE).scale(0.8).next_to(sentence05, DOWN)
        sentence07 = TextMobject("从拓扑学一角窥见它的美妙！", color = BLUE).scale(0.8).next_to(sentence06, DOWN)
        self.play(Write(sentence05),run_time = 2)
        self.wait(2)
        self.play(Write(sentence06),run_time = 1)
        self.wait(1)
        self.play(DrawBorderThenFill(sentence07),run_time = 1.5)
        self.wait(1)

class Plot(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position":{
            "phi": 60*DEGREES,
            "theta": 60*DEGREES,
            "distance":50,
            "gamma":0,
        },
    }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        self.add(axes)
        surface = ParametricSurface(lambda u, v: np.array([u, v, np.sin(v**2+u**2)]),
                                     u_min = -PI**0.5, u_max = PI**0.5, v_min = -PI**0.5, v_max = PI**0.5,resolution = (120,120))
        self.add(surface)
        self.wait(5)
import cv2
from manimlib import *
import numpy as np
from scipy import signal
class BeginAnimation(Scene):
    def construct(self):
        source = Text("What is Convolution", height = 0.8)
        target = Text("by Muse_0824", height = 1)
        self.play(Write(source), run_time = 2)
        self.wait()
        kw = {"run_time":2, "path_arc": PI/3}
        self.play(Transform(source, target, **kw))
        self.wait()

class Outline(Scene):
    def construct(self):
        title = Text("Outline").scale(1.5).to_edge(UL)
        part1 = Text("* The Concept of Convolution").next_to(title,4*DOWN).align_to(title,LEFT).shift(RIGHT)
        part2 = Text("* Bonus Question").next_to(part1,3*DOWN).align_to(part1,LEFT)
        part3 = Text("* Convolution in CV").next_to(part2,3*DOWN).align_to(part2,LEFT)
        self.play(Write(title))
        self.play(Write(part1),run_time = 1.5)
        self.wait(3)
        self.play(Write(part2),run_time = 1.5)
        self.wait(4)
        self.play(Write(part3),run_time = 1.5)
        self.wait(3)


class Part1(Scene):
    def construct(self):
        term = Text('Convolution Sum:')
        definition = Tex("y[n]= x[n]*h[n] = \sum_{k=-\infty}^{+\infty}x[k]h[n-k]")
        term.shift(UP*3).shift(LEFT*3)
        definition.next_to(term,DOWN * 1.5).shift(RIGHT)
        rec = SurroundingRectangle(definition)
        self.play(Write(term), run_time = 2)
        self.wait()
        self.play(Write(definition), run_time = 3)
        self.play(ShowCreation(rec))
        self.wait()
        delta = Tex(" \delta [n]= \\begin{cases} 1,\quad n = 0 \\\\ 0, \quad else \end{cases}" )
        delta.next_to(definition, DOWN*1.5).shift(LEFT).align_to(definition,LEFT)
        self.play(Write(delta))
        self.wait(2)
        axes1 = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-5, 5),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(0, 1.5, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            width=8,
            height = 4,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        axes1.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        axes1.shift(RIGHT*2.2)
        self.play(ShowCreation(axes1))
        dot = Dot(color=RED)
        dot.move_to(axes1.c2p(0, 1))
        f_always(dot.move_to, lambda: axes1.c2p(0, 1))
        self.play(FadeIn(dot,scale=0.5))
        v_line = always_redraw(lambda: axes1.get_v_line(dot.get_bottom(),line_func = Line,color = RED))

        self.play(
            ShowCreation(v_line)
        )

        self.play(
            axes1.animate.scale(0.8).to_corner(DR).shift(UP),
            run_time=2,
        )

        ques = Text("Question:")
        question = Tex("x[n]*\delta[n]=?")
        ques.next_to(delta,DOWN).align_to(term,LEFT)
        question.next_to(ques,DOWN*1.4).align_to(delta,LEFT)
        self.play(Write(ques))
        self.wait()
        self.play(Write(question))
        self.wait(2)

        question_ = Tex("\sum_{k=-\infty}^{+\infty}x[k]\delta[n-k]=?").next_to(ques,DOWN*1.2).align_to(question,LEFT)
        self.play(TransformMatchingShapes(question,question_))
        self.wait()

        ans = Tex("\sum_{k=-\infty}^{+\infty}x[k]\delta[n-k]=x[n]").next_to(ques,DOWN*1.2).align_to(question,LEFT)
        kw = {"run_time": 2, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(question_,ans,**kw))
        self.wait()

class Part2(Scene):
    def construct(self):
        axes1 = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-5, 5),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-1.2, 1.2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            width=10,
            height = 2.2,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        axes1.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        axes1.shift(UP*2)
        self.play(ShowCreation(axes1))
        Dot_and_line = VGroup()
        for i in range(-5,5,1):
            Dot_and_line.add(Dot(color=RED).move_to(axes1.c2p(i,np.sin(i))))
            Dot_and_line.add((axes1.get_v_line(Dot_and_line[2*(i+5)].get_bottom(), line_func=Line, color=RED)))
        self.play(ShowCreation(Dot_and_line),run_time = 5)

        axes2 = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(-5, 5),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-1.2, 1.2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            width=10,
            height=2.2,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        axes2.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        axes2.shift(DOWN)
        self.play(ShowCreation(axes2))
        dot = Dot(color = GREEN).move_to(axes2.c2p(0,1))
        line = always_redraw(lambda: axes2.get_v_line(dot.get_bottom(), line_func=Line, color=GREEN))
        self.play(ShowCreation(line))
        self.wait()
        conv_sum = Tex("x[n]*\delta[n]=\sum_{k=-\infty}^{+\infty}x[k]\delta[n-k]").shift(RIGHT*3).shift(UP*3.5)
        conv_sum.set_height(0.7)
        self.play(Write(conv_sum))
        self.wait()
        for i in range (-5, 5, 1):
            self.play(dot.animate.move_to(axes2.c2p(i,1)),run_time = 0.3)
            rec = SurroundingRectangle(VGroup(Dot_and_line[2*(i+5)+1],line))
            rec.set_color(color = BLUE).set_opacity(opacity=0.3)
            self.play(VFadeInThenOut(rec))
            dot_ = Dot(color=YELLOW).move_to(axes2.c2p(i,np.sin(i)))
            run_time = 0.5
            if i == -5:
                run_time = 1
            self.play(ShowCreation(dot_),run_time = run_time)
            self.play(ShowCreation(axes2.get_v_line(dot_.get_bottom(),line_func = Line, color = YELLOW)), run_time = run_time)
        self.wait()
        #筛选性质
        conv_sum_ = Tex("x[n]=\sum_{k=-\infty}^{+\infty}x[k]\delta[n-k]").shift(RIGHT*3).shift(UP*3.5).set_height(0.7)
        self.play(Transform(conv_sum,conv_sum_))

def conv_op(x,y):
    res = []
    l = len(x)
    for i in range(0,l):
        temp = 0
        for j in range(0,l):
            if(i-j>=0):
               temp += x[j]*y[i-j]
        res.append(temp)
    return res

class Part3(Scene):
    def construct(self):
        axes1 = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(0, 10),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-1.2, 1.2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            width=10,
            height=2.2,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        axes1.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        axes1.shift(UP * 2)
        self.play(ShowCreation(axes1))
        Dot_and_line = VGroup()
        for i in range(0, 5, 1):
            Dot_and_line.add(Dot(color=RED).move_to(axes1.c2p(i, np.sin(i))))
            Dot_and_line.add((axes1.get_v_line(Dot_and_line[2 * (i)].get_bottom(), line_func=Line, color=RED)))
        self.play(ShowCreation(Dot_and_line), run_time=2)

        axes2 = Axes(
            # x-axis ranges from -1 to 10, with a default step size of 1
            x_range=(0, 10),
            # y-axis ranges from -2 to 2 with a step size of 0.5
            y_range=(-1.2, 1.2, 0.5),
            # The axes will be stretched so as to match the specified
            # height and width
            width=10,
            height=2.2,
            # Axes is made of two NumberLine mobjects.  You can specify
            # their configuration with axis_config
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # Alternatively, you can specify configuration for just one
            # of them, like this.
            y_axis_config={
                "include_tip": False,
            }
        )
        axes2.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        axes2.shift(DOWN)
        self.play(ShowCreation(axes2))
        linear = VGroup()
        for i in range(0, 5, 1):
            linear.add(Dot(color=GREEN).move_to(axes2.c2p(i, 1/5*(i))))
            linear.add((axes2.get_v_line(linear[2 * (i)].get_bottom(), line_func=Line, color=GREEN)))
        self.play(ShowCreation(linear), run_time=3)
        inv_linear = VGroup()
        for i in range(-4, 1, 1):
            inv_linear.add(Dot(color=GREEN).move_to(axes2.c2p(i, -1/5*(i))))
            inv_linear.add((axes2.get_v_line(inv_linear[2 * (i+4)].get_bottom(), line_func=Line, color=GREEN)))
        kw = {"run_time": 1, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(linear,inv_linear,**kw))
        self.wait(3)
        res = VGroup()

        x = [0]*11
        y = [0]*11
        for i in range(0,5,1):
            x[i]=(math.sin(i))
            y[i]=(1/5*i)
        res_num = conv_op(x,y)

        for i in range(0,10,1):
            res.add(Dot(color=YELLOW).move_to(axes2.c2p(i,res_num[i])))
            res.add(axes2.get_v_line(res[2*i].get_bottom(),line_func = Line, color = YELLOW))

        for i in range(0,10,1):
            if(i != 0):
                self.play(inv_linear.animate.shift(RIGHT))
            rec = VGroup()
            for j in range(0,5,1):
                if j <= i and 4-i+j>=0:
                    rec.add(SurroundingRectangle(VGroup(inv_linear[2*(4-i+j)+1],Dot_and_line[2*j+1]),color = BLUE,opacity = 0.3))
            run_time = 0.3
            if(i==0 and i== 1):
                run_time = 1
            self.play(ShowCreation(rec),run_time = run_time)
            self.play(ReplacementTransform(rec,res[2*(i)+1]),run_time = run_time)
            self.play(ShowCreation(res[2*(i)]),run_time = 0.1)
        self.wait()
        #物理阐释
        #卷积动画


class Part4(Scene):
    def construct(self):
        Title = Text("Bonus Question About Signal and Systems:")
        Title.to_edge(UL)
        self.play(Write(Title))
        system = Text(""" 
                        A linear time-
                        invariant system 
                        """)
        rec = SurroundingRectangle(system).set_color(BLUE).set_opacity(0.5).scale(1.3)
        arrow1 = Arrow().move_to(rec.get_left()).set_color(RED).shift(LEFT)
        arrow2 = Arrow().move_to(rec.get_right()).set_color(RED).shift(RIGHT)
        self.play(ShowCreation(rec))
        self.play(Write(system))

        self.wait(3)
        self.play(ShowCreation(arrow1))
        self.play(ShowCreation(arrow2))

        #linear
        input_1 = Tex("x_1[n]",color = RED).next_to(arrow1,UP).align_to(arrow1,LEFT)
        input_2 = Tex("x_2[n]",color = GREEN).next_to(arrow1,DOWN).align_to(arrow1,LEFT)
        output_1 = Tex("y_1[n]",color = RED).next_to(arrow2,UP).align_to(arrow2,RIGHT)
        output_2 = Tex("y_2[n]",color = GREEN).next_to(arrow2,DOWN).align_to(arrow2,RIGHT)
        self.play(Write(input_1),Write(output_1),run_time = 2)
        self.wait()
        self.play(Write(input_2),Write(output_2),run_time = 2)
        self.wait()
        input_3 = Tex("c_1 x_1[n]+c_2 x_2[n]",color = YELLOW).next_to(arrow1,UP).align_to(arrow1,LEFT).shift(LEFT)
        output_3 = Tex("c_1 y_1[n]+c_2 y_2[n]",color = YELLOW).next_to(arrow2,UP).align_to(arrow2,RIGHT).shift(RIGHT)
        vg1 = VGroup(input_1,input_2)
        vg2 = VGroup(output_1,output_2)
        self.play(ReplacementTransform(vg1,input_3),ReplacementTransform(vg2,output_3))
        linearity = Tex("Linearity: x_1[n]+x_2[n]\\rightarrow y_1[n]+y_2[n]").scale(0.9).next_to(Title,DOWN).align_to(Title,LEFT).shift(RIGHT)
        self.play(Write(linearity))
        self.wait(3)
        self.play(FadeOut(input_3),FadeOut(output_3))

        #time-invariant
        input_4 = Tex("x[n]",color = RED).next_to(arrow1,UP).align_to(arrow1,LEFT)
        output_4 = Tex("y[n]",color = RED).next_to(arrow2,UP).align_to(arrow2,RIGHT)

        input_5 = Tex("x[n-n_0]",color = BLUE).next_to(arrow1,UP).align_to(arrow1,LEFT).shift(LEFT*0.5)
        output_5 = Tex("y[n-n_0]",color = BLUE).next_to(arrow2,UP).align_to(arrow2,RIGHT).shift(RIGHT*0.5)
        time_invariance = Tex("Time-invariance:x[n-n_0]\\rightarrow y[n-n_0]").scale(0.9).next_to(linearity,DOWN).align_to(linearity,LEFT)
        self.play(Write(input_4),Write(output_4),run_time = 2)
        self.wait()
        self.play(Transform(input_4,input_5),Transform(output_4,output_5),run_time = 2)
        self.wait()
        self.play(Write(time_invariance))
        self.play(FadeOut(input_4), FadeOut(output_4))
        self.wait()

        #根据以上性质
        d = Tex("\delta[n]").set_color(BLUE).next_to(arrow1,UP).align_to(arrow1,LEFT)
        d_out = Tex("h[n]").set_color(BLUE).next_to(arrow2,UP).align_to(arrow2,RIGHT)
        self.play(Write(d),Write(d_out),run_time = 2)
        self.play()
        x = Tex("x[n]=\sum_{k=-\infty}^{+\infty}x[k]\delta[n-k]").set_color(RED).align_to(arrow1,LEFT).next_to(arrow1,DOWN).scale(0.8)
        x_out = Tex("y[n]=\sum_{k=-\infty}^{+\infty}x[k]h[n-k]").set_color(RED).align_to(arrow2,RIGHT).next_to(arrow2,DOWN).scale(0.8)
        hint = Text("According to the linearity and time-incovariance...",height = 0.8).shift(DOWN*2)
        self.play(Write(x))
        self.wait(2)
        self.play(FadeIn(hint))
        self.wait(2)
        self.play(FadeOut(hint))
        self.play(Write(x_out))
        self.wait()

        h = Tex("h[n]").shift(DOWN*2)
        arrow3 = Arrow(system.get_bottom(),h.get_center(),color = RED)
        self.play(ShowCreation(arrow3))
        self.play(Write(h))
        self.wait()

        filter = Text("Filter").scale(1.2)
        filter_1 = Text("Highpass Filter")
        filter_2 = Text("Lowpass Filter")
        am = Text("Amplifier")
        self.play(TransformMatchingShapes(system, filter))
        self.wait(0.5)
        self.play(TransformMatchingShapes(filter, filter_1))
        self.wait(0.5)
        self.play(TransformMatchingShapes(filter_1, filter_2))
        self.wait(0.5)
        self.play(TransformMatchingShapes(filter_2,am))
        self.wait(0.5)
        self.play(TransformMatchingShapes(am, system))
        self.wait()


class Part5(Scene):
    def construct(self):
        # gray = (b + r + g)/3
        # imgHeight = 30
        # imgWidth = 30
        # step = 5/imgWidth
        # dst = np.random.random((imgHeight, imgWidth))
        #
        # img_matrix = VGroup()
        # for i in range(imgHeight):
        #     for j in range(imgWidth):
        #         rec = Rectangle(width=step,height=step).set_color(BLACK).set_opacity(dst[i,j])
        #         rec.move_to(np.array([-6+step*j,3-step*i,0]))
        #         img_matrix.add(rec)
        # self.play(ShowCreation(img_matrix))
        # self.wait()

        img = cv2.imread('github_logo_.jpg', 1)
        imgHeight, imgWidth, imgDeep = img.shape
        img_matrix = VGroup()
        step = 5 / imgWidth
        dst = np.zeros((imgHeight, imgWidth), np.uint8)

        for i in range(imgHeight):
            for j in range(imgWidth):
                (b, g, r) = img[i, j]
                gray = (int(b) + int(g) + int(r)) / 3
                dst[i, j] = np.uint8(gray)
                rec = Rectangle(width=step,height=step).set_color(BLACK).set_opacity(dst[i,j]/255)
                rec.move_to(np.array([-6 + step * j, 3 - step * i, 0]))
                img_matrix.add(rec)
        self.play(ShowCreation(img_matrix))
        self.wait()

        filter = np.array([[0,-1,0],
                          [-1,4,-1],
                          [0,-1,0]])
        text_filter = Tex("\\begin{bmatrix} 0 & -1 & 0 \\\\ -1 & 4 & -1 \\\\ 0 & -1 & 0 \end{bmatrix}")
        text_filter.shift(UP*2.5)
        text_filter.set_color(BLUE)
        filter_name = Text("Filter").next_to(text_filter,DOWN).scale(0.8)
        self.play(Write(text_filter))
        self.play(Write(filter_name))
        self.wait()
        res = signal.convolve2d(dst,filter,boundary='symm',mode='same')
        img_matrix_ = VGroup()
        for i in range(imgHeight):
            for j in range(imgWidth):
                rec = Rectangle(width=step,height=step).set_color(BLACK).set_opacity(abs(res[i,j])/255)
                rec.move_to(np.array([-6+step*j,3-step*i,0]))
                img_matrix_.add(rec)
        img_matrix_.shift(RIGHT*7)
        self.play(TransformFromCopy(img_matrix,img_matrix_),run_time = 3)
        self.wait()
class Part6(Scene):
    def construct(self):
        img = cv2.imread('github_logo_.jpg', 1)
        imgHeight, imgWidth, imgDeep = img.shape
        img_matrix = VGroup()
        step = 5 / imgWidth
        dst = np.zeros((imgHeight, imgWidth), np.uint8)

        for i in range(imgHeight):
            for j in range(imgWidth):
                (b, g, r) = img[i, j]
                gray = (int(b) + int(g) + int(r)) / 3
                dst[i, j] = np.uint8(gray)
                rec = Rectangle(width=step,height=step).set_color(BLACK).set_opacity(dst[i,j]/255)
                rec.move_to(np.array([-6 + step * j, 3 - step * i, 0]))
                img_matrix.add(rec)
        self.play(ShowCreation(img_matrix))
        self.wait()

        filter = np.array([[-1,-2,-1],
                          [0,0,0],
                          [1,2,1]])
        text_filter = Tex("\\begin{bmatrix} -1 & -2 & -1 \\\\ 0 & 0 & 0 \\\\ 1 & 2 & 1 \end{bmatrix}")
        text_filter.shift(UP*2.5)
        text_filter.set_color(BLUE)
        filter_name = Text("Filter").next_to(text_filter,DOWN).scale(0.8)
        self.play(Write(text_filter))
        self.play(Write(filter_name))
        self.wait()
        res = signal.convolve2d(dst,filter,boundary='symm',mode='same')
        img_matrix_ = VGroup()
        for i in range(imgHeight):
            for j in range(imgWidth):
                rec = Rectangle(width=step,height=step).set_color(BLACK).set_opacity(abs(res[i,j])/255)
                rec.move_to(np.array([-6+step*j,3-step*i,0]))
                img_matrix_.add(rec)
        img_matrix_.shift(RIGHT*7)
        self.play(TransformFromCopy(img_matrix,img_matrix_),run_time = 3)
        self.wait()
class Part7(Scene):
    def construct(self):
        filter = np.array([[1/9,1/9,1/9],
                          [1/9,1/9,1/9],
                          [1/9,1/9,1/9]])

        filter_size = 3
        step = 0.5
        fil_vg = VGroup()
        for i in range(3):
            for j in range(3):
                rec = Rectangle(width=0.5,height=0.5).set_color(RED).set_opacity(0.8).move_to(np.array([i*step,j*step,0]))
                fil_vg.add(rec)
        self.play(ShowCreation(fil_vg))
        word = Text("Filter").next_to(fil_vg,DOWN)
        self.play(Write(word))
        self.wait()
        self.play(FadeOut(word))

        imgHeight = 10
        imgWidth = 10
        step = 5/imgWidth
        dst = np.random.random((imgHeight, imgWidth))

        img_matrix = VGroup()
        for i in range(imgHeight):
            for j in range(imgWidth):
                rec = Rectangle(width=step,height=step).set_color(BLUE).set_opacity(dst[i,j])
                rec.move_to(np.array([-6+step*j,3-step*i,0]))
                img_matrix.add(rec)
        self.play(ShowCreation(img_matrix))
        self.wait()

        res = signal.convolve2d(dst, filter, boundary='symm', mode='same')
        img_matrix_ = VGroup()
        for i in range(imgHeight):
            for j in range(imgWidth):
                rec = Rectangle(width=step, height=step).set_color(BLUE).set_opacity(abs(res[i, j]))
                rec.move_to(np.array([-6 + step * j, 3 - step * i, 0]))
                img_matrix_.add(rec)
        img_matrix_.shift(RIGHT * 7)

        for i in range(1,imgHeight-1,1):
            for j in range(1,imgWidth-1,1):
                run_time = 0.005
                if(i==1 and (j <= 5 )):
                    run_time = 1
                self.play(fil_vg.animate.move_to(np.array([-6 + step * j, 3 - step * i, 0])),run_time = run_time)
                line = VGroup()
                x = -6 + step * (j-1)
                y = 3 - step * (i) + step
                for k in range(0,3):
                    for m in range(0,3):
                        line.add(Line(np.array([x+k*step,y-m*step,0]),np.array([x+7+step,y-step,0]),color = YELLOW)).set_opacity(0.2)
                if(i==1 and (j<=5)):
                    self.play(ShowCreation(line),run_time=run_time)
                self.play(ShowCreation(img_matrix_[i*imgWidth+j]),run_time = run_time)
        self.wait(3)
        self.play(ShowCreation(img_matrix_))
        self.wait()



class Part8(Scene):
    CONFIG = {
        'starsky':"starsky.jpg",
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        title1 = Text("Fully Connected")
        title2 = Text("Partially Connected")
        frame = self.camera.frame
        frame.set_euler_angles(
            phi= 45 * DEGREES, theta = -90*DEGREES, gamma = 90*DEGREES
        )
        starsky = ImageMobject(self.starsky).shift(IN*5).set_height(6)
        title1.next_to(starsky,UP).shift(RIGHT)
        title2.next_to(starsky,UP).shift(RIGHT)
        self.play(FadeIn(starsky))
        imgHeight = 4
        imgWidth = 6
        x_step = 0.6
        y_step = 0.4
        vec_vg = VGroup()
        for i in range(0,imgHeight+3,1):
            for j in range(0,imgWidth+1,1):
                vec_vg.add(Arrow(starsky.get_corner(UL)+RIGHT*j+DOWN*i,np.array([0,-1,5])).set_color(GREEN).set_opacity(0.5))
        self.play(ShowCreation(vec_vg))
        node = Sphere(radius = 0.3, color = GREEN,opacity = 1).move_to(np.array([0,-1,5]))
        self.play(ShowCreation(node))

        vec_vg_ = VGroup()
        for i in range(0,imgHeight+3,1):
            for j in range(0,imgWidth+1,1):
                vec_vg_.add(Arrow(starsky.get_corner(UL)+RIGHT*j+DOWN*i,np.array([0,1.5,5])).set_color(GREEN).set_opacity(0.5))
        self.play(ShowCreation(vec_vg_))
        node_ = Sphere(radius = 0.3, color = GREEN,opacity = 1).move_to(np.array([0,1.5,5]))
        self.play(ShowCreation(node_))
        self.play(Write(title1))
        x = (starsky.get_corner(UL))[0]
        y = (starsky.get_corner(UL))[1]
        print(starsky.get_corner(UL))

        x = x-2
        y = y-2

        vg_1 = VGroup()
        for k in range(0,3 ):
            for m in range(0, 3):
                rec = Rectangle(width=x_step, height=y_step).set_color(YELLOW).set_opacity(0.5)
                rec.move_to(np.array([x +0.5 + x_step * k, y - y_step * m, 0]))
                vg_1.add(rec)
                vg_1.add(Arrow(np.array([x + k * x_step, y - m * y_step, 0]), np.array([-2, 2, 5]),
                              ).set_color(YELLOW).set_opacity(0.5))
        node1 = Sphere(radius=0.3, color=YELLOW, opacity=1).move_to(np.array([-2, 2, 5]))
        x += 4
        vg_2 = VGroup()
        for k in range(0, 3):
            for m in range(0, 3):
                rec = Rectangle(width=x_step, height=y_step).set_color(BLUE).set_opacity(0.5)
                rec.move_to(np.array([x + x_step * k, y - y_step * m, 0]))
                vg_2.add(rec)
                vg_2.add(Arrow(np.array([x + k * x_step, y - m * y_step, 0]),np.array([0,2,5]),
                               ).set_color(BLUE).set_opacity(0.5))
        node2 = Sphere(radius=0.3, color=BLUE, opacity=1).move_to(np.array([0, 2, 5]))
        x -= 2
        y += -1.5
        vg_3 = VGroup()
        for k in range(0, 3):
            for m in range(0, 3):
                rec = Rectangle(width=x_step, height=y_step).set_color(RED).set_opacity(0.5)
                rec.move_to(np.array([x + x_step * k, y - y_step * m, 0]))
                vg_3.add(rec)
                vg_3.add(Arrow(np.array([x + k * x_step, y - m * y_step, 0]), np.array([-1, -1, 5]),
                               ).set_color(RED).set_opacity(0.5))
        node3 = Sphere(radius=0.3, color=RED, opacity=1).move_to(np.array([-1, -1 , 5]))
        self.play(FadeOut(node),FadeOut(vec_vg),FadeOut(node_),FadeOut(vec_vg_))
        self.wait()

        self.play(ShowCreation(vg_1),ShowCreation(node1))
        self.play(ShowCreation(vg_2),ShowCreation(node2))
        self.play(ShowCreation(vg_3),ShowCreation(node3))
        self.wait()
        self.play(TransformMatchingShapes(title1,title2))
        self.wait()
        self.play(vg_1.animate.shift(RIGHT),node1.animate.shift(RIGHT),run_time = 2)
        self.play(vg_2.animate.shift(RIGHT),node2.animate.shift(RIGHT),run_time = 2)
        self.play(vg_3.animate.shift(RIGHT),node3.animate.shift(RIGHT),run_time = 2)


class Part9(Scene):
    CONFIG = {
        'starsky':"starsky.jpg",
        'part1':"starsky_1.jpg",
        'part2':"starsky_2.jpg",
        'sea':"sea.jpg",
        "camera_class": ThreeDCamera,
        'fuse':"fuse.png"
    }

    def construct(self):
        frame = self.camera.frame
        frame.set_euler_angles(
            phi= 45 * DEGREES, theta = -90*DEGREES, gamma = 90*DEGREES
        )

        starsky = ImageMobject(self.starsky).shift(IN*10).set_height(6).shift(RIGHT*2)
        title = Text("Style Transfer").next_to(starsky,UP).shift(IN*10).scale(2).shift(RIGHT*4+UP*2)
        part1 = ImageMobject(self.part1).set_height(2).shift(UP*1.5+IN*5)
        part2 = ImageMobject(self.part2).set_height(2).shift(DOWN*1.5+IN*5)
        self.play(Write(title))
        self.play(FadeIn(starsky))
        imgHeight = 4
        imgWidth = 6
        vec_vg = VGroup()
        for i in range(0,imgHeight-1,1):
            for j in range(0,imgWidth-3,1):
                vec_vg.add(Arrow(starsky.get_corner(UL)+RIGHT*j+DOWN*i,part1.get_center())).set_color(YELLOW).set_opacity(0.5)
        self.play(ShowCreation(vec_vg),FadeIn(part1))

        vec_vg_ = VGroup()
        for i in range(3,imgHeight+2,1):
            for j in range(2,imgWidth-1,1):
                vec_vg_.add(Arrow(starsky.get_corner(UL)+RIGHT*j+DOWN*i,part2.get_center())).set_color(YELLOW).set_opacity(0.5)
        self.play(ShowCreation(vec_vg_),FadeIn(part2))

        self.wait()
        fuse = ImageMobject(self.fuse).shift(OUT*5).set_height(3)
        sea = ImageMobject(self.sea).shift(OUT).set_height(3)
        arrow1 = Arrow(part1.get_center(),sea.get_center(),stroke_width = 5).set_color(BLUE).set_opacity(0.5)
        arrow2 = Arrow(part2.get_center(),sea.get_center(),stroke_width = 5).set_color(BLUE).set_opacity(0.5)
        self.play(ShowCreation(arrow1))
        self.play(ShowCreation(arrow2))
        self.play(ShowCreation(sea))
        self.wait()
        arrow3 = Arrow(sea.get_center(),fuse.get_center(),stroke_width = 5).set_color(BLUE)
        self.play(ShowCreation(arrow3))
        self.wait()
        self.play(ShowCreation(fuse),run_time = 2)
        self.wait()

        delta_d1 = 10/45
        delta_d2 = 5/45
        delta_d3 = 1.015
        dt = 1/15
        phi,theta,gamma = 0,0,0
        phi_0,theta_0,gamma_0=45*DEGREES,-90*DEGREES,90*DEGREES
        delta_phi,delta_theta,delta_gamma = (phi-phi_0)/45,(theta-theta_0)/45,(gamma-gamma_0)/45
        for i in range(45):
            phi_0 += delta_phi
            theta_0 += delta_theta
            gamma_0 += delta_gamma
            frame.set_euler_angles(
                phi=phi_0,theta = theta_0, gamma = gamma_0
            )
            self.play(fuse.animate.scale(delta_d3).shift(IN*delta_d2),title.animate.shift(OUT*delta_d1+LEFT*5.5/45),run_time = dt)
        self.wait()
class Part10(Scene):
    def construct(self):
        text_filter = Tex("\\begin{bmatrix} 0 & -1 & 0 \\\\ -1 & 4 & -1 \\\\ 0 & -1 & 0 \end{bmatrix}")
        text_filter.shift(UP * 2.5 + RIGHT*2)
        text_filter.set_color(BLUE)

        text_img = Tex("\\begin{bmatrix} 15 & 200 & 100 \\\\ 201 & 205 & 190 \\\\ 75 & 210 & 100 \end{bmatrix}")
        text_img.shift(UP * 2.5 + LEFT * 3)

        img_name = Text("Image").next_to(text_img, DOWN)
        fil_name = Text("Filter").next_to(text_filter,DOWN)

        self.play(Write(text_filter))
        self.play(Write(fil_name))
        self.wait()
        self.play(Write(text_img))
        self.play(Write(img_name))
        self.wait()
        width = text_img.get_width()
        height = text_img.get_height()

        equation = Tex("15 \\times 0 + 200 \\times (-1) + 0\\times 100 \\\\ 201 \\times (-1) + 205 \\times 4 +190 \\times (-1) \\\\ + 75 \\times 0 + 210 \\times (-1) + 100 \\times 0 \\\\ = 19")
        equation.shift(RIGHT*2+DOWN)
        self.play(Write(equation),run_time = 3)
        num = [[15,200,100],[201,205,190],[75,210,100]]

        init_xy = np.array([-5.5,0,0])

        rec = VGroup()
        for i in range(0, 3):
            for j in range(0, 3):
                temp = Rectangle(width=1, height=1,color = BLUE).move_to(init_xy+RIGHT*i+DOWN*j).set_opacity(num[i][j]/256)
                rec.add(temp)
        self.play(ShowCreation(rec))
        self.wait(2)
        self.play(rec[4].animate.set_opacity(19/256),run_time = 2)
        self.wait()
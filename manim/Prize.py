from manimlib.imports import *
import random

def read_fans():
    f = open('./fans.txt', 'r', encoding= 'utf-8')
    lines = f.readlines()
    f.close()
    return lines

class prize(TeacherStudentsScene):
    def construct(self):
        self.teacher_says(
            "大家准备好抽奖了吗？"
        )
        self.change_student_modes(
            look_at_arg=4 * LEFT + 2 * UP
        )
        self.wait()
        lst = read_fans()
        random.seed(None)
        ans = random.randint(0,len(lst)-1)
        fans_lst=[]
        for i in lst:
            i=i.strip('\n')
            fans_lst.append(i)
        fans = VGroup()
        for fan in fans_lst:
            #fans_group.add(TextMobject(fan, color = BLUE).scale(0.8).to_edge(UP))
            fans.append(TextMobject("", color = BLUE).to_edge(UP))
        count = TextMobject("3","2","1",color = RED).to_edge(UP)
        count[1].to_edge(UP)
        count[2].to_edge(UP)
        self.play(FadeIn(count[0]))
        self.wait(0.5)
        self.play(ClockwiseTransform(count[0], count[1]), run_time = 0.5)
        self.wait(0.5)
        self.play(ClockwiseTransform(count[0], count[2]), run_time = 0.5)
        self.wait(0.5)
        self.play(FadeOut(count[0]))
        self.teacher_says(
            "让我们开始吧！"
        )
        len_lst = len(lst)
        for j in range(0,2):
            for i in range(0,len_lst):
                if (j==0 and i==0):
                    self.play(FadeIn(fans[0]), run_time = 0.01)
                elif (i==0 and j!=0):
                    self.play(FadeOut(fans[len_lst-1]),FadeIn(fans[i]), run_time = 0.01)
                else:
                    self.play(FadeOut(fans[i-1]),FadeIn(fans[i]), run_time = 0.01)
                if (i == ans and j == 1):
                    self.play(Indicate(fans[i]), run_time=1)
                    self.wait(1)
                    break
        self.teacher_says(
            "Congratulations!!!"
        )
        self.wait(2)
        self.student_says(
            "OHHHHHHHHH!!!"
        )
        self.wait(2)

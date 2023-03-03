from manim import *

processings = [ 2, 2.5, 2, 2, 2, 1.5 ]
schedule1 = [ [1,3,5],
              [2,4,6] ]
schedule2 = [ [1,2],
              [2,5,4,6] ]

def makespan(processings, schedule):
    Cs = []
    for i, jobs in enumerate(schedule):
        Cs.append(sum([processings[j-1] for j in jobs]))
    return max(Cs)

def set_schedule(rects, schedule):
    # for centering the schedule
    M = makespan(processings, schedule1)

    anims = []
    for i, jobs in enumerate(schedule):
        C = 0
        for j in jobs:
            rect = rects[j-1]
            anims.append(rect.animate.move_to(
                Point(location=[
                C + rect.width/2 - M/2,
                -i,
                0
                ])
            ))
            C += rect.width

    return anims

def set_fills(rects, fills):
    anims = []
    for j in range(6):
        if j in fills:
            anims.append(rects[j-1].animate.set_fill(ORANGE, 0.7))
        else:
            anims.append(rects[j-1].animate.set_fill('#000'))
    return anims

class Schedule(Scene):
    def construct(self):
        prev = None
        rects = []
        vgroups = []
        for j, p in enumerate(processings):
            rect = Rectangle(height=1.0, width=p)
            if prev:
                rect.next_to(prev, direction=DOWN)
            else:
                rect.align_on_border(UP)
                rect.align_on_border(LEFT)
            text = Text(str(j+1)).move_to(rect.get_center())
            vgroups.append(VGroup(rect, text))
            rects.append(rect)
            prev = rect

        self.play(*[Create(vg) for vg in vgroups])

        self.wait(2)

        self.play(*set_schedule(vgroups, schedule1))

        self.play(*set_fills(rects, [1, 2, 3]))

        self.wait(2)

        self.play(*set_fills(rects, []))

        self.play(rects[1].animate.stretch_to_fit_width(1.5))

        self.wait(2)

        self.play(*set_schedule(vgroups, schedule2))

        self.play(*set_fills(rects, [1, 2, 5]))

        self.wait(2)


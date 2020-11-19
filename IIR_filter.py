class IIR_filter_2ndOrder:
    def __init__(self,b0,b1,b2,a1,a2):
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.a1 = a1
        self.a2 = a2
        self.acc = 0;        # accumulator
        self.b_x1 = 0;       # input x delay buffer
        self.b_x2 = 0;
        self.b_y1 = 0;       # output y delay buffer
        self.b_y2 = 0;
        
    def dofilter(self,x):
        self.acc = (x*self.b0) + (self.b_x1*self.b1) + (self.b_x2*self.b2) - (self.b_y1*self.a1) - (self.b_y2*self.a2)
        self.b_x2 = self.b_x1      # delay lines
        self.b_x1 = x
        self.b_y2 = self.b_y1
        self.b_y1 = self.acc
        return self.acc
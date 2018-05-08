import cv2
import numpy as np

class Env:
    def __init__(self):
        #self.iter = 0
        self.x = np.matrix([0.,320.])
        self.vr = np.matrix([5.,0.])
        self.vl = np.matrix([-5.,0.])

    def call(self):
        
        self.x += self.vr
        im = self.draw(self.x.astype(int))
        #self.iter += 1
        return im
        

    def draw(self, x):
        im = np.zeros( (640,700,3), np.uint8)
        r = 10
        im = cv2.rectangle(im, (x[0,0]-r,x[0,1]-r), (x[0,0]+r,x[0,1]+r), (255,0,0), -1)
        cv2.imshow('src2', im)
        return im
        


if __name__ == '__main__':
    env = Env()
    c = 0
    
    while(c != ord('q') ):
        im = env.call()
        c = cv2.waitKey(0)
             
    print('exit')
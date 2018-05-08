import cv2
import numpy as np

class Moving:
    def __init__(self):
        self.x = np.matrix([320,320])
        self.c=0
        
        
        while(self.c!=ord('q')):
            img=self.control()
            print self.c
            cv2.imshow('simulation',img)
            self.c=cv2.waitKey(0)
            

    def control(self):
        img = np.zeros( (640,700,3), np.uint8)
        r = 10
        
        print self.x
        print self.c
        if self.c==ord('d'):
            self.x=self.x+np.matrix([5,0])
        elif self.c==ord('a'):
            self.x=self.x+np.matrix([-5,0])
        
        x=self.x    
        img = cv2.rectangle(img, (x[0,0]-r,x[0,1]-r), (x[0,0]+r,x[0,1]+r), (255,0,0), -1)
        print 1
        return img
        
        

if __name__ == '__main__':
    Moving()
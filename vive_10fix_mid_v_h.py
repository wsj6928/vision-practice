import cv2
import numpy as np
import random

class Moving:
    def __init__(self):
        self.x = np.matrix([320,320])
        self.c=0
        self.a=320
        
        while(self.c!=ord('q')):
            img=self.control()
            cv2.imshow('simulation',img)
            self.c=cv2.waitKey(0)
            

    def control(self):
        img = np.zeros( (640,700,3), np.uint8)
        r = 10
        
    
        if self.c==ord('d'):
            self.a=self.a+2
            self.x=np.matrix([self.a,320])+np.matrix([random.randrange(-10,11),random.randrange(-10,11)])
        elif self.c==ord('a'):
            self.a=self.a-2
            self.x=np.matrix([self.a,320])+np.matrix([random.randrange(-10,11),random.randrange(-10,11)])
        
        x=self.x    
        img = cv2.rectangle(img, (x[0,0]-r,x[0,1]-r), (x[0,0]+r,x[0,1]+r), (255,0,0), -1)
        
        return img
        
        

if __name__ == '__main__':
    Moving()
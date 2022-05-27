import torch
import cv2
import csv
#import numpy
#import csv
#import random
#import pandas as pd
#import matplotlib.pyplot as plt
#from itertools import count
#from matplotlib.animation import FuncAnimation
#cap =  cv2.VideoCapture('video.mp4')
#xvalue=0
with open('density.csv','w') as csv_file:
    csv_writer=csv.DictWriter(csv_file, fieldnames=["data","data2"])
    csv_writer.writeheader()

def write2csv(x,reto):
    with open('density.csv','a') as csv_file:
         csv_writer=csv.DictWriter(csv_file,fieldnames=["data","data2"])
         info={"data":x,
               "data2":reto
               }
         csv_writer.writerow(info)
    return    
#xvalue=0
model = torch.hub.load('ultralytics/yolov5', 'custom','yolov5s.pt')
def main_program(cap):
    xvalue=0
    ret,frame = cap.read()
    while(ret):
        ret,frame = cap.read()
        results = model(frame)
        #results.print()
        #print(results.xyxy[0])
        df = results.pandas().xyxy[0]
        df0 = df[df['name'].isin(["car","truck","bike"])]#1for car
        xmin = df0['xmin'].values
        ymin = df0['ymin'].values
        xmax = df0['xmax'].values
        ymax = df0['ymax'].values
        name = df0['name'].values
        
        
        df1 = df[df['name'].isin(["car"])]#1for car
        xmin1 = df1['xmin'].values
        ymin1 = df1['ymin'].values
        xmax1 = df1['xmax'].values
        ymax1 = df1['ymax'].values
        name1 = df1['name'].values
        vhcont1 = len(name1)
    
        df2 = df[df['name'].isin(["truck"])]#2for truck
        xmin2 = df2['xmin'].values
        ymin2 = df2['ymin'].values
        xmax2 = df2['xmax'].values
        ymax2 = df2['ymax'].values
        name2 = df2['name'].values
        vhcont2 = len(name2)

        df3 = df[df['name'].isin(["bike"])]#3for bike
        xmin3 = df3['xmin'].values
        ymin3 = df3['ymin'].values
        xmax3 = df3['xmax'].values
        ymax3 = df3['ymax'].values
        name3 = df3['name'].values
        vhcont3 = len(name3)     

        wtsum=vhcont3+4.8*vhcont1+11.2*vhcont2
        xvalue=xvalue+1
        #print(wtsum)
        write2csv(wtsum,xvalue)
        #density_=wtsum#/0.01
        #density=numpy.log(density_)
        #print(density_)
       
        
        #from writedata import writed
        #writed(1)


        
        for(x,y,x_,y_,oname) in zip(xmin,ymin,xmax,ymax,name):
            cv2.rectangle(frame,(int(x),int(y)),(int(x_),int(y_)),(0,255,0),2)
            cv2.putText(frame,oname,(int(x),int(y)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            #cv2.rectangle(frame,(int(x2),int(y2)),(int(x_2),int(y_2)),(0,255,0),2)
            #cv2.putText(frame,oname2,(int(x2),int(y2)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            #cv2.rectangle(frame,(int(x3),int(y3)),(int(x_3),int(y_3)),(0,255,0),2)
            #cv2.putText(frame,oname3,(int(x3),int(y3)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
        
            cv2.putText(frame,"Cars-",(10,30),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)    
            cv2.putText(frame,str(vhcont1),(100,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
    
            cv2.putText(frame,"Trucks-",(10,70),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)
            cv2.putText(frame,str(vhcont2),(150,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

            cv2.putText(frame,"Bikes-",(10,110),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)
            cv2.putText(frame,str(vhcont3),(150,110),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

        cv2.imshow('frame',frame)
        if cv2.waitKey(100)&0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    cap.release() 
 

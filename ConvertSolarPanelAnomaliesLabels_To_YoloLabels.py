

import numpy as np
import cv2
import os

########################################################################
# Function to check if a file is empty, copied from
# https://medium.com/@varunpn7405/vehicle-accident-detection-yolov11-with-custom-data-and-preprocessing-a793d51cc4ba
def is_empty_file(file_path):
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

def convertlabels(dirnameLabels):
 
     imgpath = dirnameLabels + "\\labels"
     
     #Labels = []
     #TabFileLabelsName=[]
     Tabxyxy=[]
     ContFiles=0
     ContLines=0

     
     print("Reading labels from ",imgpath)
     
        
     for root, dirnames, filenames in os.walk(imgpath):
         
         for filename in filenames:
                 #print(filename)
                           
                 filepath = os.path.join(root, filename)
                 if is_empty_file(filepath):
                      continue
                 filename_jpg=filename[:len(filename) - 3] + "jpg"
                 #print(filename_jpg)
                 img=cv2.imread(dirnameLabels+"\\images\\"+ filename_jpg)
                 #cv2.imshow("PP.jpg", img)
                 #cv2.waitKey(0)
                 cv2.imwrite("Converted\\"+dirnameLabels+"\\images\\"+ filename_jpg, img)
                    
                 #print("Fichero " + str(filepath))
                 f=open(filepath,"r")
                 ContFiles= ContFiles+1
                 
                 Label=""
                 xyxy=""
                 x=0.0
                 y=0.0
                 w=0.0
                 h=0.0
                 label=99
                 LabelYolo=[]
                 filepath2 = "Converted\\" + filepath
                 with open(filepath2, "w") as text_file:
                 #print(filepath)
                   
                   for box in f:
                      Xmin=1.0
                      Xmax=-1.0
                      Ymin=1.0
                      Ymax=-1.0
                      LabelYolo=[]
                     
                      #print("Linea Original")
                      #print(box)
                      xywh=box.split(" ")
                      
                      for i in range(len(xywh)):
                           if i== 0:
                                LabelYolo.append(str(xywh[i]))
                                continue
                                
                           if i%2 != 0.0:
                           # pares  son x
                              if float(xywh[i]) > Xmax: Xmax= float(xywh[i])
                              if float(xywh[i]) < Xmin: Xmin= float(xywh[i])
                           # impares son y
                           else:
                                 if float(xywh[i]) > Ymax: Ymax= float(xywh[i])
                                 if float(xywh[i]) < Ymin: Ymin= float(xywh[i])
                                     
                      x=(Xmax+Xmin)/ 2.0 # x center
                      y=(Ymax+Ymin)/ 2.0 # y center
                      w=Xmax - Xmin
                      h= Ymax -Ymin
                     
                      LabelYolo.append(str(x))
                      LabelYolo.append(str(y))
                      LabelYolo.append(str(w))
                      LabelYolo.append(str(h))
                      NewLine=" ".join(LabelYolo)
                      NewLine =  NewLine + "\n"
                      ContLines=ContLines+1
                      text_file.write(NewLine)
                      #print("Linea a imprimir")
                      #print(NewLine)
                      #img=cv2.imread("pp.jpg")
                      #cv2.imshow("PP.jpg", img)
                      #cv2.waitKey(0)
                #text_file.close
                      
                                            
                 
                
     return ContFiles, ContLines


import shutil
output_dir="Converted"
if  os.path.exists(output_dir):shutil.rmtree(output_dir)
os.mkdir(output_dir)

output_dir=output_dir + "\\Solar-panel-anomalies-1"
os.mkdir(output_dir)


if  os.path.exists(output_dir):shutil.rmtree(output_dir)
os.mkdir(output_dir)
os.mkdir(output_dir + "\\train")
os.mkdir(output_dir+ "\\valid")
os.mkdir(output_dir+ "\\test")

os.mkdir(output_dir + "\\train\\images")
os.mkdir(output_dir + "\\train\\labels")

os.mkdir(output_dir + "\\valid\\images")
os.mkdir(output_dir + "\\valid\\labels")

os.mkdir(output_dir + "\\test\\images")
os.mkdir(output_dir + "\\test\\labels")


dirname="Solar-panel-anomalies-1\\train"
ContFiles, ContLines= convertlabels(dirname)
print(" Converted in " + dirname + " " + " Files " + str(ContFiles) + " Lines " + str(ContLines))
dirname="Solar-panel-anomalies-1\\valid"
ContFiles, ContLines= convertlabels(dirname)
print(" Converted in " + dirname + " " + " Files " + str(ContFiles) + " Lines " + str(ContLines))

dirname="Solar-panel-anomalies-1\\test"
ContFiles, ContLines= convertlabels(dirname)
print(" Converted in " + dirname + " " + " Files " + str(ContFiles) + " Lines " + str(ContLines))

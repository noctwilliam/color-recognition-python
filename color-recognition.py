import numpy as np
import pandas as pd
import cv2


img = cv2.imread(input("Input a File location: "))
index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0

def recognize_color(R, G, B):
	minimum = 10000
	for i in range(len(csv)):
		d = abs(R- int(csv.loc[i, "R"])) + abs(G- int(csv.loc[i, "G"]))+ abs(B- int(csv.loc[i, "B"]))
		if d <= minimum:
			minimum = d
			cname = csv.loc[i, "color_name"]
	return cname

def mouse_click(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b, g, r = img[y, x]
		r = int(r)
		g = int(g)
		b = int(b)

cv2.namedWindow('Color Recognition')
cv2.setMouseCallback('Color Recognition', mouse_click)

while(1):
    cv2.imshow("Color Recognition App")
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)#Creating text string to display( Color name and RGB values )
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA) #For very light colours we will display text in black colour
        if(r + g + b >= 600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        
        clicked = False
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
savefile  =  cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', savefile , 20.0 , (640,480))
try:
	while True:
		ret, frame =cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		out.write(frame)
		cv2.imshow('frame',frame)
		
		cv2.imshow('gray',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
finally:
	cap.release()
	out.release()
	cv2.destroyAllWindows()
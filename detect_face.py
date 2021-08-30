import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	for (x, y, w, h) in faces:
		center_coordinates = x+w//2, y+h//2
		radius = h//2 
		cv2.circle(frame, center_coordinates, radius, (0, 0, 255), 3)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
	cv2.imshow("Live Video", frame)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

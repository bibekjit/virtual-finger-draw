import mediapipe as mp
import cv2


mp_draw=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands

# initialise parameters
hands=mp_hands.Hands(min_detection_confidence=0.8,
                     min_tracking_confidence=0.5,
                     max_num_hands=2)


coords=[] # for storing coordinates

# to draw on screen
def draw(coords):
    for coord in coords:
        cv2.circle(im,(coord[0],coord[1]),6,(255,0,0),cv2.FILLED)

# initialise webcam
cam=cv2.VideoCapture(0)

with hands as hand:

    while True:

        _,im=cam.read()
        im = cv2.flip(im, 1)
        h,w,_=im.shape

        #convert to RGB
        rgb=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

        # find landmarks
        hand_lm=hands.process(rgb)

        im=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)

        new_coor = [] # for updating new coordinates

        if hand_lm.multi_hand_landmarks:
            for lm in hand_lm.multi_hand_landmarks:

                # iterate over all the landmarks
                for i,pts in enumerate(lm.landmark):

                    # get landmark of tip of index finger
                    x,y = lm.landmark[8].x,lm.landmark[8].y
                    x,y = int(x*w),int(y*h)

                    # create a circle on the tip
                    cv2.circle(im,(x,y),10,(255,0,0),cv2.FILLED)

                    # update new coordinates
                    new_coor.append([x,y])

                # draw hand landmarks
                mp_draw.draw_landmarks(im,lm,mp_hands.HAND_CONNECTIONS)

        # store the updated coordinates
        if len(new_coor)!=0:
            for coor in new_coor:
                coords.append(coor)

        # draw the updated coordinates
        if len(coords)!=0:
            draw(coords)

        cv2.imshow('cam',im)

        if cv2.waitKey(1) & 0xff==ord('q'):
            break

cam.release()
cv2.destroyAllWindows()

'''
Прога основана на функции inRange, как и в детекте парковок. Это неудобно. В зависимости
от камеры, "границы" для цветов вообще разные получаются

цвета настраивал по видео 'traffic.mp4'
'''



import cv2
import numpy as np
import imutils


# видео с компьютера
cap= cv2.VideoCapture("videos/traffic.mp4")
# видео с вебкамеры
#cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# создаем "ядро", которое передвигается по фото и делает сглаживание
kernel = np.ones((5,5), np.uint8)

# Функция подписывает цвета объктов на кадре
def draw_color_contours(frame, cnts, color_name, text_color):
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 1000:
            # можно убрать коментарий и тогда будут рисоваться контуры
            #cv2.drawContours(frame,[c],-1,(0,255,0), 1)

            M = cv2.moments(c)

            # координаты центра контура
            cx = int(M["m10"]/ M["m00"])
            cy = int(M["m01"]/ M["m00"])

            # рисуется точка в центре контура и подписывается цвет
            cv2.circle(frame,(cx,cy),2,(0,255,0),-1)
            cv2.putText(frame, color_name, (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

    return frame


while True:

    # читаем кадр
    _,frame= cap.read()

    # изменяем размер
    frame = imutils.resize(frame, width=800, height=600)
    no_blur = frame
    # делаем размытие
    frame = cv2.medianBlur(frame, 15) # slower
    #frame = cv2.blur(frame, ksize=(15,15)) faster
    # переводим из BRG в HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #КРАСНЫЙ ЦВЕТ
    lower_red = np.array([134, 79, 51])# 0,50,120
    upper_red = np.array([251, 255, 255])# 10,255,255

    red_mask = cv2.inRange(hsv,lower_red,upper_red)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # dilation делает главный контур однородным, а шумы - больше
    red_mask = cv2.dilate(red_mask, kernel, iterations=1)
    # erosion убирает цветовые шум на заднем фоне, но чуть-чуть уменьшает главный контур
    red_mask = cv2.erode(red_mask, kernel, iterations=1)
    # opening убирает false positives то есть шум сзади
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    # closing убирает  true negatives то есть черные шумы на главном контуре
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    red_cnts = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    red_cnts = imutils.grab_contours(red_cnts)

    # СИНИЙ ЦВЕТ
    lower_blue = np.array([55, 118, 118])# 90, 60, 0; 0, 116, 144
    upper_blue = np.array([121, 255, 255])# 121, 255, 255; 255, 255, 255
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # dilation делает главный контур однородным, а шумы - больше
    blue_mask = cv2.dilate(blue_mask, kernel, iterations=1)
    # erosion убирает цветовые шум на заднем фоне, но чуть-чуть уменьшает главный контур
    blue_mask = cv2.erode(blue_mask, kernel, iterations=1)
    # opening убирает false positives то есть шум сзади
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
    # closing убирает  true negatives то есть черные шумы на главном контуре
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel)
    blue_cnts = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    blue_cnts = imutils.grab_contours(blue_cnts)

    # ЗЕЛЕНЫЙ ЦВЕТ
    lower_green= np.array([40, 70, 80])
    upper_green = np.array([70, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    # dilation делает главный контур однородным, а шумы - больше
    green_mask = cv2.dilate(green_mask, kernel, iterations=1)
    # erosion убирает цветовые шум на заднем фоне, но чуть-чуть уменьшает главный контур
    green_mask = cv2.erode(green_mask, kernel, iterations=1)
    # opening убирает false positives то есть шум сзади
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
    # closing убирает  true negatives то есть черные шумы на главном контуре
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)
    green_cnts = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    green_cnts = imutils.grab_contours(green_cnts)

    # ЖЕЛТЫЙ ЦВЕТ
    lower_yellow = np.array([4, 134, 26])# 25, 70, 120; 14, 62, 104
    upper_yellow = np.array([26, 255, 255])# 30, 255, 255; 32, 255, 255
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # dilation делает главный контур однородным, а шумы - больше
    yellow_mask = cv2.dilate(yellow_mask, kernel, iterations=1)
    # erosion убирает цветовые шум на заднем фоне, но чуть-чуть уменьшает главный контур
    yellow_mask = cv2.erode(yellow_mask, kernel, iterations=1)
    # opening убирает false positives то есть шум сзади
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
    # closing убирает  true negatives то есть черные шумы на главном контуре
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, kernel)
    yellow_cnts = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    yellow_cnts = imutils.grab_contours(yellow_cnts)

    # СЕРЫЙ ЦВЕТ
    lower_grey = np.array([[74, 37, 174]]) # 0, 0, 109; 0, 0, 21; 86, 40, 183
    upper_grey = np.array([125, 130, 241]) # 132, 23, 211; 255, 84, 69; 106, 100, 236
    grey_mask = cv2.inRange(hsv, lower_grey, upper_grey)
    # dilation делает главный контур однородным, а шумы - больше
    grey_mask = cv2.dilate(grey_mask, kernel, iterations=1)
    # erosion убирает цветовые шум на заднем фоне, но чуть-чуть уменьшает главный контур
    grey_mask = cv2.erode(grey_mask, kernel, iterations=1)
    # opening убирает false positives то есть шум сзади
    grey_mask = cv2.morphologyEx(grey_mask, cv2.MORPH_OPEN, kernel)
    # closing убирает  true negatives то есть черные шумы на главном контуре
    grey_mask = cv2.morphologyEx(grey_mask, cv2.MORPH_CLOSE, kernel)
    grey_cnts = cv2.findContours(grey_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    grey_cnts = imutils.grab_contours(grey_cnts)

    # БЕЛЫЙ ЦВЕТ
    lower_white = np.array([[0, 0, 250]]) # 0, 0, 190; 0, 0, 86; 0, 0, 140
    upper_white  = np.array([169, 11, 255]) # 193, 28, 255; 255, 32, 216; 255, 5, 255
    white_mask = cv2.inRange(hsv, lower_white , upper_white )
    # dilation делает главный контур однородным, а шумы - больше
    white_mask = cv2.dilate(white_mask, kernel, iterations=1)
    # erosion убирает цветовые шум на заднем фоне, но чуть-чуть уменьшает главный контур
    white_mask = cv2.erode(white_mask, kernel, iterations=1)
    # opening убирает false positives то есть шум сзади
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_OPEN, kernel)
    # closing убирает  true negatives то есть черные шумы на главном контуре
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)
    white_cnts = cv2.findContours(white_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    white_cnts = imutils.grab_contours(white_cnts)

    # ЧЕРНЫЙ ЦВЕТ
    lower_black = np.array([[102, 118, 81]]) # 0, 0, 7; 56, 16, 7; 88, 93, 70
    upper_black = np.array([148, 169, 121]) # 255, 255, 50; 134, 255, 93; 139, 222, 234
    black_mask = cv2.inRange(hsv, lower_black, upper_black)
    # dilation делает главный контур однородным, а шумы - больше
    black_mask = cv2.dilate(black_mask, kernel, iterations=1)
    # erosion убирает цветовые шум на заднем фоне, но чуть-чуть уменьшает главный контур
    black_mask = cv2.erode(black_mask, kernel, iterations=1)
    # opening убирает false positives то есть шум сзади
    black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)
    # closing убирает  true negatives то есть черные шумы на главном контуре
    black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_CLOSE, kernel)
    black_cnts = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    black_cnts = imutils.grab_contours(black_cnts)



    # По отдельности рисуем контуры
    draw_color_contours(no_blur, red_cnts, "red", (250, 230, 230))
    draw_color_contours(no_blur, blue_cnts, "blue", (255, 144, 30))
    draw_color_contours(no_blur, green_cnts, "green", (170, 178, 32))
    draw_color_contours(no_blur, yellow_cnts, "yellow", (205, 0, 0))
    draw_color_contours(no_blur, grey_cnts, "grey", (0, 255, 255))
    draw_color_contours(no_blur, white_cnts, "white", (0, 0, 255))
    draw_color_contours(no_blur, black_cnts, "black", (0, 255, 0))

    # выводим результат на экран
    cv2.imshow("result",no_blur)

    # работа прекращается при нажатии на q
    k = cv2.waitKey(5)
    if k == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
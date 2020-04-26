import cv2

cam = cv2.VideoCapture(0)



while True:
    ret, frame = cam.read()
    cv2.imshow("CAMERA", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    print(k)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = input("enter image name")
        img_name=img_name+'.png'
        cv2.imwrite(img_name, frame)
        print(f"{img_name} is saved")
       

cam.release()

cv2.destroyAllWindows()
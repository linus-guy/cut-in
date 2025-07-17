import cv2



def main():
    imgpath=input("Enter the path to the image: ")
    img = cv2.imread(imgpath)
    if img is None:
        print("Error: Could not read the image.")
        return
    cv2.imshow("Image", img)


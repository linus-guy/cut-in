import cv2

def diff(img1, img2):
    # Compute the absolute difference between the two images
    return cv2.absdiff(img1, img2)

def main():
    imgpath=input("Enter the path to the image: ")
    img = cv2.imread(imgpath)
    if img is None:
        print("Error: Could not read the image.")
        return
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    choice=input("do you want to add another image to do other operations? (y/n)")
    if choice.lower() == 'y':
        imgpath=input("Enter the path to the image: ")
        img = cv2.imread(imgpath)
        if img is None:
            print("Error: Could not read the image.")
            return
        cv2.imshow("Image", img)
    else:
        pass
if __name__ == "__main__":
    main()
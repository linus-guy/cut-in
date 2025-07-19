import cv2
import argparse

def setup():
    parser = argparse.ArgumentParser(description="Image processing script")
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()
    return args.image

def diff(img1, img2):
    # Compute the absolute difference between the two images
    difference = cv2.absdiff(img1, img2)
    cv2.imshow("Difference", difference)
    cv2.waitKey(0)

def imshowplus(img, title):
    try:
        cv2.imshow(title, img)
        cv2.waitKey(0)
    except IOError as e:
        print(f"Error displaying image: {e}")
    #finally:
    #    cv2.destroyAllWindows()

def main():
    setup()
    imgpath=setup()
    img = cv2.imread(imgpath)
    if img is None:
        print("Error: Could not read the image.")
        return
    imshowplus(img, "Image")
    choice=input("do you want to add another image to do other operations? (y/n)")
    if choice.lower() == 'y':
        imgpath2=input("Enter the path to the image: ")
        img2 = cv2.imread(imgpath2)
        if img2 is None:
            print("Error: Could not read the image.")
            return
        imshowplus(img2, "Image2")
        choice=input("do you want to diff them? (y/n)")
        if choice.lower() == 'y':
            diff(img, img2)

    else:
        pass
if __name__ == "__main__":
    main()
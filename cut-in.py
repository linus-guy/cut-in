import cv2
import argparse

def args():
    parser=argparse.ArgumentParser(description="Image processing script")
    parser.add_argument("image", type=str, help="Path to the input image")
    parser.add_argument("-i2", "--image2", type=str, help="Path to the second image for comparison", default=None)
    parser.add_argument("-d", "--diff", action="store_true", help="Compute the difference between two images")
    parser.add_argument("--frame-to-images", action="store_true", help="Convert video frames to images")
    args=parser.parse_args()
    return args.image,args.image2,args.diff,args.frame_to_images

def diff(img1, img2):
    # Compute the absolute difference between the two images
    difference=cv2.absdiff(img1, img2)
    cv2.imshow("Difference", difference)
    cv2.waitKey(0)

def imshowplus(img, title):
    try:
        cv2.imshow(title, img)
        cv2.waitKey(0)
    except IOError as e:
        print(f"Error displaying image: {e}")

def main():
    #args()
    img1,img2,diff_flag,frame_to_images=args()
    if (img2 is None and diff_flag) or (img2 is not None and not diff_flag):
        print("Error: Invalid combination of arguments. Use -d with two images or without it for one image.")
        exit(1)
    img=cv2.imread(img1)
    
    imshowplus(img, "Image")
    if img2:
        img2=cv2.imread(img2)
        if img2 is None:
            print("Error: Could not read the second image.")
            return
        imshowplus(img2, "Image2")
        if diff_flag:
            diff(img, img2)

if __name__=="__main__":
    main()
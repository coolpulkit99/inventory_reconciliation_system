from skimage.metrics import structural_similarity
import cv2
import numpy as np

## Function to compare images and get similarity index
def compareImages(prevStateImage,currentStateImage):
    before = prevStateImage
    after = currentStateImage
    # Convert images to grayscale
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between the two images
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    print("Image Similarity: {:.4f}%".format(score * 100))
    if(score<0.6):
        print("Image diff is greater than threshold can't detect object properly")

    # The diff image contains the actual image differences between the two images
    # and is represented as a floating point data type in the range [0,1] 
    # so we must convert the array to 8-bit unsigned integers in the range
    # [0,255] before we can use it with OpenCV
    diff = (diff * 255).astype("uint8")
    
    return before,after,diff, score

def fetchCountoursAndMask(diff, before, after):
    # Threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    after=after.copy()
    before=before.copy()
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(before.shape, dtype='uint8')
    diff_box = cv2.merge([diff, diff, diff])
    contours = contours[0] if len(contours) == 2 else contours[1]
    filled_after = after.copy()

    for c in contours:
        area = cv2.contourArea(c)
        if area > 40:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(before, (x, y), (x + w, y + h), (36,255,12), 2)
            cv2.rectangle(after, (x, y), (x + w, y + h), (36,255,12), 2)
            cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36,255,12), 2)
            cv2.drawContours(mask, [c], 0, (255,255,255), -1)
            cv2.drawContours(filled_after, [c], 0, (0,255,0), -1 )
    after_with_bound=after
    before_with_bound=before
    return contours, diff_box, mask, filled_after, after_with_bound, before_with_bound

## Displays images for demo purpose
def displayImages(before,after,diff,contours, diff_box, mask, filled_after):
    
    cv2.imshow('n-1 th state', before)
    cv2.imshow('n th state', after)
    cv2.imshow('Image_diff', diff)
    cv2.imshow('Image_diff_box', diff_box)
    cv2.imshow('Object mask', mask)
    cv2.imshow('filled after', filled_after)
    cv2.waitKey()

def test():        
    # Load images
    before = cv2.imread('assets/n-1_state.jpg')
    after = cv2.imread('assets/n_state.jpg')
    before,after,diff, score=compareImages(before,after)
    contours, diff_box, mask, filled_after,after_with_bound, before_with_bound = fetchCountoursAndMask(diff, before, after)
    displayImages(before_with_bound,after_with_bound,diff,contours, diff_box, mask, filled_after)
    return before,after,diff,contours, diff_box, mask, filled_after



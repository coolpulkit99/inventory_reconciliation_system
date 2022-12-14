import state_processor,regional_diff_checker
import storage

import cv2
import random

## Only for demo
## Function displays stored data for a random stored product unless id is supplied
def displayStoredData(id=-1):
    if(id<0):
        id = storage.getRandomData()
    productInfo = storage.retreiveData(id)
    contours, diff_box, mask, filled_after = state_processor.fetchCountoursAndMask(productInfo["diff"], productInfo["before"],productInfo["after"])
    state_processor.displayImages(productInfo["before"],productInfo["after"], productInfo["diff"],contours, diff_box, mask, filled_after)
    
## Function will be used to fetch product details from a barcode or manually fed serial no.
## For demo purposes we are generating a random serial number as product identity
def scanProductDetails():
    print("Generating serial no. (to be scanned off of product in real life scenario)")
    randomSerialNumber = int(random.random()*100000)
    print("Serial No.:",randomSerialNumber)
    return randomSerialNumber

## Function creates a new product entry in the database after scanning and image processing
def createProductEntry(serialNo, prevState='assets/n-1_state.jpg', currentState='assets/n_state.jpg'):
    print("Starting image diff (to be done through realtime camera in real life scenario)")
    ## Rack image before object is placed
    print("Processed image before object placement")
    prevState = cv2.imread(prevState)
    ## Rack image after object is placed
    print("Processed image after object placement")
    currentState = cv2.imread(currentState)

    ## comparing both images and saving relevant diff info
    before, after, diff, score = state_processor.compareImages(prevState,currentState)
    contours, diff_box, mask, filled_after = state_processor.fetchCountoursAndMask(diff, before,after)
    productData = dict()
    
    ## For now we are storing actual image information too for demo purposes 
    ## but for efficient storage on prod we won't be storing the image 
    ## rather just the masked portion of the image 
    productData["before"]=before
    productData["after"]=after
    productData["diff"]=diff
    productData["mask"]=mask

    print("Storing object location info")
    storage.storeData(serialNo,productData)


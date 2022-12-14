import cv2
import state_processor


def compareImages(objectImage,reconciliationImage, mask):
    before = objectImage
    after = reconciliationImage
    maskedBefore=cv2.bitwise_and(before,mask)
    maskedAfter=cv2.bitwise_and(after,mask)
    beforeImage,afterImage,diff, score = state_processor.compareImages(maskedBefore,maskedAfter)
    ## good confidence score on image similarity index
    cv2.destroyAllWindows()
    cv2.imshow('Object Image during object storage', before)
    cv2.imshow('Reconciliation image (realtime)', after)
    cv2.imshow('Object Mask', maskedBefore)
    cv2.imshow('Reconciliation image mask', maskedAfter)
    cv2.waitKey()
    return score

def test():
    before,after,diff,contours, diff_box, mask, filled_after = state_processor.test()
    later = cv2.imread('assets/reconciliation.jpg')
    compareImages(after,later, mask)

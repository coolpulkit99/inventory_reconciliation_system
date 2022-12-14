import business_logic
import regional_diff_checker
import sys

def main():
    args = sys.argv[1:]
    serialNumber = business_logic.scanProductDetails()
    if(len(args)>=2):
        ## If user passes their own image paths for validation
        business_logic.createProductEntry(serialNumber,prevState=args[0],currentState=args[1])
        if(len(args)>2):
            business_logic.performReconciliation(serialNumber,args[2])
    else:
        ## Use test images
        business_logic.createProductEntry(serialNumber)
        business_logic.performReconciliation(serialNumber)
    business_logic.displayStoredData(serialNumber)
    
def test():
    regional_diff_checker.test()

if __name__ == "__main__":
    main()

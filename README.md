# Inventory Reconciliation System


## How to run?

- Install all requirements using pip. ```cd``` into the directory and run:
>  pip install -r requirements.txt

- Run without ```cmd``` line args to work with test images
> python3 main.py

- Run without ```cmd``` line args to work with your own images
> python3 main.py path/to/image_before_object_storage.jpg path/to/image_after_object_storage.jpg [path/to/reconciliation_realtime.jpg]

Note: If reconciliation image path is not passed during custom image code execution, reconciliation step is skipped.



## Module Description

### state_processor.py

Houses all logic related to comparing image diff and calculating the Structural Similarity Index of images.
Also has utility function to calculate masks and contours and to display images

### regional_diff_checker.py

Houses all logic related to comparing images for inventory reconciliation purposes

### business_logic.py

Houses all the business logic related to running the scanning(generating) product details,executing state processor, executing regional diff checker and visualizing the output.


### storage.py

This file houses all the logic related to db operations. We current use python shelve for local storage for demo.


### main.py

This file houses all the logic to run the app and respective logic based on the arguments passed while executing application


## Dependencies

- OpenCV
- Python Shelve
- skimage

## Demo link
[Link to demo video](https://www.youtube.com/watch?v=JhzunFHMQY8)


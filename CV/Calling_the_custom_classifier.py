from watson_developer_cloud import VisualRecognitionV3
import json
import glob

with open("Visual_Recognition_api_key.txt", "r") as key:
    version, api_key = key.read().split()

visual_recognition = VisualRecognitionV3(version = version, iam_apikey = api_key)

image_path = glob.glob(r"F:\Docs\Computer Vision\Projects\Object Detection using YOLO\Classification using YOLO\Dataset\cars_and_truck\Test\*.jpg")
car_file_paths = glob.glob(r"F:\Docs\Computer Vision\Projects\Object Detection using YOLO\Classification using YOLO\Dataset\Datasets\car\*.jpg")
truck_file_paths = glob.glob(r"F:\Docs\Computer Vision\Projects\Object Detection using YOLO\Classification using YOLO\Dataset\Datasets\truck\*.jpg")
acc = 0
for path in image_path:
    # opening the image and calling the classifier
    
    with open(path, 'rb') as images_file:
        classes = visual_recognition.classify(images_file, threshold='0.3', classifier_ids='DefaultCustomModel_1685924753').get_result()
    
    # finding the class and conf 
    
    classified_as = classes['images'][0]['classifiers'][0]["classes"][0]["class"]
    confidence = classes['images'][0]['classifiers'][0]["classes"][0]["score"]
    
    # finding the filename
    
    file_name = path.split("\\")[-1]
    relative_path = r"F:\Docs\Computer Vision\Projects\Object Detection using YOLO\Classification using YOLO\Dataset\Datasets"
    
    # finding the accuracy
    
    if((classified_as == "truck") and (relative_path + "\\truck\\" + file_name in truck_file_paths)):
        acc += 1
    elif((classified_as == "car") and (relative_path + "\\car\\" + file_name in car_file_paths)):
        acc += 1
    
    print("Classified as : ", classified_as, " with a confidence of : ", confidence)
    
print("Accuracy : ", acc/len(image_path))
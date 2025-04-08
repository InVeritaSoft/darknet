./darknet detector train custom/Set1/labelled_data.data custom/yolov3_custom_train.cfg weights/yolov3.weights -clear

./darknet detector demo custom/Set1/labelled_data.data custom/yolov3_custom_test.cfg backup/yolov3_custom_train_final.weights -dont_show -thresh 0.5 custom/IMG_7224.MP4 -out_filename result.avi
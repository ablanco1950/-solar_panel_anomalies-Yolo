# solar_panel_anomalies-Yolo

This is an essay that obtains a model to detect anomalies in solar panels using the roboflow file https://universe.roboflow.com/ron-zhyan/solar-panel-anomalies-hikbk-0joqn/dataset/1 as a dataset and a training with yolov11

Installation.

To avoid incompatibilities with other versions of yolo, install ultralytics in a new environment (you can easily create a new environment if you have the Anaconda development environment). Once the new environment is created, run in it:

pip install ultralytics

There may be incompatibilities with the installed version of numpy, so you should downgrade it;

pip install numpy==1.23

Download all the project files to disk, they will be unzipped into a folder named solar_panel_anomalies-Yolo

You have to download the file that is used to train the model from the address
https://universe.roboflow.com/ron-zhyan/solar-panel-anomalies-hikbk-0joqn/dataset/1
To do this you need to have a Roboflow account that you can get for free at https://app.roboflow.com/?ref=blog.roboflow.com

The file that is downloaded to train the model will be found in a folder named solar-panel-anomalies-1 that must be moved to the project folder.

The file in this folder must be converted so that the files that contain the labels in a polygonal format have the usual format in yolo:

Class, x, y, w, h

and eliminate the images that do not have labels

For this, the program is executed:

ConvertSolarPanelAnomaliesLabels_To_YoloLabels.py

which creates the Converted folder with the labels subdirectories in the precise format to train the model.

As the project has a best.pt model, it can be evaluated by testing the images in the test folder, executing:

EvaluateTESTSolarpanelAnomalies_Yolov11.py

The successive images appear on the screen with green boxes indicating the labeled anomalies and red boxes indicating the predicted ones. Sometimes the green box overlaps the red one and the detected anomaly must be predicted based on the rough label with the probability and class that overlaps it. A box with only red without proximity to green would indicate a false detection.
The images appear tangled, but it is the way to estimate the differences between the predicted and real anomalies.

The model has been obtained by training with the execution of the program.

TrainYolov11SolarPanelAnomalies.py

The model has been trained with 200 epochs, but it has not shown signs of exhaustion, with a continuous improvement of the mAP indicators (LOG-200epoch.txt file with the training log and results.png with the graphics is attached)

In the data.yaml file, necessary for training, the absolute addresses of the train, valid and test files appear as if the project had been located in the c: directory. If this were not the case, these absolute addresses would have to be changed.

Considerations:

The results obtained are comparable with those offered in the query https://universe.roboflow.com/ron-zhyan/solar-panel-anomalies-hikbk-0joqn/model/1 . An Excel sheet with the results obtained with both models is attached : ComparingResultsSolarPanelAnomalies.xlsx.
It has also been tested with yolov10 instead of yolov11 and the results have been worse

References:

https://universe.roboflow.com/ron-zhyan/solar-panel-anomalies-hikbk-0joqn/dataset/1

https://medium.com/@varunpn7405/vehicle-accident-detection-yolov11-with-custom-data-and-preprocessing-a793d51cc4ba

https://stackoverflow.com/questions/34051737/numpy-core-multiarray-failed-to-import

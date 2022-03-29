## Dry Bean Classification

![image](https://user-images.githubusercontent.com/6497242/160657242-dcbe4ed6-704f-4e0f-bc45-6ba8e4394d69.png)

Seven different types of dry beans were used in this research, taking into account the features such as form, shape, type, and structure by the market situation. A computer vision system was developed to distinguish seven different registered varieties of dry beans with similar features in order to obtain uniform seed classification. For the classification model, images of 13,611 grains of 7 different registered dry beans were taken with a high-resolution camera. Bean images obtained by computer vision system were subjected to segmentation and feature extraction stages, and a total of 16 features; 12 dimensions and 4 shape forms, were obtained from the grains.

A Random Forest Classifier was trained on a dataset with default setting achieved 92.2%. The data is then analysed for outliers using z-scores grouped by classes. The outliers (Z-Score > 3 or Z-Score < -3) are then dropped from the training data set. The accuracy increases to 93.4%. 

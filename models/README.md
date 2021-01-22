# Model performance:

## Normal_Gen_200.h5
<p> This model displays results but is mostly incorrect and inconsistent with where the cedar trees are. 
To improve this one increasing training time (number of epochs). </p>

## Tree_segmentation.h5
<p> This was the original model before image augmentation was implemented. Very poor predictive power.
Often there are straight lines of predictions. Small circular clusters is what should be appearing. </p>

## Normal_Gen_4000.h5
<p> This model is somewhat better at determining the shapes of what the cedar trees look like. However,
There are still linear features appearing in the predictions and most of the predictions are in the 
wrong place all together. </p>

## Horizontal_200.h5
<p> Designed to introduce horizontal filpping of the images to introduce novel training data, this 
resulted in confusing the model. Very poor predictive power. </p>

## Normal_Gen_10000.h5
<p> As of December 16, 2020, this model seems to be the most accurate because of the small circular
clusters it can  produce. The locations are often wrong but the model is starting to predict on
ciricular green features. </p>

## combo_gen_2800.h5
<p> In hopes to generate a large amount of training data from augmentation, this model used 
horizontal flipping, vertical flipping, random rotation within 90 degrees, image shearing of 0.1, 
and brightness flux. Ultimately this resulted in very poor predictions on the edges of the image.

## comb_gen_10000.h5
<p> Best described as the kitchen sink augmentation model. Turning on horizontal flipping, vertical 
flipping, random rotation within 90 degrees, image shearing of 0.1, and brightness flux, resulted
in very poor performance. All predictions were on the edge of the the output image with almost a 
completely black center. </p>  

## rotation_gen_10000.h5
<p> Prediction locations incorrect and often are not large enough. Overall very poor results. 
Proved that data augmentation might not have been the best solution for this training length.
Possible model overfitting or images are not being rotated correctly with original image.</p>

## more_data_Normal_Gen_3000.h5
<p> Poor performance, mostly white images with few black blobs. The model is generalizing 
everything that is green and more is a Cedar Tree.</p>

## flipper_3000.h5
<p> In this model there is some cedar tree blobbing. However, there is a lot of white streaking.
It is unknown what is causing this issue. Overall this model underperforms.</p>

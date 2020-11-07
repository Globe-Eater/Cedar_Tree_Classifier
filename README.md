# Cedar Tree Image Classifier

<p> Intended for the use of Google Earth Imagery to identify Cedar Trees within the State of Oklahoma.</p>

# Usage:
<ol>
	<li> Collect data from Google Earth Pro as .png file types.</li>
	<li> Put the imagery into a folder named Unclassified.</li>

	<li> Create the enviroment with Anaconda. If Anaconda has not been installed please visit: </li>

	'''
	Conda create env -f enviorment.yml
	'''	

	<li> Activate the enviroment by using the command: </li>

	'''
	conda activate tensorflow
	'''

	<li> Run Image_Slicer.c over the folder contraining Unclassified. This will create a new folder containing 160 by 160 slices of the images.<li>
        
	'''
	./slice.out
	'''
 
	<li> Run Prediction.py to create black and white images of where Cedar Trees are as white and where they are not as black. This will
	output the images into a file named predictions. </li>

	'''
	python prediction.py
	'''	
</ol>

#  Custom Training:
 
### Input Data
<ul>
	<li>Imagery should be from Google Earth Pro at 1046px by 586px resolution or greater.</li>
        <li>The time of the year the imagery was taken should be during the winter months for best results.</li>
        <li>The pre-trained model was done on imagery with 1046px by 586px.</li>
</ul>


### Image preprocessing
<p> This folder will contain programs such as Image_Standardization.c that will split images to the correct sizes for the model to process.</p>

## Labeling the Data
<p> To train your own model you will need to create a training dataset. This will require you to make duplicates of the images you want to classify.
One will be in normal RGB color the other will require you to edit the imagery marking where Cedar Trees are. This can be done with using Microsoft
paint, blender, photoshop, or varity of image modification software. Paint over the Cedar trees with white. Then run Image_Standarize.c over the 
labled imagery to convert it to a black and white image. You can do as many or as few as you like. The more input data you give the model the
better it will be able to classify Cedar Trees from unseen images.</p>

## Training the model:
<ol>
	<li> After you have labeled your images place them in the following folders: training_img, labeled_img. </li>
	<li> Activate the Anaconda enviorment by: </li>
	
	'''
	conda activate tensorflow
	'''
	
	<li> Run Model_Builder.py by: </li>

	'''
	python Model_Builder.py
	'''

</ol>

## Getting predictions from your new model:
<p> By running predction.py the program will use your new model. </p>



# Cedar Tree Image Classifier

<p> This library is for developing a cedar trees classifier from aerial imagery. </p>
 

### Dataset
<ul>
	<li>Sourced from Google Images</li>
        <li>Located in Oklahoma during March 2019 leaf off conditions.</li>
        <li>Original resloution is 1046px by 586px.</li>
</ul>


### Image preprocessing
<p> This folder will contain programs such as Image_Standardization.c that will split images to the correct sizes for the model to process.</p>

## Labeling the Data
<p> One image will be fully labeled by hand in a program such as qgis or arcgis. Likely the vector shapefile will be converted to a raster format
to line up with the image. There will be 5 classes detailed below:</p>
<ul>
	<li>Cedar Trees</li>
        <li>Water</li>
        <li>Grassland</li> 
        <li>Oak Trees</li>
        <li>Urban</li>
</ul>


## Modeling 

<ul>
	<li>Haven't decidied what method I am going to use yet but it might be CNN.</li>
</ul>

## Evalutation

<ul>
	<li> MRSE Mean Root Squared Error </li>
</ul>

# Usage:



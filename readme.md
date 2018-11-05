# Project Tracr - Data Engineer Assignment

## Background:

The role of data engineer is intended to support the work of our data scientists by helping them get the data they need in order to continue their research. As such, "practical" and "done" is more important than "perfect", but the validity of our models depends on obtaining good quality, timely correct data. 

This assignment is intended to see how you would approach an every-day data engineering problem. We expect that it should take approximately three hours to complete. 

Your work will be assessed on a number of criteria:
* Does it work as required? We will follow any instructions you have provided and attempt to re-run your project.
* We will assess code-quality - for example correct idiomatic use of Python, readability and style.

Please submit your work back as a zip file. Include any file or component which is needed to re-run the assignment such as scripts and instructions. Please do not include any database internal files.

## Assignment:

Our data scientists are working on a new image classifier. They require somme images in order to train the system. They have identified a public source of images which may be suitable at this URL:

http://groups.csail.mit.edu/vision/TinyImages/thumbnails64x64/

We want these images to be downloaded and placed into a database. The data scientists have determined that 1000 images will be sufficient for now, but more images may be required in the near future. It should be possible to re-run your script in order to fetch even more images.

Each image should be stored along with some metadata, such as URL from which the image was originally downloaded, the title of the image (if known), and a timestamp which says when the image was downloaded.

### Reading back the stored images

The team will require an easy way to access these images. Please provide a function in order to randomly retreive images:

```python
def get_random_images()->Iterator[ImageStructure]:    
```

Where image ImageStructure is a data-structure which you have designed which contains the image. 

## Task Summary

 - Use the docker-compose file in this project to spin up a new postgres database.
 - Create an appropriate database schema - please provide a way for us to recreate this schema.
 - Write a script that imports a random sample of 1000 images into a the database. All of the images you download must me stored in records in the database.
 - Provide a python function which will allow the data scientists to iterate over the image collection. Each iteration should give a data structure containing a randomly chosen image from the database.
 - Provided some instructions which will allow us to repeat everything you have done.

# Requirements

We store all our data in a postgres database. The docker-compose.yaml configuration in this project will spin up a correctly configured database. You can see the user account, database and password in the docker-compse file.

 - Please use a test-driven development approach.
 - Please use Python as your main programming language. You may also use shell-scripts, SQL and other tools. 
 - Please store additional metadata such as the URL from which each image was downloaded and a time-stamp when the image was fetched.
 - We will want to re-run the script ourselves, so so please make sure that all aspects of this assignment is easily rerunnable. It should be possible for us to re-create your schema and run your import script.




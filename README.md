# Material for Robotics Scholar Intermediate Class 2022

## Setup

You need a compatible python environment.  I recommend the Anaconda python distribution, with python 3.10.

After you install the free version of Anaconda, you can setup an environment like so:

```conda create -n supertechft python=3.10```

Don't forget to activate the environment once it's created.

Now install the python package requirements like so:

```pip install -r requirements.txt```

## Programs

* track_camera.py - Simple OpenCV program which shows how to use your laptop's web camera to get a frame of pixels.

* track_camera_and_show.py - Extends track_camera.py adding code to display what the camera captures.

* track_red.py - Extends track_camera_and_show.py adding code to filter only red pixels.

* track_red_and_counters.py - Extends track_red.py adding code to locate the red "object."

* track_green.py - Changes to track the green "object."

* track_green_and_video.py - Continuously track the green "object."




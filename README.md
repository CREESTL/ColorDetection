# ColorDetection
This simple app allows you to create your own color detector!

I`ve watched a couple of videos on YouTube about color detection in OpenCV. Most of them were about detecting one specific color or about tracking colored objects on the video. But I've decided to make my own app to detect several colors on the video.

As an example I took `traffic.mp4` from `videos/` folder. Using `color_range_detector.py` I've figured out boundaries for each of 7 colors:
- red
- green
- blue
- yellow
- white
- black
- grey

<strong>IMPORTANT!</strong> Those boundaries are specific only for `traffic.mp4`. When using on another video you will need to search for those boundaries yourself via `color_range_detector.py`.

Yes, I know this is a strange way to make it work, but I couldn't find any other though. That can take you quite a long time to find correct boundaries, so be patient!

____
Basically, I use simple OpenCV `inRange()` to separate each of 7 colors in a frame. Then a center of a contour of a specific color is calculated and the name of the color is printed above it.

Yes, that works pretty fast even on not such powerful computers, but the accuracy is not that high (due to boundaries)
____
So, if you want, you can modify this code for your own needs. Good luck!
____
(the result)

![Image alt](https://github.com/CREESTL/ColorDetection/raw/master/result.gif)


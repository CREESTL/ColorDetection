# ColorDetection
This simple app allows you to create your own color detector!

I`ve watched a couple of videos on YouTube about color detection in OpenCV. Most of them were about detecting one specific color or about tracking colored objects on the video. But I've decided to make my own app to detect several colors on the video.

As an example I took `traffic.mp4` from `videos/` folder. 

The following steps are pretty standart and you can find them in many other projects
- Each frame if resized
- The frame is blurred to lower the noise
- The frame if converted from BGR to HSV format
- Using `color_range_detector (<strong>run it from command line!</strong>) I've figured out the boundaries for each of 7 colors:
    - red
    - green
    - blue
    - yellow
    - white
    - black
    - grey
- Morphological transformation (`erosion`, `dilation`, `opening`, `closing` more about those [here](https://www.youtube.com/watch?v=YA5u2PI3hF0&t=361s)) is used to, again, remove all the noise from frame. 
- A `color-mask` is applied on the frame. As a result we get bright areas of a specific color (blue, for example) and all other colors turn black. Imagine having a picture of a blue bowling ball on the floor. After proccessing it with all the steps above, you'll get a black&white image where the ball is white and all the rest is black.
- This is done for every color
- The contours of the colored area are grabbed (then you can draw them of the frame, just un-comment `line 31`)
- The name of the color is printed above the colored area on the frame
- The proccessed frame is displayed to the user

<strong>IMPORTANT!</strong> Those boundaries are specific only for `traffic.mp4`. When using on another video you will need to search for those boundaries yourself via `color_range_detector.py`.

Yes, I know this is a strange way to make it work, but I couldn't find any other though. That can take you quite a long time to find correct boundaries, so be patient!

That works pretty fast even on not such powerful computers, but the accuracy is not that high (due to boundaries)
____
So, if you want, you can modify this code for your own needs. Good luck!
____
(the result)

![Image alt](https://github.com/CREESTL/ColorDetection/raw/master/result.gif)


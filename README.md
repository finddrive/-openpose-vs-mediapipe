## Model selection
This section compares MediaPipe with Farneback and OpenPose to select the optimal human pose estimation framework for further project implementation. The experiments confirm MediaPipe's superior frame rate, visual output, and accuracy performance, making it the preferred choice for this project's implementation.
#### MediaPipe vs Farneback
- Farneback uses a small-scale Keras CNN model for frame-by-frame motion analysis to count pull-ups.
- MediaPipe detects body key points in video frames and using head-hand displacement for counting, performs faster with a frame rate of at least 20 compared to Farneback's 6 to 8.
- Conclusion: MediaPipe is preferred for its higher speed and better visual output in this project.

#### MediaPipe vs OpenPose
- OpenPose modifies open-source code to count rope skips using MPI dataset key points, analyzing the vertical displacement of selected key points frame-by-frame.
- MediaPipe, using relative displacement of key points for counting, offers less output jitter, especially around knee joints, and a higher frame rate of at least 20 versus OpenPose's 0.16.
- Conclusion: MediaPipe, with its faster performance, better visual output, and accurate counting, is deemed more suitable for this project.

  <img hight="150" width="171" alt="MediaPipe vs Farneback" src="https://github.com/yahan-ds/mediapipe-AI-counter/assets/93264144/5e01912f-4d06-4c8b-a83a-b30996ca8e78">
  <img hight="150" width="171" alt="MediaPipe vs OpenPose" src="https://github.com/yahan-ds/mediapipe-AI-counter/assets/93264144/7e61ed4e-58f9-4ae8-8c4a-6702d3d57c31">

## App Development
#### WeChat Mini Program
- Utilized for frontend display and interaction.
- Consists of four main files: xxx.js for executing main logic, xxx.json for configuration, xxx.wxss for styling, and xxx.wxml for webpage structure/UI design.
- Users can select the type of exercise, upload or record a video on the "Home" page, and view the count results, exercise type, and current date after clicking "Start Detection". They can also choose to save the results.
- On the "My" page, users can view/filter saved detection records based on "Exercise Type" and "Date" using wx:for and wx:if-wx:elif for conditional rendering.
app file: the back end built in Flask

  <img hight="100" width="171" alt="Home" src="https://github.com/yahan-ds/mediapipe-AI-counter/assets/93264144/a0830648-1775-4534-ac52-92ddc4330977">
  <img hight="100" width="173" alt="My" src="https://github.com/yahan-ds/mediapipe-AI-counter/assets/93264144/abf50936-7eb2-4080-a360-aab9efea114f">
  <img hight="150" width="250" alt="Filter" src="https://github.com/yahan-ds/mediapipe-AI-counter/assets/93264144/01f89d0b-eb45-4d0d-bc91-e526563ffa2f">


#### Flask Backend
- Handles POST requests from the frontend, retrieves the exercise type parameter, reads in the video, decodes the video using base64, and calls the respective counting function for the exercise type.
- Returns the current date (date), exercise type (type), and count results (count) to the frontend post-processing.
 


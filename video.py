import cv2
from threading import Thread
from datetime import datetime


class FPS:
    def __init__(self):
        self._start = None
        self._end = None
        self._num_frames = 0

    def start(self):
        self._start = datetime.now()
        return self

    def stop(self):
        self._end = datetime.now()

    def update(self):
        self._num_frames += 1

    def elapsed(self):
        return (self._end - self._start).total_seconds()

    def fps(self):
        return self._num_frames / self.elapsed()


class VideoStream:

    def __init__(self, src=None, loop=True):
        self.src = 0 if src is None else src
        self.loop = loop

        self.stream = cv2.VideoCapture(src)
        if not self.stream.isOpened():
            raise IOError('Source ' + str(src) + ' could not be opened!')

        self.grabbed, self.frame = self.stream.read()
        # self.fps = self.stream.get(cv2.CAP_PROP_FPS)
        self.stopped = False

    def start(self):

        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            self.grabbed, frame = self.stream.read()
            if not self.grabbed and self.loop:
                self.reset_video()
            else:
                self.frame = frame

    def reset_video(self):
        self.stream.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.grabbed, frame = self.stream.read()
        if not self.grabbed:
            raise IOError('Stream could not be reset!')
        self.frame = frame

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True


class VideoStreamOld:
    def __init__(self, src=None, loop=True):
        self.src = 0 if src is None else src
        self.loop = loop
        self.stream = cv2.VideoCapture(src)
        if not self.stream.isOpened():
            raise IOError('Source ' + str(src) + ' could not be opened!')
        self.grabbed, self.frame = self.stream.read()

    def read(self):
        self.grabbed, self.frame = self.stream.read()



if __name__ == "__main__":

    vs = VideoStream(src="img/mockup/vid_08.avi", loop=True).start()
    fps = FPS().start()

    while fps._num_frames < 10000:
        frame = vs.read()
        frame = cv2.resize(frame, (400,400))
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        fps.update()

    fps.stop()
    print("elapsed time: {:.2f}".format(fps.elapsed()))
    print("approx fps: {:.2f}".format(fps.fps()))

    cv2.destroyAllWindows()
    vs.stop()
import rclpy
from rclpy.node import Node
import cv2
import numpy as np


class VisualLock(Node):

    def __init__(self):
        super().__init__('visual_lock')

        self.cap = cv2.VideoCapture(0)

        self.timer = self.create_timer(0.03, self.process_frame)

        self.state = "SEARCHING"

    def process_frame(self):

        ret, frame = self.cap.read()
        if not ret:
            return

        height, width, _ = frame.shape

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([20, 100, 100])
        upper = np.array([35, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        output = frame.copy()
        new_state = "SEARCHING"

        if len(contours) == 0:

            new_state = "SEARCHING"
            output = cv2.bitwise_not(frame)

        else:

            largest = max(contours, key=cv2.contourArea)

            if cv2.contourArea(largest) > 500:

                x, y, w, h = cv2.boundingRect(largest)

                cx = x + w // 2

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(frame, (cx, y + h // 2), 5, (255, 0, 0), -1)

                if cx < width / 3:

                    new_state = "ALIGNING LEFT"

                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    output = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

                elif cx < 2 * width / 3:

                    new_state = "LOCKED"

                    output = frame

                else:

                    new_state = "ALIGNING RIGHT"

                    edges = cv2.Canny(frame, 100, 200)
                    output = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        if new_state != self.state:
            self.get_logger().info(f"STATE: {new_state}")
            self.state = new_state

        cv2.imshow("Visual Lock - Yellow Tracking", output)
        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = VisualLock()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

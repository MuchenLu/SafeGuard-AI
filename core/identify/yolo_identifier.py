'''
.core.indentify.yolo_identifier
用於以 YOLO 進行物件與動作辨識
'''

import time
from ultralytics import YOLO
from pathlib import Path
# from core.notify.notifier import send_notification
# from core.identify.analyzer import ai_analyze

class YOLOIdentifier :
    """
    使用 YOLO 模型進行物件與動作辨識，當檢測到特定物件且信心度高於 0.5 時，發送通知。
    """

    def __init__(self, base_path: Path) :
        self.last_notif_time = 0
        self.base_path = base_path
        self.base_model = YOLO(str(self.base_path / "weights" / "yolo11n.pt"))
        self.face_model = YOLO(str(self.base_path / "weights" / "yolov11n-face.pt"))
        self.pose_model = YOLO(str(self.base_path / "weights" / "yolo11n-pose.pt"))

    def detect(self):
        """載入 YOLO 模型，並使用攝影機進行物件檢測，當檢測到特定物件且信心度高於 0.5 時，發送通知。
        """
        result = self.base_model(source = "0", show = True, stream = True)

        for r in result :
            for box in r.boxes :
                class_id = int(box.cls[0])
                confidence = box.conf[0]
                
                # if class_id == 43 and confidence > 0.5 :
                #     # result = ai_analyze(r.orig_img)
                #     if result == "Dangerous" :
                #         current_time = time.time()
                #         if current_time - self.last_notif_time > 60:  # 發送通知的時間間隔
                #             send_notification("警告！", "偵測到刀具")
                #             self.last_notif_time = current_time
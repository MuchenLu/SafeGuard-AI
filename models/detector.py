import time
from ultralytics import YOLO
from models.notifier import send_notification
from models.analyzer import ai_analyze

last_notif_time = 0

def detect() :
    """載入 YOLO 模型，並使用攝影機進行物件檢測，當檢測到特定物件且信心度高於 0.5 時，發送通知。
    """
    model = YOLO("./weights/yolo11n.pt")
    result = model(source = "0", show = True, stream = True)

    for r in result :
        for box in r.boxes :
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            
            if class_id == 43 and confidence > 0.5 :
                result = ai_analyze(r.orig_img)
                if result == "Dangerous" :
                    current_time = time.time()
                    if current_time - last_notif_time > 60:  # 發送通知的時間間隔
                        send_notification("警告！", "偵測到刀具")
                        last_notif_time = current_time
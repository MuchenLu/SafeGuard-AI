'''
.core.camera.driver
實質控制攝影機，包含取得影像資料與回傳等
'''

from onvif import ONVIFCamera
import cv2
import av
from typing import Literal
import queue
import threading

from models.video import VideoInfo

# 定義攝影機物件（提供本機攝影機與 IP 攝影機兩方式）
class Camera :
    def __init__(self, type: Literal["IP", "USB"], **kwargs) :
        self.fps = 1
        self.queue = queue.Queue(maxsize=self.fps)
        if type == "USB":
            self.camera = cv2.VideoCapture(0)
        elif type == "IP":
            # 透過 ONVIF 協定取得 IP 攝影機的串流 URL
            ip = kwargs.get("ip")
            port = kwargs.get("port")
            username = kwargs.get("username")
            password = kwargs.get("password")
            media_service = ONVIFCamera(ip, port, username, password).create_media_service()
            token = media_service.GetProfiles()[0].token
            obj = media_service.GetStreamUri({"StreamSetup": {"Stream": "RTP-Unicast", "Transport": {"Protocol": "RTSP"}}, "ProfileToken": token})
            uri = obj.Uri
            self.camera = cv2.VideoCapture(uri)
    
    def _stream_loop(self) :
        container = av.open(self.camera)
        stream = container.streams.video[0]
        stream.thread_type = 'AUTO'
        
        try :
            for frame in container.decode(stream) :
                img = frame.to_ndarray(format='bgr24')
                yield VideoInfo(yolo_image=img)
                
                if not self.queue.empty() :
                    try :
                        self.queue.get_nowait()
                    except queue.Empty :
                        pass
                self.queue.put(img)
        except :
            raise Exception("攝影機串流異常")
        finally :
            container.close()
    
    def start(self) :
        threading.Thread(target=self._stream_loop, daemon=True).start()
        return self
    
    def changeFPS(self, fps: Literal[1, 30]) :
        self.fps = fps
        self.queue.maxsize = self.fps
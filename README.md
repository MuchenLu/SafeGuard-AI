# SafeGuard AI
## 核心功能
- PyAV 影像辨識與偵數控制
- YOLOv11 物件辨識與動作辨識
- Gemini 2.5 Flash 二階段意境與物品辨識
- Line Messaging 通知推播
- ntfy 公共廣播

## 技術棧
1. 核心環境
- 程式語言：Python 3.11
- 部屬工具：Docker
2. 影像處理
- 影像辨識與偵數控制：PyAV
- 影像讀取：Python-ONVIF
3. AI 辨識
- 物件辨識與動作辨識：YOLOv11
- 隱私保護：YOLOv11-face
- 雲端驗證：google-genai
4. 公共廣播
- 公務人員確認訊息：line-bot-sdk-python
- 民眾廣播與通知：requests
5. 資料庫儲存
- 持久化資料庫：PostgreSQL
- 快取資料庫：Redis

## 專案檔案架構
```
/
├── core/ # 全程式核心功能
    ├── camera/ # 攝影機相關功能
        ├── controller.py # 攝影機控制器
        ├── driver.py # 攝影機驅動程式
    ├── database/ # 資料庫相關功能
        ├── postgresql.py # 提供 PostgreSQL 相關操作方法
        ├── redis.py # 提供 Redis 相關操作方法
    ├── identify/ # 影像辨識相關功能
        ├── gemini_identifier.py # Gemini 辨識引擎
        ├── yolo_identifier.py # YOLOv11 辨識引擎
    ├── notify/
        ├── line_notifier.py # Line 通知核心
        ├── ntfy_notifier.py # ntfy 通知核心
├── models/
    ├── database.py # 資料庫相關資料建模
    ├── video.py # 影像辨識相關資料建模
├── weights/
    ├── yolo11n.pt # YOLOv11 訓練權重
├── main.py # 程式主入口
├── .env # 環境變數檔
├── .gitignore # git 忽略檔
├── .python-version # Python 版本檔
├── config.yaml # 配置檔
├── pyproject.toml # Python 設定檔
├── uv.lock
├── README.md
```

## Landing Page 檔案架構
```
├── static/ # 網頁相關圖片
    ├── Concept.png 
├── index.html # Landing Page 首頁
```
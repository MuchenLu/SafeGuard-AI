'''
.models.database
針對影響處理過程的資料建模
'''
from pydantic import BaseModel, Field
from typing import Optional, Literal
from numpy import ndarray

class CameraInfo(BaseModel) :
    """
    攝影機基本資訊
    """
    id: str = Field(..., description="攝影機 ID")
    name: Optional[str] = Field(None, description="攝影機名稱")
    location: Optional[str] = Field(None, description="攝影機位置")
    fps: Literal[1, 30] = Field(..., description="攝影機幀率，1 或 30")

class VideoInfo(BaseModel) :
    """
    影片基本資訊
    """
    from_camera: Optional[str] = Field(..., description="影片來源攝影機 ID")
    location: Optional[str] = Field(None, description="影片來源位置")
    yolo_image: ndarray = Field(..., description="YOLO 模型分析使用的影像幀")
    gemini_image: Optional[bytes] = Field(None, description="Gemini 模型分析使用的影像幀")

class YOLOResult(BaseModel) :
    """
    YOLO 模型的檢測結果
    """
    class_id: int = Field(..., description="檢測到的物件類別 ID")
    confidence: float = Field(..., description="檢測到的物件信心度")
    dangerous: bool = Field(..., description="是否為危險物件")

class GeminiResult(BaseModel) :
    """
    Gemini 模型的分析結果
    """
    dangerous: bool = Field(..., description="是否為危險情況")


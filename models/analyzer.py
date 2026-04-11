from google import genai
from google.genai import types
from PIL import Image
import cv2
from dotenv import load_dotenv
import os
from typing import Literal

load_dotenv()

def ai_analyze(frame) -> Literal["Dangerous", "Safe"]:
    """使用 Gemini 深入分析影像，以避免誤報

    Args:
        frame (Any): 從攝影機捕獲的影像幀
    
    Returns:
        str: 分析結果，"Dangerous" 或 "Safe"
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_frame)
    
    prompt = """你是一個專業的安全監控大腦。
    系統表示已在畫面中偵測到刀具，請分析此影像，並判斷人物動作與情境是否危險。
    如果你認為情境危險，請回覆 "Dangerous"；如果你認為情境安全，請回覆 "Safe"。"""
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = [prompt, pil_img],
        config = types.GenerateContentConfig(
            temperature = 0.2
        )
    )
    
    result = response.text.strip()
    return result
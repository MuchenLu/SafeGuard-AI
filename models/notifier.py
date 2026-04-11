import requests

def send_notification(title: str, message: str) :
    """使用 ntfy 傳送通知給使用者

    Args:
        title (str): 訊息標題
        message (str): 訊息內容
    """
    requests.post(r"https://ntfy.sh/",
                  json = {
                      "topic": "safeguard_ai",
                      "title": title,
                      "message": message,
                      "priority": 4,
                  })
    
if __name__ == "__main__":
    send_notification("測試通知", "這是一則測試通知，請忽略。")
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def play_video_in_incognito(url, duration, repeat):
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-minimized")
    options.add_argument("--window-size=850,850")
    
    # Membuka browser Chrome dengan opsi incognito
    driver = webdriver.Chrome(options=options)
    
    for _ in range(repeat):
        driver.get(url)
        time.sleep(duration)  # Menunggu sesuai durasi tayang
        time.sleep(2)  # Jeda antar pengulangan
    
    # Tutup browser setelah pemutaran selesai
    driver.quit()

if __name__ == "__main__":
    url = "https://www.bstation.com/video"
    duration = 60
    repeat = 3
    play_video_in_incognito(url, duration, repeat)

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

projects = [
    {
        "title": "DirX - إدارة الملفات والمجلدات",
        "description": "أداة سطح مكتب بواجهة Tkinter لإدارة الملفات بالجملة: ترتيب الملفات، فك المجلدات الفرعية، إعادة تسمية دفعية، تشفير وفك تشفير، وتنظيف الملفات المؤقتة.",
        "tech_stack": ["Python", "Tkinter"],
        "github_url": "https://github.com/mahmoud122453-source/dirx-file-organizer",
        "image": "images/dirx.png",
    },
    {
        "title": "Audio Extractor - استخراج الصوت من الفيديو",
        "description": "برنامج بواجهة رسومية يستخرج الصوت من ملف فيديو ويحفظه بالصيغة التي يختارها المستخدم مثل mp3 أو wav.",
        "tech_stack": ["Python", "MoviePy", "Tkinter"],
        "github_url": "https://github.com/mahmoud122453-source/Audio-Extractor",
        "image": "images/audio-extractor.png",
    },
    {
        "title": "BulkImageEditor - معالجة الصور",
        "description": "أداة بسطر الأوامر لتصغير مجموعة صور مع الحفاظ على نسبة الأبعاد، وإضافة علامة مائية نصية أو صورة مع التحكم في الموضع والشفافية.",
        "tech_stack": ["Python", "argparse"],
        "github_url": "https://github.com/mahmoud122453-source/BulkImageEditor1",
        "image": "images/image-editor.png",
    },
    {
        "title": "Speech Recognition - تحويل الكلام إلى نص",
        "description": "تطبيق يلتقط الصوت من الميكروفون ويحوله إلى نص مكتوب باستخدام خدمة Google، ويعمل التعرف في Thread منفصل كي لا تتجمد الواجهة.",
        "tech_stack": ["Python", "Tkinter", "SpeechRecognition", "Threading"],
        "github_url": "https://github.com/mahmoud122453-source/Speech-Recognition",
        "image": "images/speech-recognition.png",
    },
    {
        "title": "YT-DLP GUI - تنزيل الفيديو والصوت",
        "description": "واجهة رسومية لتنزيل الفيديو أو الصوت عبر yt-dlp، مع طابور تنزيلات واختيار الصيغة والجودة وتحويل الصوت باستخدام FFmpeg.",
        "tech_stack": ["Python", "Tkinter", "yt-dlp", "FFmpeg"],
        "github_url": "https://github.com/mahmoud122453-source/ytdlp-gui",
        "image": "images/ytdlp-gui.png",
    },
]

@app.route("/")
def home():
        return render_template("index.html", projects=projects, year=datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)
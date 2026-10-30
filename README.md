# Portfolio شخصي باستخدام Flask

موقع Portfolio شخصي مبني بلغة Python وإطار Flask، يعرض نبذة شخصية ومهارات تقنية ومشاريع Python، مع روابط التواصل.

## المميزات
- بطاقات المشاريع تُبنى ديناميكياً من قائمة قواميس في `app.py` عبر حلقة Jinja.
- تصميم متجاوب يعمل على الهاتف والحاسوب.
- واجهة عربية بالكامل (RTL).

## التقنيات
Python, Flask, Jinja2, HTML, CSS

## طريقة التشغيل محلياً

1. أنشئ البيئة الافتراضية وفعّلها:
```
python -m venv venv
venv\Scripts\activate
```
(على Mac/Linux: `source venv/bin/activate`)

2. ثبّت الاعتماديات:
```
pip install -r requirements.txt
```

3. شغّل التطبيق:
```
flask run
```

4. افتح `http://127.0.0.1:5000` في المتصفح.

## هيكل المشروع
```
portfolio_flask/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    └── images/
```
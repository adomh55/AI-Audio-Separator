# 🎵 AI Audio Separator (Demucs GUI)
### High-Fidelity Stem Separation Powered by AI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Framework](https://img.shields.io/badge/UI-CustomTkinter-orange.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![AI-Model](https://img.shields.io/badge/Model-Facebook--Demucs-red.svg)](https://github.com/facebookresearch/demucs)

أداة برمجية بواجهة رسومية عصرية تتيح لك فصل المسارات الصوتية (غناء، طبول، بيس، آلات أخرى) باستخدام خوارزميات الذكاء الاصطناعي المتطورة من Meta (Demucs). تم تصميم الأداة لتكون سهلة الاستخدام للموسيقيين والمهندسين على حد سواء.

---

## ✨ المميزات (Features)
* **Modern UI:** واجهة مستخدم رسومية تدعم الوضع الداكن (Dark Mode).
* **Unique Output Folders:** تنظيم تلقائي للمخرجات في مجلدات تحمل طوابع زمنية فريدة لمنع تداخل الملفات.
* **Multi-Stem Separation:** فصل الصوت إلى 4 مسارات: `vocals`, `drums`, `bass`, `other`.
* **Safe Execution:** تشغيل العمليات في مسارات منفصلة (Threading) لضمان عدم تجمد الواجهة أثناء المعالجة.
* **Cross-Platform:** يعمل على Windows, macOS, و Linux.

---

## 🛠 المتطلبات (Prerequisites)
يجب التأكد من تثبيت الأدوات التالية:
1.  **Python 3.8+**
2.  **FFmpeg:** ضروري جداً لمعالجة الملفات الصوتية.
    * *ملاحظة: تأكد من إضافة FFmpeg إلى الـ PATH في نظامك.*

---

## 🚀 التثبيت (Installation)

1. **نسخ المستودع:**
   ```bash
   git clone [https://github.com/your-username/AI-Audio-Separator.git](https://github.com/your-username/AI-Audio-Separator.git)
   cd AI-Audio-Separator

   pip install customtkinter demucs

   python main.py

/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/



 3-  📖 كيفية الاستخدام (Usage)
قم بتشغيل البرنامج.

اضغط على "Browse Audio" لاختيار الملف (MP3, WAV, FLAC, M4A).

اضغط على "Start Separation".

سيتم إنشاء مجلد باسم outputs يحتوي على النتائج مفصلة في مجلد فريد لكل عملية.

⚙️ التفاصيل التقنية (Technical Specs)
Core Model: HDemucs (Hybrid Transformer Demucs).

Processing Unit: CPU (Default).

GUI Library: CustomTkinter.

Output Pathing: Dynamic Path Generation using datetime.

🤝 المساهمة (Contributing)
بصفتي مهندس اتصالات وإلكترونيات، أرحب دائماً بالتطويرات البرمجية والهندسية. إذا كان لديك أي تحسينات على خوارزميات المعالجة أو الواجهة، لا تتردد في فتح Pull Request.

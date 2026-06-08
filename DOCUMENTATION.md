# Nasimi 1.0 Documentation

Nasimi 1.0 Python üzərində qurulan Azərbaycan dili qatıdır. Kod əvvəlcə Python-a çevrilir, sonra Python özü tərəfindən işlədilir.

HTML sənədləşmə: [docs.html](docs.html)

## AZJ: Azərbaycan dili, Latin əlifbası

### Quraşdırma

```bash
./install
nasimi azj examples/azj/sayHello.nasimi
```

Əgər `nasimi` tapılmırsa, installer-in göstərdiyi `~/.local/bin` yolunu `PATH` dəyişəninə əlavə edin.

### Əsas komandalar

```bash
nasimi azj fayl.nasimi
nasimi run azj fayl.nasimi
nasimi translate azj fayl.nasimi
nasimi serve
```

`nasimi serve` lokal playground açır. Terminalda göstərilən `http://localhost:8008/playground.html` ünvanını brauzerdə açın.

### Sadə proqram

```python
qoy salam = "Salam"
yaz(salam)
```

### Funksiya

```python
funksiya topla(a, b):
    qaytar a + b

yaz(topla(3, 4))
```

`funksiya`, `işləmə`, `əməl`, `yarat` sözləri Python-dakı `def` kimi işləyir.

### Şərt

```python
qoy yaş = 12

əgər yaş >= 10 isə:
    yaz("Hazırsan")
əks halda:
    yaz("Bir az da məşq edək")
```

Python-a yaxın yazılış da mümkündür:

```python
əgər yaş >= 10:
    yaz("Hazırsan")
```

### Dövr

Daha təbii söz sırası:

```python
qoy adlar = ["Aylin", "Tural", "Leyla"]

gəz adlar içində ad:
    yaz(ad)
```

Python-a daha yaxın söz sırası da dəstəklənir:

```python
gəz ad içində adlar:
    yaz(ad)
```

### Təkrar

```python
qoy sayğac = 0

sayğac < 3 olduqca:
    yaz(sayğac)
    sayğac = sayğac + 1
```

### Sinif

```python
sinif Uşaq:
    başla __init__(özü, ad):
        özü.ad = ad

    funksiya salamla(özü):
        yaz("Salam, " + özü.ad)

qoy uşaq = Uşaq("Aylin")
uşaq.salamla()
```

### Sözlük

| Nasimi | Python |
| --- | --- |
| `qoy`, `dəyişən` | variable marker, removed before Python runs |
| `funksiya`, `işləmə`, `əməl`, `yarat` | `def` |
| `qaytar`, `ver` | `return` |
| `əgər` | `if` |
| `yoxsa` | `elif` |
| `əks halda` | `else` |
| `gəz`, `dövr` | `for` |
| `içində`, `özündədir` | `in` |
| `olduqca`, `qədər` | `while` |
| `dayan` | `break` |
| `davamet`, `davam_et` | `continue` |
| `denə`, `sına` | `try` |
| `istisna` | `except` |
| `nəhayət` | `finally` |
| `gətir`, `içəri_al` | `import` |
| `sinif`, `sınıf` | `class` |
| `özü` | `self` |
| `yaz` | `print` |
| `oxu` | `input` |
| `say`, `uzunluq` | `len` |
| `siyahı` | `list` |
| `lügət` | `dict` |
| `çoxluq`, `dəstə` | `set` |
| `doğru`, `düz` | `True` |
| `yanlış`, `səhv` | `False` |
| `boş` | `None` |

<h2 dir="rtl" align="right">AZB: تورکجه / آذربایجان دیلی، عرب الفباسی</h2>

<h3 dir="rtl" align="right">قوراشدیرما</h3>

```bash
./install
nasimi azb examples/azb/sayHello.nasimi
```

<p dir="rtl" align="right">اگر <code>nasimi</code> تاپیلمیرسا، installer-in گؤستردییی <code>~/.local/bin</code> یولونو <code>PATH</code>-ه علاوه ائدین.</p>

<h3 dir="rtl" align="right">اساس کوماندالار</h3>

```bash
nasimi azb fayl.nasimi
nasimi run azb fayl.nasimi
nasimi translate azb fayl.nasimi
nasimi serve
```

<p dir="rtl" align="right"><code>nasimi serve</code> لوکال playground آچیر. ترمینالدا گؤرونن <code>http://localhost:8008/playground.html</code> آدرئسینی براوزرده آچین.</p>

<h3 dir="rtl" align="right">ساده پروقرام</h3>

<pre dir="rtl" align="right"><code>قوی salam = "سلام"
یاز(salam)
</code></pre>

<h3 dir="rtl" align="right">فونکسییا</h3>

<pre dir="rtl" align="right"><code>فونکسییا topla(a, b):
    قایتار a + b

یاز(topla(3, 4))
</code></pre>

<p dir="rtl" align="right"><code>فونکسییا</code>, <code>ایشلمه</code>, <code>عمل</code>, <code>یارات</code> سؤزلری Python-داکی <code>def</code> کیمی ایشلیر.</p>

<h3 dir="rtl" align="right">شرط</h3>

<pre dir="rtl" align="right"><code>قوی yas = 12

اگر yas >= 10 ایسه:
    یاز("حاضیرسان")
عکس حالدا:
    یاز("بیر آز دا مشق ائدک")
</code></pre>

<p dir="rtl" align="right">Python-a یاخین یازیلش دا اولار:</p>

<pre dir="rtl" align="right"><code>اگر yas >= 10:
    یاز("حاضیرسان")
</code></pre>

<h3 dir="rtl" align="right">دؤور</h3>

<p dir="rtl" align="right">دیلده داها طبیعی سؤز سیراسی:</p>

<pre dir="rtl" align="right"><code>قوی adlar = ["آیلین", "تورال", "لیلا"]

گز adlar ایچینده ad:
    یاز(ad)
</code></pre>

<p dir="rtl" align="right">Python-a یاخین سؤز سیراسی دا ایشلیر:</p>

<pre dir="rtl" align="right"><code>گز ad ایچینده adlar:
    یاز(ad)
</code></pre>

<h3 dir="rtl" align="right">تکرار</h3>

<pre dir="rtl" align="right"><code>قوی saygac = 0

saygac < 3 اولدوقجا:
    یاز(saygac)
    saygac = saygac + 1
</code></pre>

<h3 dir="rtl" align="right">کیلاس</h3>

<pre dir="rtl" align="right"><code>سینیف Usaq:
    باشلا __init__(اؤزو, ad):
        اؤزو.ad = ad

    فونکسییا salamla(اؤزو):
        یاز("سلام، " + اؤزو.ad)

قوی usaq = Usaq("آیلین")
usaq.salamla()
</code></pre>

<h3 dir="rtl" align="right">سؤزلوک</h3>

<table dir="rtl" align="right">
  <thead>
    <tr><th align="right">Nasimi</th><th align="right">Python</th></tr>
  </thead>
  <tbody>
    <tr><td><code>قوی</code>, <code>دییشن</code></td><td>variable marker, Python-dan قاباق سیلینیر</td></tr>
    <tr><td><code>فونکسییا</code>, <code>ایشلمه</code>, <code>عمل</code>, <code>یارات</code></td><td><code>def</code></td></tr>
    <tr><td><code>قایتار</code>, <code>وئر</code></td><td><code>return</code></td></tr>
    <tr><td><code>اگر</code></td><td><code>if</code></td></tr>
    <tr><td><code>یوخسا</code></td><td><code>elif</code></td></tr>
    <tr><td><code>عکس حالدا</code></td><td><code>else</code></td></tr>
    <tr><td><code>گز</code>, <code>دؤور</code></td><td><code>for</code></td></tr>
    <tr><td><code>ایچینده</code>, <code>اؤزونده‌دیر</code></td><td><code>in</code></td></tr>
    <tr><td><code>اولدوقجا</code>, <code>اولاناقدر</code></td><td><code>while</code></td></tr>
    <tr><td><code>دایان</code></td><td><code>break</code></td></tr>
    <tr><td><code>دوام_ائت</code>, <code>دوامئت</code></td><td><code>continue</code></td></tr>
    <tr><td><code>دئنه</code>, <code>سینا</code></td><td><code>try</code></td></tr>
    <tr><td><code>ایستیسنا</code></td><td><code>except</code></td></tr>
    <tr><td><code>نهایت</code></td><td><code>finally</code></td></tr>
    <tr><td><code>گتیر</code>, <code>ایچری_آل</code></td><td><code>import</code></td></tr>
    <tr><td><code>سینیف</code>, <code>کیلاس</code></td><td><code>class</code></td></tr>
    <tr><td><code>اؤزو</code></td><td><code>self</code></td></tr>
    <tr><td><code>یاز</code></td><td><code>print</code></td></tr>
    <tr><td><code>اوخو</code></td><td><code>input</code></td></tr>
    <tr><td><code>سای</code>, <code>اوزونلوق</code></td><td><code>len</code></td></tr>
    <tr><td><code>لیست</code></td><td><code>list</code></td></tr>
    <tr><td><code>سؤزلوک</code></td><td><code>dict</code></td></tr>
    <tr><td><code>چوخلوق</code>, <code>دسته</code></td><td><code>set</code></td></tr>
    <tr><td><code>دوغرو</code>, <code>دوز</code></td><td><code>True</code></td></tr>
    <tr><td><code>یانلیش</code>, <code>سهف</code></td><td><code>False</code></td></tr>
    <tr><td><code>بوش</code></td><td><code>None</code></td></tr>
  </tbody>
</table>

## Notes

Nasimi faylları Python indent qaydalarına əməl edir. Sətir blokları üçün `:` və eyni səviyyədə boşluq istifadə edin.

The playground on GitHub Pages can show the editor, but only the local `nasimi serve` mode can execute code because browsers cannot run a local Python binary directly.

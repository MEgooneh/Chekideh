---
hide:
    - navigation
    - toc
---

#خانه


## چکیده؛ خلاصه‌ی کتاب‌های مشهور از زبان ChatGPT

تمامی مطالب این سایت توسط مدل GPT3.5-turbo نوشته شده است. یک پروسه‌ی کاملا اتوماتیک!

## نحوه‌ی کارکرد

``` mermaid
stateDiagram-v2
  state fork_state <<fork>>
    کتاب --> fork_state
    fork_state --> GPT3.5_turbo
    fork_state --> Google_Books_API

    state join_state <<join>>
    GPT3.5_turbo --> join_state
    Google_Books_API --> join_state
    join_state --> چکیده
    چکیده --> [*]
```


* لیستی از عناوین کتاب‌ها بصورت انگلیسی داده می‌شود
* دیتاها بدلیل کم حجم بودن و سادگی در یک فایل json ریخته می‌شود و اطلاعات نوشته شده بودن مقاله و موضوع آن ذخیره می‌شود
* تک تک عناوین با پرامپت‌های از پیش نوشته شده به جی‌پی‌تی داده می‌شود و او در قالب مارک‌داون یک خلاصه می‌نویسد.
* برای اطلاعاتی مانند ناشر و عکس کتاب هم از Google Books API استفاده می‌شود.

## لینک‌ها

در :simple-github: به این پروژه :star:{ .heart }  بدهید : [لینک](https://github.com/MEgooneh/Chekideh)

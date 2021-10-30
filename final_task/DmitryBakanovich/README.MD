[Readme for RSS reader].
===================================================================
One-shot command-line RSS reader.
RSS reader is a command-line utility which receive [RSS](https://wikipedia.org/wiki/RSS) URL and prints results in human-readable format.
The program allows you to read news articles directly in the console output. 


[Common usage]:
===================================================================
    > python rss_reader -h

    usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT] [--date DATE] [--to-pdf] [--to-html] [source]

    Pure Python command-line RSS reader.

    positional arguments:

    source          RSS feed URL

    optional arguments:

    -h, --help      show this help message and exit
    --version, --V  Print version info
    --json          Print result as JSON in stdout
    --verbose, --v  Outputs verbose status messages
    --limit LIMIT   Limit news topics if this parameter provided. For example: --limit 4. Note: --limit -1 shows all available feed
    --date DATE     The cashed news can be read with it. For example: `--date 20191020` The new from the specified day will be printed out.
    --to-pdf        Converts news to PDF format --to-pdf
    --to-html       Converts news to HTML format --to-html]


[Features]:
=========================================================
    --version

Show program version

----------------------------------------------------------
    source       

RSS feed URL. Address to RSS-source in format 'https://example.com/rss' or
'http://example.com'
----------------------------------------------------------
    --limit

The amount of displayed (and subsequently processed)
news articles is governed by the optional --limit command
line argument. If limit is not presented: will operate with
all available news articles.

------------------------------------------------------------
    --json

Shows news articles to console output in JavaScript Object
Notation format

------------------------------------------------------------
By default, the program saves all new news into a cache file 
named 'news_cached.txt' (Excepts only if --date is provided). 
To avoid adding duplicate news articles when the news is being saved,
a simple check for a duplicates is performed in the cache: if there is
a duplicate, adding article to cache is not performed. 
------------------------------------------------------------
    --date %Y%M%D 

Shows news only from the cache. With this argument, the program
searches for news articles only in the local cache. The parameter
of the --date is used as a date search label, and the entered
address in the *source argument is used as a label for the search by
the address of the news resource. If *source argument in not provided:
it will show news from the entire cache regardless of the news source 
address.
-------------------------------------------------------------
    --to-html
    --to-pdf

Optional commands --to-pdf and --to-html will also allow
you to save news in PDF or HTML format, for reading offline or on
portable electronic devices. 
File has signature  '{creation_time} -RSS-Reader.{pdf/html}' 

    For Example: '2021-10-30 14'40'49.965231 -RSS-Reader.pdf'

[Examples]:
=============================================================
#1
    > python rss_reader4 https://news.yahoo.com/rss --limit 2
----------------------------------------------------------------------
    Feed: Yahoo News - Latest News & Headlines

    # 1
    Title: Asian spider takes hold in Georgia, sends humans scurrying
    Date: 2021-10-29T13:43:21Z
    Link: https://news.yahoo.com/asian-spider-takes-hold-georgia-134321868.html
    Description: ATLANTA (AP) — A large spider native to East Asia has spun its thick, golden web on power lines, porches and vegetable patches all over north Georgia this
    year — a proliferation that has driven some unnerved homeowners indoors and prompted a flood of anxious social media posts.In metro Atlanta, Jennifer Turpin — a self-de
    scribed arachnophobe — stopped blowing leaves in her yard after inadvertently walking into a web created by the Joro spider. Stephen Carter has avoided a walking trail
    along the Chattahoochee River where he encountered Joro webs every dozen steps. 
    Image: https://s.yimg.com/uu/api/res/1.2/Yi6.JOnBe81VmNVIAkmz3w--~B/aD0yMzYwO3c9MzU0MjthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/7019fdea85ace2b1d54dc4dff
    4f3db33
    # 2
    Title: Supreme Court Justices Brett Kavanaugh and Amy Coney Barrett side with liberal justices, decline to block Maine's vaccine mandate for health workers with religio
    us objections
    Date: 2021-10-30T03:03:49Z
    Link: https://news.yahoo.com/supreme-court-justices-brett-kavanaugh-030349167.html
    Description: The Supreme Court denied a request brought by healthcare workers seeking to skirt a vaccine mandate.
    Image: https://s.yimg.com/uu/api/res/1.2/rIx0HqfrcoN5QS3W4bVejA--~B/aD0yNjgwO3c9MzU3MzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/business_insider_articles_888/9c
    173798a6617070e8c7e291dc5647b8
    
    End

#2
    > python rss_reader4 https://dev.by/rss --limit 1 --json
---------------------------------------------------------------------
    dev.by: Все о работе в IT
     [
      {
        "title": "За какое поведение компания (не) может уволить? Анкета",
        "link": "https://dev.by/news/kodeks-pravil-anketa",
        "pubDate": "Sat, 30 Oct 2021 11:03:00 GMT",
        "image": "https://dev.by/storage/images/80/16/11/18/derived/1b244518febfb581b52e42c3509bd225.jpg",
        "description": "\nМожет ли компания мониторить социальные сети сотрудников? Должен ли работник нести отвественность за репутацию компании? Кодекс правил — это огран
    ичительная мера или инструмент, который призван сделать работу в компании безопасной? Хотим знать ваше мнение! Просим заполнить анкету — это анонимно и займет 2 минуты.
     Результаты мы опубликуем на сайте.\n"
      }
    ]
    
    End

#3 News from cache:

    > python rss_reader4 --limit 4 --date 20211030
-----------------------------------------------------------------------
    Start Reading..
    1 ================================================================
    {
      "title": "В Британии обнаружили уникальные древнеримские статуи",
      "link": "https://www.belta.by/world/view/v-britanii-obnaruzhili-unikalnye-drevnerimskie-statui-467110-2021/",
      "pubDate": "Sat, 30 Oct 2021 00:59:00 +0300",
      "image": "No image found",
      "description": "Раньше на месте церкви находился римский мавзолей, который разрушили норманны. Помимо статуй, специалисты также обнаружили древний стеклянный римский
    кувшин, большие осколки которого хорошо сохранились. В земле кувшин пролежал более тысячи лет."
    }
    -------------------------------------------------------------------
    2 ================================================================
    {
      "title": "Глава ВОЗ прогнозирует появление на Земле нового опасного вируса",
      "link": "https://www.belta.by/world/view/glava-voz-prognoziruet-pojavlenie-na-zemle-novogo-opasnogo-virusa-467109-2021/",
      "pubDate": "Sat, 30 Oct 2021 00:34:00 +0300",
      "image": "No image found",
      "description": "По данным ВОЗ на 29 октября, в мире за время пандемии зарегистрировано 245 373 039 случаев заражения коронавирусом, умер 4 979 421 человек."
    }
    -------------------------------------------------------------------
    3 ================================================================
    {
      "title": "В США провели вторые испытания двигателя гиперзвуковой ракеты",
      "link": "https://www.belta.by/world/view/v-ssha-proveli-vtorye-ispytanija-dvigatelja-giperzvukovoj-rakety-467108-2021/",
      "pubDate": "Sat, 30 Oct 2021 00:09:21 +0300",
      "image": "No image found",
      "description": "Первая ступень твердотопливного двигателя станет частью новой ракеты, полезной нагрузкой для которой будет гиперзвуковой планируемый блок - все вместе
     это образует гиперзвуковую ракету."
    }
    -------------------------------------------------------------------
    4 ================================================================
    {
      "title": "Илон Маск собирается открыть технологический институт в США",
      "link": "https://dev.by/news/ilon-mask-sobiraetsya-otkryt-tehnologicheskii-institut-v-ssha",
      "pubDate": "Sat, 30 Oct 2021 07:13:00 GMT",
      "image": "https://dev.by/storage/images/28/78/98/39/derived/d91a01ac5affffd3a4fd453fc1a20762.jpg",
      "description": "\nГендиректор Tesla Илон Маск заявил в Twitter, что подумывает о запуске нового вуза и даже раскрыл возможное название.\n"
    }
    -------------------------------------------------------------------
---------------------------------------------------------------
    > python rss_reader4 https://news.yahoo.com/rss --limit 4 --date 20211030
-------------------------------------------------------------------
    Start Reading..
    1 ================================================================
    {
      "title": "Supreme Court Justices Brett Kavanaugh and Amy Coney Barrett side with liberal justices, decline to block Maine's vaccine mandate for health workers with re
    ligious objections",
      "link": "https://news.yahoo.com/supreme-court-justices-brett-kavanaugh-030349167.html",
      "pubDate": "2021-10-30T03:03:49Z",
      "image": "https://s.yimg.com/uu/api/res/1.2/rIx0HqfrcoN5QS3W4bVejA--~B/aD0yNjgwO3c9MzU3MzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/business_insider_articles_8
    88/9c173798a6617070e8c7e291dc5647b8",
      "description": "The Supreme Court denied a request brought by healthcare workers seeking to skirt a vaccine mandate."
    }
    -------------------------------------------------------------------
    2 ================================================================
    {
      "title": "Tyler Perry says he suggested 'Survivor' make swimsuits 'look worn and tattered' but denies telling Jeff Probst to get rid of them altogether",
      "link": "https://news.yahoo.com/tyler-perry-says-suggested-survivor-011157169.html",
      "pubDate": "2021-10-30T01:11:57Z",
      "image": "https://s.yimg.com/uu/api/res/1.2/JE2Y9CgmoMy8J0soi3NUxg--~B/aD04NTk7dz0xMTQ2O2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/insider_articles_922/c88545b9c2
    e50daecd046521de46b506",
      "description": "\"Survivor\" players haven't had swimsuits since 2018, and some fans and players blame Tyler Perry."
    }
    -------------------------------------------------------------------
    
    End
--------------------------------------------------

[Known problems]:
=================================================================

Some RSS feeds do not provide a description of news, so the program
implements a mechanism for parsing content directly from the link of a 
news article. In this regard, the program takes a long time to process 
some RCC sources with a large value of the -limit. 
For example: 

https://news.yahoo.com/rss

    > python rss_reader4 https://news.yahoo.com/rss --limit 10 --verbose
    ..............
    2021-10-30 14:35:19,991 - 
    DEBUG - Program completed, time of operating: 5.177200555801392
----------------------------------------------------------------
https://dev.by/rss

    > python rss_reader4 https://dev.by/rss --limit 10 --verbose
    ..............
    2021-10-30 14:38:26,165 - 
    DEBUG - Program completed, time of operating: 1.0548028945922852
----------------------------------------------------------------
In case if there are no news articles, the --to-html or --to-pdf
argument is present program creates an empty file of the corresponding
format
----------------------------------------------------------------

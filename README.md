# Film

Web application that takes the RSI television schedule and allows you to find out about upcoming films.

### URL request:

> https://epg.rsi.ch/mp-epg-frontend-api/web/[channel]?Period=[time]

> https://epg.rsi.ch/mp-epg-frontend-api/web/la1?StartTime=2024-09-26T00:00:00%2B02:00&EndTime=2024-09-26T23:59:59%2B02:00
> 


# .env
~~~
SECRET_KEY=your_secret_key
DATABASE_URL=mysql+pymysql://film_adm:Admin$00@localhost/film
~~~
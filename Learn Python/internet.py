def scrape():

    from urllib.request import urlopen
    with urlopen('https://docs.python.org/3.7/tutorial/stdlib.html#internet-access') as response:
        for line in response:
            line = line.decode('utf-8')
            if 'EST' in line or 'EDT' in line:
                print(line)


def send():

    import smtplib
    server = smtplib.SMTP('localhost')

    # <BR>Nov. 25, 09:43:32 PM EST

    server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    """To: jcaesar@example.org
    From: soothsayer@example.org
    Beware the Ides of March.
    """)

    server.quit()


def currentDate():

    from datetime import datetime
    now = date.today()
    print(now)

    now = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
    print(now)


def timer():

    from timeit import Timer
    print(Timer('send()').timeit())



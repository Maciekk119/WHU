import lxml.html

def convert(file):
    # file = "G:\PycharmProjects\WHU\DataBase_convert\dbdata.php.htm"
    db_site = open(file, "r", encoding="utf-8")
    lxml_mysite = lxml.html.fromstring(db_site.read())
    table = lxml_mysite.find('.//*[@id="carddb"]')
    cards = table.findall('.//')

    print(table)


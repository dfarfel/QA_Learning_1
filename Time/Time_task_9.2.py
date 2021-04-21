import datetime
now=datetime.datetime.now()
american=now.strftime('%m/%d/%y')
europeian=now.strftime('%d/%m/%y')
print(f'American - {american}\nEurope - {europeian}')
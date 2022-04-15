from xml.dom import minidom

'''
ADUReport_add.xml
ADUReport_after.xml
ADUReport_before.xml
report = minidom.parse(r'C:\cnshield\ADUReport.xml')
devices = report.getElementsByTagName('Device')
'''

report = minidom.parse(r'ADUReport_add.xml')
errors = report.getElementsByTagName('Errors')
for i in errors:
    req = i.getElementsByTagName('Message')
    for l in req:
        marktname=l.getAttribute('marketingName')
        print('MarketingName:'+marktname)
        message=l.getAttribute('message')
        print('Message:'+message)
        sev=l.getAttribute('severity')
        print('Severity:'+sev)
        print('--------------')


print('-----------after xml------------ ')

report = minidom.parse(r'ADUReport_after.xml')
errors = report.getElementsByTagName('Errors')
for i in errors:
    req = i.getElementsByTagName('Message')
    for l in req:
        marktname=l.getAttribute('marketingName')
        print('MarketingName:'+marktname)
        message=l.getAttribute('message')
        print('Message:'+message)
        sev=l.getAttribute('severity')
        print('Severity:'+sev)
        print('--------------')


print('-----------before xml------------ ')

report = minidom.parse(r'ADUReport_before.xml')
errors = report.getElementsByTagName('Errors')
for i in errors:
    req = i.getElementsByTagName('Message')
    for l in req:
        marktname=l.getAttribute('marketingName')
        print('MarketingName:'+marktname)
        message=l.getAttribute('message')
        print('Message:'+message)
        sev=l.getAttribute('severity')
        print('Severity:'+sev)
        print('--------------')


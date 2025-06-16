# emp={
#     'eid':101,
#     'ename':'rahul',
#     'esal':50000.45,
#     'loc':['wy','nd','noida']
# }

# print(emp)
# print(emp['eid'])

# emp={
#     'eid':101,
#     'ename':'rahul',
#     'esal':50000.45,
#     'loc':'wayanad'
# }

# print(emp.keys())
# print(emp.values())
# print(emp.items())

# for key,values in emp.items():
#     print(key, ":",values)
employees=[{"id":1,"name":"Jammie","gender":"Female","country":"Equatorial Guinea"},
{"id":2,"name":"Franni","gender":"Female","country":"France"},
{"id":3,"name":"Darline","gender":"Female","country":"Ukraine"},
{"id":4,"name":"Jecho","gender":"Male","country":"Indonesia"},
{"id":5,"name":"Isabel","gender":"Female","country":"United States"},
{"id":6,"name":"Kerk","gender":"Male","country":"Czech Republic"},
{"id":7,"name":"Dev","gender":"Male","country":"China"},
{"id":8,"name":"Agnella","gender":"Female","country":"Russia"},
{"id":9,"name":"Iorgo","gender":"Male","country":"Czech Republic"},
{"id":10,"name":"Rob","gender":"Male","country":"Indonesia"},
{"id":11,"name":"Ambur","gender":"Female","country":"Indonesia"},
{"id":12,"name":"Fee","gender":"Male","country":"China"},
{"id":13,"name":"Stanfield","gender":"Polygender","country":"Mexico"},
{"id":14,"name":"Hercules","gender":"Male","country":"China"},
{"id":15,"name":"Ferdinande","gender":"Female","country":"Yemen"},
{"id":16,"name":"Way","gender":"Male","country":"Canada"},
{"id":17,"name":"Britta","gender":"Female","country":"Russia"},
{"id":18,"name":"Jonathon","gender":"Male","country":"Philippines"},
{"id":19,"name":"Rafferty","gender":"Genderfluid","country":"Burkina Faso"},
{"id":20,"name":"Mayer","gender":"Male","country":"Serbia"},
{"id":21,"name":"Quinn","gender":"Female","country":"Indonesia"},
{"id":22,"name":"Nickolas","gender":"Male","country":"China"},
{"id":23,"name":"Celine","gender":"Female","country":"China"},
{"id":24,"name":"Torry","gender":"Male","country":"Philippines"},
{"id":25,"name":"Druci","gender":"Female","country":"Azerbaijan"},
{"id":26,"name":"Shelia","gender":"Female","country":"United Kingdom"},
{"id":27,"name":"Sheri","gender":"Female","country":"Poland"},
{"id":28,"name":"Jewel","gender":"Agender","country":"Greece"},
{"id":29,"name":"Mordecai","gender":"Male","country":"Tunisia"},
{"id":30,"name":"Silvie","gender":"Non-binary","country":"China"},
{"id":31,"name":"Starla","gender":"Polygender","country":"Colombia"},
{"id":32,"name":"Bernadette","gender":"Female","country":"Brazil"},
{"id":33,"name":"Teodor","gender":"Male","country":"Sweden"},
{"id":34,"name":"Hyatt","gender":"Male","country":"Chad"},
{"id":35,"name":"Tabbie","gender":"Non-binary","country":"Nicaragua"},
{"id":36,"name":"Delainey","gender":"Male","country":"Bosnia and Herzegovina"},
{"id":37,"name":"Terrence","gender":"Male","country":"Portugal"},
{"id":38,"name":"Kelly","gender":"Female","country":"Greece"},
{"id":39,"name":"Gabe","gender":"Male","country":"Czech Republic"},
{"id":40,"name":"Appolonia","gender":"Female","country":"Philippines"},
{"id":41,"name":"Fred","gender":"Genderqueer","country":"South Africa"},
{"id":42,"name":"Sal","gender":"Male","country":"China"},
{"id":43,"name":"Nisse","gender":"Female","country":"France"},
{"id":44,"name":"Lexy","gender":"Female","country":"France"},
{"id":45,"name":"Zachary","gender":"Male","country":"Honduras"},
{"id":46,"name":"Franky","gender":"Male","country":"South Africa"},
{"id":47,"name":"Gusty","gender":"Female","country":"Brazil"},
{"id":48,"name":"Ivy","gender":"Female","country":"Canada"},
{"id":49,"name":"Jonathan","gender":"Male","country":"China"},
{"id":50,"name":"Michale","gender":"Male","country":"China"},
{"id":51,"name":"Mackenzie","gender":"Genderqueer","country":"Ukraine"},
{"id":52,"name":"Valenka","gender":"Female","country":"United States"},
{"id":53,"name":"Demetris","gender":"Female","country":"Dominican Republic"},
{"id":54,"name":"Lea","gender":"Female","country":"Japan"},
{"id":55,"name":"Jefferey","gender":"Male","country":"Canada"},
{"id":56,"name":"Melisenda","gender":"Female","country":"China"},
{"id":57,"name":"Timi","gender":"Female","country":"Latvia"},
{"id":58,"name":"Yves","gender":"Male","country":"Portugal"},
{"id":59,"name":"Mel","gender":"Male","country":"China"},
{"id":60,"name":"Zacharie","gender":"Male","country":"Indonesia"},
{"id":61,"name":"Tristan","gender":"Male","country":"Lesotho"},
{"id":62,"name":"Dacie","gender":"Female","country":"Portugal"},
{"id":63,"name":"Ardis","gender":"Female","country":"Indonesia"},
{"id":64,"name":"Gisela","gender":"Female","country":"Indonesia"},
{"id":65,"name":"Myrilla","gender":"Female","country":"China"},
{"id":66,"name":"Celesta","gender":"Female","country":"Greece"},
{"id":67,"name":"Alon","gender":"Male","country":"Bulgaria"},
{"id":68,"name":"Cordy","gender":"Male","country":"Nigeria"},
{"id":69,"name":"Jeno","gender":"Male","country":"Vietnam"},
{"id":70,"name":"Christiana","gender":"Female","country":"Bahamas"},
{"id":71,"name":"Minta","gender":"Female","country":"Japan"},
{"id":72,"name":"Orsola","gender":"Female","country":"Honduras"},
{"id":73,"name":"Coop","gender":"Male","country":"Russia"},
{"id":74,"name":"Hollis","gender":"Male","country":"Greece"},
{"id":75,"name":"Curtice","gender":"Male","country":"China"},
{"id":76,"name":"Harald","gender":"Male","country":"Niger"},
{"id":77,"name":"Fanny","gender":"Female","country":"Cape Verde"},
{"id":78,"name":"Maury","gender":"Male","country":"Argentina"},
{"id":79,"name":"Maxwell","gender":"Male","country":"Cape Verde"},
{"id":80,"name":"Gus","gender":"Male","country":"Poland"},
{"id":81,"name":"Shelley","gender":"Male","country":"Indonesia"},
{"id":82,"name":"Allyn","gender":"Female","country":"Ivory Coast"},
{"id":83,"name":"Rafaelia","gender":"Female","country":"Argentina"},
{"id":84,"name":"Darelle","gender":"Female","country":"France"},
{"id":85,"name":"Tye","gender":"Male","country":"Venezuela"},
{"id":86,"name":"Kimmie","gender":"Female","country":"Egypt"},
{"id":87,"name":"Dennison","gender":"Male","country":"Spain"},
{"id":88,"name":"Jorey","gender":"Female","country":"Indonesia"},
{"id":89,"name":"Roger","gender":"Male","country":"Indonesia"},
{"id":90,"name":"Vicky","gender":"Female","country":"Poland"},
{"id":91,"name":"Terrie","gender":"Female","country":"Philippines"},
{"id":92,"name":"Adrea","gender":"Female","country":"Indonesia"},
{"id":93,"name":"Goldy","gender":"Female","country":"Jordan"},
{"id":94,"name":"Godard","gender":"Male","country":"Peru"},
{"id":95,"name":"Cesya","gender":"Female","country":"Indonesia"},
{"id":96,"name":"Jannelle","gender":"Non-binary","country":"Serbia"},
{"id":97,"name":"Ximenez","gender":"Male","country":"Sweden"},
{"id":98,"name":"Gerardo","gender":"Male","country":"Ukraine"},
{"id":99,"name":"Danice","gender":"Female","country":"China"},
{"id":100,"name":"Gwendolyn","gender":"Female","country":"Portugal"}]


male_employees=[]
female_employees=[]
for emp in employees:
    if emp['gender'] == 'male':
      male_employees.append(emp['name'])
    elif emp['gender'] == 'female':
      female_employees.append(emp['name'])

print(male_employees)
print(female_employees)

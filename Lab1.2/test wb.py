from matplotlib import pyplot
from openpyxl import load_workbook
wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']
x=sheet['A'][1:]
y=sheet['C'][1:]
z=sheet['D'][1:]
def getvalue(x):return x.value
list_x=list(map(getvalue, x))
list_y=list(map(getvalue, y))
list_z=list(map(getvalue, z))
pyplot.xlabel('Годы')
pyplot.ylabel('Температура/Активность Солнца')
first=pyplot.plot(list_x, list_y,'-g', label="Метка")
second=pyplot.plot(list_x, list_z,'-r', Label="метка2")
pyplot.show()
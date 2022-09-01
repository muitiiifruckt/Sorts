import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
import matplotlib.ticker as ticker


X = np.linspace(-5, 5, 500)
figures = []
values = [1,-10,-5,-1,0,1,5,10]
i=0
while i< 8:
    plt.xlabel(r'$X$')
    plt.ylabel(r'$F(x)$')
    plt.title(r'f(x)=\(cos(3**n*x))/2**n  x={}'.format(values[i]))
    plt.grid(True)
    figure = plt.figure()
    axes = figure.subplots()
    axes.plot(X, (np.cos(3**X*values[i]))/2**X)
    i +=1
    figures.append(figure)
# Массив фигур.
# figures = []


# Отступ
indent = 1.5

# Создаем canvas и устанавливаем текущее значение высоты
c = canvas.Canvas("Matan.pdf")
c.setTitle("Matan")
height = indent

# Цикл по фигурам.
for figure in figures:
    # dpi и размер (в дюймах) графика
    dpi = figure.get_dpi()
    figureSize = figure.get_size_inches()
    # Создаем рамку вокруг графика.
    # Это не обязательно, но так удобнее вырезать распечатанный график ножницами.
    figure.patches.extend(
        [plt.Rectangle((0, 1/(dpi*figureSize[1])), width=1-2/(dpi*figureSize[0]),
                       height=1-2/(dpi*figureSize[1]),
                       transform=figure.transFigure, figure=figure, clip_on=False,
                       edgecolor="black",
                       facecolor="none", linewidth=1)])


    # Рендер фигуры.
    image = BytesIO()
    figure.savefig(image, format="png")
    image.seek(0)
    image = ImageReader(image)


    # Размер фигуры в см.
    figureSize = figure.get_size_inches()*3.54

    # A4 210×297 мм
    # Если выходим за пределы листа, то добавляем новый лист
    if height + figureSize[1] + indent > 29.7:
        height = indent
        c.showPage()

    # Добавляем image в pdf
    c.drawImage(image, (10.5-figureSize[0]/2)*cm, height*cm,
                figureSize[0]*cm, figureSize[1]*cm)
    height += figureSize[1]

# Сохраняем.
c.save()
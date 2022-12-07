#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from cycler import cycler


def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)

    cut = photo[350:835, 450:960, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = (0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2])
    luma = luma
    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'black', label='I')
    plt.legend()

    plt.savefig(plotName)

    return luma

luma_mercury = readIntensity("calibre.png", "calibration.png", "mercury", "white")
luma_blue = readIntensity("blue.png", "blue_plt.png", "tungsten ", " blue")
luma_green = readIntensity("green.png", "green_plt.png", "tungsten ", " green")
luma_red = readIntensity("red.png", "red_plt.png", "tungsten ", " red")
luma_white = readIntensity("white.png", "white_plt.png", "tungsten ", " white")
luma_yellow = readIntensity("yellow.png", "yellow_plt.png", "tungsten ", " yellow")

lw = []

for i in range(485):
    lw.append(1.2174*i+300)

fig = plt.figure(figsize=(10, 5), dpi=200)
plt.plot(lw, luma_blue, c = "blue", label = "синий лист")
plt.plot(lw, luma_green, c = "green", label = "зелёный лист")
plt.plot(lw, luma_red, c = "red", label = "красный лист")
plt.plot(lw, luma_white, c = "white", label = "белый лист")
plt.plot(lw, luma_yellow, c = "yellow", label = "жёлтый лист")

plt.xlabel('Длина волны, нм')
plt.ylabel('Яркость')

ax = plt.gca()

ax.set_facecolor('lightgray')

plt.title('Отраженная интенсивность излучения лампы накаливания')
plt.minorticks_on()
plt.grid(which = 'major', c = 'gray', linewidth = 1)
plt.grid(which = 'minor', c = 'gray', linestyle = ':')

plt.legend(fontsize = 8)
plt.savefig("Reflected_luma_5colours.png")











import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from cycler import cycler


def readIntensity(photoName, plotName):
    photo = imageio.imread(photoName)

    cut = photo[350:835, 450:960, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))
    luma = (0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2])
    luma = luma
    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Альбедо различных поверхностей\n' + '{} / {}')
    plt.xlabel('Длина волны, нм')
    plt.ylabel('Альбедо')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'black', label='I')
    plt.legend()

    plt.savefig(plotName)

    return luma

luma_blue = readIntensity("blue.png", "tmp.png")
luma_green = readIntensity("green.png", "tmp.png")
luma_red = readIntensity("red.png", "tmp.png")
luma_white = readIntensity("white.png", "tmp.png")
luma_yellow = readIntensity("yellow.png", "tmp.png")

albedo_blue = np.array(luma_blue)/np.array(luma_white)
albedo_green = np.array(luma_green)/np.array(luma_white)
albedo_red = np.array(luma_red)/np.array(luma_white)
albedo_white = np.array(luma_white)/np.array(luma_white)
albedo_yellow = np.array(luma_yellow)/np.array(luma_white)



lw = []

for i in range(485):
    lw.append(1.2174*i+300)

fig = plt.figure(figsize=(10, 5), dpi=200)
plt.plot(lw, albedo_blue, c = "blue", label = "синий лист")
plt.plot(lw, albedo_green, c = "green", label = "зелёный лист")
plt.plot(lw, albedo_red, c = "red", label = "красный лист")
plt.plot(lw, albedo_white, c = "white", label = "белый лист")
plt.plot(lw, albedo_yellow, c = "yellow", label = "жёлтый лист")

plt.xlabel('Длина волны, нм')
plt.ylabel('Альбедо')

ax = plt.gca()

ax.set_facecolor('lightgray')

plt.title('Альбедо различных поверхностей')
plt.minorticks_on()
plt.grid(which = 'major', c = 'gray', linewidth = 1)
plt.grid(which = 'minor', c = 'gray', linestyle = ':')

plt.legend(fontsize = 8)
plt.savefig("albedo.png")
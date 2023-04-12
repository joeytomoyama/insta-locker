import win32gui
import win32api

# Define the coordinates of the pixel
x = 0
y = 1079

# Get the handle to the desktop window
hDesktop = win32gui.GetDesktopWindow()

# Get the device context for the entire screen
hDC = win32gui.GetWindowDC(hDesktop)

# Get the pixel value at the specified location
pixel = win32gui.GetPixel(hDC, x, y)

# Release the device context
win32gui.ReleaseDC(hDesktop, hDC)

# Print the pixel value as RGB tuple
print("Pixel value:", (pixel & 0xff), ((pixel >> 8) & 0xff), ((pixel >> 16) & 0xff))
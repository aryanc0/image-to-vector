import cv2
import svgwrite

img = cv2.imread("input/sample.png")
if img is None:
    raise FileNotFoundError("Put an image named sample.png inside input/")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray, 100, 200)


contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)


h, w = gray.shape
dwg = svgwrite.Drawing("output/result.svg", size=(w, h))

for cnt in contours:
    points = [(int(p[0][0]), int(p[0][1])) for p in cnt]
    if len(points) > 1:
        dwg.add(dwg.polyline(points, stroke="black", fill="none", stroke_width=1))

dwg.save()
print("SVG saved in output /result dawggg.svg")

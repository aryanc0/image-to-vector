import cv2
import svgwrite


img = cv2.imread("input/sample.png")
if img is None:
    raise FileNotFoundError("Put an image named sample.png inside input please/")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(
    blur, 150, 255, cv2.THRESH_BINARY_INV
)

edges = cv2.Canny(thresh, 50, 150)

contours, _ = cv2.findContours(
    edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)


h, w = gray.shape
dwg = svgwrite.Drawing("output/result.svg", size=(w, h))

for cnt in contours:
    if cv2.contourArea(cnt) < 100:  # 🔹 remove tiny noise
        continue

    points = [(int(p[0][0]), int(p[0][1])) for p in cnt]
    if len(points) > 1:
        dwg.add(
            dwg.polyline(
                points,
                stroke="black",
                fill="none",
                stroke_width=1
            )
        )

dwg.save()
print("SVG saved in output/result.svg")

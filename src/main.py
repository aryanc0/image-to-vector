import cv2
import svgwrite
import ezdxf


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

dxf_doc = ezdxf.new()
dxf_msp = dxf_doc.modelspace()


for cnt in contours:
    if cv2.contourArea(cnt) < 150:
        continue

    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    points = [(int(p[0][0]), int(p[0][1])) for p in approx]

    if len(points) > 1:
        dwg.add(
            dwg.polyline(
                points,
                stroke="black",
                fill="none",
                stroke_width=1
            )
        )
        
dxf_msp.add_lwpolyline(points)



dwg.save()
dxf_doc.saveas("output/result.dxf")

print("SVG and DXF saved in output Thank you!!!/")


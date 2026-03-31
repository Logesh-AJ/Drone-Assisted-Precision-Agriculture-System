from ultralytics import YOLO
import cv2
import os

# ============================
# 🔧 CONFIGURE YOUR INPUT HERE
# ============================
SOURCE = r'C:\Users\logesh A.J\Documents\projects\image_vis_leaf\trail_2(suger cane only )\test_images\yellow\download.jpeg'  # Image path
#SOURCE = r'C:\Users\logesh A.J\Documents\projects\image_vis_leaf\trail_2(suger cane only )\test_images\rust\rust_sug.mp4'  # Video path
#SOURCE = 0  # For webcam (0 = default camera)

# ============================
# 🔧 MODEL PATH
# ============================
model_path = r'C:\Users\logesh A.J\Documents\projects\image_vis_leaf\trail_2(suger cane only )\YOLOv8_Sugarcane_Weights-20250607T155401Z-1-001\YOLOv8_Sugarcane_Weights\best.pt'
model = YOLO(model_path)

# ============================
# 📸 SOURCE TYPE HANDLER
# ============================
is_webcam = isinstance(SOURCE, int) or (isinstance(SOURCE, str) and SOURCE.isdigit())
source_valid = True

if is_webcam:
    print("[INFO] Starting webcam detection...")
    cap = cv2.VideoCapture(int(SOURCE))
    if not cap.isOpened():
        print("[ERROR] Could not open webcam.")
        source_valid = False

    while source_valid:
        ret, frame = cap.read()
        if not ret:
            print("[INFO] Webcam frame not received. Exiting.")
            break
        results = model.predict(source=frame, stream=True)
        for r in results:
            frame = r.plot()
        cv2.imshow("YOLOv8 - Webcam Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

elif isinstance(SOURCE, str) and os.path.isfile(SOURCE):
    ext = os.path.splitext(SOURCE)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        print("[INFO] Running detection on image...")
        results = model.predict(source=SOURCE, save=True)
        print(f"[RESULT] Output saved at: {results[0].save_path}")
    elif ext in ['.mp4', '.avi', '.mov']:
        print("[INFO] Running detection on video...")
        results = model.predict(source=SOURCE, save=True)
        print(f"[RESULT] Video detection done. Output saved in: {results[0].save_dir}")
    else:
        print(f"[ERROR] Unsupported file type: {ext}")
else:
    print(f"[ERROR] Invalid source or file not found: {SOURCE}")

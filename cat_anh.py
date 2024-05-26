from PIL import Image
import os

# Đường dẫn tới thư mục chứa các bức ảnh
input_folder = "E:/3231"
# Tạo thư mục mới để chứa các bức ảnh cắt
output_folder = "E:/3231_out"

# Tạo thư mục output nếu nó không tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lặp qua tất cả các tệp trong thư mục đầu vào
for filename in os.listdir(input_folder):
    # Chỉ xử lý các tệp ảnh
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Đường dẫn đầy đủ đến tệp ảnh đầu vào
        input_path = os.path.join(input_folder, filename)
        
        # Mở ảnh đầu vào
        img = Image.open(input_path)
        
        # Tính kích thước mới cho ảnh đã cắt
        width, height = img.size
        new_width = new_height = min(width, height)
        
        # Tính toán vị trí cắt
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2
        
        # Cắt ảnh
        img_cropped = img.crop((left, top, right, bottom))
        
        # Resize ảnh cắt thành kích thước 640x640
        img_resized = img_cropped.resize((640, 640), Image.ANTIALIAS)
        
        # Lưu ảnh đã cắt vào thư mục đầu ra với cùng tên file
        output_path = os.path.join(output_folder, filename)
        img_resized.save(output_path)

        print(f"{filename} đã được cắt và lưu thành công.")

from PIL import Image
import os

def convert_HEIC_to_png(input_folder, output_folder):
    # Tạo thư mục đầu ra nếu nó không tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Lặp qua tất cả các tệp trong thư mục đầu vào
    for filename in os.listdir(input_folder):
        if filename.endswith(".HEIC"):
            # Đường dẫn của tệp HEIC
            HEIC_path = os.path.join(input_folder, filename)
            
            # Tên tệp PNG đầu ra (loại bỏ phần mở rộng .HEIC và thêm .png)
            png_filename = os.path.splitext(filename)[0] + ".jpg"
            
            # Đường dẫn của tệp PNG đầu ra
            png_path = os.path.join(output_folder, png_filename)
            
            # Mở tệp HEIC và lưu dưới dạng tệp PNG
            with Image.open(HEIC_path) as img:
                img.save(png_path, 'JPG')

# Thư mục chứa các tệp HEIC
input_folder = "D:/Air_Pollution_Data/New folder/TLU_Lab_ Air_Polution_Data-20240522T082344Z-001/TLU_Lab/101_150"

# Thư mục đầu ra cho các tệp PNG
output_folder = "E:/chuyen_doi"

# Chuyển đổi các tệp HEIC thành tệp PNG
convert_HEIC_to_png(input_folder, output_folder)
print("hoàn thành")
import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(source_folder, destination_folder):
    # Kiểm tra xem thư mục đích có tồn tại không, nếu không thì tạo mới
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Lặp qua các tệp trong thư mục nguồn
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(source_folder, filename)
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(destination_folder, jpg_filename)

            # Đọc tệp HEIC
            heif_file = pillow_heif.read_heif(heic_path)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )

            # Lưu ảnh dưới định dạng JPG
            image.save(jpg_path, "JPEG")

source_folder = "D:/Air_Pollution_Data/New folder/TLU_Lab_ Air_Polution_Data-20240522T082344Z-001/TLU_Lab/101_150"
destination_folder = "E:/chuyen_doi"

# Gọi hàm chuyển đổi
convert_heic_to_jpg(source_folder, destination_folder)
print('Hoàn thành')

import os
import shutil

# Đường dẫn tới thư mục cần duyệt
source_folder = r'C:\Users\NhanAZ\Downloads\MinecraftMarketplace'
# Đường dẫn tới thư mục cần sao chép tệp hình ảnh
destination_folder = r'C:\Users\NhanAZ\Downloads\PNG'

print("Bắt đầu duyệt thư mục...")

# Duyệt qua tất cả các thư mục và tệp tin trong thư mục nguồn
for foldername, subfolders, filenames in os.walk(source_folder):
    for filename in filenames:
        # Kiểm tra nếu tệp tin là hình ảnh (.png, .jpg)
        if filename.endswith('.png') or filename.endswith('.jpg'):
            # Tạo đường dẫn tới tệp tin
            file_path = os.path.join(foldername, filename)
            # Tạo đường dẫn tới vị trí sao chép
            destination_path = os.path.join(destination_folder, filename)
            
            # Kiểm tra nếu tệp tin đã tồn tại trong thư mục đích
            if os.path.exists(destination_path):
                base, extension = os.path.splitext(filename)
                i = 1
                # Tìm một tên mới cho tệp tin sao chép
                while os.path.exists(os.path.join(destination_folder, f"{base}_{i}{extension}")):
                    i += 1
                destination_path = os.path.join(destination_folder, f"{base}_{i}{extension}")
            
            print(f"Đang sao chép tệp tin: {file_path} tới {destination_path}")
            # Sao chép tệp tin vào thư mục đích
            shutil.copy(file_path, destination_path)

print("Hoàn thành việc sao chép!")

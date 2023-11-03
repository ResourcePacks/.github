import os

def delete_files_with_extensions(path, extensions):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                print(f"Đang xử lý tệp: {file}")
                try:
                    if os.access(file_path, os.W_OK):
                        os.remove(file_path)
                        print(f"Đã xóa tệp: {file}")
                    else:
                        # Đặt quyền truy cập
                        os.chmod(file_path, 0o777)
                        os.remove(file_path)
                        print(f"Đã xóa tệp: {file}")
                except Exception as e:
                    print(f"Không thể xóa tệp: {file}. Lỗi: {str(e)}")

def main():
    path = "C:\\Users\\NhanAZ\\Downloads\\MinecraftMarketplace"
    extensions = (".mcpack", ".mctemplate", ".mcpersona")
    delete_files_with_extensions(path, extensions)

if __name__ == "__main__":
    main()

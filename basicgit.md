# Để push một dự án lên GitHub, bạn thực hiện theo các bước sau:
- Bước 0: Tạo repo mới trên GitHub

Vào GitHub, tạo một repository mới (bỏ chọn Initialize this repository with a README).
-   Bước 1: Tạo Git repo
Tạo repo Git:
```bash
git init
```
-  Bước 2: Tạo file .gitignore

Export các thư viện trong môi trường ảo:
```bash
pip freeze > requirements.txt
```
Thêm tất cả các tệp:
```bash
git add .
git commit -m "Initial commit"
```
- Bước 3: Tạo liên kết với GitHub (sao chép URL repo mới trên GitHub):
```bash
git remote add origin https://github.com/your-username/your-new-repo.git
```
- Push lần đầu:
```bash
git branch -M main
git push -u origin main
```
- Các lần Push lần sau:
```bash
git add .
git commit -m "Update message"
git push
```

# Cách xóa hoàn toàn liên kết với GitHub hiện tại và push lại như một project mới
- Bước 1: Xóa thư mục .git (Cắt kết nối Git)
```bash
Remove-Item -Recurse -Force .git
```
- Bước 2: Xóa remote (GitHub)
```bash
git remote remove origin
```
-  Bước 3: Xóa tất cả các tệp đã được Git theo dõi
```bash
git rm -r --cached .
```
# Cách làm việc với nhánh trên Github
- Bước 1: Lấy thông tin đầy đủ các nhánh từ remote:
```bash
git fetch --all
```  
- Bước 2: Kiểm tra các nhánh hiện có trên remote
```bash
git branch -r
```
- Bước 3: Sang nhánh muốn làm việc. Giả sử bạn muốn làm việc với nhánh dev10:
```bash
git checkout -b dev origin/dev10
```
- Bước 4: Pull code từ nhánh đó
```bash
git pull origin dev10
```
- Bước 5: Nếu bạn đã ở trong repo và muốn chuyển sang nhánh khác
```bash
git fetch
```
```bash
git checkout dev100  # hoặc tên nhánh bạn muốn
```
- Nếu pull code từ 1 nhánh mà gặp lỗi "Please commit your changes or stash them before you merge." Sau đó có thể pull code [Mất thay đổi cá nhân]
```bash
git reset --hard
```

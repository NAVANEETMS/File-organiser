import os
import shutil


source_dir=r"C:\Users\navan\Downloads"
destination_dir=r"C:\Users\navan\Desktop"

a=source_dir.rfind("\\")
d_fol_address = os.path.join(destination_dir,source_dir[a+1:]+"_split_folder")

if not os.path.exists(d_fol_address):
    os.makedirs(d_fol_address)

image_e = {".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
           ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"}
video_e = {".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"}
audio_e = {".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"}
document_e = {".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"}

d_image = os.path.join(d_fol_address,"Images")
d_vedio = os.path.join(d_fol_address,"Vedios")
d_audio = os.path.join(d_fol_address,"Audios")
d_document = os.path.join(d_fol_address,"Documents")

for folder in [d_image,d_vedio,d_audio,d_document]:
    if not os.path.exists(folder):
        os.makedirs(folder) 

with os.scandir(source_dir) as entries:
    for entry in entries:
        if entry.is_file():
            filename, file_extension = os.path.splitext(entry.name)
            if file_extension in image_e:
                destination = os.path.join(d_image,entry.name)
                shutil.move(entry.path,destination)
            elif file_extension in video_e:
                destination = os.path.join(d_vedio,entry.name)
                shutil.move(entry.path,destination)
            elif file_extension in audio_e:
                destination = os.path.join(d_audio,entry.name)
                shutil.move(entry.path,destination)
            elif file_extension in document_e:
                destination = os.path.join(d_document,entry.name)
                shutil.move(entry.path,destination)
            
           

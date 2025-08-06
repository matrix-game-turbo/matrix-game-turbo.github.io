#!/usr/bin/env python3
import os
import glob

def generate_video_array(directory_path, variable_name="video_gta"):
    """
    生成指定目录下所有 .mp4 文件的 JavaScript 数组格式
    
    Args:
        directory_path: 视频文件目录路径
        variable_name: JavaScript 变量名
    
    Returns:
        str: 格式化的 JavaScript 数组字符串
    """
    # 获取目录下所有 .mp4 文件
    video_files = glob.glob(os.path.join(directory_path, "*.mp4"))
    
    # 对文件名进行排序（数字排序）
    video_files.sort(key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))
    
    # 转换为相对路径格式
    video_paths = [file_path.replace("\\", "/") for file_path in video_files]
    
    # 生成 JavaScript 数组格式
    paths_str = "', '".join(video_paths)
    result = f"const {variable_name}=['{paths_str}']"
    
    return result

def main():
    # 设置目录路径
    gta_directory = "static/videos/gta"
    
    # 检查目录是否存在
    if not os.path.exists(gta_directory):
        print(f"错误: 目录 {gta_directory} 不存在")
        return
    
    # 生成 GTA 视频数组
    gta_array = generate_video_array(gta_directory, "video_gta")
    
    print("GTA 视频文件数组：")
    print(gta_array)
    print()
    
    # 如果还有其他目录，也可以一并生成
    other_directories = [
        ("static/videos/mc", "video_mc"),
        ("static/videos/unreals", "video_unreals")
    ]
    
    for dir_path, var_name in other_directories:
        if os.path.exists(dir_path):
            array_str = generate_video_array(dir_path, var_name)
            print(f"{dir_path} 视频文件数组：")
            print(array_str)
            print()

if __name__ == "__main__":
    main()
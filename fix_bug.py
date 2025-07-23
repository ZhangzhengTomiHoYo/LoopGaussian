from plyfile import PlyData

def inspect_ply_file(ply_path):
    plydata = PlyData.read(ply_path)
    print(f"PLY 文件元素: {plydata.elements}")
    
    # 打印第一个元素的所有字段
    if plydata.elements:
        print(f"第一个元素的字段: {plydata.elements[0].properties}")
    
    # 检查是否存在 f_rest_0 字段
    if "f_rest_0" in plydata.elements[0]:
        print("文件包含 f_rest_0 字段")
    else:
        print("文件不包含 f_rest_0 字段")

# 使用示例
inspect_ply_file('/home/u2024110476/LoopGaussian/output/dress-20250723_150534_191/point_cloud/iteration_50000/point_cloud.ply')
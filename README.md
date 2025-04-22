# png-convert-GeoJSON
将 PNG 等图片格式的地图图像转换为 GeoJSON 坐标文件。

## 功能
- 读取 PNG 格式的地图图像。
- 自动检测图像中的轮廓并生成多边形。
- 将多边形数据导出为 GeoJSON 格式文件。

## 安装
在运行此项目之前，请确保已安装以下依赖项：

```
pip install opencv-python shapely geojson Polygon
```

## 使用方法
1. **准备输入图像**  
   将需要处理的 PNG 格式地图图像命名为 `map.jpg` 并放置在项目根目录下。

2. **运行脚本**  
   在终端中运行以下命令：
   ```
   python main.py
   ```

3. **输出结果**  
   脚本运行完成后，会在项目根目录生成一个名为 `mapData.json` 的文件，其中包含转换后的 GeoJSON 数据。

## 文件说明
- `main.py`：主脚本，负责图像处理和 GeoJSON 文件生成。
- `map.jpg`：输入的地图图像文件。
- `mapData.json`：输出的 GeoJSON 文件，包含地图轮廓的坐标数据。

## 注意事项
- 输入图像应为清晰的二值化地图，以便更好地检测轮廓。
- 如果脚本运行时出现错误，请检查输入图像是否符合要求，或调整代码中阈值处理的参数。

## 示例
以下是一个简单的示例：

**输入图像**  
![map.jpg](/map.jpg)

**输出 GeoJSON**  
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]]
      },
      "properties": {}
    }
  ]
}
```

## 依赖版本
- Python 版本：3.8 或更高
- OpenCV：`opencv-python`
- Shapely：`shapely`
- GeoJSON：`geojson`

## 许可证
本项目遵循 MIT 许可证。
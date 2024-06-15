# 自定义名字生成器

这是一个简单的名字生成器应用程序，用于随机生成姓和名的组合。  
其中生成的姓和名需要手动输入根目录下的'NameLibrary'文件夹中的 `surname.txt` 和 `name.txt` 文件中。  
为了方便，已经提前写入了一些常见的姓和名。  

## 如何使用

1. 克隆或下载本项目到本地计算机。
2. 运行 `name_generator.exe` 文件以启动应用程序。
3. 点击 "生成" 按钮即可生成随机名字。
4. 点击 "复制" 按钮可以复制生成的名字到剪贴板。

## 文件结构

- `name_generator.py`：主程序文件，包含名字生成器的逻辑。
- `favicon.ico`：应用程序图标。
- `surname.txt`：姓库文件，存储姓的列表。
- `name.txt`：名字库文件，存储名字的列表。

## 注意事项

- 如果需要添加新的姓或名字，可以编辑根目录下的'NameLibrary'文件夹中的 `surname.txt` 和 `name.txt` 文件文本文件并保存。
- 目前是姓在名前的，适用于汉语等姓在名前的语言。
- 这只是本人练习python和github发布的一个习作，没啥含金量，目前比较简陋，之后还准备添加新功能。

## 版权与许可

- 作者：Rinmiolc
- 版权所有 © 2024 Rinmiolc. 保留所有权利。

该项目采用 MIT 许可证，详情请查阅 [LICENSE.txt](LICENSE.txt) 文件。

## 反馈

如果您发现任何问题或有改进建议，请提出 issue 或提交 pull request，或联系邮箱 rinmiolc@outlook.com

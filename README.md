# GameTimeTracker

这是一个计时和统计工具，可以用于记录游戏过程中的时间、击打次数、失败次数等信息，并将结果复制到剪贴板。
[在这里下载Windows可执行程序](https://github.com/HKLHaoBin/GameTimeTracker/actions/runs/12288939622)

## 功能

- 记录并格式化时间
- 统计击打次数、失败次数
- 计算胜利条件并复制结果到剪贴板

## 安装

1. 确保你已经安装了 Python。
2. 克隆此仓库到本地：

```bash
git clone <仓库地址>
```

3. 安装依赖库：

```bash
pip install -r requirements.txt
```

## 使用方法

1. 运行 `game_time_tracker.py`：

```bash
python game_time_tracker.py
```

2. 根据提示输入对应的指令：

- `回车`：增加一次击打并显示结果
- `d`：增加一次失败并显示结果
- `end`：结束程序
- `t`：修改时间
- `+t`：增加时间
- `tt`：重置时间并修改
- `dd`：修改死亡次数
- `p`：暂停并继续计时
- `now`：显示当前结果
- `win`：设置胜利并显示结果

## 示例

```plaintext
start_time 1669826400.123456

end_time 1669827600.654321
用时1小时20分钟30秒,被5次击打,失败共2次后胜利!
```

## 依赖

- `time`: Python 内置库
- `pyperclip`: 用于复制结果到剪贴板

## 许可证

此项目遵循 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

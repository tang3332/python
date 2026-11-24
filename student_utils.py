"""实验4任务7所需的工具模块：学生记录解析函数。

放在 Notebook 同级目录，供 import 调用。
"""


def parse_student(line):
    """把一行 'name,score' 文本解析为字典。

    校验：字段数量、姓名非空、成绩为整数且在 0~100 之间。
    任何一项不满足都抛出 ValueError。
    """
    parts = line.split(",")

    # 1. 字段数量必须是 2
    if len(parts) != 2:
        raise ValueError(f"字段数量应为 2，实际为 {len(parts)}")

    name = parts[0].strip()
    score_str = parts[1].strip()

    # 2. 姓名不能为空
    if not name:
        raise ValueError("姓名为空")

    # 3. 成绩必须能转成整数
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩无法转换为整数：{score_str!r}")

    # 4. 成绩必须在 0~100 范围内
    if not (0 <= score <= 100):
        raise ValueError(f"成绩超出 0~100 范围：{score}")

    return {"name": name, "score": score}

#!/usr/bin/env python3
with open("test_report_16_keys.md", "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.split("\n")

print("检查第 2 个表格的分隔符和表头:")
found = False
for i, line in enumerate(lines):
    if "模型-API密钥可用性矩阵 (第 2 部分)" in line:
        found = True
        for j in range(i, min(i+15, len(lines))):
            print(f"行 {j}: {repr(lines[j])}")
        break
if not found:
    print("未找到第 2 部分")

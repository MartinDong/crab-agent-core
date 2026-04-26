#!/usr/bin/env python3
test_ids = ["KEY_10", "KEY_11", "KEY_12", "KEY_13", "KEY_14", "KEY_15", "KEY_16"]
header = "| 模型名称 | " + " | ".join(test_ids) + " |"
print(repr(header))
separator = "|----------|" + "|".join(["----------" for _ in test_ids]) + "|"
print(repr(separator))

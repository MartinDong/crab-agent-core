
#!/usr/bin/env python3
"""
Test script for WeatherSkill
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from skills import WeatherSkill

print("="*60)
print("测试 WeatherSkill")
print("="*60)

skill = WeatherSkill()

print("\n1. 测试北京天气查询...")
result = skill.execute("北京")
print(result)

print("\n2. 测试上海天气查询...")
result = skill.execute("上海")
print(result)

print("\n3. 测试广州天气查询...")
result = skill.execute("广州")
print(result)

print("\n" + "="*60)
print("测试完成！")
print("="*60)

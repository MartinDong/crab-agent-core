#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from qianfan_model_tester import QianfanModelTester


def test_table_splitting():
    """测试表格分割功能在不同列数下的表现"""
    print("=" * 80)
    print("测试表格分割功能")
    print("=" * 80)
    
    # 测试 1: 正好 10 列 (9 个密钥 + 模型名称)
    print("\n\n--- 测试 1: 正好 10 列 ---")
    test_case_1 = create_test_summary(9)
    tester1 = QianfanModelTester(api_keys=[f"key_{i}" for i in range(1, 10)])
    report1 = tester1.generate_markdown_report(test_case_1)
    print(report1)
    print("=" * 80)
    
    # 测试 2: 11 列 (10 个密钥)
    print("\n\n--- 测试 2: 11 列 (10 个密钥) ---")
    test_case_2 = create_test_summary(10)
    tester2 = QianfanModelTester(api_keys=[f"key_{i}" for i in range(1, 11)])
    report2 = tester2.generate_markdown_report(test_case_2)
    print(report2)
    print("=" * 80)
    
    # 测试 3: 超过 10 列，例如 16 个密钥 (17 列)
    print("\n\n--- 测试 3: 超过 10 列，16 个密钥 (17 列) ---")
    test_case_3 = create_test_summary(16)
    tester3 = QianfanModelTester(api_keys=[f"key_{i}" for i in range(1, 17)])
    report3 = tester3.generate_markdown_report(test_case_3)
    print(report3)
    print("=" * 80)
    
    # 将测试 3 保存为文件
    test_case_3 = create_test_summary(16)
    tester3 = QianfanModelTester(api_keys=[f"key_{i}" for i in range(1, 17)])
    report3 = tester3.generate_markdown_report(test_case_3)
    
    # 保存到文件
    output_filename = "test_report_16_keys.md"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(report3)
    print(f"\n✅ 所有测试完成！16 密钥报告已保存到 {os.path.abspath(output_filename)}")


def create_test_summary(num_api_keys):
    """创建用于测试的模拟数据"""
    from datetime import datetime

    api_keys = [f"KEY_{i+1}" for i in range(num_api_keys)]
    models = [f"model_{i+1}" for i in range(5)]  # 5 个模型
    
    overall_summary = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "api_keys_count": num_api_keys,
        "duration": 10.5,
        "keys_results": {}
    }
    
    for api_key_id in api_keys:
        key_result = {
            "api_key_id": api_key_id,
            "api_key_display": f"bce-v3/...",
            "model_list_status": "成功",
            "model_list": [{"id": m} for m in models],
            "test_results": [],
            "summary": {
                "total_models": len(models),
                "passed": 3,
                "failed": 1,
                "timeout": 1,
                "exceptions": []
            }
        }
        
        # 为每个模型创建测试结果
        for idx, model in enumerate(models):
            results = ["通过", "失败", "超时"]
            key_result["test_results"].append({
                "model_name": model,
                "test_result": results[idx % 3]
            })
        
        overall_summary["keys_results"][api_key_id] = key_result
    
    return overall_summary


if __name__ == "__main__":
    test_table_splitting()

#!/usr/bin/env python3
import os
import re
import requests
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional, Set
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from dotenv import load_dotenv

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(dotenv_path=os.path.join(PROJECT_ROOT, ".env"))


class QianfanModelTester:
    """百度千帆模型自动化测试工具 - 支持多API密钥和并发测试"""

    @staticmethod
    def fetch_webpage_content(url: str, timeout: int = 30) -> Optional[str]:
        """
        获取网页内容
        
        Args:
            url: 目标网页URL
            timeout: 请求超时时间（秒）
        
        Returns:
            网页HTML内容，失败返回None
        """
        try:
            print(f"正在获取网页内容: {url}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            print(f"成功获取网页内容，长度: {len(response.text)} 字符")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"获取网页内容失败: {str(e)}")
            return None
        except Exception as e:
            print(f"获取网页时发生未知错误: {str(e)}")
            return None

    @staticmethod
    def extract_api_keys_from_content(content: str) -> List[str]:
        """
        从网页内容中提取API密钥
        
        Args:
            content: 网页HTML内容
        
        Returns:
            去重后的API密钥列表
        """
        if not content:
            print("未提供有效的网页内容")
            return []
        
        print("正在从网页内容中提取API密钥...")
        
        # 正则表达式匹配 bce-v3/AL 开头的API密钥
        # 格式通常为 bce-v3/AK/SK，其中AK和SK是字母数字组合
        pattern = r'bce-v3/AL[^"\s\'<>`]+'
        
        matches = re.findall(pattern, content)
        
        if not matches:
            print("未找到匹配的API密钥")
            return []
        
        # 去重处理
        unique_keys: Set[str] = set()
        for key in matches:
            # 清理可能的尾部字符
            cleaned_key = key.strip()
            # 简单验证密钥格式
            if cleaned_key.startswith("bce-v3/AL") and len(cleaned_key) > len("bce-v3/AL"):
                unique_keys.add(cleaned_key)
        
        result = list(unique_keys)
        print(f"找到 {len(matches)} 个匹配项，去重后保留 {len(result)} 个有效API密钥")
        
        if result:
            for i, key in enumerate(result, 1):
                print(f"  [{i}] {key[:40]}...")
        
        return result

    @staticmethod
    def load_config(config_file: str = "qianfan_config.json") -> Dict[str, Any]:
        """
        从 JSON 配置文件加载配置
        
        Args:
            config_file: 配置文件路径，默认为 qianfan_config.json
        
        Returns:
            配置字典
        """
        if not os.path.exists(config_file):
            return {}
        
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"读取配置文件 {config_file} 失败: {str(e)}")
            return {}

    def __init__(self, api_keys: Optional[List[str]] = None, base_url: Optional[str] = None, max_workers: int = 20, config_file: Optional[str] = None, github_search_url: Optional[str] = None):
        """
        初始化千帆模型测试工具
        
        Args:
            api_keys: 百度千帆API密钥列表，每个格式为 bce-v3/AK/SK
            base_url: 百度千帆API基础地址
            max_workers: 并发测试的最大线程数
            config_file: JSON 配置文件路径，优先级高于环境变量和直接参数
            github_search_url: GitHub搜索页面URL，用于自动获取API密钥
        """
        config = {}
        if config_file:
            config = self.load_config(config_file)
        else:
            default_config_path = os.path.join(os.path.dirname(__file__), "qianfan_config.json")
            if os.path.exists(default_config_path):
                config = self.load_config(default_config_path)
        
        self.base_url = base_url or config.get("base_url") or os.getenv("QIANFAN_API_BASE", "https://qianfan.baidubce.com")
        self.max_workers = max_workers or config.get("max_workers", 5)
        
        if api_keys:
            self.api_keys = api_keys
        elif "api_keys" in config and config["api_keys"]:
            self.api_keys = config["api_keys"]
        else:
            api_keys_str = os.getenv("QIANFAN_API_KEYS") or os.getenv("QIANFAN_API_KEY")
            if api_keys_str:
                self.api_keys = [key.strip() for key in api_keys_str.split(",") if key.strip()]
            else:
                self.api_keys = []
        
        # 如果没有找到密钥，尝试从GitHub搜索页面获取
        if not self.api_keys:
            # 优先使用传入的URL，其次使用配置文件中的URL，最后使用默认URL
            search_url = (
                github_search_url 
                or config.get("github_search_url") 
                or os.getenv("QIANFAN_GITHUB_SEARCH_URL")
                or "https://github.com/search?q=https%3A%2F%2Fqianfan.baidubce.com+bce-v3%2FAL&type=code"
            )
            
            print("\n" + "=" * 60)
            print("尝试从GitHub搜索页面获取API密钥...")
            print("=" * 60)
            
            webpage_content = self.fetch_webpage_content(search_url)
            if webpage_content:
                extracted_keys = self.extract_api_keys_from_content(webpage_content)
                if extracted_keys:
                    self.api_keys = extracted_keys
                    print("成功从GitHub搜索页面获取API密钥")
                else:
                    print("GitHub搜索页面未找到有效的API密钥")
            else:
                print("无法获取GitHub搜索页面内容")
        
        if not self.api_keys:
            config_example = os.path.join(os.path.dirname(__file__), "qianfan_config.example.json")
            raise ValueError(f"API密钥未配置。\n请使用以下方式之一配置：\n1. 创建配置文件 qianfan_config.json（可参考 {config_example}）\n2. 设置环境变量 QIANFAN_API_KEYS（逗号分隔多个密钥）\n3. 在初始化时传入 api_keys 参数\n4. 传入 github_search_url 参数从GitHub搜索页面获取")
        
        self.test_results = {}
        self.start_time = None
        self.end_time = None
        self.lock = Lock()

    def get_headers(self, api_key: str) -> Dict[str, str]:
        """为指定API密钥构建请求头"""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def get_model_list(self, api_key: str) -> Optional[List[Dict[str, Any]]]:
        """获取指定API密钥的模型列表"""
        url = f"{self.base_url}/v2/models"
        try:
            response = requests.get(url, headers=self.get_headers(api_key), timeout=30)
            response.raise_for_status()
            result = response.json()
            if result.get("object") == "list":
                return result.get("data", [])
            return None
        except Exception as e:
            print(f"获取模型列表失败 (密钥: {api_key[:20]}...): {str(e)}")
            return None

    def test_model_inference(self, model_id: str, api_key: str, api_key_id: str) -> Dict[str, Any]:
        """测试单个模型的推理通路"""
        result = {
            "model_name": model_id,
            "api_key_id": api_key_id,
            "request_params": None,
            "response_status": None,
            "response_time": None,
            "test_result": None,
            "error_message": None,
            "response_data": None
        }

        url = f"{self.base_url}/v2/chat/completions"
        payload = {
            "model": model_id,
            "messages": [
                {"role": "user", "content": "你好，请用一句话介绍一下你自己"}
            ]
        }
        result["request_params"] = payload

        try:
            start_time = time.time()
            response = requests.post(url, headers=self.get_headers(api_key), json=payload, timeout=60)
            end_time = time.time()

            result["response_status"] = response.status_code
            result["response_time"] = round((end_time - start_time) * 1000, 2)
            result["response_data"] = response.json()

            if response.status_code == 200:
                response_data = response.json()
                if "choices" in response_data and len(response_data["choices"]) > 0:
                    result["test_result"] = "通过"
                else:
                    result["test_result"] = "失败"
                    result["error_message"] = "响应格式不符合预期"
            else:
                result["test_result"] = "失败"
                result["error_message"] = f"HTTP错误: {response.status_code}"

        except requests.exceptions.Timeout:
            result["test_result"] = "超时"
            result["error_message"] = "请求超时"
        except requests.exceptions.ConnectionError:
            result["test_result"] = "失败"
            result["error_message"] = "网络连接错误"
        except Exception as e:
            result["test_result"] = "失败"
            result["error_message"] = str(e)

        return result

    def run_tests_for_key(self, api_key: str, api_key_id: str) -> Dict[str, Any]:
        """为单个API密钥运行测试"""
        key_results = {
            "api_key_id": api_key_id,
            "api_key_display": f"{api_key[:20]}...",
            "model_list_status": "失败",
            "model_list": None,
            "test_results": [],
            "summary": {
                "total_models": 0,
                "passed": 0,
                "failed": 0,
                "timeout": 0,
                "exceptions": []
            }
        }

        model_list = self.get_model_list(api_key)
        
        if model_list:
            key_results["model_list_status"] = "成功"
            key_results["model_list"] = model_list
            key_results["summary"]["total_models"] = len(model_list)

            print(f"\n[密钥 {api_key_id}] 开始测试 {len(model_list)} 个模型...")
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {
                    executor.submit(self.test_model_inference, model.get("id", "unknown"), api_key, api_key_id): model
                    for model in model_list
                }

                for idx, future in enumerate(as_completed(futures), 1):
                    model = futures[future]
                    model_id = model.get("id", "unknown")
                    try:
                        test_result = future.result()
                        key_results["test_results"].append(test_result)
                        
                        with self.lock:
                            if test_result["test_result"] == "通过":
                                key_results["summary"]["passed"] += 1
                                result_icon = "✅ 通过"
                            elif test_result["test_result"] == "超时":
                                key_results["summary"]["timeout"] += 1
                                result_icon = "⏱️ 超时"
                            else:
                                key_results["summary"]["failed"] += 1
                                key_results["summary"]["exceptions"].append({
                                    "model": model_id,
                                    "error": test_result["error_message"]
                                })
                                result_icon = "❌ 失败"
                        
                        print(f"  [{idx}/{len(model_list)}] {model_id}: {result_icon}")
                    except Exception as e:
                        print(f"  [{idx}/{len(model_list)}] {model_id}: ❌ 测试异常: {str(e)}")

        return key_results

    def run_tests(self) -> Dict[str, Any]:
        """运行完整的测试流程"""
        self.start_time = datetime.now()
        overall_summary = {
            "timestamp": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "api_keys_count": len(self.api_keys),
            "keys_results": {}
        }

        print("=" * 60)
        print(f"千帆模型自动化测试工具 - 多密钥并发测试")
        print(f"配置了 {len(self.api_keys)} 个API密钥")
        print(f"最大并发数: {self.max_workers}")
        print("=" * 60)

        for idx, api_key in enumerate(self.api_keys, 1):
            api_key_id = f"KEY_{idx}"
            print(f"\n开始测试 API密钥 {api_key_id}: {api_key[:30]}...")
            
            key_result = self.run_tests_for_key(api_key, api_key_id)
            overall_summary["keys_results"][api_key_id] = key_result
            
            with self.lock:
                self.test_results[api_key_id] = key_result

        self.end_time = datetime.now()
        overall_summary["duration"] = (self.end_time - self.start_time).total_seconds()

        return overall_summary

    def generate_markdown_report(self, overall_summary: Dict[str, Any]) -> str:
        """生成Markdown格式的测试报告 - 以模型为行，API密钥为列，每表最多10列"""
        report_lines = []
        report_lines.append("# 千帆模型自动化测试报告\n")
        report_lines.append(f"**测试时间**: {overall_summary['timestamp']}\n")
        report_lines.append(f"**测试时长**: {round(overall_summary['duration'], 2)} 秒\n")
        report_lines.append(f"**API密钥数量**: {overall_summary['api_keys_count']}\n")
        report_lines.append(f"**环境信息**: Windows / Python 3\n\n")

        model_key_map = {}
        api_key_ids = list(overall_summary["keys_results"].keys())

        for api_key_id, key_result in overall_summary["keys_results"].items():
            for test_result in key_result["test_results"]:
                model_name = test_result["model_name"]
                if model_name not in model_key_map:
                    model_key_map[model_name] = {}
                model_key_map[model_name][api_key_id] = test_result["test_result"]

        sorted_model_names = sorted(model_key_map.keys())

        # 每表最多 10 列（模型名称 + 9 个密钥）
        max_columns_per_table = 10
        num_api_keys = len(api_key_ids)
        num_tables = (num_api_keys + max_columns_per_table - 2) // (max_columns_per_table - 1)

        for table_idx in range(num_tables):
            start_col = table_idx * (max_columns_per_table - 1)
            end_col = min(start_col + (max_columns_per_table - 1), num_api_keys)
            table_api_key_ids = api_key_ids[start_col:end_col]

            if table_idx > 0:
                report_lines.append("\n")
            report_lines.append(f"## 模型-API密钥可用性矩阵 (第 {table_idx + 1} 部分)\n")
            
            header = "| 模型名称 | " + " | ".join(table_api_key_ids) + " |"
            report_lines.append(header.rstrip())
            separator = "|----------|" + "|".join(["----------" for _ in table_api_key_ids]) + "|"
            report_lines.append(separator.rstrip())

            for model_name in sorted_model_names:
                row = [model_name]
                for api_key_id in table_api_key_ids:
                    result = model_key_map[model_name].get(api_key_id, "-")
                    if result == "通过":
                        row.append("✅")
                    elif result == "超时":
                        row.append("⏱️")
                    elif result == "失败":
                        row.append("❌")
                    else:
                        row.append("-")
                report_line = "| " + " | ".join(row) + " |"
                report_lines.append(report_line.rstrip())

        report_lines.append("\n")
        report_lines.append("**说明**：\n")
        report_lines.append("- ✅: 测试通过\n")
        report_lines.append("- ⏱️: 测试超时\n")
        report_lines.append("- ❌: 测试失败\n")
        report_lines.append("- -: 未测试\n")

        return "\n".join(report_lines)

    def save_report(self, report_content: str, filename: str = None):
        """保存测试报告到文件"""
        if filename is None:
            filename = f"qianfan_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        filepath = f"e:\\Crab\\crab-agent-core\\demos\\{filename}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(report_content)

        print(f"\n测试报告已保存到: {filepath}")
        return filepath


def test_extract_from_github():
    """
    独立测试函数：仅测试从GitHub搜索页面提取API密钥的功能
    """
    print("=" * 60)
    print("GitHub API密钥提取测试")
    print("=" * 60)
    
    github_url = "https://github.com/search?q=https%3A%2F%2Fqianfan.baidubce.com+bce-v3%2FAL&type=code"
    
    # 获取网页内容
    content = QianfanModelTester.fetch_webpage_content(github_url)
    
    if not content:
        print("\n测试失败：无法获取网页内容")
        return
    
    # 提取API密钥
    api_keys = QianfanModelTester.extract_api_keys_from_content(content)
    
    if api_keys:
        print(f"\n✅ 测试成功！提取到 {len(api_keys)} 个API密钥")
    else:
        print("\n⚠️ 未找到API密钥")
    
    print("=" * 60)


def main():
    """主函数：执行千帆模型自动化测试"""
    try:
        tester = QianfanModelTester()
    except ValueError as e:
        print(f"配置错误: {e}")
        return

    overall_summary = tester.run_tests()

    print("\n" + "=" * 60)
    print("测试完成!")
    for api_key_id, key_result in overall_summary["keys_results"].items():
        print(f"  {api_key_id}: 通过={key_result['summary']['passed']}, 失败={key_result['summary']['failed']}, 超时={key_result['summary']['timeout']}")
    print(f"总耗时: {round(overall_summary['duration'], 2)} 秒")
    print("=" * 60)

    report = tester.generate_markdown_report(overall_summary)
    tester.save_report(report)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test-extract":
        test_extract_from_github()
    else:
        main()

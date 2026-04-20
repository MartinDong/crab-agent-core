# 千帆模型自动化测试报告

**测试时间**: 2026-04-20 23:49:34

**测试时长**: 4742.95 秒

**API密钥数量**: 54

**环境信息**: Windows / Python 3


---


## API密钥: KEY_1

**密钥显示**: bce-v3/ALTAK-mdpXzVb...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 105 |
| 失败 | 44 |
| 超时 | 44 |
| 通过率 | 54.4% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-char-fiction-8k**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1099.68 | ❌ 失败 | HTTP错误: 403 |
| 2 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1209.4 | ❌ 失败 | HTTP错误: 500 |
| 3 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1348.79 | ❌ 失败 | HTTP错误: 403 |
| 4 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 424.13 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1887.79 | ✅ 通过 | - |
| 6 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 1903.29 | ✅ 通过 | - |
| 7 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 1969.19 | ✅ 通过 | - |
| 8 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 2467.39 | ✅ 通过 | - |
| 9 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2469.99 | ✅ 通过 | - |
| 10 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 2495.7 | ✅ 通过 | - |
| 11 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2488.32 | ✅ 通过 | - |
| 12 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 200 | 2546.64 | ✅ 通过 | - |
| 13 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 2628.93 | ✅ 通过 | - |
| 14 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2656.7 | ✅ 通过 | - |
| 15 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2841.39 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 2954.83 | ✅ 通过 | - |
| 17 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2918.59 | ✅ 通过 | - |
| 18 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 3118.63 | ✅ 通过 | - |
| 19 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3328.4 | ✅ 通过 | - |
| 20 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1201.85 | ✅ 通过 | - |
| 21 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 4937.91 | ✅ 通过 | - |
| 22 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2050.6 | ✅ 通过 | - |
| 23 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 524.89 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 534.87 | ❌ 失败 | HTTP错误: 429 |
| 25 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2230.83 | ✅ 通过 | - |
| 26 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1484.4 | ✅ 通过 | - |
| 27 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 7102.31 | ✅ 通过 | - |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 351.48 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 425.19 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1365.17 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 439.47 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 328.09 | ❌ 失败 | HTTP错误: 403 |
| 33 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 9512.18 | ✅ 通过 | - |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 2312.76 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 388.26 | ❌ 失败 | HTTP错误: 403 |
| 36 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 2078.77 | ✅ 通过 | - |
| 37 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 433.56 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 431.71 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 859.74 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 1608.13 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 357.75 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 2442.46 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1257.82 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1096.4 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 839.56 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 1004.65 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 808.12 | ✅ 通过 | - |
| 48 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 8980.69 | ✅ 通过 | - |
| 49 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1135.91 | ✅ 通过 | - |
| 50 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 896.36 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 850.18 | ✅ 通过 | - |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1522.4 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 1702.05 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1317.18 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1300.57 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 8889.53 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 716.83 | ✅ 通过 | - |
| 66 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1055.38 | ✅ 通过 | - |
| 71 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 814.95 | ✅ 通过 | - |
| 74 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 1006.74 | ✅ 通过 | - |
| 75 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 977.42 | ✅ 通过 | - |
| 76 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2169.86 | ✅ 通过 | - |
| 78 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 584.29 | ❌ 失败 | HTTP错误: 403 |
| 79 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1698.88 | ✅ 通过 | - |
| 80 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 981.07 | ✅ 通过 | - |
| 81 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1748.69 | ✅ 通过 | - |
| 82 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 1690.31 | ✅ 通过 | - |
| 83 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1031.62 | ✅ 通过 | - |
| 84 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 607.94 | ❌ 失败 | HTTP错误: 403 |
| 85 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 861.16 | ✅ 通过 | - |
| 86 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 2103.84 | ✅ 通过 | - |
| 87 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2911.1 | ✅ 通过 | - |
| 90 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1187.4 | ✅ 通过 | - |
| 91 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1144.97 | ✅ 通过 | - |
| 92 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1294.16 | ✅ 通过 | - |
| 93 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1418.7 | ✅ 通过 | - |
| 94 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2319.01 | ✅ 通过 | - |
| 95 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 96 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 2107.14 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 312.75 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 376.6 | ❌ 失败 | HTTP错误: 403 |
| 99 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 606.89 | ✅ 通过 | - |
| 100 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1261.01 | ✅ 通过 | - |
| 101 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6722.71 | ✅ 通过 | - |
| 102 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 641.09 | ✅ 通过 | - |
| 103 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 5843.44 | ✅ 通过 | - |
| 104 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 655.51 | ✅ 通过 | - |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1738.79 | ✅ 通过 | - |
| 106 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 1873.96 | ✅ 通过 | - |
| 107 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 12575.17 | ✅ 通过 | - |
| 108 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 7025.31 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1873.1 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 17373.7 | ✅ 通过 | - |
| 111 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1868.83 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 4580.65 | ✅ 通过 | - |
| 113 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 6835.45 | ✅ 通过 | - |
| 114 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 115 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 2393.31 | ✅ 通过 | - |
| 116 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 17321.16 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 908.18 | ✅ 通过 | - |
| 118 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 3945.61 | ✅ 通过 | - |
| 119 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 120 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 5063.6 | ✅ 通过 | - |
| 121 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 8724.78 | ✅ 通过 | - |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 2417.44 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2575.64 | ✅ 通过 | - |
| 124 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 13913.94 | ✅ 通过 | - |
| 125 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 17526.15 | ✅ 通过 | - |
| 126 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 11451.19 | ✅ 通过 | - |
| 127 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 129 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 754.72 | ✅ 通过 | - |
| 133 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 612.81 | ❌ 失败 | HTTP错误: 500 |
| 134 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 135 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 452.24 | ❌ 失败 | HTTP错误: 403 |
| 140 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 531.67 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 536.46 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 523.47 | ❌ 失败 | HTTP错误: 500 |
| 144 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1149.07 | ✅ 通过 | - |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 473.98 | ❌ 失败 | HTTP错误: 500 |
| 147 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 148 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 556.49 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 652.62 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 1016.41 | ❌ 失败 | HTTP错误: 500 |
| 151 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 943.82 | ✅ 通过 | - |
| 152 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2436.92 | ✅ 通过 | - |
| 153 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 9739.9 | ✅ 通过 | - |
| 154 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1317.96 | ✅ 通过 | - |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1038.16 | ✅ 通过 | - |
| 156 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2448.64 | ✅ 通过 | - |
| 157 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1016.02 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 474.01 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 518.0 | ❌ 失败 | HTTP错误: 500 |
| 160 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1095.08 | ✅ 通过 | - |
| 161 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1351.36 | ✅ 通过 | - |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 496.74 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 518.6 | ❌ 失败 | HTTP错误: 500 |
| 164 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2116.85 | ✅ 通过 | - |
| 165 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 526.17 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 529.29 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 562.56 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 558.97 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 547.91 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 540.63 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 549.77 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 762.69 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 516.82 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 551.37 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 531.58 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 527.97 | ❌ 失败 | HTTP错误: 500 |
| 177 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1577.73 | ✅ 通过 | - |
| 178 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 9265.51 | ✅ 通过 | - |
| 181 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 7718.43 | ✅ 通过 | - |
| 182 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 8976.96 | ✅ 通过 | - |
| 183 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 11915.04 | ✅ 通过 | - |
| 184 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 15689.9 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_2

**密钥显示**: bce-v3/ALTAK-z6Nrmu8...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 20 |
| 失败 | 144 |
| 超时 | 29 |
| 通过率 | 10.36% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-x1-32k-preview**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-publicopinion-classification**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **qianfan-engcard-vl**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **qwen-image-edit**: HTTP错误: 429

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **kimi-k2.5**: HTTP错误: 403

- **minimax-m2.5**: HTTP错误: 403

- **glm-5**: HTTP错误: 403

- **qwen3.5-122b-a10b**: HTTP错误: 403

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **glm-5.1**: HTTP错误: 403

- **kling-custom-voices_voices**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1119.39 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1132.01 | ❌ 失败 | HTTP错误: 403 |
| 3 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1094.2 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1164.79 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1161.43 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1162.67 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1200.87 | ❌ 失败 | HTTP错误: 403 |
| 8 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1169.22 | ❌ 失败 | HTTP错误: 429 |
| 9 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1226.82 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1217.23 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1259.43 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1282.08 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1306.23 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1342.39 | ❌ 失败 | HTTP错误: 403 |
| 15 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1302.09 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1378.72 | ❌ 失败 | HTTP错误: 403 |
| 17 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1352.22 | ❌ 失败 | HTTP错误: 403 |
| 18 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1322.95 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1524.01 | ❌ 失败 | HTTP错误: 403 |
| 20 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1579.94 | ❌ 失败 | HTTP错误: 403 |
| 21 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1016.78 | ❌ 失败 | HTTP错误: 403 |
| 22 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1112.11 | ❌ 失败 | HTTP错误: 403 |
| 23 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1060.12 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1076.02 | ❌ 失败 | HTTP错误: 403 |
| 25 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 966.4 | ❌ 失败 | HTTP错误: 429 |
| 26 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 578.73 | ❌ 失败 | HTTP错误: 429 |
| 27 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 635.69 | ❌ 失败 | HTTP错误: 403 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 465.54 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 518.73 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 502.18 | ❌ 失败 | HTTP错误: 429 |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 399.71 | ❌ 失败 | HTTP错误: 429 |
| 32 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 664.83 | ❌ 失败 | HTTP错误: 403 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 380.24 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 356.75 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 428.98 | ❌ 失败 | HTTP错误: 403 |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 409.31 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3339.06 | ✅ 通过 | - |
| 38 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 355.77 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 402.06 | ❌ 失败 | HTTP错误: 403 |
| 40 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 521.41 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 389.22 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 508.92 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 500.82 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 717.71 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 471.72 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 528.88 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 354.31 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 510.65 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 492.33 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 437.8 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 438.85 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 497.72 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 498.28 | ❌ 失败 | HTTP错误: 403 |
| 54 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 404.43 | ❌ 失败 | HTTP错误: 403 |
| 55 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 432.19 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 510.86 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 568.38 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | 403 | 399.57 | ❌ 失败 | HTTP错误: 403 |
| 59 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 592.41 | ❌ 失败 | HTTP错误: 403 |
| 60 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 540.06 | ❌ 失败 | HTTP错误: 403 |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 835.39 | ✅ 通过 | - |
| 62 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 856.07 | ✅ 通过 | - |
| 63 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 433.47 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 559.72 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 391.28 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 370.77 | ❌ 失败 | HTTP错误: 403 |
| 67 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 429.7 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 410.27 | ❌ 失败 | HTTP错误: 403 |
| 69 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 426.27 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 551.42 | ❌ 失败 | HTTP错误: 403 |
| 71 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 321.18 | ❌ 失败 | HTTP错误: 403 |
| 72 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 381.45 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 337.62 | ❌ 失败 | HTTP错误: 403 |
| 74 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 375.65 | ❌ 失败 | HTTP错误: 403 |
| 75 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 406.75 | ❌ 失败 | HTTP错误: 403 |
| 76 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 84 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 86 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 87 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 708.43 | ❌ 失败 | HTTP错误: 403 |
| 91 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 717.3 | ❌ 失败 | HTTP错误: 403 |
| 92 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 787.79 | ❌ 失败 | HTTP错误: 403 |
| 93 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 839.99 | ❌ 失败 | HTTP错误: 403 |
| 96 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 882.72 | ❌ 失败 | HTTP错误: 403 |
| 97 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 918.19 | ❌ 失败 | HTTP错误: 403 |
| 98 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 935.16 | ❌ 失败 | HTTP错误: 403 |
| 99 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 921.26 | ❌ 失败 | HTTP错误: 403 |
| 100 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 101 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 891.05 | ❌ 失败 | HTTP错误: 429 |
| 102 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 862.49 | ❌ 失败 | HTTP错误: 429 |
| 103 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 893.69 | ❌ 失败 | HTTP错误: 429 |
| 104 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 940.6 | ❌ 失败 | HTTP错误: 403 |
| 105 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 943.81 | ❌ 失败 | HTTP错误: 403 |
| 106 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 881.16 | ❌ 失败 | HTTP错误: 429 |
| 107 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 874.63 | ❌ 失败 | HTTP错误: 429 |
| 108 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 895.24 | ❌ 失败 | HTTP错误: 403 |
| 109 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 977.49 | ❌ 失败 | HTTP错误: 403 |
| 110 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 982.15 | ❌ 失败 | HTTP错误: 403 |
| 111 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 938.71 | ❌ 失败 | HTTP错误: 403 |
| 112 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 1000.47 | ❌ 失败 | HTTP错误: 403 |
| 113 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 960.83 | ❌ 失败 | HTTP错误: 403 |
| 114 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 875.36 | ❌ 失败 | HTTP错误: 403 |
| 115 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 894.02 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 1017.55 | ❌ 失败 | HTTP错误: 403 |
| 117 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 923.86 | ❌ 失败 | HTTP错误: 403 |
| 118 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 965.07 | ❌ 失败 | HTTP错误: 403 |
| 119 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 945.19 | ❌ 失败 | HTTP错误: 403 |
| 120 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 1017.02 | ❌ 失败 | HTTP错误: 403 |
| 121 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 850.2 | ❌ 失败 | HTTP错误: 429 |
| 122 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 898.61 | ❌ 失败 | HTTP错误: 429 |
| 123 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 867.85 | ❌ 失败 | HTTP错误: 403 |
| 124 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 876.26 | ❌ 失败 | HTTP错误: 403 |
| 125 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 926.03 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 804.77 | ❌ 失败 | HTTP错误: 403 |
| 127 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 923.25 | ❌ 失败 | HTTP错误: 403 |
| 128 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 1016.64 | ❌ 失败 | HTTP错误: 403 |
| 129 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 824.36 | ❌ 失败 | HTTP错误: 429 |
| 130 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 1229.39 | ❌ 失败 | HTTP错误: 403 |
| 131 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 928.28 | ❌ 失败 | HTTP错误: 403 |
| 132 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 1122.05 | ❌ 失败 | HTTP错误: 403 |
| 133 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 713.5 | ❌ 失败 | HTTP错误: 403 |
| 134 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 720.66 | ❌ 失败 | HTTP错误: 403 |
| 135 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 732.25 | ❌ 失败 | HTTP错误: 500 |
| 136 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 796.72 | ✅ 通过 | - |
| 137 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 441.84 | ❌ 失败 | HTTP错误: 403 |
| 138 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1770.98 | ✅ 通过 | - |
| 139 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2178.17 | ✅ 通过 | - |
| 140 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 490.73 | ❌ 失败 | HTTP错误: 500 |
| 141 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 492.63 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 526.98 | ❌ 失败 | HTTP错误: 500 |
| 143 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1377.12 | ✅ 通过 | - |
| 144 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 524.76 | ❌ 失败 | HTTP错误: 500 |
| 145 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 146 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 504.71 | ❌ 失败 | HTTP错误: 500 |
| 147 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 443.09 | ❌ 失败 | HTTP错误: 500 |
| 148 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2673.2 | ✅ 通过 | - |
| 149 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 488.2 | ❌ 失败 | HTTP错误: 500 |
| 150 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 403 | 509.13 | ❌ 失败 | HTTP错误: 403 |
| 151 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 813.23 | ✅ 通过 | - |
| 152 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 403 | 386.9 | ❌ 失败 | HTTP错误: 403 |
| 153 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 959.24 | ❌ 失败 | HTTP错误: 403 |
| 154 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2192.28 | ✅ 通过 | - |
| 155 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1338.57 | ✅ 通过 | - |
| 156 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 403 | 444.86 | ❌ 失败 | HTTP错误: 403 |
| 157 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 6874.65 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 498.16 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 382.25 | ❌ 失败 | HTTP错误: 500 |
| 160 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1708.23 | ✅ 通过 | - |
| 161 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 453.71 | ❌ 失败 | HTTP错误: 500 |
| 162 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1138.85 | ✅ 通过 | - |
| 163 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 475.41 | ❌ 失败 | HTTP错误: 500 |
| 164 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 165 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 491.32 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 519.53 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 555.68 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 571.53 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 573.46 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 552.87 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 545.37 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 464.51 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 545.23 | ❌ 失败 | HTTP错误: 500 |
| 174 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 585.61 | ❌ 失败 | HTTP错误: 500 |
| 175 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 403 | 461.18 | ❌ 失败 | HTTP错误: 403 |
| 176 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 587.78 | ❌ 失败 | HTTP错误: 500 |
| 177 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 3077.07 | ✅ 通过 | - |
| 178 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 823.41 | ❌ 失败 | HTTP错误: 500 |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1490.75 | ✅ 通过 | - |
| 180 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 181 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 9988.45 | ✅ 通过 | - |
| 182 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 11380.91 | ✅ 通过 | - |
| 183 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 16288.87 | ✅ 通过 | - |
| 184 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 17133.74 | ✅ 通过 | - |
| 185 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_3

**密钥显示**: bce-v3/ALTAKSP-MhjY1...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_4

**密钥显示**: bce-v3/ALTAK-olfnO0x...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 68 |
| 失败 | 99 |
| 超时 | 26 |
| 通过率 | 35.23% |


### 3. 异常汇总

- **irag-1.0**: HTTP错误: 429

- **deepseek-v3**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **yi-34b-chat**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **aquilachat-7b**: HTTP错误: 403

- **llama-2-13b-chat**: HTTP错误: 403

- **gemma-7b-it**: HTTP错误: 403

- **llama-2-7b-chat**: HTTP错误: 403

- **mixtral-8x7b-instruct**: HTTP错误: 403

- **xuanyuan-70b-chat-4bit**: HTTP错误: 403

- **llama-2-70b-chat**: HTTP错误: 403

- **bloomz-7b**: HTTP错误: 403

- **codellama-7b-instruct**: HTTP错误: 403

- **sqlcoder-7b**: HTTP错误: 403

- **chatglm2-6b-32k**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **qianfan-bloomz-7b-compressed**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 403

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-7b**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 403

- **qianfan-chinese-llama-2-70b**: HTTP错误: 403

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **stable-diffusion-xl**: HTTP错误: 429

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1100.21 | ❌ 失败 | HTTP错误: 429 |
| 2 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1185.34 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1213.05 | ❌ 失败 | HTTP错误: 403 |
| 4 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1204.06 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1307.33 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1279.07 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1325.98 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1323.7 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1371.94 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1402.53 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1403.44 | ❌ 失败 | HTTP错误: 403 |
| 12 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1384.7 | ❌ 失败 | HTTP错误: 403 |
| 13 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1352.36 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1534.94 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1688.07 | ❌ 失败 | HTTP错误: 403 |
| 16 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 871.73 | ❌ 失败 | HTTP错误: 403 |
| 17 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | 403 | 921.03 | ❌ 失败 | HTTP错误: 403 |
| 18 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 924.55 | ❌ 失败 | HTTP错误: 403 |
| 19 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | 403 | 865.62 | ❌ 失败 | HTTP错误: 403 |
| 20 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | 403 | 860.04 | ❌ 失败 | HTTP错误: 403 |
| 21 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | 403 | 907.87 | ❌ 失败 | HTTP错误: 403 |
| 22 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | 403 | 912.76 | ❌ 失败 | HTTP错误: 403 |
| 23 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | 403 | 907.52 | ❌ 失败 | HTTP错误: 403 |
| 24 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | 403 | 845.49 | ❌ 失败 | HTTP错误: 403 |
| 25 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | 403 | 869.04 | ❌ 失败 | HTTP错误: 403 |
| 26 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | 403 | 940.77 | ❌ 失败 | HTTP错误: 403 |
| 27 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | 403 | 1062.55 | ❌ 失败 | HTTP错误: 403 |
| 28 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | 403 | 945.01 | ❌ 失败 | HTTP错误: 403 |
| 29 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | 403 | 1198.86 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 2504.23 | ✅ 通过 | - |
| 31 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 846.78 | ❌ 失败 | HTTP错误: 403 |
| 32 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | 403 | 936.6 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2948.59 | ✅ 通过 | - |
| 34 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 2965.62 | ✅ 通过 | - |
| 35 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 826.99 | ❌ 失败 | HTTP错误: 403 |
| 36 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 2978.14 | ✅ 通过 | - |
| 37 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 843.99 | ❌ 失败 | HTTP错误: 429 |
| 38 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 849.07 | ❌ 失败 | HTTP错误: 403 |
| 39 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 403 | 872.71 | ❌ 失败 | HTTP错误: 403 |
| 40 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 3174.38 | ✅ 通过 | - |
| 41 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 979.91 | ❌ 失败 | HTTP错误: 403 |
| 42 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | 403 | 1024.17 | ❌ 失败 | HTTP错误: 403 |
| 43 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 1060.43 | ❌ 失败 | HTTP错误: 403 |
| 44 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 403 | 973.67 | ❌ 失败 | HTTP错误: 403 |
| 45 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | 403 | 1080.77 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 1018.89 | ❌ 失败 | HTTP错误: 403 |
| 47 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 1027.59 | ❌ 失败 | HTTP错误: 429 |
| 48 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 1004.64 | ❌ 失败 | HTTP错误: 403 |
| 49 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 1060.04 | ❌ 失败 | HTTP错误: 403 |
| 50 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 952.49 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 1017.59 | ❌ 失败 | HTTP错误: 403 |
| 52 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 1121.39 | ❌ 失败 | HTTP错误: 403 |
| 53 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 1103.1 | ❌ 失败 | HTTP错误: 403 |
| 54 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 1050.81 | ❌ 失败 | HTTP错误: 403 |
| 55 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 1146.06 | ❌ 失败 | HTTP错误: 403 |
| 56 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 969.49 | ❌ 失败 | HTTP错误: 403 |
| 57 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 1271.29 | ❌ 失败 | HTTP错误: 403 |
| 58 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 840.65 | ❌ 失败 | HTTP错误: 403 |
| 59 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 978.48 | ❌ 失败 | HTTP错误: 403 |
| 60 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 868.75 | ❌ 失败 | HTTP错误: 403 |
| 61 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 979.89 | ❌ 失败 | HTTP错误: 403 |
| 62 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 884.87 | ❌ 失败 | HTTP错误: 403 |
| 63 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 908.45 | ❌ 失败 | HTTP错误: 403 |
| 64 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 1022.79 | ❌ 失败 | HTTP错误: 403 |
| 65 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 1019.15 | ❌ 失败 | HTTP错误: 403 |
| 66 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2812.6 | ✅ 通过 | - |
| 67 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 1053.63 | ❌ 失败 | HTTP错误: 403 |
| 68 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 1052.84 | ❌ 失败 | HTTP错误: 403 |
| 69 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 1066.52 | ✅ 通过 | - |
| 70 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 1275.12 | ✅ 通过 | - |
| 71 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1357.97 | ✅ 通过 | - |
| 72 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1533.86 | ✅ 通过 | - |
| 73 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1331.05 | ✅ 通过 | - |
| 74 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | 429 | 566.17 | ❌ 失败 | HTTP错误: 429 |
| 75 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 1279.05 | ✅ 通过 | - |
| 76 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 1187.15 | ✅ 通过 | - |
| 77 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1664.46 | ✅ 通过 | - |
| 78 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 586.15 | ❌ 失败 | HTTP错误: 403 |
| 79 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 611.05 | ❌ 失败 | HTTP错误: 403 |
| 80 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1695.75 | ✅ 通过 | - |
| 81 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 611.35 | ❌ 失败 | HTTP错误: 403 |
| 82 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 642.56 | ❌ 失败 | HTTP错误: 403 |
| 83 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 682.03 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 885.49 | ❌ 失败 | HTTP错误: 403 |
| 85 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2512.81 | ✅ 通过 | - |
| 86 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 603.91 | ❌ 失败 | HTTP错误: 403 |
| 87 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2527.65 | ✅ 通过 | - |
| 88 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 860.61 | ✅ 通过 | - |
| 89 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1352.56 | ✅ 通过 | - |
| 90 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1038.37 | ✅ 通过 | - |
| 91 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1208.29 | ✅ 通过 | - |
| 92 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1192.43 | ✅ 通过 | - |
| 93 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1729.67 | ✅ 通过 | - |
| 94 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1438.62 | ✅ 通过 | - |
| 95 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1962.0 | ✅ 通过 | - |
| 96 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 9041.01 | ✅ 通过 | - |
| 97 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6859.06 | ✅ 通过 | - |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 395.81 | ❌ 失败 | HTTP错误: 403 |
| 99 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 5862.32 | ✅ 通过 | - |
| 100 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 676.74 | ❌ 失败 | HTTP错误: 403 |
| 101 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 867.2 | ✅ 通过 | - |
| 102 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 758.29 | ✅ 通过 | - |
| 103 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1366.32 | ✅ 通过 | - |
| 104 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 556.98 | ✅ 通过 | - |
| 105 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 398.09 | ❌ 失败 | HTTP错误: 403 |
| 106 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 11501.57 | ✅ 通过 | - |
| 107 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1364.1 | ✅ 通过 | - |
| 108 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 10890.46 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1662.3 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 813.48 | ✅ 通过 | - |
| 111 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 6902.95 | ✅ 通过 | - |
| 112 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 8849.06 | ✅ 通过 | - |
| 113 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 4204.64 | ✅ 通过 | - |
| 114 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 7139.96 | ✅ 通过 | - |
| 115 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1861.66 | ✅ 通过 | - |
| 116 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 4536.92 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 3962.0 | ✅ 通过 | - |
| 118 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 1371.79 | ✅ 通过 | - |
| 119 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 8438.12 | ✅ 通过 | - |
| 120 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 121 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 892.19 | ✅ 通过 | - |
| 123 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 124 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 125 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 126 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 127 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 1589.56 | ✅ 通过 | - |
| 128 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 129 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 134 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 135 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 534.03 | ❌ 失败 | HTTP错误: 500 |
| 136 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 754.92 | ✅ 通过 | - |
| 137 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 529.86 | ❌ 失败 | HTTP错误: 403 |
| 139 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 399.54 | ❌ 失败 | HTTP错误: 500 |
| 140 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 891.32 | ✅ 通过 | - |
| 141 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 440.95 | ❌ 失败 | HTTP错误: 500 |
| 142 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 516.69 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 476.37 | ❌ 失败 | HTTP错误: 500 |
| 144 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 642.47 | ❌ 失败 | HTTP错误: 500 |
| 146 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 360.07 | ❌ 失败 | HTTP错误: 500 |
| 147 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2706.71 | ✅ 通过 | - |
| 148 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 604.07 | ❌ 失败 | HTTP错误: 500 |
| 149 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 6168.96 | ✅ 通过 | - |
| 150 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 910.7 | ✅ 通过 | - |
| 151 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1846.76 | ✅ 通过 | - |
| 152 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1188.05 | ✅ 通过 | - |
| 153 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1173.16 | ✅ 通过 | - |
| 154 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 830.1 | ✅ 通过 | - |
| 155 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 3108.28 | ✅ 通过 | - |
| 156 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 9287.65 | ✅ 通过 | - |
| 157 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1715.29 | ✅ 通过 | - |
| 158 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 3727.12 | ✅ 通过 | - |
| 159 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1659.79 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 544.17 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 550.62 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 495.39 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 890.3 | ❌ 失败 | HTTP错误: 500 |
| 164 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 7527.63 | ✅ 通过 | - |
| 165 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 494.1 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 686.16 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 589.56 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 566.35 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 524.95 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 547.74 | ❌ 失败 | HTTP错误: 500 |
| 171 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 172 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 534.88 | ❌ 失败 | HTTP错误: 500 |
| 173 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 174 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 588.97 | ❌ 失败 | HTTP错误: 500 |
| 175 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 575.94 | ❌ 失败 | HTTP错误: 500 |
| 176 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 595.02 | ❌ 失败 | HTTP错误: 500 |
| 177 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 13525.48 | ✅ 通过 | - |
| 178 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 533.23 | ❌ 失败 | HTTP错误: 500 |
| 179 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 583.03 | ❌ 失败 | HTTP错误: 500 |
| 180 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1521.94 | ✅ 通过 | - |
| 181 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 4129.21 | ✅ 通过 | - |
| 182 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 6652.3 | ✅ 通过 | - |
| 183 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 17876.4 | ✅ 通过 | - |
| 184 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 26234.16 | ✅ 通过 | - |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_5

**密钥显示**: bce-v3/ALTAK-FZUmdbf...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_6

**密钥显示**: bce-v3/ALTAK-sbjCdT2...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_7

**密钥显示**: bce-v3/ALTAK-cQuNNcv...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_8

**密钥显示**: bce-v3/ALTAK-z0POcGw...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_9

**密钥显示**: bce-v3/ALTAK-BUYW7Pa...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 12 |
| 失败 | 149 |
| 超时 | 32 |
| 通过率 | 6.22% |


### 3. 异常汇总

- **deepseek-v3**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **deepseek-v3.1-250821**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **qwen-image-edit**: HTTP错误: 429

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **paddleocr-vl-0.9b**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 429

- **pp-structurev3**: HTTP错误: 429

- **deepseek-ocr**: HTTP错误: 403

- **ernie-x1.1**: HTTP错误: 403

- **qianfan-ocr**: HTTP错误: 403

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **qianfan-vl-1.5-flash**: HTTP错误: 403

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **qianfan-ocr-fast**: HTTP错误: 403

- **viduq3-pro_text2video**: HTTP错误: 500

- **kimi-k2.5**: HTTP错误: 403

- **minimax-m2.1**: HTTP错误: 403

- **glm-5**: HTTP错误: 403

- **ernie-5.0**: HTTP错误: 403

- **minimax-m2.5**: HTTP错误: 403

- **qwen3.5-35b-a3b**: HTTP错误: 403

- **qwen3.5-397b-a17b**: HTTP错误: 403

- **qwen3.5-122b-a10b**: HTTP错误: 403

- **qwen3.5-27b**: HTTP错误: 403

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **ernie-4.5-turbo-20260402**: HTTP错误: 403

- **kling-custom-voices_voices**: HTTP错误: 500

- **glm-5.1**: HTTP错误: 403

- **viduq300-turbo_text2video**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1109.59 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1234.57 | ❌ 失败 | HTTP错误: 403 |
| 3 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1254.31 | ❌ 失败 | HTTP错误: 500 |
| 4 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1305.07 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1297.11 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1316.58 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1271.5 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1309.1 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1282.95 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1309.56 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1335.52 | ❌ 失败 | HTTP错误: 403 |
| 12 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1266.49 | ❌ 失败 | HTTP错误: 403 |
| 13 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1347.91 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1386.13 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1400.96 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1392.68 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1424.26 | ❌ 失败 | HTTP错误: 403 |
| 18 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1492.66 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1544.15 | ❌ 失败 | HTTP错误: 403 |
| 20 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1590.51 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 965.79 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1116.02 | ❌ 失败 | HTTP错误: 403 |
| 23 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 956.55 | ❌ 失败 | HTTP错误: 429 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1193.09 | ❌ 失败 | HTTP错误: 403 |
| 25 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1277.7 | ❌ 失败 | HTTP错误: 403 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 709.41 | ❌ 失败 | HTTP错误: 403 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 648.61 | ❌ 失败 | HTTP错误: 429 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 891.55 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 857.62 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 399.98 | ❌ 失败 | HTTP错误: 429 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 434.84 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 452.23 | ❌ 失败 | HTTP错误: 500 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 390.25 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 397.76 | ❌ 失败 | HTTP错误: 403 |
| 35 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3142.05 | ✅ 通过 | - |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 462.65 | ❌ 失败 | HTTP错误: 403 |
| 37 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 734.56 | ❌ 失败 | HTTP错误: 403 |
| 38 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 583.43 | ❌ 失败 | HTTP错误: 403 |
| 39 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 420.07 | ❌ 失败 | HTTP错误: 403 |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 428.37 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 593.61 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 420.45 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 391.36 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 507.76 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 413.5 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 499.29 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 423.78 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 448.6 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 429.24 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 892.06 | ✅ 通过 | - |
| 51 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 1031.87 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1331.85 | ✅ 通过 | - |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 479.12 | ❌ 失败 | HTTP错误: 403 |
| 54 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 466.47 | ❌ 失败 | HTTP错误: 403 |
| 55 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 410.73 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 482.5 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1016.29 | ✅ 通过 | - |
| 58 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 66 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 453.85 | ❌ 失败 | HTTP错误: 403 |
| 73 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 855.6 | ❌ 失败 | HTTP错误: 403 |
| 76 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 864.88 | ❌ 失败 | HTTP错误: 403 |
| 77 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 840.35 | ❌ 失败 | HTTP错误: 403 |
| 78 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 859.96 | ❌ 失败 | HTTP错误: 403 |
| 79 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 879.62 | ❌ 失败 | HTTP错误: 403 |
| 80 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 887.36 | ❌ 失败 | HTTP错误: 403 |
| 81 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 893.91 | ❌ 失败 | HTTP错误: 403 |
| 83 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 898.56 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 857.51 | ❌ 失败 | HTTP错误: 403 |
| 85 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 903.57 | ❌ 失败 | HTTP错误: 403 |
| 86 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1105.66 | ✅ 通过 | - |
| 87 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 891.18 | ❌ 失败 | HTTP错误: 403 |
| 88 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1219.4 | ✅ 通过 | - |
| 89 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 971.67 | ❌ 失败 | HTTP错误: 403 |
| 90 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 832.29 | ❌ 失败 | HTTP错误: 403 |
| 91 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 888.29 | ❌ 失败 | HTTP错误: 403 |
| 92 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 906.14 | ❌ 失败 | HTTP错误: 403 |
| 93 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 977.89 | ❌ 失败 | HTTP错误: 403 |
| 94 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 855.18 | ❌ 失败 | HTTP错误: 403 |
| 95 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1254.3 | ✅ 通过 | - |
| 96 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 823.04 | ❌ 失败 | HTTP错误: 429 |
| 97 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 949.2 | ❌ 失败 | HTTP错误: 403 |
| 98 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 932.7 | ❌ 失败 | HTTP错误: 403 |
| 99 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 1041.39 | ❌ 失败 | HTTP错误: 403 |
| 100 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 1132.07 | ❌ 失败 | HTTP错误: 403 |
| 101 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 683.4 | ❌ 失败 | HTTP错误: 403 |
| 102 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 788.51 | ❌ 失败 | HTTP错误: 429 |
| 103 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 759.59 | ❌ 失败 | HTTP错误: 403 |
| 104 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 780.04 | ❌ 失败 | HTTP错误: 403 |
| 105 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 780.98 | ❌ 失败 | HTTP错误: 403 |
| 106 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 717.58 | ❌ 失败 | HTTP错误: 403 |
| 107 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 720.82 | ❌ 失败 | HTTP错误: 403 |
| 108 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 773.39 | ❌ 失败 | HTTP错误: 403 |
| 109 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 1077.89 | ✅ 通过 | - |
| 110 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 600.39 | ❌ 失败 | HTTP错误: 403 |
| 111 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 592.87 | ❌ 失败 | HTTP错误: 403 |
| 112 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 655.23 | ❌ 失败 | HTTP错误: 403 |
| 113 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 604.64 | ❌ 失败 | HTTP错误: 429 |
| 114 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 660.87 | ❌ 失败 | HTTP错误: 403 |
| 115 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 615.59 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 1211.81 | ✅ 通过 | - |
| 117 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 729.59 | ❌ 失败 | HTTP错误: 429 |
| 118 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2631.93 | ✅ 通过 | - |
| 119 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 578.53 | ❌ 失败 | HTTP错误: 403 |
| 120 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 636.53 | ❌ 失败 | HTTP错误: 403 |
| 121 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 680.58 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 693.78 | ❌ 失败 | HTTP错误: 403 |
| 123 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 669.12 | ❌ 失败 | HTTP错误: 403 |
| 124 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 667.05 | ❌ 失败 | HTTP错误: 403 |
| 125 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 719.57 | ❌ 失败 | HTTP错误: 403 |
| 126 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 651.36 | ❌ 失败 | HTTP错误: 429 |
| 127 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 874.95 | ❌ 失败 | HTTP错误: 403 |
| 128 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 679.76 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 678.68 | ❌ 失败 | HTTP错误: 403 |
| 130 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 611.27 | ❌ 失败 | HTTP错误: 403 |
| 131 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 594.77 | ❌ 失败 | HTTP错误: 403 |
| 132 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 647.85 | ❌ 失败 | HTTP错误: 403 |
| 133 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 668.81 | ❌ 失败 | HTTP错误: 403 |
| 134 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | 429 | 536.18 | ❌ 失败 | HTTP错误: 429 |
| 135 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 429 | 535.87 | ❌ 失败 | HTTP错误: 429 |
| 136 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | 429 | 542.72 | ❌ 失败 | HTTP错误: 429 |
| 137 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 667.99 | ❌ 失败 | HTTP错误: 403 |
| 138 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 403 | 495.92 | ❌ 失败 | HTTP错误: 403 |
| 139 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 403 | 441.52 | ❌ 失败 | HTTP错误: 403 |
| 140 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 785.7 | ❌ 失败 | HTTP错误: 403 |
| 141 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 465.78 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 497.99 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 473.49 | ❌ 失败 | HTTP错误: 500 |
| 144 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 423.35 | ❌ 失败 | HTTP错误: 500 |
| 146 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 403 | 458.09 | ❌ 失败 | HTTP错误: 403 |
| 147 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 148 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 505.43 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 484.46 | ❌ 失败 | HTTP错误: 500 |
| 150 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 403 | 551.43 | ❌ 失败 | HTTP错误: 403 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 603.14 | ❌ 失败 | HTTP错误: 500 |
| 152 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 403 | 534.0 | ❌ 失败 | HTTP错误: 403 |
| 153 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 154 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 403 | 541.66 | ❌ 失败 | HTTP错误: 403 |
| 155 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 537.16 | ❌ 失败 | HTTP错误: 403 |
| 156 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 403 | 502.37 | ❌ 失败 | HTTP错误: 403 |
| 157 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 403 | 537.89 | ❌ 失败 | HTTP错误: 403 |
| 158 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 403 | 513.02 | ❌ 失败 | HTTP错误: 403 |
| 159 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 403 | 546.71 | ❌ 失败 | HTTP错误: 403 |
| 160 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 403 | 577.56 | ❌ 失败 | HTTP错误: 403 |
| 161 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 403 | 549.52 | ❌ 失败 | HTTP错误: 403 |
| 162 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 586.71 | ❌ 失败 | HTTP错误: 500 |
| 163 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 3165.0 | ✅ 通过 | - |
| 164 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 628.15 | ❌ 失败 | HTTP错误: 500 |
| 165 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 734.17 | ❌ 失败 | HTTP错误: 500 |
| 166 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 623.57 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 567.57 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 569.76 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 569.89 | ❌ 失败 | HTTP错误: 500 |
| 170 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 631.96 | ❌ 失败 | HTTP错误: 500 |
| 171 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 661.24 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 550.35 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 550.98 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 778.68 | ❌ 失败 | HTTP错误: 500 |
| 175 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 723.21 | ❌ 失败 | HTTP错误: 500 |
| 176 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 519.27 | ❌ 失败 | HTTP错误: 500 |
| 177 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 403 | 531.08 | ❌ 失败 | HTTP错误: 403 |
| 178 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 579.95 | ❌ 失败 | HTTP错误: 500 |
| 179 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 403 | 537.24 | ❌ 失败 | HTTP错误: 403 |
| 180 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 741.93 | ❌ 失败 | HTTP错误: 500 |
| 181 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 7887.91 | ✅ 通过 | - |
| 182 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_10

**密钥显示**: bce-v3/ALTAK-In2F2dE...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 105 |
| 失败 | 60 |
| 超时 | 28 |
| 通过率 | 54.4% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **ernie-char-fiction-8k**: HTTP错误: 403

- **yi-34b-chat**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **llama-2-7b-chat**: HTTP错误: 403

- **gemma-7b-it**: HTTP错误: 403

- **chatglm2-6b-32k**: HTTP错误: 403

- **aquilachat-7b**: HTTP错误: 403

- **llama-2-13b-chat**: HTTP错误: 403

- **bloomz-7b**: HTTP错误: 403

- **mixtral-8x7b-instruct**: HTTP错误: 403

- **codellama-7b-instruct**: HTTP错误: 403

- **llama-2-70b-chat**: HTTP错误: 403

- **xuanyuan-70b-chat-4bit**: HTTP错误: 403

- **sqlcoder-7b**: HTTP错误: 403

- **qianfan-bloomz-7b-compressed**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-7b**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **qianfan-chinese-llama-2-70b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 500

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1199.26 | ❌ 失败 | HTTP错误: 403 |
| 2 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1363.12 | ❌ 失败 | HTTP错误: 429 |
| 3 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1438.28 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1803.96 | ✅ 通过 | - |
| 5 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 1856.81 | ✅ 通过 | - |
| 6 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | 403 | 485.43 | ❌ 失败 | HTTP错误: 403 |
| 7 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 490.48 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 2317.62 | ✅ 通过 | - |
| 9 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2368.79 | ✅ 通过 | - |
| 10 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | 403 | 533.26 | ❌ 失败 | HTTP错误: 403 |
| 11 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | 403 | 588.05 | ❌ 失败 | HTTP错误: 403 |
| 12 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | 403 | 662.48 | ❌ 失败 | HTTP错误: 403 |
| 13 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | 403 | 608.93 | ❌ 失败 | HTTP错误: 403 |
| 14 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 200 | 2665.06 | ✅ 通过 | - |
| 15 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2715.08 | ✅ 通过 | - |
| 16 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2730.26 | ✅ 通过 | - |
| 17 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | 403 | 497.72 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2945.92 | ✅ 通过 | - |
| 19 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 2979.79 | ✅ 通过 | - |
| 20 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | 403 | 554.79 | ❌ 失败 | HTTP错误: 403 |
| 21 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 3064.39 | ✅ 通过 | - |
| 22 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | 403 | 638.67 | ❌ 失败 | HTTP错误: 403 |
| 23 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | 403 | 695.41 | ❌ 失败 | HTTP错误: 403 |
| 24 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | 403 | 599.89 | ❌ 失败 | HTTP错误: 403 |
| 25 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 3187.56 | ✅ 通过 | - |
| 26 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 3157.15 | ✅ 通过 | - |
| 27 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 3210.82 | ✅ 通过 | - |
| 28 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 3256.83 | ✅ 通过 | - |
| 29 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | 403 | 731.1 | ❌ 失败 | HTTP错误: 403 |
| 30 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3410.48 | ✅ 通过 | - |
| 31 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | 403 | 773.89 | ❌ 失败 | HTTP错误: 403 |
| 32 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | 403 | 828.45 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 3720.85 | ✅ 通过 | - |
| 34 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 862.46 | ❌ 失败 | HTTP错误: 403 |
| 35 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1206.81 | ✅ 通过 | - |
| 36 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 915.92 | ❌ 失败 | HTTP错误: 429 |
| 37 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | 403 | 901.42 | ❌ 失败 | HTTP错误: 403 |
| 38 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 946.86 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | 403 | 968.68 | ❌ 失败 | HTTP错误: 403 |
| 40 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 948.75 | ❌ 失败 | HTTP错误: 429 |
| 41 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 934.17 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 963.4 | ❌ 失败 | HTTP错误: 500 |
| 43 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 623.86 | ❌ 失败 | HTTP错误: 403 |
| 44 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 701.18 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1502.75 | ✅ 通过 | - |
| 46 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 720.04 | ❌ 失败 | HTTP错误: 403 |
| 47 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 1095.59 | ❌ 失败 | HTTP错误: 403 |
| 48 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 1244.53 | ✅ 通过 | - |
| 49 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2607.02 | ✅ 通过 | - |
| 50 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 2320.47 | ✅ 通过 | - |
| 51 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 680.18 | ✅ 通过 | - |
| 52 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1886.26 | ✅ 通过 | - |
| 53 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1125.15 | ✅ 通过 | - |
| 54 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 1015.17 | ✅ 通过 | - |
| 55 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1374.2 | ✅ 通过 | - |
| 56 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 1201.58 | ✅ 通过 | - |
| 57 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 5926.01 | ✅ 通过 | - |
| 58 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3037.81 | ✅ 通过 | - |
| 59 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 2098.65 | ✅ 通过 | - |
| 60 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 928.61 | ✅ 通过 | - |
| 61 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1249.75 | ✅ 通过 | - |
| 62 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1870.71 | ✅ 通过 | - |
| 63 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 885.27 | ✅ 通过 | - |
| 64 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1038.56 | ✅ 通过 | - |
| 65 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 3330.0 | ✅ 通过 | - |
| 66 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 709.99 | ✅ 通过 | - |
| 67 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1570.7 | ✅ 通过 | - |
| 68 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 1094.01 | ✅ 通过 | - |
| 69 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 896.75 | ✅ 通过 | - |
| 70 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1440.0 | ✅ 通过 | - |
| 71 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 912.2 | ✅ 通过 | - |
| 72 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1061.48 | ✅ 通过 | - |
| 73 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 671.88 | ✅ 通过 | - |
| 74 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2124.06 | ✅ 通过 | - |
| 75 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 415.01 | ❌ 失败 | HTTP错误: 403 |
| 76 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 1986.27 | ✅ 通过 | - |
| 77 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 953.97 | ❌ 失败 | HTTP错误: 403 |
| 78 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1484.18 | ✅ 通过 | - |
| 79 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1809.05 | ✅ 通过 | - |
| 80 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 1883.72 | ✅ 通过 | - |
| 81 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 624.89 | ✅ 通过 | - |
| 82 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 1963.91 | ✅ 通过 | - |
| 83 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2091.85 | ✅ 通过 | - |
| 84 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1256.09 | ✅ 通过 | - |
| 85 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 8298.37 | ✅ 通过 | - |
| 86 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 526.42 | ❌ 失败 | HTTP错误: 403 |
| 87 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1211.74 | ✅ 通过 | - |
| 88 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 947.53 | ✅ 通过 | - |
| 89 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1129.52 | ✅ 通过 | - |
| 90 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1709.1 | ✅ 通过 | - |
| 91 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1936.9 | ✅ 通过 | - |
| 92 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 4894.72 | ✅ 通过 | - |
| 93 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 10178.32 | ✅ 通过 | - |
| 94 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1706.86 | ✅ 通过 | - |
| 95 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 9571.58 | ✅ 通过 | - |
| 96 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 4146.51 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 372.5 | ❌ 失败 | HTTP错误: 403 |
| 98 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 13108.35 | ✅ 通过 | - |
| 99 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 435.35 | ❌ 失败 | HTTP错误: 403 |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 729.75 | ✅ 通过 | - |
| 101 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 686.99 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1045.75 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 847.21 | ✅ 通过 | - |
| 104 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 15492.58 | ✅ 通过 | - |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1654.11 | ✅ 通过 | - |
| 106 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 1733.0 | ✅ 通过 | - |
| 107 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8417.08 | ✅ 通过 | - |
| 108 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 10674.16 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1657.21 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1078.86 | ✅ 通过 | - |
| 111 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 8538.88 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1637.73 | ✅ 通过 | - |
| 113 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 6015.97 | ✅ 通过 | - |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1697.9 | ✅ 通过 | - |
| 115 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 7317.06 | ✅ 通过 | - |
| 116 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 117 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 118 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 119 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 927.71 | ✅ 通过 | - |
| 120 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 4293.44 | ✅ 通过 | - |
| 121 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 123 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 124 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 125 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 126 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1721.22 | ✅ 通过 | - |
| 127 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2105.07 | ✅ 通过 | - |
| 129 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 134 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 135 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 729.64 | ✅ 通过 | - |
| 136 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 786.01 | ❌ 失败 | HTTP错误: 500 |
| 137 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 490.52 | ❌ 失败 | HTTP错误: 403 |
| 138 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 845.38 | ✅ 通过 | - |
| 139 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 395.02 | ❌ 失败 | HTTP错误: 500 |
| 140 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 387.68 | ❌ 失败 | HTTP错误: 500 |
| 141 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 347.2 | ❌ 失败 | HTTP错误: 500 |
| 142 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 816.16 | ❌ 失败 | HTTP错误: 500 |
| 143 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 3394.43 | ✅ 通过 | - |
| 144 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 428.47 | ❌ 失败 | HTTP错误: 500 |
| 145 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 462.39 | ❌ 失败 | HTTP错误: 500 |
| 146 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 448.59 | ❌ 失败 | HTTP错误: 500 |
| 148 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 11927.41 | ✅ 通过 | - |
| 149 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 687.6 | ✅ 通过 | - |
| 150 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2089.17 | ✅ 通过 | - |
| 151 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1371.16 | ✅ 通过 | - |
| 152 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 153 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 10891.04 | ✅ 通过 | - |
| 154 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 853.46 | ✅ 通过 | - |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 2351.56 | ✅ 通过 | - |
| 156 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2070.39 | ✅ 通过 | - |
| 157 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1491.3 | ✅ 通过 | - |
| 158 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1041.5 | ✅ 通过 | - |
| 159 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 504.37 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 512.74 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 509.97 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 527.69 | ❌ 失败 | HTTP错误: 500 |
| 163 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 466.5 | ❌ 失败 | HTTP错误: 500 |
| 164 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 732.52 | ❌ 失败 | HTTP错误: 500 |
| 165 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 5291.07 | ✅ 通过 | - |
| 166 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 486.09 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 761.98 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 486.56 | ❌ 失败 | HTTP错误: 500 |
| 169 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 520.74 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 462.51 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 543.88 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 491.33 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 518.55 | ❌ 失败 | HTTP错误: 500 |
| 174 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 510.87 | ❌ 失败 | HTTP错误: 500 |
| 175 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 6144.36 | ✅ 通过 | - |
| 176 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 736.58 | ❌ 失败 | HTTP错误: 500 |
| 178 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 16692.98 | ✅ 通过 | - |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1421.59 | ✅ 通过 | - |
| 180 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 16208.43 | ✅ 通过 | - |
| 181 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 20696.14 | ✅ 通过 | - |
| 182 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 9617.79 | ✅ 通过 | - |
| 184 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 16063.47 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_11

**密钥显示**: bce-v3/ALTAK-evaaWrM...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_12

**密钥显示**: bce-v3/ALTAK-YEO5FrR...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 25 |
| 失败 | 137 |
| 超时 | 31 |
| 通过率 | 12.95% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **qwen3-reranker-8b**: HTTP错误: 403

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen-image-edit**: HTTP错误: 429

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **deepseek-v3.2-think**: HTTP错误: 403

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **paddleocr-vl-0.9b**: HTTP错误: 429

- **pp-structurev3**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 429

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **ernie-x1.1**: HTTP错误: 403

- **qianfan-ocr**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **qianfan-vl-1.5-flash**: HTTP错误: 403

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **qianfan-ocr-fast**: HTTP错误: 403

- **kimi-k2.5**: HTTP错误: 403

- **glm-5**: HTTP错误: 403

- **minimax-m2.1**: HTTP错误: 403

- **minimax-m2.5**: HTTP错误: 403

- **qwen3.5-35b-a3b**: HTTP错误: 403

- **ernie-5.0**: HTTP错误: 403

- **qwen3.5-122b-a10b**: HTTP错误: 403

- **qwen3.5-27b**: HTTP错误: 403

- **qwen3.5-397b-a17b**: HTTP错误: 403

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **ernie-4.5-turbo-20260402**: HTTP错误: 403

- **kling-custom-voices_voices**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **glm-5.1**: HTTP错误: 403


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1109.05 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1155.02 | ❌ 失败 | HTTP错误: 403 |
| 3 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1121.49 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1210.8 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1215.38 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1242.0 | ❌ 失败 | HTTP错误: 403 |
| 7 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1225.54 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1281.09 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1290.95 | ❌ 失败 | HTTP错误: 403 |
| 10 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1256.17 | ❌ 失败 | HTTP错误: 500 |
| 11 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1300.84 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1301.63 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1274.32 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1344.22 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1409.36 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1398.92 | ❌ 失败 | HTTP错误: 403 |
| 17 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1343.23 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1454.87 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1463.05 | ❌ 失败 | HTTP错误: 403 |
| 20 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 871.88 | ❌ 失败 | HTTP错误: 403 |
| 21 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 898.44 | ❌ 失败 | HTTP错误: 403 |
| 22 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1065.31 | ❌ 失败 | HTTP错误: 403 |
| 23 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 609.76 | ❌ 失败 | HTTP错误: 429 |
| 24 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 588.29 | ❌ 失败 | HTTP错误: 403 |
| 25 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1400.75 | ❌ 失败 | HTTP错误: 403 |
| 26 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 422.46 | ❌ 失败 | HTTP错误: 429 |
| 27 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 531.83 | ❌ 失败 | HTTP错误: 403 |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 495.83 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 321.68 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 415.03 | ❌ 失败 | HTTP错误: 403 |
| 31 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2950.51 | ✅ 通过 | - |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 540.3 | ❌ 失败 | HTTP错误: 500 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 347.75 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 390.77 | ❌ 失败 | HTTP错误: 403 |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 357.35 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 312.93 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 366.09 | ❌ 失败 | HTTP错误: 403 |
| 38 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 376.13 | ❌ 失败 | HTTP错误: 403 |
| 39 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 1980.47 | ✅ 通过 | - |
| 40 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 8053.53 | ✅ 通过 | - |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 1826.65 | ✅ 通过 | - |
| 42 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 387.87 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 442.02 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 693.09 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 375.08 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 446.14 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 412.81 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 428.84 | ❌ 失败 | HTTP错误: 403 |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 619.6 | ✅ 通过 | - |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 378.54 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1340.38 | ✅ 通过 | - |
| 52 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 447.74 | ❌ 失败 | HTTP错误: 403 |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 429.22 | ❌ 失败 | HTTP错误: 403 |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 510.97 | ❌ 失败 | HTTP错误: 403 |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1281.52 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 7820.5 | ✅ 通过 | - |
| 57 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 15354.92 | ✅ 通过 | - |
| 58 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 637.26 | ✅ 通过 | - |
| 59 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 323.46 | ❌ 失败 | HTTP错误: 403 |
| 60 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 798.43 | ✅ 通过 | - |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 890.02 | ✅ 通过 | - |
| 62 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 489.29 | ❌ 失败 | HTTP错误: 403 |
| 63 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 322.26 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 387.76 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 313.56 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 321.49 | ❌ 失败 | HTTP错误: 403 |
| 67 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 391.6 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 422.54 | ❌ 失败 | HTTP错误: 403 |
| 69 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 785.22 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 767.34 | ❌ 失败 | HTTP错误: 403 |
| 85 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 740.52 | ❌ 失败 | HTTP错误: 403 |
| 86 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 832.04 | ❌ 失败 | HTTP错误: 403 |
| 87 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 789.15 | ❌ 失败 | HTTP错误: 403 |
| 88 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 801.18 | ❌ 失败 | HTTP错误: 403 |
| 90 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 840.74 | ❌ 失败 | HTTP错误: 403 |
| 91 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 869.78 | ❌ 失败 | HTTP错误: 403 |
| 92 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 863.93 | ❌ 失败 | HTTP错误: 403 |
| 94 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1299.97 | ✅ 通过 | - |
| 96 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1547.23 | ✅ 通过 | - |
| 97 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 791.8 | ❌ 失败 | HTTP错误: 429 |
| 98 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 730.51 | ❌ 失败 | HTTP错误: 429 |
| 99 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1640.59 | ✅ 通过 | - |
| 100 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 602.39 | ❌ 失败 | HTTP错误: 403 |
| 101 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1159.23 | ✅ 通过 | - |
| 102 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 583.88 | ❌ 失败 | HTTP错误: 403 |
| 103 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1403.8 | ✅ 通过 | - |
| 104 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 612.37 | ❌ 失败 | HTTP错误: 403 |
| 105 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1508.82 | ✅ 通过 | - |
| 106 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 611.25 | ❌ 失败 | HTTP错误: 403 |
| 107 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 717.88 | ✅ 通过 | - |
| 108 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 810.46 | ❌ 失败 | HTTP错误: 403 |
| 109 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 597.08 | ❌ 失败 | HTTP错误: 403 |
| 110 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2488.86 | ✅ 通过 | - |
| 111 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1653.75 | ✅ 通过 | - |
| 112 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 643.03 | ❌ 失败 | HTTP错误: 403 |
| 113 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 955.01 | ✅ 通过 | - |
| 114 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 554.57 | ❌ 失败 | HTTP错误: 403 |
| 115 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 646.48 | ❌ 失败 | HTTP错误: 403 |
| 116 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 658.34 | ❌ 失败 | HTTP错误: 429 |
| 117 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 619.2 | ❌ 失败 | HTTP错误: 403 |
| 118 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 623.67 | ❌ 失败 | HTTP错误: 429 |
| 119 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 645.18 | ❌ 失败 | HTTP错误: 403 |
| 120 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 703.95 | ❌ 失败 | HTTP错误: 403 |
| 121 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 651.93 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 699.95 | ❌ 失败 | HTTP错误: 403 |
| 123 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 710.14 | ❌ 失败 | HTTP错误: 403 |
| 124 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 765.04 | ❌ 失败 | HTTP错误: 403 |
| 125 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 676.3 | ❌ 失败 | HTTP错误: 403 |
| 126 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 654.48 | ❌ 失败 | HTTP错误: 429 |
| 127 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 874.28 | ❌ 失败 | HTTP错误: 403 |
| 128 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 676.08 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 636.67 | ❌ 失败 | HTTP错误: 403 |
| 130 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 592.76 | ❌ 失败 | HTTP错误: 403 |
| 131 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 654.44 | ❌ 失败 | HTTP错误: 403 |
| 132 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 673.43 | ❌ 失败 | HTTP错误: 403 |
| 133 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 629.28 | ❌ 失败 | HTTP错误: 403 |
| 134 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 625.9 | ❌ 失败 | HTTP错误: 403 |
| 135 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | 429 | 623.53 | ❌ 失败 | HTTP错误: 429 |
| 136 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | 429 | 498.15 | ❌ 失败 | HTTP错误: 429 |
| 137 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 429 | 658.12 | ❌ 失败 | HTTP错误: 429 |
| 138 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 554.61 | ❌ 失败 | HTTP错误: 403 |
| 139 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 403 | 601.86 | ❌ 失败 | HTTP错误: 403 |
| 140 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 403 | 569.94 | ❌ 失败 | HTTP错误: 403 |
| 141 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 4537.76 | ✅ 通过 | - |
| 142 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 515.18 | ❌ 失败 | HTTP错误: 500 |
| 143 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 493.0 | ❌ 失败 | HTTP错误: 500 |
| 144 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 543.89 | ❌ 失败 | HTTP错误: 500 |
| 145 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 495.67 | ❌ 失败 | HTTP错误: 500 |
| 146 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 403 | 498.02 | ❌ 失败 | HTTP错误: 403 |
| 147 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 556.02 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 595.08 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 543.44 | ❌ 失败 | HTTP错误: 500 |
| 150 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 403 | 436.05 | ❌ 失败 | HTTP错误: 403 |
| 151 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 403 | 489.12 | ❌ 失败 | HTTP错误: 403 |
| 152 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 468.01 | ❌ 失败 | HTTP错误: 403 |
| 153 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 403 | 531.77 | ❌ 失败 | HTTP错误: 403 |
| 154 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2373.93 | ✅ 通过 | - |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 403 | 457.96 | ❌ 失败 | HTTP错误: 403 |
| 156 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 403 | 524.72 | ❌ 失败 | HTTP错误: 403 |
| 157 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 403 | 745.76 | ❌ 失败 | HTTP错误: 403 |
| 158 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 403 | 521.1 | ❌ 失败 | HTTP错误: 403 |
| 159 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 403 | 485.94 | ❌ 失败 | HTTP错误: 403 |
| 160 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 403 | 650.13 | ❌ 失败 | HTTP错误: 403 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 550.59 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 534.15 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 695.93 | ❌ 失败 | HTTP错误: 500 |
| 164 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 776.61 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 859.31 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 536.09 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 534.09 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 695.18 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 470.61 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 541.43 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 506.17 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 528.14 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 593.75 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 555.38 | ❌ 失败 | HTTP错误: 500 |
| 175 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 7448.38 | ✅ 通过 | - |
| 176 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 403 | 429.76 | ❌ 失败 | HTTP错误: 403 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 555.5 | ❌ 失败 | HTTP错误: 500 |
| 178 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 803.16 | ❌ 失败 | HTTP错误: 500 |
| 179 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 403 | 612.98 | ❌ 失败 | HTTP错误: 403 |
| 180 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 181 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_13

**密钥显示**: bce-v3/ALTAK-gkYESB8...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 94 |
| 失败 | 57 |
| 超时 | 42 |
| 通过率 | 48.7% |


### 3. 异常汇总

- **deepseek-v3**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen-image-edit**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1180.41 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1247.23 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1244.58 | ❌ 失败 | HTTP错误: 403 |
| 4 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1214.18 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1229.41 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1265.75 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1270.19 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1278.14 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1280.94 | ❌ 失败 | HTTP错误: 403 |
| 10 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1251.59 | ❌ 失败 | HTTP错误: 500 |
| 11 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1361.26 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1767.97 | ✅ 通过 | - |
| 13 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 778.73 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2352.65 | ✅ 通过 | - |
| 15 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2540.72 | ✅ 通过 | - |
| 16 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2637.55 | ✅ 通过 | - |
| 17 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 2729.86 | ✅ 通过 | - |
| 18 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 2820.0 | ✅ 通过 | - |
| 19 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 3106.45 | ✅ 通过 | - |
| 20 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 799.59 | ✅ 通过 | - |
| 21 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3316.1 | ✅ 通过 | - |
| 22 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 553.21 | ❌ 失败 | HTTP错误: 403 |
| 23 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 393.78 | ❌ 失败 | HTTP错误: 429 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 1626.01 | ✅ 通过 | - |
| 25 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 4628.79 | ✅ 通过 | - |
| 26 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2480.31 | ✅ 通过 | - |
| 27 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1630.56 | ✅ 通过 | - |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 404.19 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 445.22 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1094.86 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 353.73 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 312.74 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 2218.15 | ✅ 通过 | - |
| 34 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1629.81 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 380.74 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 317.74 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 561.84 | ❌ 失败 | HTTP错误: 403 |
| 38 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 852.0 | ✅ 通过 | - |
| 39 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 394.9 | ❌ 失败 | HTTP错误: 403 |
| 40 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 19478.68 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 433.35 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 2359.37 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1339.96 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1251.2 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 726.32 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 692.9 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 691.21 | ✅ 通过 | - |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1018.6 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 598.63 | ✅ 通过 | - |
| 50 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 15695.65 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 622.91 | ✅ 通过 | - |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1237.71 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2360.57 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 946.47 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1254.63 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 11295.28 | ✅ 通过 | - |
| 57 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 66 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 700.97 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 1043.39 | ✅ 通过 | - |
| 71 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 1121.24 | ✅ 通过 | - |
| 73 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 1102.89 | ✅ 通过 | - |
| 74 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1193.31 | ✅ 通过 | - |
| 75 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1332.0 | ✅ 通过 | - |
| 77 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1530.59 | ✅ 通过 | - |
| 78 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 549.86 | ❌ 失败 | HTTP错误: 403 |
| 79 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 431.02 | ❌ 失败 | HTTP错误: 403 |
| 81 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1068.68 | ✅ 通过 | - |
| 82 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2470.29 | ✅ 通过 | - |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 1774.93 | ✅ 通过 | - |
| 84 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 889.78 | ✅ 通过 | - |
| 85 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1417.12 | ✅ 通过 | - |
| 86 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 87 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1002.51 | ✅ 通过 | - |
| 89 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2466.11 | ✅ 通过 | - |
| 90 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1071.67 | ✅ 通过 | - |
| 91 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 3125.57 | ✅ 通过 | - |
| 92 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1470.23 | ✅ 通过 | - |
| 93 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 3163.99 | ✅ 通过 | - |
| 94 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2127.33 | ✅ 通过 | - |
| 96 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1947.31 | ✅ 通过 | - |
| 97 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 583.04 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 448.29 | ❌ 失败 | HTTP错误: 403 |
| 99 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 439.91 | ❌ 失败 | HTTP错误: 403 |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 642.77 | ✅ 通过 | - |
| 101 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 709.86 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1336.26 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 1346.6 | ✅ 通过 | - |
| 104 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1117.98 | ✅ 通过 | - |
| 105 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 1777.25 | ✅ 通过 | - |
| 106 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 5450.64 | ✅ 通过 | - |
| 107 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 9761.43 | ✅ 通过 | - |
| 108 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 7299.0 | ✅ 通过 | - |
| 109 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 427.6 | ❌ 失败 | HTTP错误: 403 |
| 110 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 519.73 | ❌ 失败 | HTTP错误: 403 |
| 111 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 558.23 | ❌ 失败 | HTTP错误: 429 |
| 112 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1109.04 | ✅ 通过 | - |
| 113 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1851.71 | ✅ 通过 | - |
| 114 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 12163.48 | ✅ 通过 | - |
| 115 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1822.19 | ✅ 通过 | - |
| 116 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 7748.36 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 876.83 | ✅ 通过 | - |
| 118 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 7234.64 | ✅ 通过 | - |
| 119 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 4370.14 | ✅ 通过 | - |
| 120 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 4734.59 | ✅ 通过 | - |
| 121 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 13079.1 | ✅ 通过 | - |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 812.8 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 1723.87 | ✅ 通过 | - |
| 124 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 8850.03 | ✅ 通过 | - |
| 125 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 5658.99 | ✅ 通过 | - |
| 126 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 127 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 13351.83 | ✅ 通过 | - |
| 129 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 13648.01 | ✅ 通过 | - |
| 130 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 603.28 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 549.24 | ❌ 失败 | HTTP错误: 500 |
| 135 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 439.5 | ❌ 失败 | HTTP错误: 403 |
| 137 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 496.04 | ❌ 失败 | HTTP错误: 500 |
| 141 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 382.46 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 143 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 697.8 | ✅ 通过 | - |
| 144 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 562.27 | ❌ 失败 | HTTP错误: 500 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 571.62 | ❌ 失败 | HTTP错误: 500 |
| 147 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2313.9 | ✅ 通过 | - |
| 148 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 466.05 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 618.57 | ❌ 失败 | HTTP错误: 500 |
| 150 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 151 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 152 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 153 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 517.13 | ❌ 失败 | HTTP错误: 500 |
| 154 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 899.72 | ✅ 通过 | - |
| 155 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1322.01 | ✅ 通过 | - |
| 156 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1148.39 | ✅ 通过 | - |
| 157 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1335.32 | ✅ 通过 | - |
| 158 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2106.23 | ✅ 通过 | - |
| 159 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 537.13 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 550.58 | ❌ 失败 | HTTP错误: 500 |
| 161 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1246.55 | ✅ 通过 | - |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 780.6 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2098.21 | ✅ 通过 | - |
| 164 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 544.89 | ❌ 失败 | HTTP错误: 500 |
| 165 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1261.69 | ✅ 通过 | - |
| 166 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 612.05 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 550.54 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 721.33 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 594.82 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 556.02 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 552.89 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 625.73 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 541.57 | ❌ 失败 | HTTP错误: 500 |
| 174 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 489.6 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 615.45 | ❌ 失败 | HTTP错误: 500 |
| 176 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 624.07 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 723.73 | ❌ 失败 | HTTP错误: 500 |
| 178 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1556.91 | ✅ 通过 | - |
| 179 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 4868.82 | ✅ 通过 | - |
| 180 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 5366.31 | ✅ 通过 | - |
| 181 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 10916.05 | ✅ 通过 | - |
| 183 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 10097.2 | ✅ 通过 | - |
| 185 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 21484.96 | ✅ 通过 | - |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_14

**密钥显示**: bce-v3/ALTAK-5tfX41H...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_15

**密钥显示**: bce-v3/ALTAK-KtDgaXP...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 105 |
| 失败 | 44 |
| 超时 | 44 |
| 通过率 | 54.4% |


### 3. 异常汇总

- **irag-1.0**: HTTP错误: 500

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1179.33 | ❌ 失败 | HTTP错误: 500 |
| 2 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1309.63 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1329.7 | ❌ 失败 | HTTP错误: 403 |
| 4 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 447.49 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1821.83 | ✅ 通过 | - |
| 6 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 1996.02 | ✅ 通过 | - |
| 7 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 2465.1 | ✅ 通过 | - |
| 8 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2480.76 | ✅ 通过 | - |
| 9 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2578.52 | ✅ 通过 | - |
| 10 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 200 | 2672.94 | ✅ 通过 | - |
| 11 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2850.96 | ✅ 通过 | - |
| 12 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 2881.81 | ✅ 通过 | - |
| 13 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 3090.99 | ✅ 通过 | - |
| 14 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 3057.28 | ✅ 通过 | - |
| 15 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3161.59 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 3342.95 | ✅ 通过 | - |
| 17 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 3545.57 | ✅ 通过 | - |
| 18 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 971.1 | ✅ 通过 | - |
| 19 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 5214.94 | ✅ 通过 | - |
| 20 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 5266.81 | ✅ 通过 | - |
| 21 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 1739.62 | ✅ 通过 | - |
| 22 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 5548.2 | ✅ 通过 | - |
| 23 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 494.84 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 363.23 | ❌ 失败 | HTTP错误: 429 |
| 25 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 6203.18 | ✅ 通过 | - |
| 26 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1506.2 | ✅ 通过 | - |
| 27 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2274.37 | ✅ 通过 | - |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 390.26 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 396.85 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1221.77 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 429.77 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 318.06 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 2008.23 | ✅ 通过 | - |
| 34 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 11989.2 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 367.29 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 318.59 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 361.24 | ❌ 失败 | HTTP错误: 403 |
| 38 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 2185.84 | ✅ 通过 | - |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 920.79 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 1980.2 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 411.15 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1912.86 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1260.52 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1330.47 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 879.68 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 787.02 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 630.11 | ✅ 通过 | - |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1548.91 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 685.23 | ✅ 通过 | - |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 2343.79 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 673.85 | ✅ 通过 | - |
| 52 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2432.95 | ✅ 通过 | - |
| 53 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 17563.44 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1150.68 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1284.29 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 9921.14 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 741.3 | ✅ 通过 | - |
| 62 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 882.08 | ✅ 通过 | - |
| 66 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 833.92 | ✅ 通过 | - |
| 68 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 569.95 | ✅ 通过 | - |
| 71 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 1088.25 | ✅ 通过 | - |
| 75 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 337.65 | ❌ 失败 | HTTP错误: 403 |
| 77 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 764.05 | ✅ 通过 | - |
| 78 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2069.75 | ✅ 通过 | - |
| 79 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1766.44 | ✅ 通过 | - |
| 80 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 357.68 | ❌ 失败 | HTTP错误: 403 |
| 81 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 1844.15 | ✅ 通过 | - |
| 82 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 889.96 | ✅ 通过 | - |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2244.45 | ✅ 通过 | - |
| 84 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 2666.38 | ✅ 通过 | - |
| 86 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 2523.9 | ✅ 通过 | - |
| 87 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1768.28 | ✅ 通过 | - |
| 88 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 999.69 | ✅ 通过 | - |
| 91 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1240.3 | ✅ 通过 | - |
| 92 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 947.06 | ✅ 通过 | - |
| 93 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2198.76 | ✅ 通过 | - |
| 94 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1447.8 | ✅ 通过 | - |
| 95 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 96 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1583.5 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 361.82 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 560.17 | ❌ 失败 | HTTP错误: 403 |
| 99 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 1020.5 | ✅ 通过 | - |
| 100 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 4455.74 | ✅ 通过 | - |
| 101 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 650.55 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1185.63 | ✅ 通过 | - |
| 103 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6852.23 | ✅ 通过 | - |
| 104 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 730.05 | ✅ 通过 | - |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1477.64 | ✅ 通过 | - |
| 106 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 2091.88 | ✅ 通过 | - |
| 107 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 14622.41 | ✅ 通过 | - |
| 108 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 12637.52 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1739.52 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1444.79 | ✅ 通过 | - |
| 111 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 11593.16 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1475.14 | ✅ 通过 | - |
| 113 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 6931.6 | ✅ 通过 | - |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1416.73 | ✅ 通过 | - |
| 115 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 18125.41 | ✅ 通过 | - |
| 116 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 3636.43 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 884.97 | ✅ 通过 | - |
| 118 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 2814.95 | ✅ 通过 | - |
| 119 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 120 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 10358.55 | ✅ 通过 | - |
| 121 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1040.08 | ✅ 通过 | - |
| 123 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 12897.83 | ✅ 通过 | - |
| 124 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 7985.04 | ✅ 通过 | - |
| 125 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 6606.35 | ✅ 通过 | - |
| 126 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 127 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 129 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 657.38 | ✅ 通过 | - |
| 132 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 134 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 135 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 422.23 | ❌ 失败 | HTTP错误: 500 |
| 136 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 16734.03 | ✅ 通过 | - |
| 140 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 599.28 | ❌ 失败 | HTTP错误: 403 |
| 141 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 614.32 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 567.97 | ❌ 失败 | HTTP错误: 500 |
| 143 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 838.93 | ✅ 通过 | - |
| 144 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 474.67 | ❌ 失败 | HTTP错误: 500 |
| 146 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 637.6 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 616.28 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 578.21 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 714.98 | ❌ 失败 | HTTP错误: 500 |
| 151 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 699.69 | ✅ 通过 | - |
| 152 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2517.55 | ✅ 通过 | - |
| 153 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1874.49 | ✅ 通过 | - |
| 154 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1131.85 | ✅ 通过 | - |
| 155 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1469.27 | ✅ 通过 | - |
| 156 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1159.35 | ✅ 通过 | - |
| 157 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1176.76 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 547.09 | ❌ 失败 | HTTP错误: 500 |
| 159 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1484.89 | ✅ 通过 | - |
| 160 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1823.88 | ✅ 通过 | - |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 459.01 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 532.93 | ❌ 失败 | HTTP错误: 500 |
| 163 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 16505.45 | ✅ 通过 | - |
| 164 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 495.12 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 519.56 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 480.69 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 530.36 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 595.15 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 736.05 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 533.87 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 532.77 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 490.85 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 511.3 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 570.39 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 567.78 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 792.23 | ❌ 失败 | HTTP错误: 500 |
| 177 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1509.58 | ✅ 通过 | - |
| 178 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 6389.15 | ✅ 通过 | - |
| 180 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 8030.87 | ✅ 通过 | - |
| 181 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 10916.04 | ✅ 通过 | - |
| 183 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 12158.8 | ✅ 通过 | - |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 10590.5 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_16

**密钥显示**: bce-v3/ALTAK-zxQQLYT...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_17

**密钥显示**: bce-v3/ALTAK-QmOnbOj...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_18

**密钥显示**: bce-v3/ALTAK-OWYLnTj...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 62 |
| 失败 | 103 |
| 超时 | 28 |
| 通过率 | 32.12% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **yi-34b-chat**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **codellama-7b-instruct**: HTTP错误: 403

- **llama-2-7b-chat**: HTTP错误: 403

- **llama-2-13b-chat**: HTTP错误: 403

- **llama-2-70b-chat**: HTTP错误: 403

- **chatglm2-6b-32k**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **gemma-7b-it**: HTTP错误: 403

- **mixtral-8x7b-instruct**: HTTP错误: 403

- **qianfan-bloomz-7b-compressed**: HTTP错误: 403

- **sqlcoder-7b**: HTTP错误: 403

- **aquilachat-7b**: HTTP错误: 403

- **xuanyuan-70b-chat-4bit**: HTTP错误: 403

- **bloomz-7b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qianfan-chinese-llama-2-7b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-chinese-llama-2-70b**: HTTP错误: 403

- **qianfan-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 500

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **stable-diffusion-xl**: HTTP错误: 429

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1167.63 | ❌ 失败 | HTTP错误: 403 |
| 2 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1206.91 | ❌ 失败 | HTTP错误: 429 |
| 3 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1239.18 | ❌ 失败 | HTTP错误: 403 |
| 4 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1159.25 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1255.81 | ❌ 失败 | HTTP错误: 403 |
| 6 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1147.82 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1247.9 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1288.51 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1312.2 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1334.05 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1344.99 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1356.7 | ❌ 失败 | HTTP错误: 403 |
| 13 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1311.47 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1373.1 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1342.54 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1387.77 | ❌ 失败 | HTTP错误: 403 |
| 17 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1314.61 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1414.72 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1501.05 | ❌ 失败 | HTTP错误: 403 |
| 20 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1133.34 | ❌ 失败 | HTTP错误: 403 |
| 21 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | 403 | 1053.25 | ❌ 失败 | HTTP错误: 403 |
| 22 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 2384.02 | ❌ 失败 | HTTP错误: 403 |
| 23 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | 403 | 1162.74 | ❌ 失败 | HTTP错误: 403 |
| 24 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | 403 | 1227.02 | ❌ 失败 | HTTP错误: 403 |
| 25 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | 403 | 1212.56 | ❌ 失败 | HTTP错误: 403 |
| 26 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | 403 | 1164.19 | ❌ 失败 | HTTP错误: 403 |
| 27 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | 403 | 1263.24 | ❌ 失败 | HTTP错误: 403 |
| 28 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1127.57 | ❌ 失败 | HTTP错误: 403 |
| 29 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1161.76 | ❌ 失败 | HTTP错误: 403 |
| 30 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | 403 | 1291.38 | ❌ 失败 | HTTP错误: 403 |
| 31 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | 403 | 1216.57 | ❌ 失败 | HTTP错误: 403 |
| 32 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | 403 | 1191.12 | ❌ 失败 | HTTP错误: 403 |
| 33 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | 403 | 1198.52 | ❌ 失败 | HTTP错误: 403 |
| 34 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | 403 | 1329.56 | ❌ 失败 | HTTP错误: 403 |
| 35 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | 403 | 1266.38 | ❌ 失败 | HTTP错误: 403 |
| 36 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | 403 | 1268.92 | ❌ 失败 | HTTP错误: 403 |
| 37 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1888.59 | ❌ 失败 | HTTP错误: 403 |
| 38 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 876.34 | ❌ 失败 | HTTP错误: 403 |
| 39 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 983.4 | ❌ 失败 | HTTP错误: 429 |
| 40 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 971.57 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 990.72 | ❌ 失败 | HTTP错误: 429 |
| 42 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | 403 | 1048.11 | ❌ 失败 | HTTP错误: 403 |
| 43 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 976.74 | ❌ 失败 | HTTP错误: 403 |
| 44 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | 403 | 1050.03 | ❌ 失败 | HTTP错误: 403 |
| 45 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 1043.7 | ❌ 失败 | HTTP错误: 403 |
| 46 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 1062.79 | ❌ 失败 | HTTP错误: 403 |
| 47 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 1112.33 | ❌ 失败 | HTTP错误: 403 |
| 48 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 1073.17 | ❌ 失败 | HTTP错误: 403 |
| 49 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 1147.77 | ❌ 失败 | HTTP错误: 500 |
| 50 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 1076.24 | ❌ 失败 | HTTP错误: 403 |
| 51 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 806.62 | ❌ 失败 | HTTP错误: 403 |
| 52 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 843.66 | ❌ 失败 | HTTP错误: 403 |
| 53 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1818.18 | ✅ 通过 | - |
| 54 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 1280.43 | ✅ 通过 | - |
| 55 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 762.84 | ❌ 失败 | HTTP错误: 403 |
| 56 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 2032.43 | ✅ 通过 | - |
| 57 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3038.08 | ✅ 通过 | - |
| 58 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 1126.93 | ✅ 通过 | - |
| 59 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 1092.0 | ✅ 通过 | - |
| 60 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 1128.04 | ✅ 通过 | - |
| 61 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 1355.35 | ✅ 通过 | - |
| 62 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 662.13 | ❌ 失败 | HTTP错误: 403 |
| 63 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1574.11 | ✅ 通过 | - |
| 64 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1726.6 | ✅ 通过 | - |
| 65 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 547.93 | ❌ 失败 | HTTP错误: 403 |
| 66 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 2055.31 | ✅ 通过 | - |
| 67 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1905.67 | ✅ 通过 | - |
| 68 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1230.69 | ✅ 通过 | - |
| 69 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 957.6 | ✅ 通过 | - |
| 70 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1395.47 | ✅ 通过 | - |
| 71 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1156.78 | ✅ 通过 | - |
| 72 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 766.95 | ✅ 通过 | - |
| 73 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 522.68 | ❌ 失败 | HTTP错误: 403 |
| 74 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | 429 | 536.29 | ❌ 失败 | HTTP错误: 429 |
| 75 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 556.2 | ❌ 失败 | HTTP错误: 403 |
| 76 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 597.45 | ❌ 失败 | HTTP错误: 403 |
| 77 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2405.35 | ✅ 通过 | - |
| 78 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 546.13 | ❌ 失败 | HTTP错误: 403 |
| 79 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 613.85 | ❌ 失败 | HTTP错误: 403 |
| 80 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 594.95 | ❌ 失败 | HTTP错误: 403 |
| 81 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 568.38 | ❌ 失败 | HTTP错误: 403 |
| 82 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 3266.88 | ✅ 通过 | - |
| 83 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 581.49 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2458.31 | ✅ 通过 | - |
| 85 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 1014.3 | ✅ 通过 | - |
| 86 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 355.95 | ❌ 失败 | HTTP错误: 403 |
| 87 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1549.15 | ✅ 通过 | - |
| 88 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1170.55 | ✅ 通过 | - |
| 89 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 863.86 | ✅ 通过 | - |
| 90 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 456.55 | ❌ 失败 | HTTP错误: 403 |
| 91 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1713.28 | ✅ 通过 | - |
| 92 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 4813.44 | ✅ 通过 | - |
| 93 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 364.71 | ❌ 失败 | HTTP错误: 403 |
| 94 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 351.63 | ❌ 失败 | HTTP错误: 403 |
| 95 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 10495.7 | ✅ 通过 | - |
| 96 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 11909.52 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 367.26 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 362.45 | ❌ 失败 | HTTP错误: 403 |
| 99 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 15991.87 | ✅ 通过 | - |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 540.78 | ✅ 通过 | - |
| 101 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 840.23 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1335.23 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 643.02 | ✅ 通过 | - |
| 104 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 773.02 | ✅ 通过 | - |
| 105 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 402.45 | ❌ 失败 | HTTP错误: 403 |
| 106 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 497.39 | ❌ 失败 | HTTP错误: 403 |
| 107 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 388.49 | ❌ 失败 | HTTP错误: 429 |
| 108 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 7942.49 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 364.72 | ❌ 失败 | HTTP错误: 403 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1436.61 | ✅ 通过 | - |
| 111 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 4960.18 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1939.99 | ✅ 通过 | - |
| 113 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 12970.32 | ✅ 通过 | - |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 435.34 | ❌ 失败 | HTTP错误: 403 |
| 115 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 345.88 | ❌ 失败 | HTTP错误: 403 |
| 116 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 2585.56 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 865.05 | ✅ 通过 | - |
| 118 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 119 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 120 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 121 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 123 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 124 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 125 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 334.82 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1010.58 | ✅ 通过 | - |
| 127 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 129 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 415.26 | ❌ 失败 | HTTP错误: 403 |
| 130 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2031.78 | ✅ 通过 | - |
| 132 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 576.68 | ✅ 通过 | - |
| 133 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 417.05 | ❌ 失败 | HTTP错误: 500 |
| 134 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 135 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 556.21 | ❌ 失败 | HTTP错误: 403 |
| 141 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 549.96 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 482.45 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 513.78 | ❌ 失败 | HTTP错误: 500 |
| 144 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 484.98 | ❌ 失败 | HTTP错误: 500 |
| 145 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1149.08 | ✅ 通过 | - |
| 146 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 721.77 | ❌ 失败 | HTTP错误: 500 |
| 147 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 594.87 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 563.31 | ❌ 失败 | HTTP错误: 500 |
| 149 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2041.86 | ✅ 通过 | - |
| 150 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 5636.93 | ✅ 通过 | - |
| 151 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1636.3 | ✅ 通过 | - |
| 152 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 797.32 | ✅ 通过 | - |
| 153 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1092.91 | ✅ 通过 | - |
| 154 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 974.03 | ✅ 通过 | - |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1417.56 | ✅ 通过 | - |
| 156 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 9035.88 | ✅ 通过 | - |
| 157 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 158 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1078.56 | ✅ 通过 | - |
| 159 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 445.6 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 408.32 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 461.42 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 502.62 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2206.55 | ✅ 通过 | - |
| 164 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 464.82 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 482.09 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 539.58 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 632.3 | ❌ 失败 | HTTP错误: 500 |
| 168 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 3991.61 | ✅ 通过 | - |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 493.28 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 533.9 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 561.98 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 600.06 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 586.04 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 572.55 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 751.93 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 843.63 | ❌ 失败 | HTTP错误: 500 |
| 177 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 178 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 3886.87 | ✅ 通过 | - |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1438.45 | ✅ 通过 | - |
| 180 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 7376.53 | ✅ 通过 | - |
| 181 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 9170.73 | ✅ 通过 | - |
| 183 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 15768.24 | ✅ 通过 | - |
| 184 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 22726.3 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_19

**密钥显示**: bce-v3/ALTAK-zUMTlWB...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_20

**密钥显示**: bce-v3/ALTAK-fEzp0Tw...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 42 |
| 失败 | 114 |
| 超时 | 37 |
| 通过率 | 21.76% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 403

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 403

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-publicopinion-classification**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **stable-diffusion-xl**: HTTP错误: 429

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qianfan-funccaller**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1202.21 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1161.89 | ❌ 失败 | HTTP错误: 403 |
| 3 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1166.92 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1201.42 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1218.77 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1207.41 | ❌ 失败 | HTTP错误: 403 |
| 7 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1188.03 | ❌ 失败 | HTTP错误: 429 |
| 8 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1231.13 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1257.26 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1257.69 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1288.37 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1325.53 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1320.94 | ❌ 失败 | HTTP错误: 403 |
| 14 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1247.6 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1356.59 | ❌ 失败 | HTTP错误: 403 |
| 16 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1337.71 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1433.4 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1471.19 | ❌ 失败 | HTTP错误: 403 |
| 19 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1555.46 | ❌ 失败 | HTTP错误: 403 |
| 20 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1626.74 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1046.8 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1123.11 | ❌ 失败 | HTTP错误: 403 |
| 23 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 991.88 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1075.42 | ❌ 失败 | HTTP错误: 403 |
| 25 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 979.75 | ❌ 失败 | HTTP错误: 429 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 597.41 | ❌ 失败 | HTTP错误: 403 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 403 | 593.04 | ❌ 失败 | HTTP错误: 403 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 589.02 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 488.61 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 403 | 521.5 | ❌ 失败 | HTTP错误: 403 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 413.14 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 449.2 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 360.28 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 425.06 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 348.52 | ❌ 失败 | HTTP错误: 403 |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 413.09 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 364.21 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3438.66 | ✅ 通过 | - |
| 39 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 378.55 | ❌ 失败 | HTTP错误: 403 |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 484.07 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 461.19 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 472.55 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 426.55 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 491.4 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 403.51 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 523.75 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 452.27 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 477.33 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 447.7 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 491.67 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 496.39 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 440.23 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 442.81 | ❌ 失败 | HTTP错误: 403 |
| 54 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 462.07 | ❌ 失败 | HTTP错误: 403 |
| 55 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 434.88 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 479.12 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 483.82 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | 403 | 400.03 | ❌ 失败 | HTTP错误: 403 |
| 59 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 430.22 | ❌ 失败 | HTTP错误: 403 |
| 60 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 457.68 | ❌ 失败 | HTTP错误: 403 |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 799.96 | ✅ 通过 | - |
| 62 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 308.01 | ❌ 失败 | HTTP错误: 403 |
| 63 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 319.23 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 383.47 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 647.09 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 364.05 | ❌ 失败 | HTTP错误: 403 |
| 67 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 470.21 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 491.95 | ❌ 失败 | HTTP错误: 403 |
| 69 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | 429 | 371.01 | ❌ 失败 | HTTP错误: 429 |
| 70 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 373.62 | ❌ 失败 | HTTP错误: 403 |
| 71 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 654.14 | ❌ 失败 | HTTP错误: 403 |
| 72 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 338.21 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 354.2 | ❌ 失败 | HTTP错误: 403 |
| 74 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 316.47 | ❌ 失败 | HTTP错误: 403 |
| 75 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 353.19 | ❌ 失败 | HTTP错误: 403 |
| 76 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | 403 | 330.48 | ❌ 失败 | HTTP错误: 403 |
| 77 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 332.58 | ❌ 失败 | HTTP错误: 403 |
| 78 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 10567.44 | ✅ 通过 | - |
| 79 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 566.46 | ✅ 通过 | - |
| 80 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 386.43 | ❌ 失败 | HTTP错误: 403 |
| 81 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1966.45 | ✅ 通过 | - |
| 82 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1089.98 | ✅ 通过 | - |
| 83 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6506.64 | ✅ 通过 | - |
| 84 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 793.16 | ✅ 通过 | - |
| 85 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 329.47 | ❌ 失败 | HTTP错误: 403 |
| 86 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 335.45 | ❌ 失败 | HTTP错误: 403 |
| 87 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 51007.59 | ✅ 通过 | - |
| 88 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 91 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 96 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 98 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 99 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 100 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 101 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 102 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 103 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 104 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 894.13 | ❌ 失败 | HTTP错误: 403 |
| 105 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 807.52 | ❌ 失败 | HTTP错误: 403 |
| 106 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 861.41 | ❌ 失败 | HTTP错误: 403 |
| 107 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 108 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 981.22 | ✅ 通过 | - |
| 109 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 1094.82 | ✅ 通过 | - |
| 110 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 1292.83 | ✅ 通过 | - |
| 111 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 584.38 | ❌ 失败 | HTTP错误: 403 |
| 112 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 666.7 | ❌ 失败 | HTTP错误: 403 |
| 113 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 529.75 | ❌ 失败 | HTTP错误: 403 |
| 114 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1536.41 | ✅ 通过 | - |
| 115 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 491.98 | ❌ 失败 | HTTP错误: 403 |
| 116 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 484.35 | ❌ 失败 | HTTP错误: 403 |
| 117 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1484.48 | ✅ 通过 | - |
| 118 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 925.67 | ✅ 通过 | - |
| 119 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1629.83 | ✅ 通过 | - |
| 120 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1925.36 | ✅ 通过 | - |
| 121 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 4724.32 | ✅ 通过 | - |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 766.82 | ✅ 通过 | - |
| 123 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 124 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 5382.45 | ✅ 通过 | - |
| 125 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 392.99 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 1938.75 | ✅ 通过 | - |
| 127 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 446.88 | ❌ 失败 | HTTP错误: 403 |
| 128 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 7261.33 | ✅ 通过 | - |
| 129 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 7475.91 | ✅ 通过 | - |
| 130 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 9104.46 | ✅ 通过 | - |
| 131 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 398.72 | ❌ 失败 | HTTP错误: 403 |
| 132 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 4722.3 | ✅ 通过 | - |
| 133 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 466.06 | ❌ 失败 | HTTP错误: 500 |
| 134 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 9351.71 | ✅ 通过 | - |
| 135 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 9752.87 | ✅ 通过 | - |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 373.98 | ❌ 失败 | HTTP错误: 403 |
| 137 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2419.29 | ✅ 通过 | - |
| 138 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 878.87 | ✅ 通过 | - |
| 139 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 395.44 | ❌ 失败 | HTTP错误: 500 |
| 140 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 360.06 | ❌ 失败 | HTTP错误: 500 |
| 141 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 434.66 | ❌ 失败 | HTTP错误: 500 |
| 142 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 393.8 | ❌ 失败 | HTTP错误: 500 |
| 143 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1604.95 | ✅ 通过 | - |
| 144 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 414.22 | ❌ 失败 | HTTP错误: 500 |
| 145 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 442.17 | ❌ 失败 | HTTP错误: 500 |
| 146 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 405.23 | ❌ 失败 | HTTP错误: 500 |
| 147 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 1123.97 | ✅ 通过 | - |
| 148 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 4169.48 | ✅ 通过 | - |
| 149 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 150 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1438.05 | ✅ 通过 | - |
| 151 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 981.42 | ✅ 通过 | - |
| 152 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 7712.5 | ✅ 通过 | - |
| 153 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 742.12 | ✅ 通过 | - |
| 154 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2105.99 | ✅ 通过 | - |
| 155 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1231.35 | ✅ 通过 | - |
| 156 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1122.67 | ✅ 通过 | - |
| 157 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 408.73 | ❌ 失败 | HTTP错误: 500 |
| 158 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 445.18 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 419.89 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 345.32 | ❌ 失败 | HTTP错误: 500 |
| 161 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 358.06 | ❌ 失败 | HTTP错误: 500 |
| 162 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 364.55 | ❌ 失败 | HTTP错误: 500 |
| 163 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 429.96 | ❌ 失败 | HTTP错误: 500 |
| 164 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 426.23 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 359.34 | ❌ 失败 | HTTP错误: 500 |
| 166 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 394.58 | ❌ 失败 | HTTP错误: 500 |
| 167 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 409.35 | ❌ 失败 | HTTP错误: 500 |
| 168 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 426.04 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 415.61 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 411.54 | ❌ 失败 | HTTP错误: 500 |
| 171 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 446.43 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 384.64 | ❌ 失败 | HTTP错误: 500 |
| 173 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1417.92 | ✅ 通过 | - |
| 174 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 175 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 176 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 177 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 178 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 181 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 23598.07 | ✅ 通过 | - |
| 184 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 12294.31 | ✅ 通过 | - |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_21

**密钥显示**: bce-v3/ALTAK-eh4pLo8...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_22

**密钥显示**: bce-v3/ALTAK-0IgCdhs...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 27 |
| 失败 | 137 |
| 超时 | 29 |
| 通过率 | 13.99% |


### 3. 异常汇总

- **deepseek-r1**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **qianfan-publicopinion-classification**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **deepseek-v3.1-250821**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **qianfan-engcard-vl**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **qwen-image-edit**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **kimi-k2.5**: HTTP错误: 403

- **glm-5**: HTTP错误: 403

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1177.7 | ❌ 失败 | HTTP错误: 403 |
| 2 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1194.49 | ❌ 失败 | HTTP错误: 429 |
| 3 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1208.4 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1239.57 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1268.09 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1315.22 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1307.61 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1307.54 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1309.82 | ❌ 失败 | HTTP错误: 403 |
| 10 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1266.53 | ❌ 失败 | HTTP错误: 403 |
| 11 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1295.25 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1343.15 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1345.12 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1347.04 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1367.94 | ❌ 失败 | HTTP错误: 403 |
| 16 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1241.27 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1396.76 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1357.58 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1401.31 | ❌ 失败 | HTTP错误: 403 |
| 20 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1420.96 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1190.52 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1192.91 | ❌ 失败 | HTTP错误: 403 |
| 23 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 1193.41 | ❌ 失败 | HTTP错误: 429 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1241.47 | ❌ 失败 | HTTP错误: 403 |
| 25 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1338.14 | ❌ 失败 | HTTP错误: 403 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 474.3 | ❌ 失败 | HTTP错误: 403 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 476.26 | ❌ 失败 | HTTP错误: 429 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 617.55 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 542.36 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 346.24 | ❌ 失败 | HTTP错误: 429 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 369.61 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 455.94 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 382.15 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 359.05 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 429.65 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3222.14 | ✅ 通过 | - |
| 37 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 357.74 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 447.51 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 374.53 | ❌ 失败 | HTTP错误: 403 |
| 40 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 564.46 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 442.47 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 467.06 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 461.83 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 448.45 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 484.18 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 507.94 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 917.95 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 409.6 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 452.2 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 505.24 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 511.87 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 429.33 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 479.65 | ❌ 失败 | HTTP错误: 403 |
| 54 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 465.1 | ❌ 失败 | HTTP错误: 403 |
| 55 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 380.44 | ❌ 失败 | HTTP错误: 403 |
| 56 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 431.64 | ❌ 失败 | HTTP错误: 403 |
| 57 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 477.04 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 397.53 | ❌ 失败 | HTTP错误: 403 |
| 59 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | 403 | 451.79 | ❌ 失败 | HTTP错误: 403 |
| 60 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 422.99 | ❌ 失败 | HTTP错误: 403 |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 732.79 | ✅ 通过 | - |
| 62 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1139.1 | ✅ 通过 | - |
| 63 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 546.98 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 551.68 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 529.98 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 658.26 | ❌ 失败 | HTTP错误: 403 |
| 67 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 431.93 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 428.63 | ❌ 失败 | HTTP错误: 403 |
| 69 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 440.47 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 325.53 | ❌ 失败 | HTTP错误: 403 |
| 71 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 410.57 | ❌ 失败 | HTTP错误: 403 |
| 72 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 505.84 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 435.19 | ❌ 失败 | HTTP错误: 403 |
| 74 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 327.09 | ❌ 失败 | HTTP错误: 403 |
| 75 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 359.41 | ❌ 失败 | HTTP错误: 403 |
| 76 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 84 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 86 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 87 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 823.38 | ❌ 失败 | HTTP错误: 403 |
| 91 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 785.36 | ❌ 失败 | HTTP错误: 403 |
| 93 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 838.15 | ❌ 失败 | HTTP错误: 403 |
| 95 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 858.05 | ❌ 失败 | HTTP错误: 403 |
| 96 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 853.63 | ❌ 失败 | HTTP错误: 403 |
| 97 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 877.35 | ❌ 失败 | HTTP错误: 403 |
| 98 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 907.26 | ❌ 失败 | HTTP错误: 403 |
| 99 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 940.56 | ❌ 失败 | HTTP错误: 403 |
| 100 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 789.75 | ❌ 失败 | HTTP错误: 429 |
| 101 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 102 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 844.23 | ❌ 失败 | HTTP错误: 429 |
| 103 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 1130.24 | ❌ 失败 | HTTP错误: 403 |
| 104 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 1061.14 | ❌ 失败 | HTTP错误: 403 |
| 105 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 1254.52 | ❌ 失败 | HTTP错误: 429 |
| 106 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 880.84 | ❌ 失败 | HTTP错误: 429 |
| 107 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 844.1 | ❌ 失败 | HTTP错误: 429 |
| 108 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 841.61 | ❌ 失败 | HTTP错误: 403 |
| 109 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 932.04 | ❌ 失败 | HTTP错误: 403 |
| 110 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 861.56 | ❌ 失败 | HTTP错误: 403 |
| 111 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 733.85 | ❌ 失败 | HTTP错误: 403 |
| 112 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 916.3 | ❌ 失败 | HTTP错误: 403 |
| 113 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 939.36 | ❌ 失败 | HTTP错误: 403 |
| 114 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 870.97 | ❌ 失败 | HTTP错误: 403 |
| 115 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 983.87 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 921.16 | ❌ 失败 | HTTP错误: 403 |
| 117 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 1054.18 | ❌ 失败 | HTTP错误: 403 |
| 118 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 935.33 | ❌ 失败 | HTTP错误: 403 |
| 119 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 802.88 | ❌ 失败 | HTTP错误: 403 |
| 120 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 838.75 | ❌ 失败 | HTTP错误: 429 |
| 121 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 840.34 | ❌ 失败 | HTTP错误: 429 |
| 122 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 802.9 | ❌ 失败 | HTTP错误: 403 |
| 123 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1542.58 | ✅ 通过 | - |
| 124 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 788.4 | ❌ 失败 | HTTP错误: 403 |
| 125 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 864.8 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 933.89 | ❌ 失败 | HTTP错误: 403 |
| 127 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 1033.54 | ❌ 失败 | HTTP错误: 403 |
| 128 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 916.72 | ❌ 失败 | HTTP错误: 429 |
| 129 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 747.39 | ❌ 失败 | HTTP错误: 403 |
| 130 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 1480.63 | ✅ 通过 | - |
| 131 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 781.2 | ❌ 失败 | HTTP错误: 403 |
| 132 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 421.94 | ❌ 失败 | HTTP错误: 403 |
| 133 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 2200.51 | ✅ 通过 | - |
| 134 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1668.67 | ✅ 通过 | - |
| 135 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 429.32 | ❌ 失败 | HTTP错误: 500 |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 365.88 | ❌ 失败 | HTTP错误: 403 |
| 137 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 3115.9 | ✅ 通过 | - |
| 138 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 418.64 | ❌ 失败 | HTTP错误: 500 |
| 140 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2235.97 | ✅ 通过 | - |
| 141 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 865.61 | ❌ 失败 | HTTP错误: 500 |
| 142 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 400.24 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 447.26 | ❌ 失败 | HTTP错误: 500 |
| 144 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 2007.6 | ✅ 通过 | - |
| 145 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 446.55 | ❌ 失败 | HTTP错误: 500 |
| 146 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 439.0 | ❌ 失败 | HTTP错误: 500 |
| 147 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 462.42 | ❌ 失败 | HTTP错误: 500 |
| 148 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 667.28 | ✅ 通过 | - |
| 149 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 403 | 404.24 | ❌ 失败 | HTTP错误: 403 |
| 150 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1637.9 | ✅ 通过 | - |
| 151 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 7272.11 | ✅ 通过 | - |
| 152 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 153 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 539.93 | ❌ 失败 | HTTP错误: 403 |
| 154 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 7196.22 | ✅ 通过 | - |
| 155 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1054.03 | ✅ 通过 | - |
| 156 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8802.63 | ✅ 通过 | - |
| 157 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1130.63 | ✅ 通过 | - |
| 158 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 863.8 | ✅ 通过 | - |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 483.67 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 518.38 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 729.77 | ❌ 失败 | HTTP错误: 500 |
| 162 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1126.57 | ✅ 通过 | - |
| 163 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 9057.97 | ✅ 通过 | - |
| 164 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 515.02 | ❌ 失败 | HTTP错误: 500 |
| 165 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1323.78 | ✅ 通过 | - |
| 166 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 488.34 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 529.27 | ❌ 失败 | HTTP错误: 500 |
| 168 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1857.03 | ✅ 通过 | - |
| 169 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 567.27 | ❌ 失败 | HTTP错误: 500 |
| 170 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 556.3 | ❌ 失败 | HTTP错误: 500 |
| 171 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 617.63 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 624.28 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 679.46 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 660.08 | ❌ 失败 | HTTP错误: 500 |
| 175 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 176 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 646.64 | ❌ 失败 | HTTP错误: 500 |
| 177 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 524.4 | ❌ 失败 | HTTP错误: 500 |
| 178 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 706.64 | ❌ 失败 | HTTP错误: 500 |
| 179 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 564.86 | ❌ 失败 | HTTP错误: 500 |
| 180 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 8501.35 | ✅ 通过 | - |
| 181 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1490.13 | ✅ 通过 | - |
| 182 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 13659.94 | ✅ 通过 | - |
| 183 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 16873.71 | ✅ 通过 | - |
| 184 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 27024.61 | ✅ 通过 | - |
| 185 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_23

**密钥显示**: bce-v3/ALTAK-BdYlLqv...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 106 |
| 失败 | 44 |
| 超时 | 43 |
| 通过率 | 54.92% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-char-fiction-8k**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1138.54 | ❌ 失败 | HTTP错误: 403 |
| 2 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1128.46 | ❌ 失败 | HTTP错误: 500 |
| 3 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1332.89 | ❌ 失败 | HTTP错误: 403 |
| 4 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 375.01 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1768.61 | ✅ 通过 | - |
| 6 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 1844.27 | ✅ 通过 | - |
| 7 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 1871.53 | ✅ 通过 | - |
| 8 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 200 | 2499.06 | ✅ 通过 | - |
| 9 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2494.87 | ✅ 通过 | - |
| 10 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2537.11 | ✅ 通过 | - |
| 11 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2701.74 | ✅ 通过 | - |
| 12 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2719.44 | ✅ 通过 | - |
| 13 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 2852.81 | ✅ 通过 | - |
| 14 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 2850.92 | ✅ 通过 | - |
| 15 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 3000.06 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 3054.31 | ✅ 通过 | - |
| 17 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3199.82 | ✅ 通过 | - |
| 18 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 3337.88 | ✅ 通过 | - |
| 19 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 3697.95 | ✅ 通过 | - |
| 20 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1029.95 | ✅ 通过 | - |
| 21 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 4100.6 | ✅ 通过 | - |
| 22 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 446.89 | ❌ 失败 | HTTP错误: 403 |
| 23 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 550.63 | ❌ 失败 | HTTP错误: 429 |
| 24 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 5668.8 | ✅ 通过 | - |
| 25 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2685.25 | ✅ 通过 | - |
| 26 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2419.77 | ✅ 通过 | - |
| 27 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 369.34 | ❌ 失败 | HTTP错误: 403 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1423.18 | ✅ 通过 | - |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 457.0 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1336.87 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 361.56 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 329.51 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 1788.91 | ✅ 通过 | - |
| 34 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 10445.46 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 348.75 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 383.37 | ❌ 失败 | HTTP错误: 403 |
| 37 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1656.19 | ✅ 通过 | - |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 396.07 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 830.47 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 2215.18 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 383.66 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1445.96 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1136.18 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1412.7 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 814.89 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 662.81 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 552.63 | ✅ 通过 | - |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1463.45 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 671.84 | ✅ 通过 | - |
| 50 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 11259.58 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 516.35 | ✅ 通过 | - |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1917.36 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2511.58 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1036.04 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 983.66 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 12373.64 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 876.05 | ✅ 通过 | - |
| 63 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 787.73 | ✅ 通过 | - |
| 65 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 66 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 715.97 | ✅ 通过 | - |
| 68 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1079.32 | ✅ 通过 | - |
| 71 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 987.11 | ✅ 通过 | - |
| 76 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 1063.92 | ✅ 通过 | - |
| 77 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 504.25 | ❌ 失败 | HTTP错误: 403 |
| 78 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 839.24 | ✅ 通过 | - |
| 79 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1682.0 | ✅ 通过 | - |
| 81 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2729.94 | ✅ 通过 | - |
| 82 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1696.85 | ✅ 通过 | - |
| 83 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 649.42 | ❌ 失败 | HTTP错误: 403 |
| 84 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 792.44 | ✅ 通过 | - |
| 85 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 1976.69 | ✅ 通过 | - |
| 86 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 2160.72 | ✅ 通过 | - |
| 87 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2418.22 | ✅ 通过 | - |
| 88 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1624.82 | ✅ 通过 | - |
| 89 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 873.46 | ✅ 通过 | - |
| 90 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 919.42 | ✅ 通过 | - |
| 91 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1050.91 | ✅ 通过 | - |
| 93 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1369.34 | ✅ 通过 | - |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2091.7 | ✅ 通过 | - |
| 96 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 393.65 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 320.28 | ❌ 失败 | HTTP错误: 403 |
| 99 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1745.26 | ✅ 通过 | - |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 637.54 | ✅ 通过 | - |
| 101 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 768.76 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1123.86 | ✅ 通过 | - |
| 103 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 5374.67 | ✅ 通过 | - |
| 104 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 842.43 | ✅ 通过 | - |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1839.9 | ✅ 通过 | - |
| 106 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 4957.28 | ✅ 通过 | - |
| 107 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 1820.78 | ✅ 通过 | - |
| 108 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6863.18 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1667.65 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1043.39 | ✅ 通过 | - |
| 111 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 14805.63 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 2609.51 | ✅ 通过 | - |
| 113 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 11063.5 | ✅ 通过 | - |
| 114 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 10564.27 | ✅ 通过 | - |
| 115 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1853.21 | ✅ 通过 | - |
| 116 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 8118.73 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 880.71 | ✅ 通过 | - |
| 118 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 3599.24 | ✅ 通过 | - |
| 119 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 5668.18 | ✅ 通过 | - |
| 120 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 4834.77 | ✅ 通过 | - |
| 121 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 2413.82 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2819.58 | ✅ 通过 | - |
| 124 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 125 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 11058.5 | ✅ 通过 | - |
| 126 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 7373.4 | ✅ 通过 | - |
| 127 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 7866.78 | ✅ 通过 | - |
| 128 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 11371.35 | ✅ 通过 | - |
| 129 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 909.88 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 406.74 | ❌ 失败 | HTTP错误: 500 |
| 135 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 380.22 | ❌ 失败 | HTTP错误: 403 |
| 139 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 553.56 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 492.33 | ❌ 失败 | HTTP错误: 500 |
| 144 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 597.08 | ❌ 失败 | HTTP错误: 500 |
| 145 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 505.43 | ❌ 失败 | HTTP错误: 500 |
| 146 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1088.58 | ✅ 通过 | - |
| 148 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 149 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 554.65 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 613.61 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 615.09 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 1157.17 | ✅ 通过 | - |
| 153 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2236.16 | ✅ 通过 | - |
| 154 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1219.54 | ✅ 通过 | - |
| 155 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1781.02 | ✅ 通过 | - |
| 156 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1137.67 | ✅ 通过 | - |
| 157 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 418.09 | ❌ 失败 | HTTP错误: 500 |
| 158 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1070.26 | ✅ 通过 | - |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 462.81 | ❌ 失败 | HTTP错误: 500 |
| 160 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1377.17 | ✅ 通过 | - |
| 161 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 693.46 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 438.08 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1419.23 | ✅ 通过 | - |
| 164 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 464.75 | ❌ 失败 | HTTP错误: 500 |
| 165 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2128.81 | ✅ 通过 | - |
| 166 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 534.26 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 577.11 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 554.89 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 537.8 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 554.51 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 536.54 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 518.52 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 582.26 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 507.48 | ❌ 失败 | HTTP错误: 500 |
| 175 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 176 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 548.26 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 553.06 | ❌ 失败 | HTTP错误: 500 |
| 178 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 4321.14 | ✅ 通过 | - |
| 179 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1641.17 | ✅ 通过 | - |
| 181 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 6163.51 | ✅ 通过 | - |
| 182 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 18075.98 | ✅ 通过 | - |
| 183 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 16772.2 | ✅ 通过 | - |
| 185 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 14663.27 | ✅ 通过 | - |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_24

**密钥显示**: bce-v3/ALTAK-7Kwdqqm...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 20 |
| 失败 | 145 |
| 超时 | 28 |
| 通过率 | 10.36% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **qianfan-8b**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **qianfan-engcard-vl**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-x1.1-preview**: HTTP错误: 403

- **qwen-image-edit**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **paddleocr-vl-0.9b**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 429

- **ernie-x1.1**: HTTP错误: 403

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **pp-structurev3**: HTTP错误: 429

- **qianfan-ocr**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1143.07 | ❌ 失败 | HTTP错误: 403 |
| 2 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1148.77 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1215.61 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1229.19 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1240.95 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1285.98 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1285.84 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1297.66 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1319.96 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1320.0 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1315.69 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1318.39 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1347.32 | ❌ 失败 | HTTP错误: 403 |
| 14 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1301.48 | ❌ 失败 | HTTP错误: 403 |
| 15 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1333.68 | ❌ 失败 | HTTP错误: 403 |
| 16 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1267.68 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1383.89 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1408.81 | ❌ 失败 | HTTP错误: 403 |
| 19 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1404.32 | ❌ 失败 | HTTP错误: 500 |
| 20 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1451.82 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 923.64 | ❌ 失败 | HTTP错误: 403 |
| 22 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1065.83 | ❌ 失败 | HTTP错误: 403 |
| 23 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1242.24 | ❌ 失败 | HTTP错误: 403 |
| 24 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1101.49 | ❌ 失败 | HTTP错误: 403 |
| 25 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 1030.27 | ❌ 失败 | HTTP错误: 429 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 682.19 | ❌ 失败 | HTTP错误: 403 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 611.97 | ❌ 失败 | HTTP错误: 429 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 637.76 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 457.98 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 505.33 | ❌ 失败 | HTTP错误: 429 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 405.3 | ❌ 失败 | HTTP错误: 403 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 400.49 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 488.12 | ❌ 失败 | HTTP错误: 429 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 452.15 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 436.94 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3400.72 | ✅ 通过 | - |
| 37 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 482.26 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 437.11 | ❌ 失败 | HTTP错误: 403 |
| 39 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 401.04 | ❌ 失败 | HTTP错误: 403 |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 449.93 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 527.93 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 410.87 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 459.83 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 468.03 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 403.27 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 689.92 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 395.95 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 464.71 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 429.83 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 417.71 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 422.54 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 444.24 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 751.49 | ✅ 通过 | - |
| 54 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 397.92 | ❌ 失败 | HTTP错误: 403 |
| 55 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 454.87 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 479.11 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 405.32 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 433.92 | ❌ 失败 | HTTP错误: 403 |
| 59 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 354.06 | ❌ 失败 | HTTP错误: 403 |
| 60 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 645.05 | ✅ 通过 | - |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 907.81 | ✅ 通过 | - |
| 62 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 403.31 | ❌ 失败 | HTTP错误: 403 |
| 63 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 345.09 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 322.94 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 517.16 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 394.5 | ❌ 失败 | HTTP错误: 403 |
| 67 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 331.7 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 338.86 | ❌ 失败 | HTTP错误: 403 |
| 69 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 544.58 | ❌ 失败 | HTTP错误: 403 |
| 84 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 86 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 855.31 | ❌ 失败 | HTTP错误: 403 |
| 87 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 881.68 | ❌ 失败 | HTTP错误: 403 |
| 88 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 817.78 | ❌ 失败 | HTTP错误: 403 |
| 89 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 975.76 | ❌ 失败 | HTTP错误: 403 |
| 90 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 913.29 | ❌ 失败 | HTTP错误: 403 |
| 91 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 1006.57 | ❌ 失败 | HTTP错误: 403 |
| 92 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 987.24 | ❌ 失败 | HTTP错误: 403 |
| 93 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 1093.43 | ❌ 失败 | HTTP错误: 403 |
| 94 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 940.46 | ❌ 失败 | HTTP错误: 403 |
| 96 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 999.65 | ❌ 失败 | HTTP错误: 403 |
| 97 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 803.88 | ❌ 失败 | HTTP错误: 403 |
| 98 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 1084.19 | ❌ 失败 | HTTP错误: 403 |
| 99 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 850.83 | ❌ 失败 | HTTP错误: 403 |
| 100 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 862.06 | ❌ 失败 | HTTP错误: 403 |
| 101 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1567.52 | ✅ 通过 | - |
| 102 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 888.87 | ❌ 失败 | HTTP错误: 429 |
| 103 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 872.65 | ❌ 失败 | HTTP错误: 429 |
| 104 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 970.57 | ❌ 失败 | HTTP错误: 429 |
| 105 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 855.03 | ❌ 失败 | HTTP错误: 403 |
| 106 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 888.56 | ❌ 失败 | HTTP错误: 403 |
| 107 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 918.93 | ❌ 失败 | HTTP错误: 403 |
| 108 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 1010.55 | ❌ 失败 | HTTP错误: 429 |
| 109 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 852.64 | ❌ 失败 | HTTP错误: 403 |
| 110 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 1036.47 | ❌ 失败 | HTTP错误: 403 |
| 111 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 1071.77 | ❌ 失败 | HTTP错误: 403 |
| 112 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 741.09 | ❌ 失败 | HTTP错误: 403 |
| 113 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 1233.84 | ❌ 失败 | HTTP错误: 429 |
| 114 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 876.63 | ❌ 失败 | HTTP错误: 403 |
| 115 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 839.49 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 1320.35 | ❌ 失败 | HTTP错误: 403 |
| 117 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 780.04 | ❌ 失败 | HTTP错误: 403 |
| 118 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 849.26 | ❌ 失败 | HTTP错误: 429 |
| 119 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 887.02 | ❌ 失败 | HTTP错误: 403 |
| 120 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 853.96 | ❌ 失败 | HTTP错误: 429 |
| 121 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 842.67 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 894.12 | ❌ 失败 | HTTP错误: 403 |
| 123 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 799.82 | ❌ 失败 | HTTP错误: 403 |
| 124 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 1058.63 | ❌ 失败 | HTTP错误: 403 |
| 125 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 805.6 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 886.3 | ❌ 失败 | HTTP错误: 403 |
| 127 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 938.0 | ❌ 失败 | HTTP错误: 403 |
| 128 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 808.23 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 790.18 | ❌ 失败 | HTTP错误: 403 |
| 130 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 816.3 | ❌ 失败 | HTTP错误: 403 |
| 131 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 921.86 | ❌ 失败 | HTTP错误: 429 |
| 132 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 783.06 | ❌ 失败 | HTTP错误: 403 |
| 133 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 838.15 | ❌ 失败 | HTTP错误: 403 |
| 134 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 840.98 | ❌ 失败 | HTTP错误: 403 |
| 135 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 832.46 | ❌ 失败 | HTTP错误: 403 |
| 136 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 854.81 | ❌ 失败 | HTTP错误: 403 |
| 137 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 839.24 | ❌ 失败 | HTTP错误: 403 |
| 138 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 747.19 | ❌ 失败 | HTTP错误: 403 |
| 139 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | 429 | 732.13 | ❌ 失败 | HTTP错误: 429 |
| 140 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 429 | 638.3 | ❌ 失败 | HTTP错误: 429 |
| 141 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 403 | 602.14 | ❌ 失败 | HTTP错误: 403 |
| 142 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 602.6 | ❌ 失败 | HTTP错误: 403 |
| 143 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | 429 | 703.97 | ❌ 失败 | HTTP错误: 429 |
| 144 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 403 | 639.08 | ❌ 失败 | HTTP错误: 403 |
| 145 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 612.45 | ❌ 失败 | HTTP错误: 500 |
| 146 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 609.73 | ❌ 失败 | HTTP错误: 500 |
| 147 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 597.26 | ❌ 失败 | HTTP错误: 500 |
| 148 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 660.83 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 648.26 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 661.85 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 614.76 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 758.11 | ✅ 通过 | - |
| 153 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 154 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1103.17 | ✅ 通过 | - |
| 156 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1904.75 | ✅ 通过 | - |
| 157 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1292.63 | ✅ 通过 | - |
| 158 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 933.52 | ✅ 通过 | - |
| 159 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2872.14 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 551.5 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 528.55 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 500.47 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1221.29 | ✅ 通过 | - |
| 164 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 518.57 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 488.68 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 573.15 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 813.56 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 511.58 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 577.97 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 535.61 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 564.77 | ❌ 失败 | HTTP错误: 500 |
| 172 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2506.11 | ✅ 通过 | - |
| 173 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 586.58 | ❌ 失败 | HTTP错误: 500 |
| 174 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 616.96 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 550.22 | ❌ 失败 | HTTP错误: 500 |
| 176 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 743.88 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 521.1 | ❌ 失败 | HTTP错误: 500 |
| 178 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1608.23 | ✅ 通过 | - |
| 179 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 5002.56 | ✅ 通过 | - |
| 180 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 4157.47 | ✅ 通过 | - |
| 181 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8870.75 | ✅ 通过 | - |
| 182 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 6343.69 | ✅ 通过 | - |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 11612.77 | ✅ 通过 | - |
| 185 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 14766.99 | ✅ 通过 | - |
| 186 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_25

**密钥显示**: bce-v3/ALTAK-eNInT9Z...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 25 |
| 失败 | 139 |
| 超时 | 29 |
| 通过率 | 12.95% |


### 3. 异常汇总

- **deepseek-v3**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **deepseek-r1**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-publicopinion-classification**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **deepseek-v3.1-250821**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **qianfan-engcard-vl**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qwen-image-edit**: HTTP错误: 429

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1111.42 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1157.25 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1207.41 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1220.88 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1257.35 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1207.87 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1263.44 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1283.34 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1275.53 | ❌ 失败 | HTTP错误: 403 |
| 10 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1248.79 | ❌ 失败 | HTTP错误: 403 |
| 11 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1215.35 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1330.12 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1345.37 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1395.56 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1342.28 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1389.31 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1447.3 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1488.7 | ❌ 失败 | HTTP错误: 403 |
| 19 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1471.3 | ❌ 失败 | HTTP错误: 429 |
| 20 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1557.68 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 948.39 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1032.98 | ❌ 失败 | HTTP错误: 403 |
| 23 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 900.73 | ❌ 失败 | HTTP错误: 429 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1122.13 | ❌ 失败 | HTTP错误: 403 |
| 25 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1298.77 | ❌ 失败 | HTTP错误: 403 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 710.14 | ❌ 失败 | HTTP错误: 403 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 603.18 | ❌ 失败 | HTTP错误: 429 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 594.65 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 469.32 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 447.64 | ❌ 失败 | HTTP错误: 429 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 444.29 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 393.11 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 414.75 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 357.99 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 439.25 | ❌ 失败 | HTTP错误: 403 |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 432.67 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 398.4 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 400.21 | ❌ 失败 | HTTP错误: 403 |
| 39 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3657.62 | ✅ 通过 | - |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 409.01 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 479.28 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 500.13 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 430.98 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 447.62 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 513.83 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 602.68 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 383.01 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 542.76 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 448.8 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 535.3 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 452.58 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 505.47 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 464.29 | ❌ 失败 | HTTP错误: 403 |
| 54 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 426.75 | ❌ 失败 | HTTP错误: 403 |
| 55 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 473.71 | ❌ 失败 | HTTP错误: 403 |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 586.36 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 406.09 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | 403 | 444.35 | ❌ 失败 | HTTP错误: 403 |
| 59 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 458.19 | ❌ 失败 | HTTP错误: 403 |
| 60 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 510.14 | ❌ 失败 | HTTP错误: 403 |
| 61 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 789.56 | ✅ 通过 | - |
| 62 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 481.44 | ❌ 失败 | HTTP错误: 403 |
| 63 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1057.04 | ✅ 通过 | - |
| 64 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 380.58 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 751.74 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 350.81 | ❌ 失败 | HTTP错误: 403 |
| 67 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 363.01 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 442.15 | ❌ 失败 | HTTP错误: 403 |
| 69 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 354.71 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 448.58 | ❌ 失败 | HTTP错误: 403 |
| 71 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 357.08 | ❌ 失败 | HTTP错误: 403 |
| 72 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 404.2 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 589.44 | ❌ 失败 | HTTP错误: 403 |
| 74 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 377.77 | ❌ 失败 | HTTP错误: 403 |
| 75 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 324.23 | ❌ 失败 | HTTP错误: 403 |
| 76 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 84 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 86 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 87 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 480.38 | ❌ 失败 | HTTP错误: 403 |
| 88 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 91 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 598.38 | ❌ 失败 | HTTP错误: 403 |
| 92 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 706.77 | ❌ 失败 | HTTP错误: 403 |
| 93 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 727.43 | ❌ 失败 | HTTP错误: 403 |
| 94 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 754.64 | ❌ 失败 | HTTP错误: 403 |
| 96 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 823.23 | ❌ 失败 | HTTP错误: 403 |
| 98 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 852.81 | ❌ 失败 | HTTP错误: 403 |
| 99 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 100 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 1021.09 | ❌ 失败 | HTTP错误: 403 |
| 101 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 852.61 | ❌ 失败 | HTTP错误: 429 |
| 102 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 904.15 | ❌ 失败 | HTTP错误: 403 |
| 103 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 834.42 | ❌ 失败 | HTTP错误: 429 |
| 104 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 953.07 | ❌ 失败 | HTTP错误: 403 |
| 105 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 914.84 | ❌ 失败 | HTTP错误: 429 |
| 106 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 1061.05 | ❌ 失败 | HTTP错误: 429 |
| 107 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 895.98 | ❌ 失败 | HTTP错误: 429 |
| 108 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 903.28 | ❌ 失败 | HTTP错误: 403 |
| 109 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 954.67 | ❌ 失败 | HTTP错误: 403 |
| 110 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 931.6 | ❌ 失败 | HTTP错误: 403 |
| 111 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 954.99 | ❌ 失败 | HTTP错误: 403 |
| 112 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 771.75 | ❌ 失败 | HTTP错误: 403 |
| 113 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 865.21 | ❌ 失败 | HTTP错误: 403 |
| 114 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 889.74 | ❌ 失败 | HTTP错误: 403 |
| 115 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 930.69 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 905.65 | ❌ 失败 | HTTP错误: 403 |
| 117 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 1153.13 | ❌ 失败 | HTTP错误: 403 |
| 118 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 947.61 | ❌ 失败 | HTTP错误: 403 |
| 119 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 806.49 | ❌ 失败 | HTTP错误: 429 |
| 120 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 1027.86 | ❌ 失败 | HTTP错误: 403 |
| 121 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 1121.98 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 925.49 | ❌ 失败 | HTTP错误: 429 |
| 123 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 901.22 | ❌ 失败 | HTTP错误: 403 |
| 124 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 887.35 | ❌ 失败 | HTTP错误: 403 |
| 125 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 823.72 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 808.15 | ❌ 失败 | HTTP错误: 403 |
| 127 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 844.49 | ❌ 失败 | HTTP错误: 403 |
| 128 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 844.67 | ❌ 失败 | HTTP错误: 403 |
| 129 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 902.68 | ❌ 失败 | HTTP错误: 403 |
| 130 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 965.26 | ❌ 失败 | HTTP错误: 403 |
| 131 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 1066.63 | ❌ 失败 | HTTP错误: 403 |
| 132 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 761.07 | ❌ 失败 | HTTP错误: 403 |
| 133 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 987.17 | ❌ 失败 | HTTP错误: 403 |
| 134 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 1466.31 | ❌ 失败 | HTTP错误: 429 |
| 135 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1419.16 | ✅ 通过 | - |
| 136 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 532.72 | ❌ 失败 | HTTP错误: 500 |
| 137 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 972.59 | ✅ 通过 | - |
| 138 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 466.67 | ❌ 失败 | HTTP错误: 403 |
| 139 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 423.5 | ❌ 失败 | HTTP错误: 500 |
| 140 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2569.44 | ✅ 通过 | - |
| 141 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 943.54 | ✅ 通过 | - |
| 142 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 394.19 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 522.83 | ❌ 失败 | HTTP错误: 500 |
| 144 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 530.09 | ❌ 失败 | HTTP错误: 500 |
| 145 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 507.8 | ❌ 失败 | HTTP错误: 500 |
| 146 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 969.09 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 426.62 | ❌ 失败 | HTTP错误: 500 |
| 149 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2749.87 | ✅ 通过 | - |
| 150 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1615.53 | ✅ 通过 | - |
| 151 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 773.05 | ✅ 通过 | - |
| 152 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1152.67 | ✅ 通过 | - |
| 153 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1246.35 | ✅ 通过 | - |
| 154 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 719.7 | ✅ 通过 | - |
| 155 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 6019.03 | ✅ 通过 | - |
| 156 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 157 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1516.38 | ✅ 通过 | - |
| 158 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1953.62 | ✅ 通过 | - |
| 159 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1345.13 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 654.13 | ❌ 失败 | HTTP错误: 500 |
| 161 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 3864.4 | ✅ 通过 | - |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 510.74 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 644.76 | ❌ 失败 | HTTP错误: 500 |
| 164 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 552.53 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 546.52 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 464.09 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 531.33 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 577.87 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 553.3 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 570.81 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 547.52 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 582.12 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 580.28 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 566.57 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 656.65 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 556.57 | ❌ 失败 | HTTP错误: 500 |
| 177 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 178 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 10252.14 | ✅ 通过 | - |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1531.91 | ✅ 通过 | - |
| 180 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 9754.35 | ✅ 通过 | - |
| 181 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 6935.15 | ✅ 通过 | - |
| 182 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 12402.45 | ✅ 通过 | - |
| 183 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 7237.06 | ✅ 通过 | - |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 11456.2 | ✅ 通过 | - |
| 185 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_26

**密钥显示**: bce-v3/ALTAK-JY3bs00...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 45 |
| 失败 | 111 |
| 超时 | 37 |
| 通过率 | 23.32% |


### 3. 异常汇总

- **irag-1.0**: HTTP错误: 429

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-x1-32k-preview**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **qianfan-publicopinion-classification**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **stable-diffusion-xl**: HTTP错误: 429

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qianfan-funccaller**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1121.52 | ❌ 失败 | HTTP错误: 429 |
| 2 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1203.42 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1209.89 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1221.86 | ❌ 失败 | HTTP错误: 403 |
| 5 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1175.13 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1219.56 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1216.0 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1218.72 | ❌ 失败 | HTTP错误: 403 |
| 9 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1209.54 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1269.71 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1309.4 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1301.58 | ❌ 失败 | HTTP错误: 403 |
| 13 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1261.44 | ❌ 失败 | HTTP错误: 403 |
| 14 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1257.56 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1365.13 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1457.21 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1467.89 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1489.44 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1838.62 | ❌ 失败 | HTTP错误: 403 |
| 20 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1873.51 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 948.81 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1059.89 | ❌ 失败 | HTTP错误: 403 |
| 23 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1172.23 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1113.67 | ❌ 失败 | HTTP错误: 403 |
| 25 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 584.65 | ❌ 失败 | HTTP错误: 403 |
| 26 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 907.74 | ❌ 失败 | HTTP错误: 429 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 403 | 539.0 | ❌ 失败 | HTTP错误: 403 |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 519.74 | ❌ 失败 | HTTP错误: 403 |
| 29 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 863.9 | ❌ 失败 | HTTP错误: 403 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 411.84 | ❌ 失败 | HTTP错误: 403 |
| 31 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 403 | 659.12 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 437.45 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 365.49 | ❌ 失败 | HTTP错误: 403 |
| 34 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2737.43 | ✅ 通过 | - |
| 35 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 443.46 | ❌ 失败 | HTTP错误: 403 |
| 36 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 408.77 | ❌ 失败 | HTTP错误: 403 |
| 37 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 427.22 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 416.93 | ❌ 失败 | HTTP错误: 403 |
| 39 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 483.3 | ❌ 失败 | HTTP错误: 403 |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 403.05 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 486.54 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 606.81 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 449.2 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 437.79 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 474.66 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 432.6 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 555.39 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 439.15 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 584.71 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 436.64 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 492.26 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 412.33 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 439.65 | ❌ 失败 | HTTP错误: 403 |
| 54 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 440.81 | ❌ 失败 | HTTP错误: 403 |
| 55 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 498.64 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 475.8 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 462.8 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 317.94 | ❌ 失败 | HTTP错误: 403 |
| 59 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | 403 | 617.29 | ❌ 失败 | HTTP错误: 403 |
| 60 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 414.28 | ❌ 失败 | HTTP错误: 403 |
| 61 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 743.62 | ✅ 通过 | - |
| 62 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 751.59 | ✅ 通过 | - |
| 63 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 367.48 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 394.22 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 460.03 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 411.01 | ❌ 失败 | HTTP错误: 403 |
| 67 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 374.91 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 485.35 | ❌ 失败 | HTTP错误: 403 |
| 69 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 453.16 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 471.78 | ❌ 失败 | HTTP错误: 403 |
| 71 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | 429 | 491.68 | ❌ 失败 | HTTP错误: 429 |
| 72 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 452.29 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 553.36 | ❌ 失败 | HTTP错误: 403 |
| 74 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 487.48 | ❌ 失败 | HTTP错误: 403 |
| 75 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 480.14 | ❌ 失败 | HTTP错误: 403 |
| 76 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 377.49 | ❌ 失败 | HTTP错误: 403 |
| 77 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | 403 | 425.06 | ❌ 失败 | HTTP错误: 403 |
| 78 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 386.84 | ❌ 失败 | HTTP错误: 403 |
| 79 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 627.58 | ✅ 通过 | - |
| 80 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 332.36 | ❌ 失败 | HTTP错误: 403 |
| 81 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2291.79 | ✅ 通过 | - |
| 82 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 747.54 | ✅ 通过 | - |
| 83 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 4717.44 | ✅ 通过 | - |
| 84 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 732.02 | ✅ 通过 | - |
| 85 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 372.05 | ❌ 失败 | HTTP错误: 403 |
| 86 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 306.0 | ❌ 失败 | HTTP错误: 403 |
| 87 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 13307.71 | ✅ 通过 | - |
| 88 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 91 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 96 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 98 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 99 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 100 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 101 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 102 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 103 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 822.07 | ❌ 失败 | HTTP错误: 403 |
| 104 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 788.4 | ❌ 失败 | HTTP错误: 403 |
| 105 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 106 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 107 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 1000.31 | ✅ 通过 | - |
| 108 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 1073.78 | ✅ 通过 | - |
| 109 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 1112.14 | ✅ 通过 | - |
| 110 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 568.47 | ❌ 失败 | HTTP错误: 403 |
| 111 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 572.6 | ❌ 失败 | HTTP错误: 403 |
| 112 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1543.58 | ✅ 通过 | - |
| 113 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 501.89 | ❌ 失败 | HTTP错误: 403 |
| 114 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 2155.06 | ✅ 通过 | - |
| 115 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 384.98 | ❌ 失败 | HTTP错误: 403 |
| 116 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 966.07 | ✅ 通过 | - |
| 117 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1637.83 | ✅ 通过 | - |
| 118 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 960.3 | ✅ 通过 | - |
| 119 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 3461.98 | ✅ 通过 | - |
| 120 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 5020.29 | ✅ 通过 | - |
| 121 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 922.62 | ✅ 通过 | - |
| 123 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 5310.39 | ✅ 通过 | - |
| 124 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 7157.64 | ✅ 通过 | - |
| 125 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 5958.94 | ✅ 通过 | - |
| 126 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 6962.13 | ✅ 通过 | - |
| 127 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 391.04 | ❌ 失败 | HTTP错误: 403 |
| 128 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 418.08 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2631.34 | ✅ 通过 | - |
| 130 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 8916.51 | ✅ 通过 | - |
| 131 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 504.75 | ✅ 通过 | - |
| 132 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 6961.06 | ✅ 通过 | - |
| 133 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 420.27 | ❌ 失败 | HTTP错误: 500 |
| 134 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 10698.59 | ✅ 通过 | - |
| 135 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 366.06 | ❌ 失败 | HTTP错误: 403 |
| 137 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2802.54 | ✅ 通过 | - |
| 139 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 411.81 | ❌ 失败 | HTTP错误: 500 |
| 140 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1100.94 | ✅ 通过 | - |
| 141 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 415.72 | ❌ 失败 | HTTP错误: 500 |
| 142 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 469.9 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 485.35 | ❌ 失败 | HTTP错误: 500 |
| 144 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 514.55 | ❌ 失败 | HTTP错误: 500 |
| 145 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 435.86 | ❌ 失败 | HTTP错误: 500 |
| 146 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 345.87 | ❌ 失败 | HTTP错误: 500 |
| 147 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1510.33 | ✅ 通过 | - |
| 148 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 550.8 | ✅ 通过 | - |
| 149 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1251.36 | ✅ 通过 | - |
| 150 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 6818.72 | ✅ 通过 | - |
| 151 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 16348.29 | ✅ 通过 | - |
| 152 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1296.97 | ✅ 通过 | - |
| 153 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1009.75 | ✅ 通过 | - |
| 154 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2239.17 | ✅ 通过 | - |
| 155 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1712.75 | ✅ 通过 | - |
| 156 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1136.8 | ✅ 通过 | - |
| 157 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 7234.41 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 361.84 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 427.84 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 388.98 | ❌ 失败 | HTTP错误: 500 |
| 161 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 446.67 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 640.57 | ❌ 失败 | HTTP错误: 500 |
| 163 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 506.01 | ❌ 失败 | HTTP错误: 500 |
| 164 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 750.01 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 427.51 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 451.83 | ❌ 失败 | HTTP错误: 500 |
| 167 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 476.93 | ❌ 失败 | HTTP错误: 500 |
| 168 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 391.66 | ❌ 失败 | HTTP错误: 500 |
| 169 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 506.12 | ❌ 失败 | HTTP错误: 500 |
| 170 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 471.78 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 511.74 | ❌ 失败 | HTTP错误: 500 |
| 172 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 488.46 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 516.26 | ❌ 失败 | HTTP错误: 500 |
| 174 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1668.19 | ✅ 通过 | - |
| 175 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 9287.3 | ✅ 通过 | - |
| 176 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 177 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 178 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 181 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 47213.45 | ✅ 通过 | - |


---


## API密钥: KEY_27

**密钥显示**: bce-v3/ALTAK-2vgbNGz...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_28

**密钥显示**: bce-v3/ALTAK-gkYESB8...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 6 |
| 失败 | 144 |
| 超时 | 43 |
| 通过率 | 3.11% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **qwq-32b**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **qianfan-engcard-vl**: HTTP错误: 403

- **ernie-x1-turbo-latest**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-x1.1**: HTTP错误: 403

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **qianfan-ocr**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **qianfan-vl-1.5-flash**: HTTP错误: 403

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **qianfan-ocr-fast**: HTTP错误: 403

- **kimi-k2.5**: HTTP错误: 403

- **glm-5**: HTTP错误: 403

- **minimax-m2.1**: HTTP错误: 403

- **ernie-5.0**: HTTP错误: 403

- **minimax-m2.5**: HTTP错误: 403

- **qwen3.5-35b-a3b**: HTTP错误: 403

- **viduq3-pro_text2video**: HTTP错误: 500

- **qwen3.5-397b-a17b**: HTTP错误: 403

- **qwen3.5-122b-a10b**: HTTP错误: 403

- **qwen3.5-27b**: HTTP错误: 403

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **ernie-4.5-turbo-20260402**: HTTP错误: 403

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **glm-5.1**: HTTP错误: 403


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1223.81 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1199.36 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1277.82 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1266.95 | ❌ 失败 | HTTP错误: 403 |
| 5 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1236.25 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1329.96 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1337.5 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1267.42 | ❌ 失败 | HTTP错误: 403 |
| 9 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1275.53 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1354.31 | ❌ 失败 | HTTP错误: 403 |
| 11 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1278.31 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1335.69 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1308.92 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1376.28 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1370.57 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1387.8 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1397.39 | ❌ 失败 | HTTP错误: 403 |
| 18 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1289.03 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1393.21 | ❌ 失败 | HTTP错误: 403 |
| 20 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1552.9 | ❌ 失败 | HTTP错误: 500 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1142.25 | ❌ 失败 | HTTP错误: 403 |
| 22 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1018.37 | ❌ 失败 | HTTP错误: 403 |
| 23 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1102.49 | ❌ 失败 | HTTP错误: 403 |
| 24 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1259.84 | ❌ 失败 | HTTP错误: 403 |
| 25 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 581.99 | ❌ 失败 | HTTP错误: 403 |
| 26 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 561.91 | ❌ 失败 | HTTP错误: 429 |
| 27 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 529.18 | ❌ 失败 | HTTP错误: 403 |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 422.85 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 390.59 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 326.61 | ❌ 失败 | HTTP错误: 403 |
| 31 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3043.01 | ✅ 通过 | - |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 414.88 | ❌ 失败 | HTTP错误: 500 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 453.14 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 412.68 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 396.08 | ❌ 失败 | HTTP错误: 403 |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 385.02 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 390.44 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 452.04 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 372.27 | ❌ 失败 | HTTP错误: 403 |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 564.93 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 313.88 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 390.12 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 421.94 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 397.87 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 351.9 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 428.22 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 358.56 | ❌ 失败 | HTTP错误: 403 |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 407.89 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 449.25 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 404.09 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 755.75 | ✅ 通过 | - |
| 52 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 419.02 | ❌ 失败 | HTTP错误: 403 |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 414.52 | ❌ 失败 | HTTP错误: 403 |
| 54 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 363.13 | ❌ 失败 | HTTP错误: 403 |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 377.96 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 430.39 | ❌ 失败 | HTTP错误: 403 |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 66 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 426.27 | ❌ 失败 | HTTP错误: 403 |
| 72 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 739.16 | ❌ 失败 | HTTP错误: 403 |
| 75 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 894.41 | ❌ 失败 | HTTP错误: 403 |
| 76 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 863.84 | ❌ 失败 | HTTP错误: 403 |
| 77 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 951.65 | ❌ 失败 | HTTP错误: 403 |
| 79 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 1008.2 | ❌ 失败 | HTTP错误: 403 |
| 81 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 1018.99 | ❌ 失败 | HTTP错误: 403 |
| 82 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 944.55 | ❌ 失败 | HTTP错误: 403 |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 989.5 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 969.96 | ❌ 失败 | HTTP错误: 403 |
| 85 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 986.5 | ❌ 失败 | HTTP错误: 403 |
| 86 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1408.22 | ✅ 通过 | - |
| 87 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 803.13 | ❌ 失败 | HTTP错误: 403 |
| 88 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1643.79 | ✅ 通过 | - |
| 89 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 756.89 | ❌ 失败 | HTTP错误: 403 |
| 90 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 762.25 | ❌ 失败 | HTTP错误: 403 |
| 91 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1224.85 | ✅ 通过 | - |
| 92 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 764.01 | ❌ 失败 | HTTP错误: 403 |
| 93 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 757.53 | ❌ 失败 | HTTP错误: 403 |
| 94 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 835.5 | ❌ 失败 | HTTP错误: 403 |
| 95 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 817.01 | ❌ 失败 | HTTP错误: 403 |
| 96 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 854.95 | ❌ 失败 | HTTP错误: 403 |
| 97 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 836.26 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 824.01 | ❌ 失败 | HTTP错误: 403 |
| 99 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 735.04 | ❌ 失败 | HTTP错误: 403 |
| 100 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 734.16 | ❌ 失败 | HTTP错误: 403 |
| 101 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 681.2 | ❌ 失败 | HTTP错误: 403 |
| 102 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 726.32 | ❌ 失败 | HTTP错误: 403 |
| 103 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 733.39 | ❌ 失败 | HTTP错误: 403 |
| 104 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 2177.52 | ❌ 失败 | HTTP错误: 403 |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 489.33 | ❌ 失败 | HTTP错误: 403 |
| 106 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 589.83 | ❌ 失败 | HTTP错误: 403 |
| 107 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 403 | 530.77 | ❌ 失败 | HTTP错误: 403 |
| 108 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 688.94 | ❌ 失败 | HTTP错误: 403 |
| 109 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 710.66 | ❌ 失败 | HTTP错误: 403 |
| 110 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 515.55 | ❌ 失败 | HTTP错误: 403 |
| 111 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 578.1 | ❌ 失败 | HTTP错误: 403 |
| 112 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 509.83 | ❌ 失败 | HTTP错误: 403 |
| 113 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 549.14 | ❌ 失败 | HTTP错误: 403 |
| 114 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 456.68 | ❌ 失败 | HTTP错误: 403 |
| 115 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 523.74 | ❌ 失败 | HTTP错误: 403 |
| 116 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 506.8 | ❌ 失败 | HTTP错误: 403 |
| 117 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 541.13 | ❌ 失败 | HTTP错误: 403 |
| 118 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 468.65 | ❌ 失败 | HTTP错误: 403 |
| 119 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 495.73 | ❌ 失败 | HTTP错误: 403 |
| 120 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 748.84 | ❌ 失败 | HTTP错误: 403 |
| 121 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 354.86 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 371.78 | ❌ 失败 | HTTP错误: 403 |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 354.03 | ❌ 失败 | HTTP错误: 403 |
| 124 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 312.2 | ❌ 失败 | HTTP错误: 403 |
| 125 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 346.54 | ❌ 失败 | HTTP错误: 403 |
| 126 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 588.72 | ❌ 失败 | HTTP错误: 403 |
| 127 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 129 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 488.75 | ❌ 失败 | HTTP错误: 403 |
| 133 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 520.14 | ❌ 失败 | HTTP错误: 500 |
| 135 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 403 | 470.36 | ❌ 失败 | HTTP错误: 403 |
| 143 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 144 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 458.07 | ❌ 失败 | HTTP错误: 403 |
| 145 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 403 | 606.29 | ❌ 失败 | HTTP错误: 403 |
| 146 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 711.32 | ❌ 失败 | HTTP错误: 500 |
| 147 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 702.2 | ❌ 失败 | HTTP错误: 500 |
| 148 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 715.73 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 635.61 | ❌ 失败 | HTTP错误: 500 |
| 150 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 403 | 685.24 | ❌ 失败 | HTTP错误: 403 |
| 151 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 717.08 | ❌ 失败 | HTTP错误: 500 |
| 152 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 711.37 | ❌ 失败 | HTTP错误: 500 |
| 153 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 154 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 155 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 403 | 596.87 | ❌ 失败 | HTTP错误: 403 |
| 156 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 403 | 631.19 | ❌ 失败 | HTTP错误: 403 |
| 157 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 573.27 | ❌ 失败 | HTTP错误: 403 |
| 158 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 403 | 623.1 | ❌ 失败 | HTTP错误: 403 |
| 159 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 403 | 564.04 | ❌ 失败 | HTTP错误: 403 |
| 160 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 403 | 610.22 | ❌ 失败 | HTTP错误: 403 |
| 161 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 403 | 600.22 | ❌ 失败 | HTTP错误: 403 |
| 162 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 1086.29 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 403 | 674.56 | ❌ 失败 | HTTP错误: 403 |
| 164 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 403 | 700.78 | ❌ 失败 | HTTP错误: 403 |
| 165 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 403 | 693.66 | ❌ 失败 | HTTP错误: 403 |
| 166 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 673.73 | ❌ 失败 | HTTP错误: 500 |
| 167 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 750.98 | ❌ 失败 | HTTP错误: 500 |
| 168 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 746.4 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 746.64 | ❌ 失败 | HTTP错误: 500 |
| 170 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 778.78 | ❌ 失败 | HTTP错误: 500 |
| 171 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 835.23 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 680.24 | ❌ 失败 | HTTP错误: 500 |
| 173 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 174 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 175 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 709.39 | ❌ 失败 | HTTP错误: 500 |
| 176 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2913.0 | ✅ 通过 | - |
| 177 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 178 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 833.83 | ❌ 失败 | HTTP错误: 500 |
| 179 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 759.05 | ❌ 失败 | HTTP错误: 500 |
| 180 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 728.96 | ❌ 失败 | HTTP错误: 500 |
| 181 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 722.16 | ❌ 失败 | HTTP错误: 500 |
| 182 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 927.05 | ❌ 失败 | HTTP错误: 500 |
| 183 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 721.4 | ❌ 失败 | HTTP错误: 500 |
| 184 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 753.93 | ❌ 失败 | HTTP错误: 500 |
| 185 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 403 | 682.04 | ❌ 失败 | HTTP错误: 403 |
| 186 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 766.3 | ❌ 失败 | HTTP错误: 500 |
| 187 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 403 | 612.55 | ❌ 失败 | HTTP错误: 403 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_29

**密钥显示**: bce-v3/ALTAK-2QsibrE...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_30

**密钥显示**: bce-v3/ALTAK-SAui2P8...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_31

**密钥显示**: bce-v3/ALTAK-KmUVUm1...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_32

**密钥显示**: bce-v3/ALTAK-KmUVUm1...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_33

**密钥显示**: bce-v3/ALTAK-QwuihwY...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_34

**密钥显示**: bce-v3/ALTAK-8kzjaxS...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 102 |
| 失败 | 48 |
| 超时 | 43 |
| 通过率 | 52.85% |


### 3. 异常汇总

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-novel-8k**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1225.7 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1274.42 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1281.28 | ❌ 失败 | HTTP错误: 403 |
| 4 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1257.63 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1349.52 | ❌ 失败 | HTTP错误: 403 |
| 6 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1343.62 | ❌ 失败 | HTTP错误: 500 |
| 7 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1419.55 | ❌ 失败 | HTTP错误: 403 |
| 8 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 584.51 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1917.95 | ✅ 通过 | - |
| 10 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 2131.86 | ✅ 通过 | - |
| 11 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2758.56 | ✅ 通过 | - |
| 12 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2772.33 | ✅ 通过 | - |
| 13 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 2961.8 | ✅ 通过 | - |
| 14 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 3184.23 | ✅ 通过 | - |
| 15 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3127.48 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 3235.69 | ✅ 通过 | - |
| 17 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 3249.13 | ✅ 通过 | - |
| 18 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 3346.71 | ✅ 通过 | - |
| 19 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 3402.17 | ✅ 通过 | - |
| 20 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1200.42 | ✅ 通过 | - |
| 21 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 4874.72 | ✅ 通过 | - |
| 22 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 367.85 | ❌ 失败 | HTTP错误: 403 |
| 23 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 5299.85 | ✅ 通过 | - |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2388.82 | ✅ 通过 | - |
| 25 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 581.06 | ❌ 失败 | HTTP错误: 429 |
| 26 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2504.53 | ✅ 通过 | - |
| 27 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 401.86 | ❌ 失败 | HTTP错误: 403 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1823.51 | ✅ 通过 | - |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 464.14 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1242.68 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 440.74 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 392.14 | ❌ 失败 | HTTP错误: 403 |
| 33 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 8901.03 | ✅ 通过 | - |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 1782.44 | ✅ 通过 | - |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1426.36 | ✅ 通过 | - |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 477.15 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 456.44 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 454.77 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 1063.94 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 2029.84 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 399.91 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 2191.14 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1070.86 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1124.91 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 925.52 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 1412.39 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 773.37 | ✅ 通过 | - |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1223.87 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 1040.31 | ✅ 通过 | - |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1480.92 | ✅ 通过 | - |
| 51 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 13777.67 | ✅ 通过 | - |
| 52 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 775.44 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2165.43 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1153.94 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1621.98 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 8252.83 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 1039.3 | ✅ 通过 | - |
| 66 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1042.43 | ✅ 通过 | - |
| 67 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 891.34 | ✅ 通过 | - |
| 68 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 697.17 | ✅ 通过 | - |
| 69 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1312.57 | ✅ 通过 | - |
| 71 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 1134.02 | ✅ 通过 | - |
| 74 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 502.01 | ❌ 失败 | HTTP错误: 403 |
| 78 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1391.67 | ✅ 通过 | - |
| 79 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 961.93 | ✅ 通过 | - |
| 80 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 424.88 | ❌ 失败 | HTTP错误: 403 |
| 82 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 793.15 | ✅ 通过 | - |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2018.87 | ✅ 通过 | - |
| 84 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 2054.98 | ✅ 通过 | - |
| 85 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1491.53 | ✅ 通过 | - |
| 86 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 3437.07 | ✅ 通过 | - |
| 87 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 794.55 | ✅ 通过 | - |
| 88 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2510.25 | ✅ 通过 | - |
| 89 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 891.47 | ✅ 通过 | - |
| 91 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1327.98 | ✅ 通过 | - |
| 94 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1374.51 | ✅ 通过 | - |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2741.82 | ✅ 通过 | - |
| 96 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 4812.31 | ✅ 通过 | - |
| 97 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1757.44 | ✅ 通过 | - |
| 98 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 395.33 | ❌ 失败 | HTTP错误: 403 |
| 99 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 411.14 | ❌ 失败 | HTTP错误: 403 |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 812.19 | ✅ 通过 | - |
| 101 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1083.83 | ✅ 通过 | - |
| 102 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 814.65 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 876.22 | ✅ 通过 | - |
| 104 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 4586.37 | ✅ 通过 | - |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1435.31 | ✅ 通过 | - |
| 106 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6707.81 | ✅ 通过 | - |
| 107 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 2068.85 | ✅ 通过 | - |
| 108 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 15042.21 | ✅ 通过 | - |
| 109 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8525.84 | ✅ 通过 | - |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1617.54 | ✅ 通过 | - |
| 111 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1712.28 | ❌ 失败 | HTTP错误: 400 |
| 112 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 10864.71 | ✅ 通过 | - |
| 113 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1958.46 | ✅ 通过 | - |
| 114 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 21131.12 | ✅ 通过 | - |
| 115 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 3617.79 | ✅ 通过 | - |
| 116 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 2254.24 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 1073.99 | ✅ 通过 | - |
| 118 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 4469.14 | ✅ 通过 | - |
| 119 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 4821.94 | ✅ 通过 | - |
| 120 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 7737.89 | ✅ 通过 | - |
| 121 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1166.23 | ✅ 通过 | - |
| 123 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 4568.48 | ✅ 通过 | - |
| 124 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 1864.02 | ✅ 通过 | - |
| 125 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 126 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 7878.03 | ✅ 通过 | - |
| 127 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 9611.02 | ✅ 通过 | - |
| 128 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 10099.01 | ✅ 通过 | - |
| 129 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 618.18 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 497.92 | ❌ 失败 | HTTP错误: 500 |
| 135 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 354.56 | ❌ 失败 | HTTP错误: 403 |
| 138 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 469.0 | ❌ 失败 | HTTP错误: 500 |
| 143 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 491.18 | ❌ 失败 | HTTP错误: 500 |
| 144 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 554.25 | ❌ 失败 | HTTP错误: 500 |
| 145 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 911.5 | ✅ 通过 | - |
| 146 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 551.9 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 542.37 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 528.73 | ❌ 失败 | HTTP错误: 500 |
| 150 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 773.24 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 798.06 | ✅ 通过 | - |
| 153 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1382.59 | ✅ 通过 | - |
| 154 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2190.96 | ✅ 通过 | - |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1252.71 | ✅ 通过 | - |
| 156 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1151.65 | ✅ 通过 | - |
| 157 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 3388.05 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 544.26 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 437.05 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 424.96 | ❌ 失败 | HTTP错误: 500 |
| 161 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 434.67 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 577.13 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1861.18 | ✅ 通过 | - |
| 164 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 484.54 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 742.66 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 428.93 | ❌ 失败 | HTTP错误: 500 |
| 167 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2345.54 | ✅ 通过 | - |
| 168 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 384.91 | ❌ 失败 | HTTP错误: 500 |
| 169 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 4312.27 | ✅ 通过 | - |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 537.38 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 578.6 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 617.47 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 457.87 | ❌ 失败 | HTTP错误: 500 |
| 174 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 609.47 | ❌ 失败 | HTTP错误: 500 |
| 175 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 176 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 536.58 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 510.99 | ❌ 失败 | HTTP错误: 500 |
| 178 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 5302.51 | ✅ 通过 | - |
| 179 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 4148.0 | ✅ 通过 | - |
| 180 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1384.11 | ✅ 通过 | - |
| 181 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 7934.52 | ✅ 通过 | - |
| 183 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 16482.19 | ✅ 通过 | - |
| 184 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 15060.28 | ✅ 通过 | - |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_35

**密钥显示**: bce-v3/ALTAKSP-UiWag...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_36

**密钥显示**: bce-v3/ALTAK-D1opbYZ...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 21 |
| 失败 | 144 |
| 超时 | 28 |
| 通过率 | 10.88% |


### 3. 异常汇总

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **qianfan-engcard-vl**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **qianfan-vl-8b**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen-image-edit**: HTTP错误: 429

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **paddleocr-vl-0.9b**: HTTP错误: 429

- **pp-structurev3**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 429

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **ernie-x1.1**: HTTP错误: 403

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1202.04 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1206.55 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1227.83 | ❌ 失败 | HTTP错误: 403 |
| 4 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1196.7 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1259.25 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1206.44 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1254.99 | ❌ 失败 | HTTP错误: 403 |
| 8 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1216.65 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1283.15 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1271.52 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1280.98 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1302.31 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1306.75 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1290.59 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1367.8 | ❌ 失败 | HTTP错误: 403 |
| 16 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1284.42 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1327.7 | ❌ 失败 | HTTP错误: 403 |
| 18 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1324.57 | ❌ 失败 | HTTP错误: 500 |
| 19 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1375.28 | ❌ 失败 | HTTP错误: 403 |
| 20 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1473.15 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1189.18 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1208.59 | ❌ 失败 | HTTP错误: 403 |
| 23 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1167.91 | ❌ 失败 | HTTP错误: 403 |
| 24 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1255.81 | ❌ 失败 | HTTP错误: 403 |
| 25 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 1163.16 | ❌ 失败 | HTTP错误: 429 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 530.95 | ❌ 失败 | HTTP错误: 403 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 490.51 | ❌ 失败 | HTTP错误: 429 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 584.55 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 378.35 | ❌ 失败 | HTTP错误: 429 |
| 30 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 709.93 | ❌ 失败 | HTTP错误: 403 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 439.54 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 405.29 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 426.71 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 351.08 | ❌ 失败 | HTTP错误: 403 |
| 35 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3018.64 | ✅ 通过 | - |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 450.17 | ❌ 失败 | HTTP错误: 403 |
| 37 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 482.23 | ❌ 失败 | HTTP错误: 403 |
| 38 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 514.19 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 454.69 | ❌ 失败 | HTTP错误: 403 |
| 40 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 504.93 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 520.75 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 432.93 | ❌ 失败 | HTTP错误: 403 |
| 43 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 516.44 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 502.39 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 493.75 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 525.01 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 517.71 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 499.9 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 478.59 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 501.74 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 464.23 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 449.41 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 828.89 | ✅ 通过 | - |
| 54 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 473.83 | ❌ 失败 | HTTP错误: 403 |
| 55 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 481.42 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 390.03 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 475.8 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 424.2 | ❌ 失败 | HTTP错误: 403 |
| 59 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 392.48 | ❌ 失败 | HTTP错误: 403 |
| 60 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 806.42 | ✅ 通过 | - |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 866.54 | ✅ 通过 | - |
| 62 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 357.42 | ❌ 失败 | HTTP错误: 403 |
| 63 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 419.06 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 325.74 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 320.26 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 345.48 | ❌ 失败 | HTTP错误: 403 |
| 67 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 351.17 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 340.09 | ❌ 失败 | HTTP错误: 403 |
| 69 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 780.07 | ❌ 失败 | HTTP错误: 403 |
| 84 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 796.2 | ❌ 失败 | HTTP错误: 403 |
| 86 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 899.06 | ❌ 失败 | HTTP错误: 403 |
| 87 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 772.7 | ❌ 失败 | HTTP错误: 403 |
| 89 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 766.03 | ❌ 失败 | HTTP错误: 403 |
| 90 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 915.16 | ❌ 失败 | HTTP错误: 403 |
| 91 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 955.07 | ❌ 失败 | HTTP错误: 403 |
| 92 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 879.48 | ❌ 失败 | HTTP错误: 403 |
| 93 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 791.97 | ❌ 失败 | HTTP错误: 403 |
| 94 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 802.03 | ❌ 失败 | HTTP错误: 403 |
| 95 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 96 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 829.05 | ❌ 失败 | HTTP错误: 403 |
| 97 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 830.7 | ❌ 失败 | HTTP错误: 403 |
| 98 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1264.9 | ✅ 通过 | - |
| 99 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 909.7 | ❌ 失败 | HTTP错误: 403 |
| 100 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 864.05 | ❌ 失败 | HTTP错误: 429 |
| 101 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 988.34 | ❌ 失败 | HTTP错误: 403 |
| 102 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 914.34 | ❌ 失败 | HTTP错误: 403 |
| 103 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 860.39 | ❌ 失败 | HTTP错误: 403 |
| 104 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 946.9 | ❌ 失败 | HTTP错误: 429 |
| 105 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 958.15 | ❌ 失败 | HTTP错误: 429 |
| 106 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 937.53 | ❌ 失败 | HTTP错误: 429 |
| 107 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 978.25 | ❌ 失败 | HTTP错误: 429 |
| 108 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 837.52 | ❌ 失败 | HTTP错误: 403 |
| 109 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 964.81 | ❌ 失败 | HTTP错误: 403 |
| 110 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 1002.29 | ❌ 失败 | HTTP错误: 403 |
| 111 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 1008.58 | ❌ 失败 | HTTP错误: 403 |
| 112 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 1052.45 | ❌ 失败 | HTTP错误: 403 |
| 113 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 947.21 | ❌ 失败 | HTTP错误: 403 |
| 114 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 768.41 | ❌ 失败 | HTTP错误: 403 |
| 115 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 835.5 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 971.28 | ❌ 失败 | HTTP错误: 403 |
| 117 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 805.21 | ❌ 失败 | HTTP错误: 429 |
| 118 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 909.07 | ❌ 失败 | HTTP错误: 403 |
| 119 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 910.06 | ❌ 失败 | HTTP错误: 403 |
| 120 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 865.1 | ❌ 失败 | HTTP错误: 403 |
| 121 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 905.63 | ❌ 失败 | HTTP错误: 429 |
| 122 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 879.53 | ❌ 失败 | HTTP错误: 403 |
| 123 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 1102.82 | ❌ 失败 | HTTP错误: 403 |
| 124 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 1007.3 | ❌ 失败 | HTTP错误: 403 |
| 125 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 839.39 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 942.53 | ❌ 失败 | HTTP错误: 403 |
| 127 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 773.42 | ❌ 失败 | HTTP错误: 403 |
| 128 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 827.56 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 853.44 | ❌ 失败 | HTTP错误: 403 |
| 130 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 828.15 | ❌ 失败 | HTTP错误: 429 |
| 131 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 839.22 | ❌ 失败 | HTTP错误: 403 |
| 132 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 785.14 | ❌ 失败 | HTTP错误: 403 |
| 133 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 829.63 | ❌ 失败 | HTTP错误: 403 |
| 134 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 832.23 | ❌ 失败 | HTTP错误: 403 |
| 135 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 824.77 | ❌ 失败 | HTTP错误: 403 |
| 136 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 825.59 | ❌ 失败 | HTTP错误: 403 |
| 137 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 853.79 | ❌ 失败 | HTTP错误: 403 |
| 138 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 660.6 | ❌ 失败 | HTTP错误: 403 |
| 139 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | 429 | 677.3 | ❌ 失败 | HTTP错误: 429 |
| 140 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | 429 | 648.95 | ❌ 失败 | HTTP错误: 429 |
| 141 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 429 | 668.58 | ❌ 失败 | HTTP错误: 429 |
| 142 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 621.96 | ❌ 失败 | HTTP错误: 403 |
| 143 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 403 | 673.49 | ❌ 失败 | HTTP错误: 403 |
| 144 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 588.73 | ❌ 失败 | HTTP错误: 500 |
| 145 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 620.78 | ❌ 失败 | HTTP错误: 500 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 562.9 | ❌ 失败 | HTTP错误: 500 |
| 147 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 632.0 | ❌ 失败 | HTTP错误: 500 |
| 148 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1092.77 | ✅ 通过 | - |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 546.65 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 664.32 | ❌ 失败 | HTTP错误: 500 |
| 151 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 826.43 | ✅ 通过 | - |
| 152 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 1054.0 | ❌ 失败 | HTTP错误: 500 |
| 153 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 154 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 155 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1201.93 | ✅ 通过 | - |
| 156 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1909.98 | ✅ 通过 | - |
| 157 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2556.7 | ✅ 通过 | - |
| 158 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1322.02 | ✅ 通过 | - |
| 159 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 987.36 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 507.26 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 504.43 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 461.19 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1173.83 | ✅ 通过 | - |
| 164 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1227.35 | ✅ 通过 | - |
| 165 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 479.78 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 539.42 | ❌ 失败 | HTTP错误: 500 |
| 167 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 554.72 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 552.76 | ❌ 失败 | HTTP错误: 500 |
| 169 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1859.88 | ✅ 通过 | - |
| 170 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 593.09 | ❌ 失败 | HTTP错误: 500 |
| 171 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 564.34 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 593.16 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 608.99 | ❌ 失败 | HTTP错误: 500 |
| 174 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 544.13 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 952.28 | ❌ 失败 | HTTP错误: 500 |
| 176 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 602.4 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 561.17 | ❌ 失败 | HTTP错误: 500 |
| 178 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 588.3 | ❌ 失败 | HTTP错误: 500 |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1410.89 | ✅ 通过 | - |
| 180 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 6193.05 | ✅ 通过 | - |
| 181 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 6381.51 | ✅ 通过 | - |
| 183 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 11946.21 | ✅ 通过 | - |
| 184 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 14822.78 | ✅ 通过 | - |
| 185 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 14374.32 | ✅ 通过 | - |
| 186 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_37

**密钥显示**: bce-v3/ALTAK-OWYLnTj...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 63 |
| 失败 | 103 |
| 超时 | 27 |
| 通过率 | 32.64% |


### 3. 异常汇总

- **ernie-speed-pro-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **chatglm2-6b-32k**: HTTP错误: 403

- **xuanyuan-70b-chat-4bit**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **codellama-7b-instruct**: HTTP错误: 403

- **llama-2-7b-chat**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **bloomz-7b**: HTTP错误: 403

- **llama-2-13b-chat**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **aquilachat-7b**: HTTP错误: 403

- **mixtral-8x7b-instruct**: HTTP错误: 403

- **sqlcoder-7b**: HTTP错误: 403

- **gemma-7b-it**: HTTP错误: 403

- **llama-2-70b-chat**: HTTP错误: 403

- **qianfan-bloomz-7b-compressed**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **yi-34b-chat**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **qianfan-chinese-llama-2-70b**: HTTP错误: 403

- **qianfan-chinese-llama-2-7b**: HTTP错误: 403

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **stable-diffusion-xl**: HTTP错误: 429

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1214.91 | ❌ 失败 | HTTP错误: 403 |
| 2 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1211.62 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1220.71 | ❌ 失败 | HTTP错误: 403 |
| 4 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1217.77 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1226.06 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1256.33 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1308.71 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1287.91 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1308.52 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1301.09 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1333.89 | ❌ 失败 | HTTP错误: 403 |
| 12 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1276.73 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1318.91 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1338.37 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1419.52 | ❌ 失败 | HTTP错误: 403 |
| 16 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1329.32 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1439.87 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1506.92 | ❌ 失败 | HTTP错误: 403 |
| 19 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1509.08 | ❌ 失败 | HTTP错误: 429 |
| 20 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1730.48 | ❌ 失败 | HTTP错误: 403 |
| 21 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | 403 | 1088.68 | ❌ 失败 | HTTP错误: 403 |
| 22 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | 403 | 1059.34 | ❌ 失败 | HTTP错误: 403 |
| 23 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1167.5 | ❌ 失败 | HTTP错误: 403 |
| 24 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | 403 | 1098.47 | ❌ 失败 | HTTP错误: 403 |
| 25 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | 403 | 1149.05 | ❌ 失败 | HTTP错误: 403 |
| 26 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1004.32 | ❌ 失败 | HTTP错误: 403 |
| 27 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | 403 | 1134.21 | ❌ 失败 | HTTP错误: 403 |
| 28 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | 403 | 1183.3 | ❌ 失败 | HTTP错误: 403 |
| 29 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1093.02 | ❌ 失败 | HTTP错误: 403 |
| 30 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | 403 | 1224.39 | ❌ 失败 | HTTP错误: 403 |
| 31 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | 403 | 1224.04 | ❌ 失败 | HTTP错误: 403 |
| 32 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | 403 | 1199.6 | ❌ 失败 | HTTP错误: 403 |
| 33 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | 403 | 1311.32 | ❌ 失败 | HTTP错误: 403 |
| 34 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | 403 | 1252.13 | ❌ 失败 | HTTP错误: 403 |
| 35 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | 403 | 1168.77 | ❌ 失败 | HTTP错误: 403 |
| 36 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1396.94 | ❌ 失败 | HTTP错误: 403 |
| 37 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | 403 | 1500.16 | ❌ 失败 | HTTP错误: 403 |
| 38 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 945.22 | ❌ 失败 | HTTP错误: 403 |
| 39 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 908.86 | ❌ 失败 | HTTP错误: 429 |
| 40 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 1066.27 | ❌ 失败 | HTTP错误: 403 |
| 41 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | 403 | 967.19 | ❌ 失败 | HTTP错误: 403 |
| 42 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | 403 | 1028.91 | ❌ 失败 | HTTP错误: 403 |
| 43 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 938.51 | ❌ 失败 | HTTP错误: 403 |
| 44 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 1066.85 | ❌ 失败 | HTTP错误: 403 |
| 45 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 1103.05 | ❌ 失败 | HTTP错误: 500 |
| 46 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 1043.9 | ❌ 失败 | HTTP错误: 403 |
| 47 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 1061.62 | ❌ 失败 | HTTP错误: 403 |
| 48 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 1312.23 | ❌ 失败 | HTTP错误: 429 |
| 49 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 1141.21 | ❌ 失败 | HTTP错误: 403 |
| 50 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 1106.69 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 1314.61 | ✅ 通过 | - |
| 52 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 817.31 | ❌ 失败 | HTTP错误: 403 |
| 53 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 897.35 | ❌ 失败 | HTTP错误: 403 |
| 54 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 764.1 | ❌ 失败 | HTTP错误: 403 |
| 55 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 2157.32 | ✅ 通过 | - |
| 56 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 919.84 | ✅ 通过 | - |
| 57 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 2127.23 | ✅ 通过 | - |
| 58 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 927.93 | ✅ 通过 | - |
| 59 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 533.45 | ❌ 失败 | HTTP错误: 403 |
| 60 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3203.18 | ✅ 通过 | - |
| 61 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 1200.69 | ✅ 通过 | - |
| 62 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1452.24 | ✅ 通过 | - |
| 63 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1281.93 | ✅ 通过 | - |
| 64 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 1319.8 | ✅ 通过 | - |
| 65 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1549.38 | ✅ 通过 | - |
| 66 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1590.23 | ✅ 通过 | - |
| 67 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1238.06 | ✅ 通过 | - |
| 68 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1316.95 | ✅ 通过 | - |
| 69 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 618.08 | ❌ 失败 | HTTP错误: 403 |
| 70 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 925.87 | ✅ 通过 | - |
| 71 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 845.64 | ❌ 失败 | HTTP错误: 403 |
| 72 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 2373.29 | ✅ 通过 | - |
| 73 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 960.12 | ✅ 通过 | - |
| 74 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1314.67 | ✅ 通过 | - |
| 75 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 1988.96 | ✅ 通过 | - |
| 76 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 1245.76 | ✅ 通过 | - |
| 77 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 584.84 | ❌ 失败 | HTTP错误: 403 |
| 78 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | 429 | 643.97 | ❌ 失败 | HTTP错误: 429 |
| 79 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 637.97 | ❌ 失败 | HTTP错误: 403 |
| 80 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 604.5 | ❌ 失败 | HTTP错误: 403 |
| 81 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 601.08 | ❌ 失败 | HTTP错误: 403 |
| 82 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 666.61 | ❌ 失败 | HTTP错误: 403 |
| 83 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 631.13 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2038.18 | ✅ 通过 | - |
| 85 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 632.39 | ❌ 失败 | HTTP错误: 403 |
| 86 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 879.09 | ✅ 通过 | - |
| 87 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 571.15 | ❌ 失败 | HTTP错误: 403 |
| 88 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 525.53 | ❌ 失败 | HTTP错误: 403 |
| 89 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1193.78 | ✅ 通过 | - |
| 90 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1442.28 | ✅ 通过 | - |
| 91 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 982.61 | ✅ 通过 | - |
| 92 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1814.02 | ✅ 通过 | - |
| 93 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 392.98 | ❌ 失败 | HTTP错误: 403 |
| 94 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 392.91 | ❌ 失败 | HTTP错误: 403 |
| 95 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 9637.53 | ✅ 通过 | - |
| 96 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6775.63 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 472.81 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 396.57 | ❌ 失败 | HTTP错误: 403 |
| 99 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 597.8 | ✅ 通过 | - |
| 100 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 9436.99 | ✅ 通过 | - |
| 101 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 942.23 | ✅ 通过 | - |
| 102 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 870.79 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 896.3 | ✅ 通过 | - |
| 104 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1100.6 | ✅ 通过 | - |
| 105 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 378.92 | ❌ 失败 | HTTP错误: 403 |
| 106 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 364.38 | ❌ 失败 | HTTP错误: 403 |
| 107 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 376.82 | ❌ 失败 | HTTP错误: 429 |
| 108 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 21361.11 | ✅ 通过 | - |
| 109 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 9586.81 | ✅ 通过 | - |
| 110 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 533.56 | ❌ 失败 | HTTP错误: 403 |
| 111 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1155.92 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1888.94 | ✅ 通过 | - |
| 113 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 7034.46 | ✅ 通过 | - |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 318.1 | ❌ 失败 | HTTP错误: 403 |
| 115 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 365.15 | ❌ 失败 | HTTP错误: 403 |
| 116 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 2532.85 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 875.12 | ✅ 通过 | - |
| 118 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 11919.05 | ✅ 通过 | - |
| 119 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 120 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 121 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1022.7 | ✅ 通过 | - |
| 123 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 124 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 125 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 126 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 127 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 520.59 | ❌ 失败 | HTTP错误: 403 |
| 128 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 516.62 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2260.16 | ✅ 通过 | - |
| 131 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 584.15 | ✅ 通过 | - |
| 133 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 444.01 | ❌ 失败 | HTTP错误: 500 |
| 135 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 479.07 | ❌ 失败 | HTTP错误: 403 |
| 141 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 524.24 | ❌ 失败 | HTTP错误: 500 |
| 142 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 473.91 | ❌ 失败 | HTTP错误: 500 |
| 143 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 904.4 | ❌ 失败 | HTTP错误: 500 |
| 144 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 436.8 | ❌ 失败 | HTTP错误: 500 |
| 145 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1085.6 | ✅ 通过 | - |
| 146 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 552.66 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 516.53 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 830.49 | ❌ 失败 | HTTP错误: 500 |
| 150 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 7254.43 | ✅ 通过 | - |
| 151 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 829.1 | ✅ 通过 | - |
| 152 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2419.04 | ✅ 通过 | - |
| 153 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1574.14 | ✅ 通过 | - |
| 154 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1516.14 | ✅ 通过 | - |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1255.21 | ✅ 通过 | - |
| 156 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1200.46 | ✅ 通过 | - |
| 157 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 7045.9 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 773.08 | ❌ 失败 | HTTP错误: 500 |
| 159 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1913.82 | ✅ 通过 | - |
| 160 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1270.75 | ✅ 通过 | - |
| 161 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1356.72 | ✅ 通过 | - |
| 162 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 537.89 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 616.03 | ❌ 失败 | HTTP错误: 500 |
| 164 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 782.43 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 493.08 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 560.32 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 952.94 | ❌ 失败 | HTTP错误: 500 |
| 168 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 169 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 505.15 | ❌ 失败 | HTTP错误: 500 |
| 170 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 535.2 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 600.01 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 524.61 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 779.78 | ❌ 失败 | HTTP错误: 500 |
| 174 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 587.42 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 592.1 | ❌ 失败 | HTTP错误: 500 |
| 176 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 4400.3 | ✅ 通过 | - |
| 177 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 453.8 | ❌ 失败 | HTTP错误: 500 |
| 178 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 688.46 | ❌ 失败 | HTTP错误: 500 |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1343.39 | ✅ 通过 | - |
| 180 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 5452.35 | ✅ 通过 | - |
| 181 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 9463.5 | ✅ 通过 | - |
| 182 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 8398.97 | ✅ 通过 | - |
| 183 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 12461.36 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_38

**密钥显示**: bce-v3/ALTAK-AxNAd2T...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_39

**密钥显示**: bce-v3/ALTAK-olfnO0x...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 9 |
| 失败 | 157 |
| 超时 | 27 |
| 通过率 | 4.66% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **deepseek-v3**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **yi-34b-chat**: HTTP错误: 403

- **chatglm2-6b-32k**: HTTP错误: 403

- **llama-2-13b-chat**: HTTP错误: 403

- **xuanyuan-70b-chat-4bit**: HTTP错误: 403

- **llama-2-70b-chat**: HTTP错误: 403

- **llama-2-7b-chat**: HTTP错误: 403

- **sqlcoder-7b**: HTTP错误: 403

- **codellama-7b-instruct**: HTTP错误: 403

- **mixtral-8x7b-instruct**: HTTP错误: 403

- **aquilachat-7b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **bloomz-7b**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **gemma-7b-it**: HTTP错误: 403

- **qianfan-bloomz-7b-compressed**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 403

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-7b**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **qianfan-8b**: HTTP错误: 403

- **qianfan-chinese-llama-2-70b**: HTTP错误: 403

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **ernie-x1-32k**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **stable-diffusion-xl**: HTTP错误: 429

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-x1.1**: HTTP错误: 403

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **qianfan-ocr**: HTTP错误: 403

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **qianfan-vl-1.5-flash**: HTTP错误: 403

- **viduq3-pro_img2video**: HTTP错误: 500

- **qianfan-ocr-fast**: HTTP错误: 403

- **minimax-m2.1**: HTTP错误: 403

- **ernie-5.0**: HTTP错误: 403

- **minimax-m2.5**: HTTP错误: 403

- **glm-5**: HTTP错误: 403

- **viduq3-pro_text2video**: HTTP错误: 500

- **qwen3.5-35b-a3b**: HTTP错误: 403

- **qwen3.5-397b-a17b**: HTTP错误: 403

- **qwen3.5-122b-a10b**: HTTP错误: 403

- **kimi-k2.5**: HTTP错误: 403

- **qwen3.5-27b**: HTTP错误: 403

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **ernie-4.5-turbo-20260402**: HTTP错误: 403

- **kling-custom-voices_voices**: HTTP错误: 500

- **glm-5.1**: HTTP错误: 403


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1222.97 | ❌ 失败 | HTTP错误: 403 |
| 2 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1185.81 | ❌ 失败 | HTTP错误: 429 |
| 3 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1190.2 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1256.83 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1290.79 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1308.73 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1306.37 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1311.03 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1346.82 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1346.52 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1323.0 | ❌ 失败 | HTTP错误: 403 |
| 12 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1281.44 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1360.46 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1376.29 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1341.9 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1425.53 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1432.86 | ❌ 失败 | HTTP错误: 403 |
| 18 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1283.07 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1442.7 | ❌ 失败 | HTTP错误: 403 |
| 20 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1473.34 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 998.02 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1065.74 | ❌ 失败 | HTTP错误: 403 |
| 23 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | 403 | 1154.96 | ❌ 失败 | HTTP错误: 403 |
| 24 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | 403 | 1186.91 | ❌ 失败 | HTTP错误: 403 |
| 25 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | 403 | 1148.25 | ❌ 失败 | HTTP错误: 403 |
| 26 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | 403 | 1166.43 | ❌ 失败 | HTTP错误: 403 |
| 27 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | 403 | 1166.8 | ❌ 失败 | HTTP错误: 403 |
| 28 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | 403 | 1239.49 | ❌ 失败 | HTTP错误: 403 |
| 29 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | 403 | 1179.74 | ❌ 失败 | HTTP错误: 403 |
| 30 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | 403 | 1234.61 | ❌ 失败 | HTTP错误: 403 |
| 31 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | 403 | 1242.06 | ❌ 失败 | HTTP错误: 403 |
| 32 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | 403 | 1306.95 | ❌ 失败 | HTTP错误: 403 |
| 33 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1306.39 | ❌ 失败 | HTTP错误: 403 |
| 34 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | 403 | 1328.2 | ❌ 失败 | HTTP错误: 403 |
| 35 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 1103.8 | ❌ 失败 | HTTP错误: 429 |
| 36 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | 403 | 1520.71 | ❌ 失败 | HTTP错误: 403 |
| 37 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | 403 | 1392.88 | ❌ 失败 | HTTP错误: 403 |
| 38 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1530.55 | ❌ 失败 | HTTP错误: 403 |
| 39 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 874.58 | ❌ 失败 | HTTP错误: 403 |
| 40 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 403 | 968.94 | ❌ 失败 | HTTP错误: 403 |
| 41 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 963.04 | ❌ 失败 | HTTP错误: 403 |
| 42 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | 403 | 1070.78 | ❌ 失败 | HTTP错误: 403 |
| 43 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 1087.89 | ❌ 失败 | HTTP错误: 403 |
| 44 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 1038.62 | ❌ 失败 | HTTP错误: 403 |
| 45 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | 403 | 1103.73 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 1093.1 | ❌ 失败 | HTTP错误: 403 |
| 47 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 1107.88 | ❌ 失败 | HTTP错误: 429 |
| 48 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 403 | 1186.31 | ❌ 失败 | HTTP错误: 403 |
| 49 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 1177.53 | ❌ 失败 | HTTP错误: 403 |
| 50 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 1011.13 | ❌ 失败 | HTTP错误: 403 |
| 51 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 886.18 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 1178.8 | ❌ 失败 | HTTP错误: 403 |
| 53 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 1182.14 | ❌ 失败 | HTTP错误: 403 |
| 54 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 1218.8 | ❌ 失败 | HTTP错误: 403 |
| 55 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 1146.53 | ❌ 失败 | HTTP错误: 403 |
| 56 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 936.26 | ❌ 失败 | HTTP错误: 403 |
| 57 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 1011.59 | ❌ 失败 | HTTP错误: 403 |
| 58 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 938.79 | ❌ 失败 | HTTP错误: 403 |
| 59 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 965.43 | ❌ 失败 | HTTP错误: 403 |
| 60 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 933.1 | ❌ 失败 | HTTP错误: 403 |
| 61 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 976.35 | ❌ 失败 | HTTP错误: 403 |
| 62 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 1017.73 | ❌ 失败 | HTTP错误: 403 |
| 63 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 969.95 | ❌ 失败 | HTTP错误: 403 |
| 64 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 1187.31 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 956.73 | ❌ 失败 | HTTP错误: 403 |
| 66 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 1109.3 | ❌ 失败 | HTTP错误: 403 |
| 67 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 976.22 | ❌ 失败 | HTTP错误: 403 |
| 68 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 1110.88 | ❌ 失败 | HTTP错误: 403 |
| 69 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 1116.66 | ❌ 失败 | HTTP错误: 403 |
| 70 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3714.8 | ✅ 通过 | - |
| 71 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 1495.78 | ❌ 失败 | HTTP错误: 403 |
| 72 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 915.26 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 808.63 | ❌ 失败 | HTTP错误: 403 |
| 74 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 818.73 | ❌ 失败 | HTTP错误: 403 |
| 75 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 757.65 | ❌ 失败 | HTTP错误: 403 |
| 76 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 780.22 | ❌ 失败 | HTTP错误: 403 |
| 77 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 787.0 | ❌ 失败 | HTTP错误: 403 |
| 78 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1722.08 | ✅ 通过 | - |
| 79 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | 429 | 797.53 | ❌ 失败 | HTTP错误: 429 |
| 80 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1194.34 | ✅ 通过 | - |
| 81 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 912.51 | ❌ 失败 | HTTP错误: 403 |
| 82 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 754.57 | ❌ 失败 | HTTP错误: 403 |
| 83 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 777.74 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 803.48 | ❌ 失败 | HTTP错误: 403 |
| 85 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1461.53 | ✅ 通过 | - |
| 86 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 745.91 | ❌ 失败 | HTTP错误: 403 |
| 87 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 717.79 | ❌ 失败 | HTTP错误: 403 |
| 88 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 743.07 | ❌ 失败 | HTTP错误: 403 |
| 89 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 778.37 | ❌ 失败 | HTTP错误: 403 |
| 90 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 770.22 | ❌ 失败 | HTTP错误: 403 |
| 91 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 788.93 | ❌ 失败 | HTTP错误: 403 |
| 92 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 725.86 | ❌ 失败 | HTTP错误: 403 |
| 93 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 746.62 | ❌ 失败 | HTTP错误: 403 |
| 94 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 775.79 | ❌ 失败 | HTTP错误: 403 |
| 95 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 778.88 | ❌ 失败 | HTTP错误: 403 |
| 96 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 787.92 | ❌ 失败 | HTTP错误: 403 |
| 97 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 668.67 | ❌ 失败 | HTTP错误: 403 |
| 98 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 654.03 | ❌ 失败 | HTTP错误: 403 |
| 99 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 818.86 | ❌ 失败 | HTTP错误: 403 |
| 100 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 470.96 | ❌ 失败 | HTTP错误: 403 |
| 101 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2024.42 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 557.25 | ❌ 失败 | HTTP错误: 403 |
| 103 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 828.24 | ✅ 通过 | - |
| 104 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 387.76 | ❌ 失败 | HTTP错误: 403 |
| 105 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 705.72 | ✅ 通过 | - |
| 106 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 452.39 | ❌ 失败 | HTTP错误: 403 |
| 107 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 532.74 | ❌ 失败 | HTTP错误: 403 |
| 108 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 441.41 | ❌ 失败 | HTTP错误: 403 |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1884.71 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 392.76 | ❌ 失败 | HTTP错误: 403 |
| 111 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 352.65 | ❌ 失败 | HTTP错误: 403 |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 310.27 | ❌ 失败 | HTTP错误: 403 |
| 113 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 394.16 | ❌ 失败 | HTTP错误: 403 |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 417.65 | ❌ 失败 | HTTP错误: 403 |
| 115 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 315.9 | ❌ 失败 | HTTP错误: 403 |
| 116 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 324.04 | ❌ 失败 | HTTP错误: 403 |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 318.95 | ❌ 失败 | HTTP错误: 403 |
| 118 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8319.98 | ✅ 通过 | - |
| 119 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 120 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 121 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 441.81 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 433.1 | ❌ 失败 | HTTP错误: 403 |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 368.28 | ❌ 失败 | HTTP错误: 403 |
| 124 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 125 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 126 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 127 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 434.17 | ❌ 失败 | HTTP错误: 403 |
| 128 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 480.38 | ❌ 失败 | HTTP错误: 403 |
| 129 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 491.79 | ❌ 失败 | HTTP错误: 403 |
| 130 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 516.64 | ❌ 失败 | HTTP错误: 403 |
| 133 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 541.25 | ❌ 失败 | HTTP错误: 500 |
| 135 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 403 | 401.6 | ❌ 失败 | HTTP错误: 403 |
| 140 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 143 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 144 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 519.39 | ❌ 失败 | HTTP错误: 403 |
| 145 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 681.9 | ❌ 失败 | HTTP错误: 500 |
| 146 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 403 | 730.11 | ❌ 失败 | HTTP错误: 403 |
| 147 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 667.05 | ❌ 失败 | HTTP错误: 500 |
| 148 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 681.51 | ❌ 失败 | HTTP错误: 500 |
| 149 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 614.93 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 602.43 | ❌ 失败 | HTTP错误: 500 |
| 151 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 403 | 609.16 | ❌ 失败 | HTTP错误: 403 |
| 152 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 790.44 | ❌ 失败 | HTTP错误: 500 |
| 153 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 403 | 633.8 | ❌ 失败 | HTTP错误: 403 |
| 154 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 403 | 634.92 | ❌ 失败 | HTTP错误: 403 |
| 155 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 403 | 551.28 | ❌ 失败 | HTTP错误: 403 |
| 156 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 403 | 588.89 | ❌ 失败 | HTTP错误: 403 |
| 157 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 791.59 | ❌ 失败 | HTTP错误: 403 |
| 158 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 1003.83 | ❌ 失败 | HTTP错误: 500 |
| 159 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 403 | 544.28 | ❌ 失败 | HTTP错误: 403 |
| 160 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 403 | 567.21 | ❌ 失败 | HTTP错误: 403 |
| 161 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 403 | 594.29 | ❌ 失败 | HTTP错误: 403 |
| 162 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 403 | 1265.13 | ❌ 失败 | HTTP错误: 403 |
| 163 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 164 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 165 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 403 | 626.3 | ❌ 失败 | HTTP错误: 403 |
| 166 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 613.51 | ❌ 失败 | HTTP错误: 500 |
| 167 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 637.94 | ❌ 失败 | HTTP错误: 500 |
| 168 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 636.38 | ❌ 失败 | HTTP错误: 500 |
| 169 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 663.3 | ❌ 失败 | HTTP错误: 500 |
| 170 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 722.73 | ❌ 失败 | HTTP错误: 500 |
| 171 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 726.97 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 676.69 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 737.78 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 691.28 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 671.93 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 930.26 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 621.2 | ❌ 失败 | HTTP错误: 500 |
| 178 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 903.75 | ❌ 失败 | HTTP错误: 500 |
| 179 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 768.82 | ❌ 失败 | HTTP错误: 500 |
| 180 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 605.78 | ❌ 失败 | HTTP错误: 500 |
| 181 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 403 | 527.18 | ❌ 失败 | HTTP错误: 403 |
| 182 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 563.03 | ❌ 失败 | HTTP错误: 500 |
| 183 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 403 | 522.27 | ❌ 失败 | HTTP错误: 403 |
| 184 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 4134.89 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_40

**密钥显示**: bce-v3/ALTAK-wKuFEIj...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_41

**密钥显示**: bce-v3/ALTAK-n5AYUIU...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_42

**密钥显示**: bce-v3/ALTAK-flztb2R...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 97 |
| 失败 | 53 |
| 超时 | 43 |
| 通过率 | 50.26% |


### 3. 异常汇总

- **deepseek-v3**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **deepseek-v3.2**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **glm-5**: HTTP错误: 403

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1200.86 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1237.85 | ❌ 失败 | HTTP错误: 403 |
| 3 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1244.17 | ❌ 失败 | HTTP错误: 500 |
| 4 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1311.99 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1360.07 | ❌ 失败 | HTTP错误: 403 |
| 6 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1387.92 | ❌ 失败 | HTTP错误: 403 |
| 7 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 582.1 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 1922.58 | ✅ 通过 | - |
| 9 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 1993.39 | ✅ 通过 | - |
| 10 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2394.68 | ✅ 通过 | - |
| 11 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 2684.27 | ✅ 通过 | - |
| 12 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2679.06 | ✅ 通过 | - |
| 13 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 2671.78 | ✅ 通过 | - |
| 14 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2734.74 | ✅ 通过 | - |
| 15 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2836.74 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 2825.44 | ✅ 通过 | - |
| 17 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 2886.26 | ✅ 通过 | - |
| 18 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 2987.98 | ✅ 通过 | - |
| 19 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 3176.75 | ✅ 通过 | - |
| 20 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3182.42 | ✅ 通过 | - |
| 21 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 3794.9 | ✅ 通过 | - |
| 22 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1152.77 | ✅ 通过 | - |
| 23 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 376.04 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 415.34 | ❌ 失败 | HTTP错误: 429 |
| 25 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 1825.26 | ✅ 通过 | - |
| 26 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1585.4 | ✅ 通过 | - |
| 27 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 332.78 | ❌ 失败 | HTTP错误: 403 |
| 28 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3149.15 | ✅ 通过 | - |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 394.9 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1467.41 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 402.95 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 309.92 | ❌ 失败 | HTTP错误: 403 |
| 33 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 8083.38 | ✅ 通过 | - |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 2159.75 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 369.09 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 321.39 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 357.28 | ❌ 失败 | HTTP错误: 403 |
| 38 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 2854.93 | ✅ 通过 | - |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 824.68 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 1987.91 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 382.73 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1747.5 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1071.89 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 970.87 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 777.18 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 678.61 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 315.88 | ❌ 失败 | HTTP错误: 403 |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1187.72 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 808.25 | ✅ 通过 | - |
| 50 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 10466.56 | ✅ 通过 | - |
| 51 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1483.31 | ✅ 通过 | - |
| 52 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 912.04 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2447.37 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1142.11 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 936.63 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 8762.85 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 692.73 | ✅ 通过 | - |
| 65 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 917.36 | ✅ 通过 | - |
| 66 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 453.78 | ❌ 失败 | HTTP错误: 403 |
| 67 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1120.43 | ✅ 通过 | - |
| 69 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 865.56 | ✅ 通过 | - |
| 75 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 1719.05 | ✅ 通过 | - |
| 78 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 587.53 | ❌ 失败 | HTTP错误: 403 |
| 79 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1410.29 | ✅ 通过 | - |
| 80 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 482.65 | ❌ 失败 | HTTP错误: 403 |
| 81 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1293.02 | ✅ 通过 | - |
| 82 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1613.49 | ✅ 通过 | - |
| 84 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 905.89 | ✅ 通过 | - |
| 85 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1312.46 | ✅ 通过 | - |
| 86 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 87 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2051.08 | ✅ 通过 | - |
| 88 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 2089.12 | ✅ 通过 | - |
| 89 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 789.56 | ✅ 通过 | - |
| 90 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2333.23 | ✅ 通过 | - |
| 91 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 994.11 | ✅ 通过 | - |
| 92 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1121.52 | ✅ 通过 | - |
| 93 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1489.11 | ✅ 通过 | - |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2121.86 | ✅ 通过 | - |
| 96 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 419.98 | ❌ 失败 | HTTP错误: 403 |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 427.11 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 364.56 | ❌ 失败 | HTTP错误: 403 |
| 99 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 596.88 | ✅ 通过 | - |
| 100 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 3035.32 | ✅ 通过 | - |
| 101 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 991.46 | ✅ 通过 | - |
| 102 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 640.83 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 854.97 | ✅ 通过 | - |
| 104 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6722.11 | ✅ 通过 | - |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1893.77 | ✅ 通过 | - |
| 106 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 1600.24 | ✅ 通过 | - |
| 107 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 313.59 | ❌ 失败 | HTTP错误: 429 |
| 108 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 9438.21 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1861.16 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1016.96 | ✅ 通过 | - |
| 111 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 15307.12 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1356.55 | ✅ 通过 | - |
| 113 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 13088.39 | ✅ 通过 | - |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 329.24 | ❌ 失败 | HTTP错误: 403 |
| 115 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 15818.21 | ✅ 通过 | - |
| 116 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 4339.9 | ✅ 通过 | - |
| 117 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 118 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 12159.7 | ✅ 通过 | - |
| 119 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 794.11 | ✅ 通过 | - |
| 120 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 5007.61 | ✅ 通过 | - |
| 121 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1009.99 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2196.48 | ✅ 通过 | - |
| 124 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 6321.85 | ✅ 通过 | - |
| 125 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 6053.5 | ✅ 通过 | - |
| 126 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 25612.99 | ✅ 通过 | - |
| 127 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 7759.2 | ✅ 通过 | - |
| 128 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 11981.12 | ✅ 通过 | - |
| 129 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 640.91 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 477.62 | ❌ 失败 | HTTP错误: 500 |
| 135 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 410.15 | ❌ 失败 | HTTP错误: 403 |
| 137 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 408.98 | ❌ 失败 | HTTP错误: 500 |
| 143 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 144 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 966.05 | ✅ 通过 | - |
| 145 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 546.07 | ❌ 失败 | HTTP错误: 500 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 536.36 | ❌ 失败 | HTTP错误: 500 |
| 147 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 542.02 | ❌ 失败 | HTTP错误: 500 |
| 148 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2350.19 | ✅ 通过 | - |
| 149 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 150 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 1025.14 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 582.75 | ❌ 失败 | HTTP错误: 500 |
| 152 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 153 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 734.04 | ❌ 失败 | HTTP错误: 500 |
| 154 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 716.63 | ✅ 通过 | - |
| 155 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 588.17 | ❌ 失败 | HTTP错误: 403 |
| 156 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2176.14 | ✅ 通过 | - |
| 157 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1530.37 | ✅ 通过 | - |
| 158 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1427.66 | ✅ 通过 | - |
| 159 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1326.31 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 541.08 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 558.66 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 563.18 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 627.31 | ❌ 失败 | HTTP错误: 500 |
| 164 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1830.52 | ✅ 通过 | - |
| 165 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 585.0 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 635.83 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 574.58 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 597.84 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 698.82 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 522.48 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 572.32 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 585.35 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 575.14 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 556.85 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 560.86 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 489.32 | ❌ 失败 | HTTP错误: 500 |
| 177 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1598.25 | ✅ 通过 | - |
| 178 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 4503.69 | ✅ 通过 | - |
| 179 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 10051.21 | ✅ 通过 | - |
| 181 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 8587.64 | ✅ 通过 | - |
| 182 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 12663.55 | ✅ 通过 | - |
| 183 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 11826.83 | ✅ 通过 | - |
| 184 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 14836.44 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_43

**密钥显示**: bce-v3/ALTAK-Cpm70UR...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 84 |
| 失败 | 67 |
| 超时 | 42 |
| 通过率 | 43.52% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-3.5-8k**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-x1-turbo-latest**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **kimi-k2.5**: HTTP错误: 403

- **glm-5**: HTTP错误: 403

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1208.87 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1227.66 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1341.62 | ❌ 失败 | HTTP错误: 403 |
| 4 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1298.03 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1400.98 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1362.72 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1468.32 | ❌ 失败 | HTTP错误: 403 |
| 8 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1379.92 | ❌ 失败 | HTTP错误: 403 |
| 9 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1512.48 | ❌ 失败 | HTTP错误: 500 |
| 10 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1579.81 | ❌ 失败 | HTTP错误: 403 |
| 11 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 651.79 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2716.95 | ✅ 通过 | - |
| 13 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 2752.64 | ✅ 通过 | - |
| 14 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2755.34 | ✅ 通过 | - |
| 15 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2937.31 | ✅ 通过 | - |
| 16 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 3052.94 | ✅ 通过 | - |
| 17 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 3144.09 | ✅ 通过 | - |
| 18 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 3189.87 | ✅ 通过 | - |
| 19 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 3299.46 | ✅ 通过 | - |
| 20 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3306.84 | ✅ 通过 | - |
| 21 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 3732.25 | ✅ 通过 | - |
| 22 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 985.75 | ✅ 通过 | - |
| 23 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 357.74 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 410.42 | ❌ 失败 | HTTP错误: 429 |
| 25 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1447.27 | ✅ 通过 | - |
| 26 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2495.04 | ✅ 通过 | - |
| 27 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2335.0 | ✅ 通过 | - |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 407.69 | ❌ 失败 | HTTP错误: 403 |
| 29 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 4927.31 | ✅ 通过 | - |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 356.89 | ❌ 失败 | HTTP错误: 429 |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 509.3 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 352.59 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 363.07 | ❌ 失败 | HTTP错误: 403 |
| 34 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1841.94 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 318.1 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 365.41 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 357.03 | ❌ 失败 | HTTP错误: 403 |
| 38 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1666.56 | ✅ 通过 | - |
| 39 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 369.54 | ❌ 失败 | HTTP错误: 403 |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 833.29 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 418.95 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 2041.28 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1097.41 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1046.65 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 901.24 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 694.52 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 359.03 | ❌ 失败 | HTTP错误: 403 |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1140.34 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 599.57 | ✅ 通过 | - |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1641.23 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 1312.76 | ✅ 通过 | - |
| 52 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 1671.93 | ✅ 通过 | - |
| 53 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 17195.48 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1234.55 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 841.28 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 11813.67 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 66 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 852.25 | ✅ 通过 | - |
| 67 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 567.32 | ❌ 失败 | HTTP错误: 403 |
| 68 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 567.64 | ❌ 失败 | HTTP错误: 403 |
| 69 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1020.76 | ✅ 通过 | - |
| 70 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 942.57 | ✅ 通过 | - |
| 71 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 983.54 | ✅ 通过 | - |
| 72 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1194.07 | ✅ 通过 | - |
| 75 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 549.01 | ❌ 失败 | HTTP错误: 403 |
| 79 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1001.3 | ✅ 通过 | - |
| 81 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2090.83 | ✅ 通过 | - |
| 82 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 534.21 | ❌ 失败 | HTTP错误: 403 |
| 83 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 657.92 | ✅ 通过 | - |
| 84 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1535.36 | ✅ 通过 | - |
| 85 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 86 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1352.85 | ✅ 通过 | - |
| 87 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 443.02 | ❌ 失败 | HTTP错误: 403 |
| 88 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 465.88 | ❌ 失败 | HTTP错误: 403 |
| 89 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 2218.92 | ✅ 通过 | - |
| 90 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 986.53 | ✅ 通过 | - |
| 91 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1384.96 | ✅ 通过 | - |
| 92 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 3071.78 | ✅ 通过 | - |
| 95 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 3038.67 | ✅ 通过 | - |
| 96 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2041.81 | ✅ 通过 | - |
| 97 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 453.43 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 480.8 | ❌ 失败 | HTTP错误: 403 |
| 99 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 540.73 | ❌ 失败 | HTTP错误: 403 |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 707.51 | ✅ 通过 | - |
| 101 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1807.38 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 991.91 | ✅ 通过 | - |
| 103 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 725.1 | ✅ 通过 | - |
| 104 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 403 | 407.27 | ❌ 失败 | HTTP错误: 403 |
| 105 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 904.09 | ✅ 通过 | - |
| 106 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1611.28 | ✅ 通过 | - |
| 107 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 749.33 | ❌ 失败 | HTTP错误: 429 |
| 108 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6766.21 | ✅ 通过 | - |
| 109 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 2586.75 | ✅ 通过 | - |
| 110 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 9167.66 | ✅ 通过 | - |
| 111 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 447.35 | ❌ 失败 | HTTP错误: 403 |
| 112 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1583.3 | ✅ 通过 | - |
| 113 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1730.03 | ✅ 通过 | - |
| 114 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 9939.1 | ✅ 通过 | - |
| 115 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 329.61 | ❌ 失败 | HTTP错误: 403 |
| 116 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 430.35 | ❌ 失败 | HTTP错误: 403 |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 883.81 | ✅ 通过 | - |
| 118 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 6064.15 | ✅ 通过 | - |
| 119 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 8817.67 | ✅ 通过 | - |
| 120 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 7643.67 | ✅ 通过 | - |
| 121 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 14838.49 | ✅ 通过 | - |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 896.97 | ✅ 通过 | - |
| 123 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 4291.17 | ✅ 通过 | - |
| 124 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 1732.55 | ✅ 通过 | - |
| 125 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 375.31 | ❌ 失败 | HTTP错误: 403 |
| 126 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 586.87 | ❌ 失败 | HTTP错误: 403 |
| 127 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 5328.65 | ✅ 通过 | - |
| 129 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 591.51 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 373.38 | ❌ 失败 | HTTP错误: 500 |
| 135 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 399.62 | ❌ 失败 | HTTP错误: 403 |
| 137 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 143 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 499.64 | ❌ 失败 | HTTP错误: 500 |
| 144 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 697.22 | ❌ 失败 | HTTP错误: 500 |
| 145 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 505.79 | ❌ 失败 | HTTP错误: 500 |
| 146 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 795.22 | ❌ 失败 | HTTP错误: 500 |
| 148 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 797.55 | ❌ 失败 | HTTP错误: 500 |
| 150 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1526.49 | ✅ 通过 | - |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 511.24 | ❌ 失败 | HTTP错误: 500 |
| 152 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 667.0 | ❌ 失败 | HTTP错误: 500 |
| 153 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 403 | 571.58 | ❌ 失败 | HTTP错误: 403 |
| 154 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 566.16 | ❌ 失败 | HTTP错误: 403 |
| 155 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 3133.66 | ✅ 通过 | - |
| 156 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 910.48 | ✅ 通过 | - |
| 157 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1842.18 | ✅ 通过 | - |
| 158 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 912.77 | ✅ 通过 | - |
| 159 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1312.97 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 564.93 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 477.74 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 555.32 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 536.93 | ❌ 失败 | HTTP错误: 500 |
| 164 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 543.85 | ❌ 失败 | HTTP错误: 500 |
| 165 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1319.02 | ✅ 通过 | - |
| 166 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1910.12 | ✅ 通过 | - |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 520.76 | ❌ 失败 | HTTP错误: 500 |
| 168 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1482.76 | ✅ 通过 | - |
| 169 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 685.57 | ❌ 失败 | HTTP错误: 500 |
| 170 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 572.9 | ❌ 失败 | HTTP错误: 500 |
| 171 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1872.05 | ✅ 通过 | - |
| 172 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 574.11 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 607.69 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 618.41 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 729.54 | ❌ 失败 | HTTP错误: 500 |
| 176 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 624.25 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 762.58 | ❌ 失败 | HTTP错误: 500 |
| 178 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 625.76 | ❌ 失败 | HTTP错误: 500 |
| 179 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 889.7 | ❌ 失败 | HTTP错误: 500 |
| 180 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 181 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1726.13 | ✅ 通过 | - |
| 182 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 15210.04 | ✅ 通过 | - |
| 186 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 18868.82 | ✅ 通过 | - |
| 187 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 13989.69 | ✅ 通过 | - |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_44

**密钥显示**: bce-v3/ALTAK-X5hU9Pq...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 79 |
| 失败 | 72 |
| 超时 | 42 |
| 通过率 | 40.93% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-x1-turbo-latest**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1222.08 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1251.77 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1262.38 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1240.0 | ❌ 失败 | HTTP错误: 403 |
| 5 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1244.69 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1329.83 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1358.67 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1366.3 | ❌ 失败 | HTTP错误: 403 |
| 9 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1334.84 | ❌ 失败 | HTTP错误: 500 |
| 10 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1383.37 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1382.47 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1430.12 | ❌ 失败 | HTTP错误: 403 |
| 13 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1686.96 | ❌ 失败 | HTTP错误: 403 |
| 14 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 786.53 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2716.05 | ✅ 通过 | - |
| 16 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 2879.64 | ✅ 通过 | - |
| 17 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2825.91 | ✅ 通过 | - |
| 18 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2922.85 | ✅ 通过 | - |
| 19 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 3021.06 | ✅ 通过 | - |
| 20 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 3076.9 | ✅ 通过 | - |
| 21 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3188.45 | ✅ 通过 | - |
| 22 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 531.16 | ❌ 失败 | HTTP错误: 403 |
| 23 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 514.47 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 370.15 | ❌ 失败 | HTTP错误: 429 |
| 25 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1574.29 | ✅ 通过 | - |
| 26 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1649.22 | ✅ 通过 | - |
| 27 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2488.61 | ✅ 通过 | - |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 422.49 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 389.67 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1167.7 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 489.04 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 371.58 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 386.32 | ❌ 失败 | HTTP错误: 403 |
| 34 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 7620.79 | ✅ 通过 | - |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 384.32 | ❌ 失败 | HTTP错误: 403 |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 416.07 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 388.43 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 407.17 | ❌ 失败 | HTTP错误: 403 |
| 39 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 340.68 | ❌ 失败 | HTTP错误: 403 |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 797.79 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 331.61 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1721.85 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1099.72 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1029.75 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 1079.89 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 1048.34 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 333.12 | ❌ 失败 | HTTP错误: 403 |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1332.9 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 757.9 | ✅ 通过 | - |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1691.93 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 705.49 | ✅ 通过 | - |
| 52 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 1485.73 | ✅ 通过 | - |
| 53 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 13231.04 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 987.0 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1160.17 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 12434.55 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 66 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 728.96 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 788.81 | ❌ 失败 | HTTP错误: 403 |
| 71 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 990.44 | ❌ 失败 | HTTP错误: 403 |
| 72 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 1209.55 | ✅ 通过 | - |
| 73 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1304.03 | ✅ 通过 | - |
| 74 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 1253.21 | ✅ 通过 | - |
| 75 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1390.3 | ✅ 通过 | - |
| 77 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 551.48 | ❌ 失败 | HTTP错误: 403 |
| 80 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 701.38 | ✅ 通过 | - |
| 82 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 391.25 | ❌ 失败 | HTTP错误: 403 |
| 83 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1038.98 | ✅ 通过 | - |
| 84 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1285.41 | ✅ 通过 | - |
| 86 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1842.74 | ✅ 通过 | - |
| 87 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2988.87 | ✅ 通过 | - |
| 88 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 1896.08 | ✅ 通过 | - |
| 89 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2283.7 | ✅ 通过 | - |
| 90 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 503.68 | ❌ 失败 | HTTP错误: 403 |
| 91 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 494.58 | ❌ 失败 | HTTP错误: 403 |
| 92 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1048.01 | ✅ 通过 | - |
| 93 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2354.28 | ✅ 通过 | - |
| 94 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1437.52 | ✅ 通过 | - |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1637.08 | ✅ 通过 | - |
| 96 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 484.17 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 438.93 | ❌ 失败 | HTTP错误: 403 |
| 99 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 612.3 | ❌ 失败 | HTTP错误: 403 |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 521.17 | ✅ 通过 | - |
| 101 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 665.2 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1014.52 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 1086.96 | ✅ 通过 | - |
| 104 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1323.81 | ✅ 通过 | - |
| 105 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 403 | 703.09 | ❌ 失败 | HTTP错误: 403 |
| 106 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 5033.78 | ✅ 通过 | - |
| 107 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 394.36 | ❌ 失败 | HTTP错误: 429 |
| 108 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 457.85 | ❌ 失败 | HTTP错误: 403 |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 447.02 | ❌ 失败 | HTTP错误: 403 |
| 110 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 2241.7 | ✅ 通过 | - |
| 111 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 6336.41 | ✅ 通过 | - |
| 112 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 8612.0 | ✅ 通过 | - |
| 113 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1892.83 | ✅ 通过 | - |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 524.38 | ❌ 失败 | HTTP错误: 403 |
| 115 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 309.96 | ❌ 失败 | HTTP错误: 403 |
| 116 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1330.14 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 887.19 | ✅ 通过 | - |
| 118 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 6878.46 | ✅ 通过 | - |
| 119 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 5605.53 | ✅ 通过 | - |
| 120 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 18295.8 | ✅ 通过 | - |
| 121 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 8442.16 | ✅ 通过 | - |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1536.67 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 3125.02 | ✅ 通过 | - |
| 124 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 125 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 5428.98 | ✅ 通过 | - |
| 126 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 403.74 | ❌ 失败 | HTTP错误: 403 |
| 127 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 409.81 | ❌ 失败 | HTTP错误: 403 |
| 128 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 6564.25 | ✅ 通过 | - |
| 129 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 502.12 | ❌ 失败 | HTTP错误: 500 |
| 134 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 643.6 | ✅ 通过 | - |
| 135 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 387.65 | ❌ 失败 | HTTP错误: 403 |
| 137 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 143 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 797.88 | ✅ 通过 | - |
| 144 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 579.76 | ❌ 失败 | HTTP错误: 500 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 608.45 | ❌ 失败 | HTTP错误: 500 |
| 147 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 148 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 492.91 | ❌ 失败 | HTTP错误: 500 |
| 149 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2147.47 | ✅ 通过 | - |
| 150 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 914.72 | ❌ 失败 | HTTP错误: 500 |
| 151 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 1011.96 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 934.84 | ✅ 通过 | - |
| 153 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 767.36 | ❌ 失败 | HTTP错误: 500 |
| 154 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 768.34 | ❌ 失败 | HTTP错误: 500 |
| 155 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 767.95 | ✅ 通过 | - |
| 156 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1240.34 | ✅ 通过 | - |
| 157 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 1046.1 | ✅ 通过 | - |
| 158 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1268.11 | ✅ 通过 | - |
| 159 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1205.3 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 554.66 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 561.91 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 470.19 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1420.88 | ✅ 通过 | - |
| 164 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1908.34 | ✅ 通过 | - |
| 165 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 541.61 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 569.2 | ❌ 失败 | HTTP错误: 500 |
| 167 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 633.13 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 571.62 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 814.64 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 583.09 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 609.07 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 638.73 | ❌ 失败 | HTTP错误: 500 |
| 173 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 594.57 | ❌ 失败 | HTTP错误: 500 |
| 174 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 756.11 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 562.66 | ❌ 失败 | HTTP错误: 500 |
| 176 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 552.75 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 538.01 | ❌ 失败 | HTTP错误: 500 |
| 178 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1715.78 | ✅ 通过 | - |
| 180 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 6381.8 | ✅ 通过 | - |
| 181 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 7863.1 | ✅ 通过 | - |
| 182 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 18519.25 | ✅ 通过 | - |
| 186 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 18707.84 | ✅ 通过 | - |
| 187 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 19590.29 | ✅ 通过 | - |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_45

**密钥显示**: bce-v3/ALTAK-nn5a4ol...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 195


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 195 |
| 通过 | 107 |
| 失败 | 44 |
| 超时 | 44 |
| 通过率 | 54.87% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1274.48 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1352.94 | ❌ 失败 | HTTP错误: 403 |
| 3 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1353.31 | ❌ 失败 | HTTP错误: 500 |
| 4 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 1852.27 | ✅ 通过 | - |
| 5 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 1871.56 | ✅ 通过 | - |
| 6 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 2057.98 | ✅ 通过 | - |
| 7 | pro-deepseek-v3 | {"model": "pro-deepseek-v3", "messages": [{"role":... | 200 | 2353.92 | ✅ 通过 | - |
| 8 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 526.79 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2549.08 | ✅ 通过 | - |
| 10 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 2620.2 | ✅ 通过 | - |
| 11 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 200 | 2592.72 | ✅ 通过 | - |
| 12 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2638.29 | ✅ 通过 | - |
| 13 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 2694.67 | ✅ 通过 | - |
| 14 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2712.34 | ✅ 通过 | - |
| 15 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 2789.15 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 2767.28 | ✅ 通过 | - |
| 17 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2926.09 | ✅ 通过 | - |
| 18 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 3596.27 | ✅ 通过 | - |
| 19 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 2355.69 | ✅ 通过 | - |
| 20 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2449.29 | ✅ 通过 | - |
| 21 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1048.86 | ✅ 通过 | - |
| 22 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 4544.59 | ✅ 通过 | - |
| 23 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 5059.05 | ✅ 通过 | - |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 1516.25 | ✅ 通过 | - |
| 25 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 457.81 | ❌ 失败 | HTTP错误: 403 |
| 26 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 472.66 | ❌ 失败 | HTTP错误: 429 |
| 27 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2805.09 | ✅ 通过 | - |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1552.8 | ✅ 通过 | - |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 410.33 | ❌ 失败 | HTTP错误: 403 |
| 30 | pro-deepseek-r1 | {"model": "pro-deepseek-r1", "messages": [{"role":... | 200 | 10253.0 | ✅ 通过 | - |
| 31 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 316.57 | ❌ 失败 | HTTP错误: 429 |
| 32 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 10419.15 | ✅ 通过 | - |
| 33 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1533.14 | ✅ 通过 | - |
| 34 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 360.32 | ❌ 失败 | HTTP错误: 500 |
| 35 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 447.54 | ❌ 失败 | HTTP错误: 403 |
| 36 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 1861.35 | ✅ 通过 | - |
| 37 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1615.13 | ✅ 通过 | - |
| 38 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 455.17 | ❌ 失败 | HTTP错误: 403 |
| 39 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 470.93 | ❌ 失败 | HTTP错误: 403 |
| 40 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 322.03 | ❌ 失败 | HTTP错误: 403 |
| 41 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 910.31 | ✅ 通过 | - |
| 42 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 2096.17 | ✅ 通过 | - |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 338.42 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1815.75 | ✅ 通过 | - |
| 45 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 2153.61 | ✅ 通过 | - |
| 46 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1209.15 | ✅ 通过 | - |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 882.49 | ✅ 通过 | - |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 641.25 | ✅ 通过 | - |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 652.26 | ✅ 通过 | - |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1031.55 | ✅ 通过 | - |
| 51 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 654.51 | ✅ 通过 | - |
| 52 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 11834.76 | ✅ 通过 | - |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 742.06 | ✅ 通过 | - |
| 54 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 2080.12 | ✅ 通过 | - |
| 55 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 1750.71 | ✅ 通过 | - |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1008.89 | ✅ 通过 | - |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1302.11 | ✅ 通过 | - |
| 58 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 9717.94 | ✅ 通过 | - |
| 59 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 809.58 | ✅ 通过 | - |
| 64 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 66 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 744.9 | ✅ 通过 | - |
| 73 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 973.3 | ✅ 通过 | - |
| 74 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 804.67 | ✅ 通过 | - |
| 75 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 1151.5 | ✅ 通过 | - |
| 78 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 387.92 | ❌ 失败 | HTTP错误: 403 |
| 79 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 852.89 | ✅ 通过 | - |
| 80 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 1998.91 | ✅ 通过 | - |
| 82 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 2218.78 | ✅ 通过 | - |
| 83 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 679.05 | ✅ 通过 | - |
| 84 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 617.0 | ❌ 失败 | HTTP错误: 403 |
| 85 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2311.05 | ✅ 通过 | - |
| 86 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1180.94 | ✅ 通过 | - |
| 87 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 2002.56 | ✅ 通过 | - |
| 88 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2124.37 | ✅ 通过 | - |
| 90 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 2534.47 | ✅ 通过 | - |
| 91 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 927.77 | ✅ 通过 | - |
| 92 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1042.02 | ✅ 通过 | - |
| 93 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1303.0 | ✅ 通过 | - |
| 94 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1696.78 | ✅ 通过 | - |
| 96 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1630.47 | ✅ 通过 | - |
| 97 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 98 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1746.61 | ✅ 通过 | - |
| 99 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 296.69 | ❌ 失败 | HTTP错误: 403 |
| 100 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 363.21 | ❌ 失败 | HTTP错误: 403 |
| 101 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 4788.89 | ✅ 通过 | - |
| 102 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 882.02 | ✅ 通过 | - |
| 103 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 773.6 | ✅ 通过 | - |
| 104 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1114.16 | ✅ 通过 | - |
| 105 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 9228.56 | ✅ 通过 | - |
| 106 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 648.22 | ✅ 通过 | - |
| 107 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 5018.67 | ✅ 通过 | - |
| 108 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1377.84 | ✅ 通过 | - |
| 109 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 1819.74 | ✅ 通过 | - |
| 110 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 11400.27 | ✅ 通过 | - |
| 111 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 4183.75 | ❌ 失败 | HTTP错误: 400 |
| 112 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1409.47 | ✅ 通过 | - |
| 113 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 10899.5 | ✅ 通过 | - |
| 114 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1900.19 | ✅ 通过 | - |
| 115 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 15221.6 | ✅ 通过 | - |
| 116 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1484.06 | ✅ 通过 | - |
| 117 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 6916.67 | ✅ 通过 | - |
| 118 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 119 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 4038.89 | ✅ 通过 | - |
| 120 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 831.9 | ✅ 通过 | - |
| 121 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 6102.78 | ✅ 通过 | - |
| 122 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 12392.08 | ✅ 通过 | - |
| 123 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 124 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 897.5 | ✅ 通过 | - |
| 125 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 3331.41 | ✅ 通过 | - |
| 126 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 7742.24 | ✅ 通过 | - |
| 127 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 7607.39 | ✅ 通过 | - |
| 128 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 13370.32 | ✅ 通过 | - |
| 129 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 13436.84 | ✅ 通过 | - |
| 130 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 134 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 739.43 | ✅ 通过 | - |
| 135 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 581.46 | ❌ 失败 | HTTP错误: 500 |
| 137 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 445.03 | ❌ 失败 | HTTP错误: 403 |
| 142 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 143 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 526.46 | ❌ 失败 | HTTP错误: 500 |
| 144 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 524.08 | ❌ 失败 | HTTP错误: 500 |
| 145 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 431.64 | ❌ 失败 | HTTP错误: 500 |
| 146 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 147 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1043.55 | ✅ 通过 | - |
| 148 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 149 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 589.46 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 544.96 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 491.74 | ❌ 失败 | HTTP错误: 500 |
| 152 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 153 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 984.55 | ❌ 失败 | HTTP错误: 500 |
| 154 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 718.24 | ✅ 通过 | - |
| 155 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2210.8 | ✅ 通过 | - |
| 156 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1678.49 | ✅ 通过 | - |
| 157 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1287.81 | ✅ 通过 | - |
| 158 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1322.64 | ✅ 通过 | - |
| 159 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 975.51 | ✅ 通过 | - |
| 160 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 439.05 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 816.39 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 598.08 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1811.06 | ✅ 通过 | - |
| 164 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1519.35 | ✅ 通过 | - |
| 165 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 455.14 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 503.6 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 562.1 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 467.5 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 754.0 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 537.92 | ❌ 失败 | HTTP错误: 500 |
| 171 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 658.42 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 797.02 | ❌ 失败 | HTTP错误: 500 |
| 173 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 3987.09 | ✅ 通过 | - |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 491.37 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 606.8 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 658.51 | ❌ 失败 | HTTP错误: 500 |
| 177 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 517.26 | ❌ 失败 | HTTP错误: 500 |
| 178 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 540.61 | ❌ 失败 | HTTP错误: 500 |
| 179 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 4240.2 | ✅ 通过 | - |
| 181 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1464.56 | ✅ 通过 | - |
| 182 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 9347.16 | ✅ 通过 | - |
| 184 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 9540.44 | ✅ 通过 | - |
| 185 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 17865.37 | ✅ 通过 | - |
| 186 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 14501.43 | ✅ 通过 | - |
| 187 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 194 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 195 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_46

**密钥显示**: bce-v3/ALTAK-n5AYUIU...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_47

**密钥显示**: bce-v3/ALTAK-znpJcA7...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 105 |
| 失败 | 44 |
| 超时 | 44 |
| 通过率 | 54.4% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1232.9 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1253.79 | ❌ 失败 | HTTP错误: 403 |
| 3 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1409.98 | ❌ 失败 | HTTP错误: 500 |
| 4 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1763.24 | ✅ 通过 | - |
| 5 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 425.1 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 1951.45 | ✅ 通过 | - |
| 7 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 2575.79 | ✅ 通过 | - |
| 8 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 200 | 2535.1 | ✅ 通过 | - |
| 9 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 2644.44 | ✅ 通过 | - |
| 10 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2711.45 | ✅ 通过 | - |
| 11 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 2810.69 | ✅ 通过 | - |
| 12 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 2817.7 | ✅ 通过 | - |
| 13 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2844.12 | ✅ 通过 | - |
| 14 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2856.91 | ✅ 通过 | - |
| 15 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2942.2 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 2968.36 | ✅ 通过 | - |
| 17 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 3073.84 | ✅ 通过 | - |
| 18 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 3107.09 | ✅ 通过 | - |
| 19 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2956.0 | ✅ 通过 | - |
| 20 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3205.65 | ✅ 通过 | - |
| 21 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1241.72 | ✅ 通过 | - |
| 22 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 388.91 | ❌ 失败 | HTTP错误: 403 |
| 23 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 516.18 | ❌ 失败 | HTTP错误: 429 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2302.22 | ✅ 通过 | - |
| 25 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2941.61 | ✅ 通过 | - |
| 26 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1536.52 | ✅ 通过 | - |
| 27 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 324.2 | ❌ 失败 | HTTP错误: 403 |
| 28 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 8097.43 | ✅ 通过 | - |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 378.1 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 8622.21 | ✅ 通过 | - |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1304.64 | ✅ 通过 | - |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 408.34 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 536.88 | ❌ 失败 | HTTP错误: 500 |
| 34 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1669.16 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 318.87 | ❌ 失败 | HTTP错误: 403 |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 360.94 | ❌ 失败 | HTTP错误: 403 |
| 37 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 2753.48 | ✅ 通过 | - |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 337.43 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 1469.24 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 1895.12 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 373.69 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1816.87 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1749.58 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1153.45 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 879.49 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 849.63 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 825.43 | ✅ 通过 | - |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1016.77 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 699.5 | ✅ 通过 | - |
| 50 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 9969.63 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 945.82 | ✅ 通过 | - |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1877.9 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 1539.66 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1097.01 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 1011.36 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 12098.93 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 822.09 | ✅ 通过 | - |
| 64 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 949.05 | ✅ 通过 | - |
| 66 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 933.52 | ✅ 通过 | - |
| 75 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 880.55 | ✅ 通过 | - |
| 76 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 1264.19 | ✅ 通过 | - |
| 77 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 564.1 | ❌ 失败 | HTTP错误: 403 |
| 78 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1425.79 | ✅ 通过 | - |
| 79 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 915.29 | ✅ 通过 | - |
| 80 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 453.38 | ❌ 失败 | HTTP错误: 403 |
| 81 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1846.11 | ✅ 通过 | - |
| 82 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 1789.41 | ✅ 通过 | - |
| 83 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 896.5 | ✅ 通过 | - |
| 84 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1650.71 | ✅ 通过 | - |
| 86 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2517.92 | ✅ 通过 | - |
| 87 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 2743.39 | ✅ 通过 | - |
| 88 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 3334.38 | ✅ 通过 | - |
| 90 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 900.38 | ✅ 通过 | - |
| 91 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1419.32 | ✅ 通过 | - |
| 92 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1188.53 | ✅ 通过 | - |
| 93 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2023.79 | ✅ 通过 | - |
| 94 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1461.08 | ✅ 通过 | - |
| 96 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 1439.76 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 368.0 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 325.39 | ❌ 失败 | HTTP错误: 403 |
| 99 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 552.8 | ✅ 通过 | - |
| 100 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1246.43 | ✅ 通过 | - |
| 101 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 4484.49 | ✅ 通过 | - |
| 102 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 764.96 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 772.16 | ✅ 通过 | - |
| 104 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6830.2 | ✅ 通过 | - |
| 105 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1188.85 | ✅ 通过 | - |
| 106 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 1629.48 | ✅ 通过 | - |
| 107 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 12164.29 | ✅ 通过 | - |
| 108 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 13533.79 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1697.87 | ❌ 失败 | HTTP错误: 400 |
| 110 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8823.95 | ✅ 通过 | - |
| 111 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1459.23 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1717.57 | ✅ 通过 | - |
| 113 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 8063.65 | ✅ 通过 | - |
| 114 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 115 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 7589.63 | ✅ 通过 | - |
| 116 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1597.48 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 1022.31 | ✅ 通过 | - |
| 118 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 5379.15 | ✅ 通过 | - |
| 119 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 22124.94 | ✅ 通过 | - |
| 120 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 5962.82 | ✅ 通过 | - |
| 121 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1166.48 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 3404.9 | ✅ 通过 | - |
| 124 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 4507.82 | ✅ 通过 | - |
| 125 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 11276.95 | ✅ 通过 | - |
| 126 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 9468.35 | ✅ 通过 | - |
| 127 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 13233.65 | ✅ 通过 | - |
| 128 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 129 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 662.41 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 673.19 | ❌ 失败 | HTTP错误: 500 |
| 135 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 339.3 | ❌ 失败 | HTTP错误: 403 |
| 141 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 567.9 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 559.54 | ❌ 失败 | HTTP错误: 500 |
| 144 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 607.15 | ❌ 失败 | HTTP错误: 500 |
| 145 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 483.03 | ❌ 失败 | HTTP错误: 500 |
| 147 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 905.79 | ✅ 通过 | - |
| 148 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 516.22 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 593.73 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 596.74 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 944.28 | ✅ 通过 | - |
| 153 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1659.54 | ✅ 通过 | - |
| 154 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1298.0 | ✅ 通过 | - |
| 155 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1147.35 | ✅ 通过 | - |
| 156 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2654.93 | ✅ 通过 | - |
| 157 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 873.85 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 548.08 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 503.15 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 452.44 | ❌ 失败 | HTTP错误: 500 |
| 161 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1254.3 | ✅ 通过 | - |
| 162 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1332.13 | ✅ 通过 | - |
| 163 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 633.04 | ❌ 失败 | HTTP错误: 500 |
| 164 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 519.07 | ❌ 失败 | HTTP错误: 500 |
| 165 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1870.57 | ✅ 通过 | - |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 537.07 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 540.72 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 525.51 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 496.69 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 583.14 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 554.36 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 572.36 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 629.03 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 468.71 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 543.55 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 983.64 | ❌ 失败 | HTTP错误: 500 |
| 177 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1379.0 | ✅ 通过 | - |
| 178 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 6566.64 | ✅ 通过 | - |
| 180 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 181 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 7203.74 | ✅ 通过 | - |
| 182 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 15547.59 | ✅ 通过 | - |
| 183 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 9183.12 | ✅ 通过 | - |
| 184 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 13311.68 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_48

**密钥显示**: bce-v3/ALTAK-rs8ZajC...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 21 |
| 失败 | 144 |
| 超时 | 28 |
| 通过率 | 10.88% |


### 3. 异常汇总

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **qianfan-engcard-vl**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **qwen-image-edit**: HTTP错误: 429

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **paddleocr-vl-0.9b**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 429

- **pp-structurev3**: HTTP错误: 429

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **ernie-x1.1**: HTTP错误: 403

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1144.53 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1255.54 | ❌ 失败 | HTTP错误: 403 |
| 3 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1160.76 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1279.31 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1282.69 | ❌ 失败 | HTTP错误: 403 |
| 6 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1154.43 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1238.15 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1238.33 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1293.52 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1317.64 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1317.26 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1318.21 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1326.94 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1337.45 | ❌ 失败 | HTTP错误: 403 |
| 15 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1287.86 | ❌ 失败 | HTTP错误: 500 |
| 16 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1271.58 | ❌ 失败 | HTTP错误: 403 |
| 17 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1377.23 | ❌ 失败 | HTTP错误: 403 |
| 18 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1319.36 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1404.59 | ❌ 失败 | HTTP错误: 403 |
| 20 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1419.41 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 767.01 | ❌ 失败 | HTTP错误: 403 |
| 22 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1028.64 | ❌ 失败 | HTTP错误: 403 |
| 23 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1194.05 | ❌ 失败 | HTTP错误: 403 |
| 24 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1133.99 | ❌ 失败 | HTTP错误: 403 |
| 25 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 1234.06 | ❌ 失败 | HTTP错误: 429 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 773.97 | ❌ 失败 | HTTP错误: 403 |
| 27 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 516.64 | ❌ 失败 | HTTP错误: 403 |
| 28 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 560.91 | ❌ 失败 | HTTP错误: 429 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 505.26 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 516.48 | ❌ 失败 | HTTP错误: 429 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 353.58 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 379.23 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 399.66 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 467.6 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 618.03 | ❌ 失败 | HTTP错误: 403 |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 472.07 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3523.64 | ✅ 通过 | - |
| 38 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 466.75 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 528.93 | ❌ 失败 | HTTP错误: 403 |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 503.19 | ❌ 失败 | HTTP错误: 403 |
| 41 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 669.48 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 500.27 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 408.25 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 651.14 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 427.97 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 477.75 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 392.55 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 440.26 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 482.43 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 467.24 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 431.81 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 418.85 | ❌ 失败 | HTTP错误: 403 |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 389.09 | ❌ 失败 | HTTP错误: 403 |
| 54 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 952.39 | ✅ 通过 | - |
| 55 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 660.88 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 367.03 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 426.03 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 449.64 | ❌ 失败 | HTTP错误: 403 |
| 59 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 300.26 | ❌ 失败 | HTTP错误: 403 |
| 60 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 836.87 | ✅ 通过 | - |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 702.81 | ✅ 通过 | - |
| 62 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 612.24 | ❌ 失败 | HTTP错误: 403 |
| 63 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 361.78 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 354.7 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 393.82 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 316.12 | ❌ 失败 | HTTP错误: 403 |
| 67 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 399.88 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 348.56 | ❌ 失败 | HTTP错误: 403 |
| 69 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 84 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 866.01 | ❌ 失败 | HTTP错误: 403 |
| 86 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 883.27 | ❌ 失败 | HTTP错误: 403 |
| 87 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 906.6 | ❌ 失败 | HTTP错误: 403 |
| 88 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 921.95 | ❌ 失败 | HTTP错误: 403 |
| 89 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 936.18 | ❌ 失败 | HTTP错误: 403 |
| 90 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 995.72 | ❌ 失败 | HTTP错误: 403 |
| 91 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 976.12 | ❌ 失败 | HTTP错误: 403 |
| 93 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 997.36 | ❌ 失败 | HTTP错误: 403 |
| 94 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 985.9 | ❌ 失败 | HTTP错误: 403 |
| 95 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 1019.65 | ❌ 失败 | HTTP错误: 403 |
| 96 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 974.73 | ❌ 失败 | HTTP错误: 403 |
| 97 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 993.55 | ❌ 失败 | HTTP错误: 403 |
| 98 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1311.85 | ✅ 通过 | - |
| 99 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 818.41 | ❌ 失败 | HTTP错误: 403 |
| 100 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 870.27 | ❌ 失败 | HTTP错误: 403 |
| 101 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 853.87 | ❌ 失败 | HTTP错误: 429 |
| 102 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 898.01 | ❌ 失败 | HTTP错误: 429 |
| 103 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 1061.24 | ❌ 失败 | HTTP错误: 403 |
| 104 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 867.1 | ❌ 失败 | HTTP错误: 429 |
| 105 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 873.55 | ❌ 失败 | HTTP错误: 429 |
| 106 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 1051.89 | ❌ 失败 | HTTP错误: 403 |
| 107 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 1042.38 | ❌ 失败 | HTTP错误: 403 |
| 108 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 775.99 | ❌ 失败 | HTTP错误: 403 |
| 109 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 1033.46 | ❌ 失败 | HTTP错误: 403 |
| 110 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 868.73 | ❌ 失败 | HTTP错误: 403 |
| 111 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 1048.01 | ❌ 失败 | HTTP错误: 403 |
| 112 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 1089.77 | ❌ 失败 | HTTP错误: 403 |
| 113 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 1094.44 | ❌ 失败 | HTTP错误: 403 |
| 114 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 1264.35 | ❌ 失败 | HTTP错误: 429 |
| 115 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 786.96 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 837.48 | ❌ 失败 | HTTP错误: 403 |
| 117 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 873.0 | ❌ 失败 | HTTP错误: 403 |
| 118 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 830.26 | ❌ 失败 | HTTP错误: 403 |
| 119 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 822.06 | ❌ 失败 | HTTP错误: 403 |
| 120 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 804.6 | ❌ 失败 | HTTP错误: 403 |
| 121 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 847.24 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 971.39 | ❌ 失败 | HTTP错误: 429 |
| 123 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 972.07 | ❌ 失败 | HTTP错误: 429 |
| 124 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 947.38 | ❌ 失败 | HTTP错误: 403 |
| 125 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 904.32 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 987.17 | ❌ 失败 | HTTP错误: 403 |
| 127 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 933.08 | ❌ 失败 | HTTP错误: 403 |
| 128 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 951.89 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 765.75 | ❌ 失败 | HTTP错误: 403 |
| 130 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 923.79 | ❌ 失败 | HTTP错误: 403 |
| 131 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 836.6 | ❌ 失败 | HTTP错误: 429 |
| 132 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 783.65 | ❌ 失败 | HTTP错误: 403 |
| 133 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 786.76 | ❌ 失败 | HTTP错误: 403 |
| 134 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 835.07 | ❌ 失败 | HTTP错误: 403 |
| 135 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 879.29 | ❌ 失败 | HTTP错误: 403 |
| 136 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 889.53 | ❌ 失败 | HTTP错误: 403 |
| 137 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 880.81 | ❌ 失败 | HTTP错误: 403 |
| 138 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 679.96 | ❌ 失败 | HTTP错误: 403 |
| 139 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | 429 | 678.53 | ❌ 失败 | HTTP错误: 429 |
| 140 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 429 | 640.39 | ❌ 失败 | HTTP错误: 429 |
| 141 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | 429 | 654.23 | ❌ 失败 | HTTP错误: 429 |
| 142 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 591.96 | ❌ 失败 | HTTP错误: 403 |
| 143 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 403 | 778.32 | ❌ 失败 | HTTP错误: 403 |
| 144 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 627.14 | ❌ 失败 | HTTP错误: 500 |
| 145 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 696.95 | ❌ 失败 | HTTP错误: 500 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 590.33 | ❌ 失败 | HTTP错误: 500 |
| 147 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1053.4 | ✅ 通过 | - |
| 148 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 835.88 | ❌ 失败 | HTTP错误: 500 |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 570.34 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 594.45 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 600.13 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1197.85 | ✅ 通过 | - |
| 153 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 784.8 | ✅ 通过 | - |
| 154 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 155 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 156 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2290.99 | ✅ 通过 | - |
| 157 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1254.56 | ✅ 通过 | - |
| 158 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 837.95 | ✅ 通过 | - |
| 159 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 443.27 | ❌ 失败 | HTTP错误: 500 |
| 160 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1513.28 | ✅ 通过 | - |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 583.19 | ❌ 失败 | HTTP错误: 500 |
| 162 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 490.12 | ❌ 失败 | HTTP错误: 500 |
| 163 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 515.46 | ❌ 失败 | HTTP错误: 500 |
| 164 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1204.71 | ✅ 通过 | - |
| 165 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1252.44 | ✅ 通过 | - |
| 166 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 541.32 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 577.9 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 575.7 | ❌ 失败 | HTTP错误: 500 |
| 169 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1832.56 | ✅ 通过 | - |
| 170 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 578.99 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 711.79 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 828.59 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 747.02 | ❌ 失败 | HTTP错误: 500 |
| 174 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 626.38 | ❌ 失败 | HTTP错误: 500 |
| 175 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 806.34 | ❌ 失败 | HTTP错误: 500 |
| 176 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 896.52 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 503.11 | ❌ 失败 | HTTP错误: 500 |
| 178 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 926.62 | ❌ 失败 | HTTP错误: 500 |
| 179 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 3755.37 | ✅ 通过 | - |
| 180 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 4344.18 | ✅ 通过 | - |
| 181 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1560.52 | ✅ 通过 | - |
| 182 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8166.64 | ✅ 通过 | - |
| 183 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 16699.28 | ✅ 通过 | - |
| 185 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 20311.34 | ✅ 通过 | - |
| 186 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_49

**密钥显示**: bce-v3/ALTAK-OjJ7ldN...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 30 |
| 失败 | 134 |
| 超时 | 29 |
| 通过率 | 15.54% |


### 3. 异常汇总

- **irag-1.0**: HTTP错误: 429

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-publicopinion-classification**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **qwen3-235b-a22b-instruct-2507**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qwen3-coder-30b-a3b-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-instruct-2507**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **deepseek-v3.1-think-250821**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **qianfan-engcard-vl**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **qwen-image-edit**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1172.79 | ❌ 失败 | HTTP错误: 429 |
| 2 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1217.2 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1230.47 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1223.57 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1241.93 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1265.2 | ❌ 失败 | HTTP错误: 403 |
| 7 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1244.84 | ❌ 失败 | HTTP错误: 403 |
| 8 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1277.45 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1296.03 | ❌ 失败 | HTTP错误: 403 |
| 10 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1247.74 | ❌ 失败 | HTTP错误: 403 |
| 11 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1344.0 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1344.04 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1336.57 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1322.24 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1349.77 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1363.12 | ❌ 失败 | HTTP错误: 403 |
| 17 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1336.04 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1369.32 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1400.73 | ❌ 失败 | HTTP错误: 403 |
| 20 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1418.86 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1005.69 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1152.97 | ❌ 失败 | HTTP错误: 403 |
| 23 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1103.7 | ❌ 失败 | HTTP错误: 403 |
| 24 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1216.09 | ❌ 失败 | HTTP错误: 403 |
| 25 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 603.81 | ❌ 失败 | HTTP错误: 403 |
| 26 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 1397.34 | ❌ 失败 | HTTP错误: 429 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 567.59 | ❌ 失败 | HTTP错误: 429 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 517.62 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 577.71 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 479.07 | ❌ 失败 | HTTP错误: 429 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 458.06 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 435.01 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 460.3 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 450.69 | ❌ 失败 | HTTP错误: 403 |
| 35 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3251.56 | ✅ 通过 | - |
| 36 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 457.19 | ❌ 失败 | HTTP错误: 403 |
| 37 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 473.48 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 454.54 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 512.73 | ❌ 失败 | HTTP错误: 403 |
| 40 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 639.04 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 315.94 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 415.57 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 516.16 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 526.24 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 386.97 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 476.03 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 352.48 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 1008.33 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 377.04 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 483.44 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 439.87 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 417.75 | ❌ 失败 | HTTP错误: 403 |
| 53 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 426.32 | ❌ 失败 | HTTP错误: 403 |
| 54 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 475.45 | ❌ 失败 | HTTP错误: 403 |
| 55 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 503.76 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 604.5 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 500.72 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | 403 | 399.82 | ❌ 失败 | HTTP错误: 403 |
| 59 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 476.45 | ❌ 失败 | HTTP错误: 403 |
| 60 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 425.12 | ❌ 失败 | HTTP错误: 403 |
| 61 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 751.14 | ✅ 通过 | - |
| 62 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 756.4 | ✅ 通过 | - |
| 63 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 702.08 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 379.64 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 422.97 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 499.11 | ❌ 失败 | HTTP错误: 403 |
| 67 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 426.74 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 390.76 | ❌ 失败 | HTTP错误: 403 |
| 69 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 455.34 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 888.78 | ❌ 失败 | HTTP错误: 403 |
| 71 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 382.24 | ❌ 失败 | HTTP错误: 403 |
| 72 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 377.56 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 404.07 | ❌ 失败 | HTTP错误: 403 |
| 74 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 346.36 | ❌ 失败 | HTTP错误: 403 |
| 75 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 321.03 | ❌ 失败 | HTTP错误: 403 |
| 76 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 84 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 85 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 86 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 87 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 403 | 632.93 | ❌ 失败 | HTTP错误: 403 |
| 91 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 717.53 | ❌ 失败 | HTTP错误: 403 |
| 93 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 719.54 | ❌ 失败 | HTTP错误: 403 |
| 94 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 403 | 861.7 | ❌ 失败 | HTTP错误: 403 |
| 96 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 898.93 | ❌ 失败 | HTTP错误: 403 |
| 98 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 1050.73 | ❌ 失败 | HTTP错误: 403 |
| 99 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 403 | 1062.41 | ❌ 失败 | HTTP错误: 403 |
| 100 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 1064.71 | ❌ 失败 | HTTP错误: 403 |
| 101 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 1044.75 | ❌ 失败 | HTTP错误: 403 |
| 102 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 1019.19 | ❌ 失败 | HTTP错误: 429 |
| 103 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 1018.84 | ❌ 失败 | HTTP错误: 429 |
| 104 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 1113.94 | ❌ 失败 | HTTP错误: 403 |
| 105 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 1072.41 | ❌ 失败 | HTTP错误: 429 |
| 106 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 874.17 | ❌ 失败 | HTTP错误: 429 |
| 107 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 1083.76 | ❌ 失败 | HTTP错误: 429 |
| 108 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 403 | 1036.22 | ❌ 失败 | HTTP错误: 403 |
| 109 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 1073.53 | ❌ 失败 | HTTP错误: 403 |
| 110 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 848.88 | ❌ 失败 | HTTP错误: 403 |
| 111 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 841.61 | ❌ 失败 | HTTP错误: 403 |
| 112 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 997.32 | ❌ 失败 | HTTP错误: 403 |
| 113 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 867.06 | ❌ 失败 | HTTP错误: 403 |
| 114 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 964.91 | ❌ 失败 | HTTP错误: 403 |
| 115 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 901.56 | ❌ 失败 | HTTP错误: 403 |
| 116 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 921.42 | ❌ 失败 | HTTP错误: 403 |
| 117 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 852.83 | ❌ 失败 | HTTP错误: 403 |
| 118 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 956.32 | ❌ 失败 | HTTP错误: 403 |
| 119 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 831.88 | ❌ 失败 | HTTP错误: 429 |
| 120 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 1085.68 | ❌ 失败 | HTTP错误: 403 |
| 121 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 880.77 | ❌ 失败 | HTTP错误: 429 |
| 122 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 910.49 | ❌ 失败 | HTTP错误: 403 |
| 123 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 872.87 | ❌ 失败 | HTTP错误: 403 |
| 124 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 932.61 | ❌ 失败 | HTTP错误: 403 |
| 125 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 755.28 | ❌ 失败 | HTTP错误: 429 |
| 126 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 1077.92 | ❌ 失败 | HTTP错误: 403 |
| 127 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 1175.18 | ❌ 失败 | HTTP错误: 403 |
| 128 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1915.95 | ✅ 通过 | - |
| 129 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 623.5 | ❌ 失败 | HTTP错误: 403 |
| 130 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 609.47 | ❌ 失败 | HTTP错误: 403 |
| 131 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 1496.88 | ✅ 通过 | - |
| 132 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1333.19 | ✅ 通过 | - |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 702.17 | ✅ 通过 | - |
| 134 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 2320.68 | ✅ 通过 | - |
| 135 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 532.19 | ❌ 失败 | HTTP错误: 500 |
| 136 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2097.01 | ✅ 通过 | - |
| 137 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 485.74 | ❌ 失败 | HTTP错误: 403 |
| 138 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 3375.81 | ✅ 通过 | - |
| 139 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 407.98 | ❌ 失败 | HTTP错误: 500 |
| 141 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 929.01 | ✅ 通过 | - |
| 142 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 500.89 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 564.98 | ❌ 失败 | HTTP错误: 500 |
| 144 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 4403.48 | ✅ 通过 | - |
| 145 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 750.38 | ❌ 失败 | HTTP错误: 500 |
| 146 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 494.81 | ❌ 失败 | HTTP错误: 500 |
| 147 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 561.02 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 577.12 | ❌ 失败 | HTTP错误: 500 |
| 149 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2729.39 | ✅ 通过 | - |
| 150 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 984.46 | ✅ 通过 | - |
| 151 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1048.84 | ✅ 通过 | - |
| 152 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2018.06 | ✅ 通过 | - |
| 153 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 5998.97 | ✅ 通过 | - |
| 154 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 155 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 6691.2 | ✅ 通过 | - |
| 156 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 728.92 | ✅ 通过 | - |
| 157 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1395.8 | ✅ 通过 | - |
| 158 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 8366.24 | ✅ 通过 | - |
| 159 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 765.66 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 446.29 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 819.73 | ❌ 失败 | HTTP错误: 500 |
| 162 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1197.63 | ✅ 通过 | - |
| 163 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 468.43 | ❌ 失败 | HTTP错误: 500 |
| 164 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1369.22 | ✅ 通过 | - |
| 165 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1789.4 | ✅ 通过 | - |
| 166 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 534.07 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 572.42 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 612.94 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 661.02 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 573.39 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 702.85 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 979.08 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 515.12 | ❌ 失败 | HTTP错误: 500 |
| 174 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 565.81 | ❌ 失败 | HTTP错误: 500 |
| 175 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 540.58 | ❌ 失败 | HTTP错误: 500 |
| 176 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 651.26 | ❌ 失败 | HTTP错误: 500 |
| 177 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 607.72 | ❌ 失败 | HTTP错误: 500 |
| 178 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1593.2 | ✅ 通过 | - |
| 180 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 5373.25 | ✅ 通过 | - |
| 181 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 10109.69 | ✅ 通过 | - |
| 182 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 14146.21 | ✅ 通过 | - |
| 183 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 18679.51 | ✅ 通过 | - |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 13292.67 | ✅ 通过 | - |
| 185 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_50

**密钥显示**: bce-v3/ALTAK-qPMLuDB...


### 1. 模型列表获取状态

- **状态**: 失败

- **模型总数**: 0


---


## API密钥: KEY_51

**密钥显示**: bce-v3/ALTAK-xhw4fAH...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 45 |
| 失败 | 111 |
| 超时 | 37 |
| 通过率 | 23.32% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **deepseek-r1**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 403

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 403

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-32k**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **ernie-4.5-turbo-128k**: HTTP错误: 403

- **ernie-x1-turbo-32k**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-sug-8k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **deepseek-r1-250528**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-publicopinion-classification**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **stable-diffusion-xl**: HTTP错误: 429

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-vl**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **deepseek-v3.1-250821**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **glm-5**: HTTP错误: 403

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1187.05 | ❌ 失败 | HTTP错误: 403 |
| 2 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1158.66 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1219.38 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1255.88 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1250.27 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1321.17 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1341.34 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1347.27 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1361.1 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1350.85 | ❌ 失败 | HTTP错误: 403 |
| 11 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1312.21 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1354.02 | ❌ 失败 | HTTP错误: 403 |
| 13 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1334.53 | ❌ 失败 | HTTP错误: 429 |
| 14 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1410.88 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1423.18 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1428.62 | ❌ 失败 | HTTP错误: 403 |
| 17 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 403 | 1439.78 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1523.65 | ❌ 失败 | HTTP错误: 403 |
| 19 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1547.25 | ❌ 失败 | HTTP错误: 403 |
| 20 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1576.99 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 982.67 | ❌ 失败 | HTTP错误: 403 |
| 22 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 1026.43 | ❌ 失败 | HTTP错误: 403 |
| 23 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 1000.54 | ❌ 失败 | HTTP错误: 403 |
| 24 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 998.8 | ❌ 失败 | HTTP错误: 429 |
| 25 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1221.61 | ❌ 失败 | HTTP错误: 403 |
| 26 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 602.09 | ❌ 失败 | HTTP错误: 403 |
| 27 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 403 | 602.42 | ❌ 失败 | HTTP错误: 403 |
| 28 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 544.38 | ❌ 失败 | HTTP错误: 403 |
| 29 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 544.04 | ❌ 失败 | HTTP错误: 403 |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 403 | 497.45 | ❌ 失败 | HTTP错误: 403 |
| 31 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 406.82 | ❌ 失败 | HTTP错误: 403 |
| 32 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 411.1 | ❌ 失败 | HTTP错误: 429 |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 404.34 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 403 | 388.75 | ❌ 失败 | HTTP错误: 403 |
| 35 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 443.4 | ❌ 失败 | HTTP错误: 403 |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 335.84 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3406.23 | ✅ 通过 | - |
| 38 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 411.72 | ❌ 失败 | HTTP错误: 403 |
| 39 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 446.22 | ❌ 失败 | HTTP错误: 403 |
| 40 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 408.1 | ❌ 失败 | HTTP错误: 403 |
| 41 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 403 | 468.97 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 403 | 476.39 | ❌ 失败 | HTTP错误: 403 |
| 43 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 554.27 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 507.92 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 485.8 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 443.35 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 524.04 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 503.29 | ❌ 失败 | HTTP错误: 403 |
| 49 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 402.76 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 420.05 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 403 | 506.72 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 379.67 | ❌ 失败 | HTTP错误: 403 |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 411.63 | ❌ 失败 | HTTP错误: 403 |
| 54 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 403 | 424.18 | ❌ 失败 | HTTP错误: 403 |
| 55 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 651.76 | ❌ 失败 | HTTP错误: 403 |
| 56 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 440.74 | ❌ 失败 | HTTP错误: 403 |
| 57 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 445.21 | ❌ 失败 | HTTP错误: 403 |
| 58 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | 403 | 414.61 | ❌ 失败 | HTTP错误: 403 |
| 59 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 397.52 | ❌ 失败 | HTTP错误: 403 |
| 60 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 404.34 | ❌ 失败 | HTTP错误: 403 |
| 61 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 821.48 | ✅ 通过 | - |
| 62 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 845.2 | ✅ 通过 | - |
| 63 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 385.53 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 371.08 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 705.8 | ✅ 通过 | - |
| 66 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 747.16 | ✅ 通过 | - |
| 67 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 328.57 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 394.82 | ❌ 失败 | HTTP错误: 403 |
| 69 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 455.52 | ❌ 失败 | HTTP错误: 403 |
| 70 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 519.25 | ❌ 失败 | HTTP错误: 403 |
| 71 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | 429 | 641.06 | ❌ 失败 | HTTP错误: 429 |
| 72 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 423.37 | ❌ 失败 | HTTP错误: 403 |
| 73 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 620.76 | ❌ 失败 | HTTP错误: 403 |
| 74 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 455.88 | ❌ 失败 | HTTP错误: 403 |
| 75 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 393.46 | ❌ 失败 | HTTP错误: 403 |
| 76 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 419.17 | ❌ 失败 | HTTP错误: 403 |
| 77 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1495.31 | ✅ 通过 | - |
| 78 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 17057.0 | ✅ 通过 | - |
| 79 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 840.36 | ✅ 通过 | - |
| 80 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 884.45 | ❌ 失败 | HTTP错误: 403 |
| 81 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2482.27 | ✅ 通过 | - |
| 82 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 901.32 | ✅ 通过 | - |
| 83 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 4757.49 | ✅ 通过 | - |
| 84 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1000.56 | ✅ 通过 | - |
| 85 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 380.84 | ❌ 失败 | HTTP错误: 403 |
| 86 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 403 | 421.46 | ❌ 失败 | HTTP错误: 403 |
| 87 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 91 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 94 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 95 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 96 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 98 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 99 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 100 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 101 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 102 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 103 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 770.14 | ❌ 失败 | HTTP错误: 403 |
| 104 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 403 | 812.73 | ❌ 失败 | HTTP错误: 403 |
| 105 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 106 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 830.8 | ❌ 失败 | HTTP错误: 403 |
| 107 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 1110.63 | ✅ 通过 | - |
| 108 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 1110.8 | ✅ 通过 | - |
| 109 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 580.35 | ❌ 失败 | HTTP错误: 403 |
| 110 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 580.61 | ❌ 失败 | HTTP错误: 429 |
| 111 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1385.46 | ✅ 通过 | - |
| 112 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 836.37 | ✅ 通过 | - |
| 113 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 689.1 | ❌ 失败 | HTTP错误: 403 |
| 114 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 532.18 | ❌ 失败 | HTTP错误: 403 |
| 115 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1387.37 | ✅ 通过 | - |
| 116 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 586.28 | ❌ 失败 | HTTP错误: 403 |
| 117 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 602.4 | ❌ 失败 | HTTP错误: 403 |
| 118 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1153.64 | ✅ 通过 | - |
| 119 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 1092.21 | ✅ 通过 | - |
| 120 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 2241.75 | ✅ 通过 | - |
| 121 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 870.53 | ✅ 通过 | - |
| 123 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 6803.91 | ✅ 通过 | - |
| 124 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 6237.76 | ✅ 通过 | - |
| 125 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 388.1 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 6068.13 | ✅ 通过 | - |
| 127 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 7127.07 | ✅ 通过 | - |
| 128 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 466.12 | ❌ 失败 | HTTP错误: 403 |
| 129 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2810.55 | ✅ 通过 | - |
| 130 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 10635.34 | ✅ 通过 | - |
| 132 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 586.77 | ✅ 通过 | - |
| 133 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 773.93 | ❌ 失败 | HTTP错误: 500 |
| 134 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 7235.13 | ✅ 通过 | - |
| 135 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 11602.74 | ✅ 通过 | - |
| 136 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 330.71 | ❌ 失败 | HTTP错误: 403 |
| 137 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2574.03 | ✅ 通过 | - |
| 138 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 920.09 | ✅ 通过 | - |
| 139 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 360.84 | ❌ 失败 | HTTP错误: 500 |
| 140 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 359.92 | ❌ 失败 | HTTP错误: 500 |
| 141 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 333.02 | ❌ 失败 | HTTP错误: 500 |
| 142 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 396.13 | ❌ 失败 | HTTP错误: 500 |
| 143 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 2352.36 | ✅ 通过 | - |
| 144 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 462.94 | ❌ 失败 | HTTP错误: 500 |
| 145 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 437.71 | ❌ 失败 | HTTP错误: 500 |
| 146 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 408.5 | ❌ 失败 | HTTP错误: 500 |
| 147 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 603.85 | ✅ 通过 | - |
| 148 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 10227.24 | ✅ 通过 | - |
| 149 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1095.84 | ✅ 通过 | - |
| 150 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 403 | 368.97 | ❌ 失败 | HTTP错误: 403 |
| 151 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1174.06 | ✅ 通过 | - |
| 152 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 4918.53 | ✅ 通过 | - |
| 153 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 788.14 | ✅ 通过 | - |
| 154 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1888.48 | ✅ 通过 | - |
| 155 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1316.72 | ✅ 通过 | - |
| 156 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 1317.67 | ✅ 通过 | - |
| 157 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 455.54 | ❌ 失败 | HTTP错误: 500 |
| 158 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 426.44 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 416.76 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 391.9 | ❌ 失败 | HTTP错误: 500 |
| 161 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 339.91 | ❌ 失败 | HTTP错误: 500 |
| 162 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 354.95 | ❌ 失败 | HTTP错误: 500 |
| 163 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 420.82 | ❌ 失败 | HTTP错误: 500 |
| 164 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 368.52 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 589.83 | ❌ 失败 | HTTP错误: 500 |
| 166 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 390.94 | ❌ 失败 | HTTP错误: 500 |
| 167 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 398.22 | ❌ 失败 | HTTP错误: 500 |
| 168 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 432.85 | ❌ 失败 | HTTP错误: 500 |
| 169 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 411.33 | ❌ 失败 | HTTP错误: 500 |
| 170 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 171 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 569.27 | ❌ 失败 | HTTP错误: 500 |
| 172 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 486.14 | ❌ 失败 | HTTP错误: 500 |
| 173 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 13874.79 | ✅ 通过 | - |
| 174 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 1098.35 | ❌ 失败 | HTTP错误: 500 |
| 175 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1561.14 | ✅ 通过 | - |
| 176 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 12464.57 | ✅ 通过 | - |
| 177 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 178 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 181 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 182 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 183 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 184 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_52

**密钥显示**: bce-v3/ALTAK-D0MCtmD...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 97 |
| 失败 | 53 |
| 超时 | 43 |
| 通过率 | 50.26% |


### 3. 异常汇总

- **deepseek-v3**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **ernie-char-fiction-8k**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1233.78 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1302.61 | ❌ 失败 | HTTP错误: 403 |
| 3 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1309.6 | ❌ 失败 | HTTP错误: 403 |
| 4 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1275.72 | ❌ 失败 | HTTP错误: 500 |
| 5 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1318.8 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1375.43 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1426.83 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1459.67 | ❌ 失败 | HTTP错误: 403 |
| 9 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 656.89 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 2237.08 | ✅ 通过 | - |
| 11 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2613.82 | ✅ 通过 | - |
| 12 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2833.65 | ✅ 通过 | - |
| 13 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2825.2 | ✅ 通过 | - |
| 14 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2895.0 | ✅ 通过 | - |
| 15 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 2962.81 | ✅ 通过 | - |
| 16 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 3021.22 | ✅ 通过 | - |
| 17 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 3101.61 | ✅ 通过 | - |
| 18 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 3219.59 | ✅ 通过 | - |
| 19 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3425.24 | ✅ 通过 | - |
| 20 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 3932.39 | ✅ 通过 | - |
| 21 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1075.19 | ✅ 通过 | - |
| 22 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 4418.22 | ✅ 通过 | - |
| 23 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 428.32 | ❌ 失败 | HTTP错误: 403 |
| 24 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 423.36 | ❌ 失败 | HTTP错误: 429 |
| 25 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2544.34 | ✅ 通过 | - |
| 26 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2474.57 | ✅ 通过 | - |
| 27 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1531.24 | ✅ 通过 | - |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 468.49 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 406.62 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1156.22 | ✅ 通过 | - |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 397.16 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 333.9 | ❌ 失败 | HTTP错误: 403 |
| 33 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 1638.79 | ✅ 通过 | - |
| 34 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 10021.64 | ✅ 通过 | - |
| 35 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 324.39 | ❌ 失败 | HTTP错误: 403 |
| 36 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 1469.33 | ✅ 通过 | - |
| 37 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 400.43 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 348.82 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 1012.7 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 2299.75 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 402.98 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1665.06 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1252.47 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 1019.83 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 957.17 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 698.68 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 648.96 | ✅ 通过 | - |
| 48 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 8895.85 | ✅ 通过 | - |
| 49 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1328.57 | ✅ 通过 | - |
| 50 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 721.03 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 787.9 | ✅ 通过 | - |
| 52 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 1490.37 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 2205.64 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 874.01 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 806.19 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 13571.74 | ✅ 通过 | - |
| 57 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 65 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 868.0 | ✅ 通过 | - |
| 66 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 67 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 774.82 | ✅ 通过 | - |
| 68 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 1141.2 | ✅ 通过 | - |
| 69 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 200 | 1179.08 | ✅ 通过 | - |
| 70 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 604.25 | ✅ 通过 | - |
| 71 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 1264.32 | ✅ 通过 | - |
| 72 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 745.27 | ❌ 失败 | HTTP错误: 403 |
| 78 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1448.37 | ✅ 通过 | - |
| 80 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 1045.53 | ✅ 通过 | - |
| 81 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 534.55 | ❌ 失败 | HTTP错误: 403 |
| 82 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1786.47 | ✅ 通过 | - |
| 83 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 764.2 | ✅ 通过 | - |
| 84 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1392.76 | ✅ 通过 | - |
| 85 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 86 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 1923.13 | ✅ 通过 | - |
| 87 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 2209.51 | ✅ 通过 | - |
| 88 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 3506.92 | ✅ 通过 | - |
| 89 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 497.34 | ❌ 失败 | HTTP错误: 403 |
| 90 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1081.18 | ✅ 通过 | - |
| 91 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 92 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 3046.89 | ✅ 通过 | - |
| 93 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1086.97 | ✅ 通过 | - |
| 94 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 1936.51 | ✅ 通过 | - |
| 95 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 96 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1713.25 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 381.79 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 362.22 | ❌ 失败 | HTTP错误: 403 |
| 99 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 2202.76 | ✅ 通过 | - |
| 100 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 1111.66 | ✅ 通过 | - |
| 101 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 685.38 | ✅ 通过 | - |
| 102 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 1149.54 | ✅ 通过 | - |
| 103 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 954.22 | ✅ 通过 | - |
| 104 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1326.76 | ✅ 通过 | - |
| 105 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 5267.1 | ✅ 通过 | - |
| 106 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 9744.09 | ✅ 通过 | - |
| 107 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6759.76 | ✅ 通过 | - |
| 108 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 2808.75 | ✅ 通过 | - |
| 109 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 9415.59 | ✅ 通过 | - |
| 110 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 424.26 | ❌ 失败 | HTTP错误: 403 |
| 111 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1843.7 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1703.59 | ✅ 通过 | - |
| 113 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 6766.64 | ✅ 通过 | - |
| 114 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 9921.13 | ✅ 通过 | - |
| 115 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 604.07 | ❌ 失败 | HTTP错误: 403 |
| 116 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 11266.19 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 809.84 | ✅ 通过 | - |
| 118 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 7074.9 | ✅ 通过 | - |
| 119 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 4509.64 | ✅ 通过 | - |
| 120 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 5063.9 | ✅ 通过 | - |
| 121 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 869.95 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 1558.92 | ✅ 通过 | - |
| 124 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 8544.37 | ✅ 通过 | - |
| 125 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 390.87 | ❌ 失败 | HTTP错误: 403 |
| 126 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 456.2 | ❌ 失败 | HTTP错误: 403 |
| 127 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 6838.01 | ✅ 通过 | - |
| 128 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 129 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 619.1 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 428.45 | ❌ 失败 | HTTP错误: 500 |
| 135 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 138 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 446.02 | ❌ 失败 | HTTP错误: 403 |
| 140 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 142 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 564.69 | ❌ 失败 | HTTP错误: 500 |
| 143 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 545.54 | ❌ 失败 | HTTP错误: 500 |
| 144 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 518.53 | ❌ 失败 | HTTP错误: 500 |
| 147 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 558.5 | ❌ 失败 | HTTP错误: 500 |
| 148 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1106.81 | ✅ 通过 | - |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 584.2 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 594.25 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 603.35 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 865.8 | ✅ 通过 | - |
| 153 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1685.31 | ✅ 通过 | - |
| 154 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1356.85 | ✅ 通过 | - |
| 155 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2582.52 | ✅ 通过 | - |
| 156 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1193.06 | ✅ 通过 | - |
| 157 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 922.53 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 481.99 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 493.62 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 441.42 | ❌ 失败 | HTTP错误: 500 |
| 161 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 481.14 | ❌ 失败 | HTTP错误: 500 |
| 162 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 425.03 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1816.78 | ✅ 通过 | - |
| 164 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2007.33 | ✅ 通过 | - |
| 165 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 396.89 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 660.21 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 476.23 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 561.5 | ❌ 失败 | HTTP错误: 500 |
| 169 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 470.18 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 910.6 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 1075.8 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 624.14 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 463.72 | ❌ 失败 | HTTP错误: 500 |
| 174 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 622.81 | ❌ 失败 | HTTP错误: 500 |
| 175 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 546.8 | ❌ 失败 | HTTP错误: 500 |
| 176 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 177 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 178 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 5308.6 | ✅ 通过 | - |
| 179 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 4165.51 | ✅ 通过 | - |
| 180 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1472.48 | ✅ 通过 | - |
| 181 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 6754.55 | ✅ 通过 | - |
| 182 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 15182.27 | ✅ 通过 | - |
| 183 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 15097.45 | ✅ 通过 | - |
| 184 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 13145.36 | ✅ 通过 | - |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_53

**密钥显示**: bce-v3/ALTAK-zJvRFvL...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 32 |
| 失败 | 132 |
| 超时 | 29 |
| 通过率 | 16.58% |


### 3. 异常汇总

- **ernie-4.0-turbo-8k-latest**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-32b**: HTTP错误: 403

- **ernie-4.0-8k-latest**: HTTP错误: 403

- **ernie-4.0-turbo-8k-preview**: HTTP错误: 403

- **ernie-speed-pro-128k**: HTTP错误: 403

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-4.0-turbo-128k**: HTTP错误: 403

- **ernie-3.5-8k**: HTTP错误: 403

- **ernie-lite-pro-128k**: HTTP错误: 403

- **deepseek-r1-distill-qwen-14b**: HTTP错误: 403

- **ernie-4.0-8k**: HTTP错误: 403

- **ernie-3.5-8k-preview**: HTTP错误: 403

- **ernie-4.0-8k-preview**: HTTP错误: 403

- **ernie-4.0-turbo-8k**: HTTP错误: 403

- **ernie-3.5-128k**: HTTP错误: 403

- **deepseek-v3**: HTTP错误: 403

- **ernie-char-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 429

- **meta-llama-3-8b**: HTTP错误: 403

- **qwen2.5-vl-7b-instruct**: HTTP错误: 403

- **qwq-32b**: HTTP错误: 403

- **flux.1-schnell**: HTTP错误: 429

- **ernie-4.5-8k-preview**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qwen2.5-vl-32b-instruct**: HTTP错误: 403

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **qwen2.5-7b-instruct**: HTTP错误: 403

- **ernie-irag-edit**: HTTP错误: 429

- **qianfan-8b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qianfan-llama-vl-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **qwen3-32b**: HTTP错误: 403

- **qwen3-14b**: HTTP错误: 403

- **qwen3-4b**: HTTP错误: 403

- **qwen3-8b**: HTTP错误: 403

- **qwen3-1.7b**: HTTP错误: 403

- **qwen3-0.6b**: HTTP错误: 403

- **qianfan-agent-intent-32k**: HTTP错误: 403

- **qianfan-check-vl**: HTTP错误: 403

- **qianfan-composition**: HTTP错误: 403

- **ernie-4.5-turbo-vl-32k-preview**: HTTP错误: 403

- **internvl3-38b**: HTTP错误: 403

- **qianfan-multipicocr**: HTTP错误: 403

- **qianfan-qi-vl**: HTTP错误: 403

- **ernie-x1-turbo-32k-preview**: HTTP错误: 403

- **ernie-4.5-turbo-128k-preview**: HTTP错误: 403

- **ernie-4.5-0.3b**: HTTP错误: 403

- **ernie-4.5-21b-a3b**: HTTP错误: 403

- **ernie-4.5-vl-28b-a3b**: HTTP错误: 403

- **ernie-4.5-turbo-vl-preview**: HTTP错误: 403

- **qwen3-embedding-4b**: HTTP错误: 403

- **qwen3-embedding-0.6b**: HTTP错误: 403

- **ernie-3.5-8k-0613**: HTTP错误: 403

- **ernie-4.0-turbo-8k-0628**: HTTP错误: 403

- **qianfan-agent-lite-8k**: HTTP错误: 403

- **ernie-3.5-128k-preview**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **ernie-3.5-8k-0701**: HTTP错误: 403

- **qwen3-235b-a22b-thinking-2507**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **qwen3-30b-a3b-thinking-2507**: HTTP错误: 403

- **qianfan-correct**: HTTP错误: 403

- **qianfan-toytalk**: HTTP错误: 403

- **qwen3-coder-480b-a35b-instruct**: HTTP错误: 403

- **musesteamer-2.0-lite-i2v**: HTTP错误: 429

- **musesteamer-2.0-pro-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v**: HTTP错误: 429

- **musesteamer-2.0-turbo-i2v-audio**: HTTP错误: 429

- **qwen3-reranker-0.6b**: HTTP错误: 403

- **qwen3-reranker-8b**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **musesteamer-2.0-turbo-i2v-effect**: HTTP错误: 429

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **qianfan-engcard-vl**: HTTP错误: 403

- **qianfan-ipcharacter**: HTTP错误: 403

- **qianfan-singlepicocr**: HTTP错误: 403

- **qianfan-vl-70b**: HTTP错误: 403

- **qianfan-vl-8b**: HTTP错误: 403

- **ernie-x1.1-preview**: HTTP错误: 403

- **ernie-4.0-8k-0613**: HTTP错误: 403

- **qwen-image**: HTTP错误: 429

- **qwen-image-edit**: HTTP错误: 429

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 403

- **qwen3-next-80b-a3b-instruct**: HTTP错误: 403

- **qwen3-vl-235b-a22b-instruct**: HTTP错误: 403

- **qwen3-next-80b-a3b-thinking**: HTTP错误: 403

- **deepseek-v3.2-think**: HTTP错误: 403

- **deepseek-v3.2**: HTTP错误: 403

- **qwen3-vl-30b-a3b-thinking**: HTTP错误: 403

- **qwen3-vl-235b-a22b-thinking**: HTTP错误: 403

- **qwen3-vl-30b-a3b-instruct**: HTTP错误: 403

- **musesteamer-air-i2v**: HTTP错误: 429

- **qwen3-vl-8b-thinking**: HTTP错误: 403

- **qwen3-vl-8b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-instruct**: HTTP错误: 403

- **qwen3-vl-32b-thinking**: HTTP错误: 403

- **ernie-5.0-thinking-preview**: HTTP错误: 403

- **ernie-5.0-thinking-latest**: HTTP错误: 403

- **deepseek-ocr**: HTTP错误: 403

- **paddleocr-vl-0.9b**: HTTP错误: 429

- **musesteamer-air-image**: HTTP错误: 429

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 403 | 1246.11 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1248.52 | ❌ 失败 | HTTP错误: 403 |
| 3 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 403 | 1134.54 | ❌ 失败 | HTTP错误: 403 |
| 4 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 403 | 1227.0 | ❌ 失败 | HTTP错误: 403 |
| 5 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 403 | 1280.28 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 403 | 1295.26 | ❌ 失败 | HTTP错误: 403 |
| 7 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1294.73 | ❌ 失败 | HTTP错误: 403 |
| 8 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 403 | 1283.46 | ❌ 失败 | HTTP错误: 403 |
| 9 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 403 | 1337.72 | ❌ 失败 | HTTP错误: 403 |
| 10 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 403 | 1337.9 | ❌ 失败 | HTTP错误: 403 |
| 11 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 403 | 1197.3 | ❌ 失败 | HTTP错误: 403 |
| 12 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 403 | 1351.75 | ❌ 失败 | HTTP错误: 403 |
| 13 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 403 | 1364.37 | ❌ 失败 | HTTP错误: 403 |
| 14 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 403 | 1372.01 | ❌ 失败 | HTTP错误: 403 |
| 15 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 403 | 1369.77 | ❌ 失败 | HTTP错误: 403 |
| 16 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 403 | 1432.35 | ❌ 失败 | HTTP错误: 403 |
| 17 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 403 | 1408.68 | ❌ 失败 | HTTP错误: 403 |
| 18 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 403 | 1467.28 | ❌ 失败 | HTTP错误: 403 |
| 19 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 429 | 1469.23 | ❌ 失败 | HTTP错误: 429 |
| 20 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 973.82 | ❌ 失败 | HTTP错误: 403 |
| 21 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 403 | 991.66 | ❌ 失败 | HTTP错误: 403 |
| 22 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 403 | 1239.44 | ❌ 失败 | HTTP错误: 403 |
| 23 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | 429 | 522.4 | ❌ 失败 | HTTP错误: 429 |
| 24 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 403 | 1298.35 | ❌ 失败 | HTTP错误: 403 |
| 25 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 504.78 | ❌ 失败 | HTTP错误: 403 |
| 26 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 508.87 | ❌ 失败 | HTTP错误: 429 |
| 27 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 403 | 621.75 | ❌ 失败 | HTTP错误: 403 |
| 28 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 560.93 | ❌ 失败 | HTTP错误: 403 |
| 29 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 368.68 | ❌ 失败 | HTTP错误: 429 |
| 30 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 403 | 402.8 | ❌ 失败 | HTTP错误: 403 |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 429 | 316.03 | ❌ 失败 | HTTP错误: 429 |
| 32 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 3340.89 | ✅ 通过 | - |
| 33 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 370.91 | ❌ 失败 | HTTP错误: 403 |
| 34 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 403 | 350.26 | ❌ 失败 | HTTP错误: 403 |
| 35 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 5424.62 | ✅ 通过 | - |
| 36 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 411.77 | ❌ 失败 | HTTP错误: 403 |
| 37 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 408.61 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 357.11 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 403 | 507.79 | ❌ 失败 | HTTP错误: 403 |
| 40 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 2278.22 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 384.57 | ❌ 失败 | HTTP错误: 403 |
| 42 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 1546.38 | ✅ 通过 | - |
| 43 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 403 | 451.52 | ❌ 失败 | HTTP错误: 403 |
| 44 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 403 | 433.77 | ❌ 失败 | HTTP错误: 403 |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 403 | 371.65 | ❌ 失败 | HTTP错误: 403 |
| 46 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 403 | 507.11 | ❌ 失败 | HTTP错误: 403 |
| 47 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 403 | 384.01 | ❌ 失败 | HTTP错误: 403 |
| 48 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 403 | 370.73 | ❌ 失败 | HTTP错误: 403 |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 403 | 402.76 | ❌ 失败 | HTTP错误: 403 |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 403 | 355.88 | ❌ 失败 | HTTP错误: 403 |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 403 | 330.71 | ❌ 失败 | HTTP错误: 403 |
| 52 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1461.06 | ✅ 通过 | - |
| 53 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 403 | 413.4 | ❌ 失败 | HTTP错误: 403 |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 403 | 559.55 | ❌ 失败 | HTTP错误: 403 |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 403 | 328.11 | ❌ 失败 | HTTP错误: 403 |
| 56 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 9632.76 | ✅ 通过 | - |
| 57 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 10848.59 | ✅ 通过 | - |
| 58 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | 403 | 375.5 | ❌ 失败 | HTTP错误: 403 |
| 59 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 403 | 298.02 | ❌ 失败 | HTTP错误: 403 |
| 60 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 834.58 | ✅ 通过 | - |
| 61 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 892.76 | ✅ 通过 | - |
| 62 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 403 | 403.08 | ❌ 失败 | HTTP错误: 403 |
| 63 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 403 | 376.23 | ❌ 失败 | HTTP错误: 403 |
| 64 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 403 | 360.05 | ❌ 失败 | HTTP错误: 403 |
| 65 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 403 | 318.42 | ❌ 失败 | HTTP错误: 403 |
| 66 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 403 | 474.11 | ❌ 失败 | HTTP错误: 403 |
| 67 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | 403 | 386.12 | ❌ 失败 | HTTP错误: 403 |
| 68 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | 403 | 417.21 | ❌ 失败 | HTTP错误: 403 |
| 69 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 75 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 76 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 77 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 78 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 79 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 81 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 82 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 403 | 784.86 | ❌ 失败 | HTTP错误: 403 |
| 84 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 403 | 790.13 | ❌ 失败 | HTTP错误: 403 |
| 85 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 403 | 795.33 | ❌ 失败 | HTTP错误: 403 |
| 86 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 403 | 849.84 | ❌ 失败 | HTTP错误: 403 |
| 87 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 833.27 | ❌ 失败 | HTTP错误: 403 |
| 88 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 403 | 890.25 | ❌ 失败 | HTTP错误: 403 |
| 89 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 90 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 403 | 857.78 | ❌ 失败 | HTTP错误: 403 |
| 91 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 840.23 | ❌ 失败 | HTTP错误: 403 |
| 92 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 403 | 858.83 | ❌ 失败 | HTTP错误: 403 |
| 94 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 403 | 936.73 | ❌ 失败 | HTTP错误: 403 |
| 95 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 403 | 1019.68 | ❌ 失败 | HTTP错误: 403 |
| 96 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 97 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 403 | 787.19 | ❌ 失败 | HTTP错误: 403 |
| 98 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | 429 | 815.81 | ❌ 失败 | HTTP错误: 429 |
| 99 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | 429 | 795.78 | ❌ 失败 | HTTP错误: 429 |
| 100 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | 429 | 757.04 | ❌ 失败 | HTTP错误: 429 |
| 101 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1597.98 | ✅ 通过 | - |
| 102 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | 429 | 794.47 | ❌ 失败 | HTTP错误: 429 |
| 103 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1765.41 | ✅ 通过 | - |
| 104 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | 403 | 767.78 | ❌ 失败 | HTTP错误: 403 |
| 105 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | 403 | 849.76 | ❌ 失败 | HTTP错误: 403 |
| 106 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 672.29 | ❌ 失败 | HTTP错误: 403 |
| 107 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1376.76 | ✅ 通过 | - |
| 108 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | 429 | 1162.71 | ❌ 失败 | HTTP错误: 429 |
| 109 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 660.1 | ❌ 失败 | HTTP错误: 403 |
| 110 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 403 | 670.01 | ❌ 失败 | HTTP错误: 403 |
| 111 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 403 | 677.83 | ❌ 失败 | HTTP错误: 403 |
| 112 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 403 | 700.13 | ❌ 失败 | HTTP错误: 403 |
| 113 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 403 | 745.89 | ❌ 失败 | HTTP错误: 403 |
| 114 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 403 | 805.09 | ❌ 失败 | HTTP错误: 403 |
| 115 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 403 | 707.29 | ❌ 失败 | HTTP错误: 403 |
| 116 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 403 | 776.89 | ❌ 失败 | HTTP错误: 403 |
| 117 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | 429 | 699.7 | ❌ 失败 | HTTP错误: 429 |
| 118 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | 429 | 735.07 | ❌ 失败 | HTTP错误: 429 |
| 119 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 403 | 750.56 | ❌ 失败 | HTTP错误: 403 |
| 120 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 2118.72 | ✅ 通过 | - |
| 121 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 403 | 729.11 | ❌ 失败 | HTTP错误: 403 |
| 122 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 403 | 695.55 | ❌ 失败 | HTTP错误: 403 |
| 123 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 403 | 755.45 | ❌ 失败 | HTTP错误: 403 |
| 124 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 403 | 665.12 | ❌ 失败 | HTTP错误: 403 |
| 125 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 403 | 747.23 | ❌ 失败 | HTTP错误: 403 |
| 126 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 403 | 705.62 | ❌ 失败 | HTTP错误: 403 |
| 127 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 403 | 1004.86 | ❌ 失败 | HTTP错误: 403 |
| 128 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 2374.81 | ✅ 通过 | - |
| 129 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 403 | 750.36 | ❌ 失败 | HTTP错误: 403 |
| 130 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | 429 | 704.77 | ❌ 失败 | HTTP错误: 429 |
| 131 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 403 | 717.05 | ❌ 失败 | HTTP错误: 403 |
| 132 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 403 | 755.45 | ❌ 失败 | HTTP错误: 403 |
| 133 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 403 | 755.4 | ❌ 失败 | HTTP错误: 403 |
| 134 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 403 | 766.21 | ❌ 失败 | HTTP错误: 403 |
| 135 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 403 | 776.58 | ❌ 失败 | HTTP错误: 403 |
| 136 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 403 | 874.67 | ❌ 失败 | HTTP错误: 403 |
| 137 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 403 | 693.1 | ❌ 失败 | HTTP错误: 403 |
| 138 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | 429 | 680.66 | ❌ 失败 | HTTP错误: 429 |
| 139 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 429 | 677.84 | ❌ 失败 | HTTP错误: 429 |
| 140 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 606.76 | ❌ 失败 | HTTP错误: 403 |
| 141 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 570.83 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 563.2 | ❌ 失败 | HTTP错误: 500 |
| 143 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 481.11 | ❌ 失败 | HTTP错误: 500 |
| 144 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1011.11 | ✅ 通过 | - |
| 145 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 432.84 | ❌ 失败 | HTTP错误: 500 |
| 146 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 516.74 | ❌ 失败 | HTTP错误: 500 |
| 147 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 650.09 | ❌ 失败 | HTTP错误: 500 |
| 148 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 456.79 | ❌ 失败 | HTTP错误: 500 |
| 149 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2310.67 | ✅ 通过 | - |
| 150 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 769.23 | ✅ 通过 | - |
| 151 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1052.4 | ✅ 通过 | - |
| 152 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 6368.15 | ✅ 通过 | - |
| 153 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1220.88 | ✅ 通过 | - |
| 154 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 7238.0 | ✅ 通过 | - |
| 155 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 4245.55 | ✅ 通过 | - |
| 156 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 157 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 491.09 | ❌ 失败 | HTTP错误: 500 |
| 158 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 2165.74 | ✅ 通过 | - |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 480.68 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 457.79 | ❌ 失败 | HTTP错误: 500 |
| 161 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1413.2 | ✅ 通过 | - |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 411.55 | ❌ 失败 | HTTP错误: 500 |
| 163 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 516.63 | ❌ 失败 | HTTP错误: 500 |
| 164 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 488.51 | ❌ 失败 | HTTP错误: 500 |
| 165 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 5411.33 | ✅ 通过 | - |
| 166 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 543.65 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 489.44 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 545.63 | ❌ 失败 | HTTP错误: 500 |
| 169 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 526.79 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 652.1 | ❌ 失败 | HTTP错误: 500 |
| 171 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 502.45 | ❌ 失败 | HTTP错误: 500 |
| 172 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 437.08 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 514.69 | ❌ 失败 | HTTP错误: 500 |
| 174 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 560.67 | ❌ 失败 | HTTP错误: 500 |
| 175 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 546.75 | ❌ 失败 | HTTP错误: 500 |
| 176 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 3927.33 | ✅ 通过 | - |
| 177 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1493.08 | ✅ 通过 | - |
| 178 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 7623.59 | ✅ 通过 | - |
| 180 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 9250.5 | ✅ 通过 | - |
| 181 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 13991.17 | ✅ 通过 | - |
| 182 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 10082.87 | ✅ 通过 | - |
| 183 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 14982.63 | ✅ 通过 | - |
| 184 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 185 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


---


## API密钥: KEY_54

**密钥显示**: bce-v3/ALTAK-rSBxzUu...


### 1. 模型列表获取状态

- **状态**: 成功

- **模型总数**: 193


### 2. 总体测试统计

| 指标 | 数值 |
|------|------|
| 测试总数 | 193 |
| 通过 | 105 |
| 失败 | 44 |
| 超时 | 44 |
| 通过率 | 54.4% |


### 3. 异常汇总

- **ernie-novel-8k**: HTTP错误: 403

- **ernie-char-fiction-8k**: HTTP错误: 403

- **irag-1.0**: HTTP错误: 500

- **meta-llama-3-8b**: HTTP错误: 403

- **internvl2.5-38b-mpo**: HTTP错误: 403

- **ernie-x1-32k-preview**: HTTP错误: 429

- **qianfan-chinese-llama-2-13b**: HTTP错误: 403

- **ernie-x1-32k**: HTTP错误: 429

- **ernie-irag-edit**: HTTP错误: 500

- **qianfan-8b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-70b**: HTTP错误: 403

- **qianfan-70b**: HTTP错误: 403

- **deepseek-r1-distill-qianfan-8b**: HTTP错误: 403

- **qwen3-30b-a3b**: HTTP错误: 403

- **ernie-char-fiction-8k-preview**: HTTP错误: 403

- **kimi-k2-instruct**: HTTP错误: 403

- **ernie-4.5-turbo-latest**: HTTP错误: 403

- **ernie-4.5-turbo-vl-latest**: HTTP错误: 403

- **ernie-4.5-21b-a3b-thinking**: HTTP错误: 400

- **musesteamer-air-image**: HTTP错误: 500

- **ernie-5.0-thinking-exp**: HTTP错误: 403

- **musesteamer-2.1-lite-i2v**: HTTP错误: 500

- **musesteamer-2.1-turbo-i2v**: HTTP错误: 500

- **kling-identify-face**: HTTP错误: 500

- **kling-advanced-lip-sync**: HTTP错误: 500

- **viduq2-pro_reference2video**: HTTP错误: 500

- **viduq3-pro_img2video**: HTTP错误: 500

- **viduq3-pro_text2video**: HTTP错误: 500

- **viduq3-turbo_start-end2video**: HTTP错误: 500

- **viduq3-pro_start-end2video**: HTTP错误: 500

- **viduq3-turbo_img2video**: HTTP错误: 500

- **viduq3-turbo_text2video**: HTTP错误: 500

- **kling-image-o1_omni-image**: HTTP错误: 500

- **kling-v3-omni_omni-image**: HTTP错误: 500

- **kling-v3_image2video**: HTTP错误: 500

- **kling-v3_generations**: HTTP错误: 500

- **kling-m1_ai-multi-shot**: HTTP错误: 500

- **vidu-tts**: HTTP错误: 500

- **vidu-audio-tts**: HTTP错误: 500

- **kling-v3_motion-control**: HTTP错误: 500

- **vidu-motion-sync_image2dance**: HTTP错误: 500

- **vidu-audio-clone**: HTTP错误: 500

- **viduq300-turbo_text2video**: HTTP错误: 500

- **kling-custom-voices_voices**: HTTP错误: 500


### 4. 各模型测试详情

| 序号 | 模型名称 | 请求参数 | 响应状态码 | 响应时间(ms) | 测试结果 | 错误信息 |
|------|----------|----------|------------|--------------|----------|----------|
| 1 | ernie-novel-8k | {"model": "ernie-novel-8k", "messages": [{"role": ... | 403 | 1238.36 | ❌ 失败 | HTTP错误: 403 |
| 2 | ernie-char-fiction-8k | {"model": "ernie-char-fiction-8k", "messages": [{"... | 403 | 1325.96 | ❌ 失败 | HTTP错误: 403 |
| 3 | irag-1.0 | {"model": "irag-1.0", "messages": [{"role": "user"... | 500 | 1360.57 | ❌ 失败 | HTTP错误: 500 |
| 4 | ernie-char-8k | {"model": "ernie-char-8k", "messages": [{"role": "... | 200 | 1783.95 | ✅ 通过 | - |
| 5 | meta-llama-3-8b | {"model": "meta-llama-3-8b", "messages": [{"role":... | 403 | 421.95 | ❌ 失败 | HTTP错误: 403 |
| 6 | ernie-lite-pro-128k | {"model": "ernie-lite-pro-128k", "messages": [{"ro... | 200 | 1854.51 | ✅ 通过 | - |
| 7 | ernie-speed-pro-128k | {"model": "ernie-speed-pro-128k", "messages": [{"r... | 200 | 1997.33 | ✅ 通过 | - |
| 8 | deepseek-v3 | {"model": "deepseek-v3", "messages": [{"role": "us... | 200 | 2207.18 | ✅ 通过 | - |
| 9 | ernie-3.5-128k | {"model": "ernie-3.5-128k", "messages": [{"role": ... | 200 | 2656.93 | ✅ 通过 | - |
| 10 | ernie-3.5-8k | {"model": "ernie-3.5-8k", "messages": [{"role": "u... | 200 | 2785.48 | ✅ 通过 | - |
| 11 | ernie-4.0-8k-latest | {"model": "ernie-4.0-8k-latest", "messages": [{"ro... | 200 | 2775.78 | ✅ 通过 | - |
| 12 | ernie-4.0-turbo-8k-preview | {"model": "ernie-4.0-turbo-8k-preview", "messages"... | 200 | 2818.1 | ✅ 通过 | - |
| 13 | ernie-4.0-8k-preview | {"model": "ernie-4.0-8k-preview", "messages": [{"r... | 200 | 2883.58 | ✅ 通过 | - |
| 14 | ernie-4.0-8k | {"model": "ernie-4.0-8k", "messages": [{"role": "u... | 200 | 2948.99 | ✅ 通过 | - |
| 15 | ernie-4.0-turbo-128k | {"model": "ernie-4.0-turbo-128k", "messages": [{"r... | 200 | 2983.83 | ✅ 通过 | - |
| 16 | deepseek-r1-distill-qwen-14b | {"model": "deepseek-r1-distill-qwen-14b", "message... | 200 | 2963.5 | ✅ 通过 | - |
| 17 | ernie-3.5-8k-preview | {"model": "ernie-3.5-8k-preview", "messages": [{"r... | 200 | 3183.48 | ✅ 通过 | - |
| 18 | deepseek-r1-distill-qwen-32b | {"model": "deepseek-r1-distill-qwen-32b", "message... | 200 | 3250.56 | ✅ 通过 | - |
| 19 | qwen2.5-vl-7b-instruct | {"model": "qwen2.5-vl-7b-instruct", "messages": [{... | 200 | 1193.69 | ✅ 通过 | - |
| 20 | ernie-4.0-turbo-8k-latest | {"model": "ernie-4.0-turbo-8k-latest", "messages":... | 200 | 4630.11 | ✅ 通过 | - |
| 21 | ernie-4.0-turbo-8k | {"model": "ernie-4.0-turbo-8k", "messages": [{"rol... | 200 | 5069.14 | ✅ 通过 | - |
| 22 | ernie-4.5-8k-preview | {"model": "ernie-4.5-8k-preview", "messages": [{"r... | 200 | 2394.92 | ✅ 通过 | - |
| 23 | internvl2.5-38b-mpo | {"model": "internvl2.5-38b-mpo", "messages": [{"ro... | 403 | 501.17 | ❌ 失败 | HTTP错误: 403 |
| 24 | deepseek-r1 | {"model": "deepseek-r1", "messages": [{"role": "us... | 200 | 5680.5 | ✅ 通过 | - |
| 25 | qwq-32b | {"model": "qwq-32b", "messages": [{"role": "user",... | 200 | 4725.06 | ✅ 通过 | - |
| 26 | ernie-x1-32k-preview | {"model": "ernie-x1-32k-preview", "messages": [{"r... | 429 | 557.13 | ❌ 失败 | HTTP错误: 429 |
| 27 | qianfan-chinese-llama-2-13b | {"model": "qianfan-chinese-llama-2-13b", "messages... | 403 | 410.23 | ❌ 失败 | HTTP错误: 403 |
| 28 | deepseek-v3-241226 | {"model": "deepseek-v3-241226", "messages": [{"rol... | 200 | 2660.1 | ✅ 通过 | - |
| 29 | qwen2.5-vl-32b-instruct | {"model": "qwen2.5-vl-32b-instruct", "messages": [... | 200 | 1664.81 | ✅ 通过 | - |
| 30 | ernie-x1-32k | {"model": "ernie-x1-32k", "messages": [{"role": "u... | 429 | 400.46 | ❌ 失败 | HTTP错误: 429 |
| 31 | ernie-irag-edit | {"model": "ernie-irag-edit", "messages": [{"role":... | 500 | 528.87 | ❌ 失败 | HTTP错误: 500 |
| 32 | qianfan-8b | {"model": "qianfan-8b", "messages": [{"role": "use... | 403 | 490.84 | ❌ 失败 | HTTP错误: 403 |
| 33 | qwen2.5-7b-instruct | {"model": "qwen2.5-7b-instruct", "messages": [{"ro... | 200 | 1277.0 | ✅ 通过 | - |
| 34 | ernie-4.5-turbo-vl-32k | {"model": "ernie-4.5-turbo-vl-32k", "messages": [{... | 200 | 2082.44 | ✅ 通过 | - |
| 35 | ernie-4.5-turbo-32k | {"model": "ernie-4.5-turbo-32k", "messages": [{"ro... | 200 | 2363.66 | ✅ 通过 | - |
| 36 | deepseek-r1-distill-qianfan-70b | {"model": "deepseek-r1-distill-qianfan-70b", "mess... | 403 | 449.58 | ❌ 失败 | HTTP错误: 403 |
| 37 | qianfan-70b | {"model": "qianfan-70b", "messages": [{"role": "us... | 403 | 605.62 | ❌ 失败 | HTTP错误: 403 |
| 38 | deepseek-r1-distill-qianfan-8b | {"model": "deepseek-r1-distill-qianfan-8b", "messa... | 403 | 409.64 | ❌ 失败 | HTTP错误: 403 |
| 39 | qianfan-llama-vl-8b | {"model": "qianfan-llama-vl-8b", "messages": [{"ro... | 200 | 1160.02 | ✅ 通过 | - |
| 40 | ernie-4.5-turbo-128k | {"model": "ernie-4.5-turbo-128k", "messages": [{"r... | 200 | 1486.19 | ✅ 通过 | - |
| 41 | qwen3-30b-a3b | {"model": "qwen3-30b-a3b", "messages": [{"role": "... | 403 | 369.17 | ❌ 失败 | HTTP错误: 403 |
| 42 | qwen3-32b | {"model": "qwen3-32b", "messages": [{"role": "user... | 200 | 1707.26 | ✅ 通过 | - |
| 43 | qwen3-14b | {"model": "qwen3-14b", "messages": [{"role": "user... | 200 | 1067.89 | ✅ 通过 | - |
| 44 | qwen3-8b | {"model": "qwen3-8b", "messages": [{"role": "user"... | 200 | 983.38 | ✅ 通过 | - |
| 45 | qwen3-4b | {"model": "qwen3-4b", "messages": [{"role": "user"... | 200 | 1489.33 | ✅ 通过 | - |
| 46 | qwen3-1.7b | {"model": "qwen3-1.7b", "messages": [{"role": "use... | 200 | 773.55 | ✅ 通过 | - |
| 47 | qwen3-0.6b | {"model": "qwen3-0.6b", "messages": [{"role": "use... | 200 | 602.73 | ✅ 通过 | - |
| 48 | qianfan-sug-8k | {"model": "qianfan-sug-8k", "messages": [{"role": ... | 200 | 1034.97 | ✅ 通过 | - |
| 49 | qianfan-agent-intent-32k | {"model": "qianfan-agent-intent-32k", "messages": ... | 200 | 821.99 | ✅ 通过 | - |
| 50 | qianfan-check-vl | {"model": "qianfan-check-vl", "messages": [{"role"... | 200 | 2122.53 | ✅ 通过 | - |
| 51 | qianfan-composition | {"model": "qianfan-composition", "messages": [{"ro... | 200 | 989.46 | ✅ 通过 | - |
| 52 | ernie-4.5-turbo-vl-32k-preview | {"model": "ernie-4.5-turbo-vl-32k-preview", "messa... | 200 | 1658.16 | ✅ 通过 | - |
| 53 | ernie-x1-turbo-32k | {"model": "ernie-x1-turbo-32k", "messages": [{"rol... | 200 | 15580.79 | ✅ 通过 | - |
| 54 | internvl3-38b | {"model": "internvl3-38b", "messages": [{"role": "... | 200 | 1066.73 | ✅ 通过 | - |
| 55 | qianfan-multipicocr | {"model": "qianfan-multipicocr", "messages": [{"ro... | 200 | 969.97 | ✅ 通过 | - |
| 56 | deepseek-r1-250528 | {"model": "deepseek-r1-250528", "messages": [{"rol... | 200 | 9578.59 | ✅ 通过 | - |
| 57 | yi-34b-chat | {"model": "yi-34b-chat", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 58 | chatglm2-6b-32k | {"model": "chatglm2-6b-32k", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 59 | gemma-7b-it | {"model": "gemma-7b-it", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 60 | llama-2-7b-chat | {"model": "llama-2-7b-chat", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 61 | aquilachat-7b | {"model": "aquilachat-7b", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 62 | llama-2-13b-chat | {"model": "llama-2-13b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 63 | codellama-7b-instruct | {"model": "codellama-7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 64 | qfintentrecogbd | {"model": "qfintentrecogbd", "messages": [{"role":... | 200 | 937.54 | ✅ 通过 | - |
| 65 | qfintentrecogbj | {"model": "qfintentrecogbj", "messages": [{"role":... | 200 | 998.12 | ✅ 通过 | - |
| 66 | ernie-4.5-0.3b | {"model": "ernie-4.5-0.3b", "messages": [{"role": ... | 200 | 769.11 | ✅ 通过 | - |
| 67 | mixtral-8x7b-instruct | {"model": "mixtral-8x7b-instruct", "messages": [{"... | - | - | ⏱️ 超时 | 请求超时 |
| 68 | xuanyuan-70b-chat-4bit | {"model": "xuanyuan-70b-chat-4bit", "messages": [{... | - | - | ⏱️ 超时 | 请求超时 |
| 69 | bloomz-7b | {"model": "bloomz-7b", "messages": [{"role": "user... | - | - | ⏱️ 超时 | 请求超时 |
| 70 | llama-2-70b-chat | {"model": "llama-2-70b-chat", "messages": [{"role"... | - | - | ⏱️ 超时 | 请求超时 |
| 71 | sqlcoder-7b | {"model": "sqlcoder-7b", "messages": [{"role": "us... | - | - | ⏱️ 超时 | 请求超时 |
| 72 | qianfan-bloomz-7b-compressed | {"model": "qianfan-bloomz-7b-compressed", "message... | - | - | ⏱️ 超时 | 请求超时 |
| 73 | search-deepseek-v3 | {"model": "search-deepseek-v3", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 74 | ernie-4.5-21b-a3b | {"model": "ernie-4.5-21b-a3b", "messages": [{"role... | 200 | 895.7 | ✅ 通过 | - |
| 75 | ernie-4.5-vl-28b-a3b | {"model": "ernie-4.5-vl-28b-a3b", "messages": [{"r... | 200 | 877.1 | ✅ 通过 | - |
| 76 | ernie-char-fiction-8k-preview | {"model": "ernie-char-fiction-8k-preview", "messag... | 403 | 439.4 | ❌ 失败 | HTTP错误: 403 |
| 77 | qianfan-agent-lite-8k | {"model": "qianfan-agent-lite-8k", "messages": [{"... | 200 | 882.89 | ✅ 通过 | - |
| 78 | ernie-4.5-turbo-128k-preview | {"model": "ernie-4.5-turbo-128k-preview", "message... | 200 | 2249.23 | ✅ 通过 | - |
| 79 | flux.1-schnell | {"model": "flux.1-schnell", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |
| 80 | ernie-4.5-turbo-vl-preview | {"model": "ernie-4.5-turbo-vl-preview", "messages"... | 200 | 1676.16 | ✅ 通过 | - |
| 81 | kimi-k2-instruct | {"model": "kimi-k2-instruct", "messages": [{"role"... | 403 | 414.84 | ❌ 失败 | HTTP错误: 403 |
| 82 | qianfan-toytalk | {"model": "qianfan-toytalk", "messages": [{"role":... | 200 | 674.18 | ✅ 通过 | - |
| 83 | ernie-3.5-8k-0613 | {"model": "ernie-3.5-8k-0613", "messages": [{"role... | 200 | 1989.11 | ✅ 通过 | - |
| 84 | ernie-3.5-8k-0701 | {"model": "ernie-3.5-8k-0701", "messages": [{"role... | 200 | 1942.78 | ✅ 通过 | - |
| 85 | qwen3-235b-a22b-instruct-2507 | {"model": "qwen3-235b-a22b-instruct-2507", "messag... | 200 | 1179.71 | ✅ 通过 | - |
| 86 | ernie-3.5-128k-preview | {"model": "ernie-3.5-128k-preview", "messages": [{... | 200 | 2091.29 | ✅ 通过 | - |
| 87 | wan-2.1-i2v-14b-480p | {"model": "wan-2.1-i2v-14b-480p", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 88 | qianfan-chinese-llama-2-7b | {"model": "qianfan-chinese-llama-2-7b", "messages"... | - | - | ⏱️ 超时 | 请求超时 |
| 89 | qwen3-30b-a3b-instruct-2507 | {"model": "qwen3-30b-a3b-instruct-2507", "messages... | 200 | 1144.46 | ✅ 通过 | - |
| 90 | qwen3-coder-30b-a3b-instruct | {"model": "qwen3-coder-30b-a3b-instruct", "message... | 200 | 1199.82 | ✅ 通过 | - |
| 91 | qwen3-coder-480b-a35b-instruct | {"model": "qwen3-coder-480b-a35b-instruct", "messa... | 200 | 1445.01 | ✅ 通过 | - |
| 92 | qianfan-chinese-llama-2-70b | {"model": "qianfan-chinese-llama-2-70b", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 93 | ernie-4.0-turbo-8k-0628 | {"model": "ernie-4.0-turbo-8k-0628", "messages": [... | 200 | 3444.72 | ✅ 通过 | - |
| 94 | ernie-4.5-turbo-vl | {"model": "ernie-4.5-turbo-vl", "messages": [{"rol... | 200 | 1453.12 | ✅ 通过 | - |
| 95 | qianfan-correct | {"model": "qianfan-correct", "messages": [{"role":... | 200 | 2249.49 | ✅ 通过 | - |
| 96 | deepseek-v3.1-250821 | {"model": "deepseek-v3.1-250821", "messages": [{"r... | 200 | 2101.99 | ✅ 通过 | - |
| 97 | ernie-4.5-turbo-latest | {"model": "ernie-4.5-turbo-latest", "messages": [{... | 403 | 379.29 | ❌ 失败 | HTTP错误: 403 |
| 98 | ernie-4.5-turbo-vl-latest | {"model": "ernie-4.5-turbo-vl-latest", "messages":... | 403 | 382.73 | ❌ 失败 | HTTP错误: 403 |
| 99 | qianfan-singlepicocr | {"model": "qianfan-singlepicocr", "messages": [{"r... | 200 | 774.16 | ✅ 通过 | - |
| 100 | qianfan-ipcharacter | {"model": "qianfan-ipcharacter", "messages": [{"ro... | 200 | 964.99 | ✅ 通过 | - |
| 101 | ernie-x1-turbo-32k-preview | {"model": "ernie-x1-turbo-32k-preview", "messages"... | 200 | 9698.27 | ✅ 通过 | - |
| 102 | qwen3-30b-a3b-thinking-2507 | {"model": "qwen3-30b-a3b-thinking-2507", "messages... | 200 | 6965.67 | ✅ 通过 | - |
| 103 | qianfan-engcard-vl | {"model": "qianfan-engcard-vl", "messages": [{"rol... | 200 | 800.38 | ✅ 通过 | - |
| 104 | qianfan-vl-8b | {"model": "qianfan-vl-8b", "messages": [{"role": "... | 200 | 691.35 | ✅ 通过 | - |
| 105 | qwen3-235b-a22b-thinking-2507 | {"model": "qwen3-235b-a22b-thinking-2507", "messag... | 200 | 8228.11 | ✅ 通过 | - |
| 106 | qianfan-vl-70b | {"model": "qianfan-vl-70b", "messages": [{"role": ... | 200 | 1259.06 | ✅ 通过 | - |
| 107 | deepseek-v3.1-think-250821 | {"model": "deepseek-v3.1-think-250821", "messages"... | 200 | 6944.16 | ✅ 通过 | - |
| 108 | ernie-4.0-8k-0613 | {"model": "ernie-4.0-8k-0613", "messages": [{"role... | 200 | 2642.2 | ✅ 通过 | - |
| 109 | ernie-4.5-21b-a3b-thinking | {"model": "ernie-4.5-21b-a3b-thinking", "messages"... | 400 | 1651.34 | ❌ 失败 | HTTP错误: 400 |
| 110 | qwen3-next-80b-a3b-instruct | {"model": "qwen3-next-80b-a3b-instruct", "messages... | 200 | 1053.37 | ✅ 通过 | - |
| 111 | ernie-x1-turbo-latest | {"model": "ernie-x1-turbo-latest", "messages": [{"... | 200 | 11014.34 | ✅ 通过 | - |
| 112 | qwen3-vl-235b-a22b-instruct | {"model": "qwen3-vl-235b-a22b-instruct", "messages... | 200 | 1636.06 | ✅ 通过 | - |
| 113 | ernie-x1.1-preview | {"model": "ernie-x1.1-preview", "messages": [{"rol... | 200 | 13222.93 | ✅ 通过 | - |
| 114 | deepseek-v3.2 | {"model": "deepseek-v3.2", "messages": [{"role": "... | 200 | 1838.73 | ✅ 通过 | - |
| 115 | qianfan-ql-vl | {"model": "qianfan-ql-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 116 | qwen3-next-80b-a3b-thinking | {"model": "qwen3-next-80b-a3b-thinking", "messages... | 200 | 12497.24 | ✅ 通过 | - |
| 117 | qwen3-vl-30b-a3b-instruct | {"model": "qwen3-vl-30b-a3b-instruct", "messages":... | 200 | 821.46 | ✅ 通过 | - |
| 118 | deepseek-v3.2-think | {"model": "deepseek-v3.2-think", "messages": [{"ro... | 200 | 5761.01 | ✅ 通过 | - |
| 119 | qwen3-vl-30b-a3b-thinking | {"model": "qwen3-vl-30b-a3b-thinking", "messages":... | 200 | 4349.82 | ✅ 通过 | - |
| 120 | qwen3-vl-235b-a22b-thinking | {"model": "qwen3-vl-235b-a22b-thinking", "messages... | 200 | 10801.08 | ✅ 通过 | - |
| 121 | qianfan-publicopinion-classification | {"model": "qianfan-publicopinion-classification", ... | - | - | ⏱️ 超时 | 请求超时 |
| 122 | qwen3-vl-8b-instruct | {"model": "qwen3-vl-8b-instruct", "messages": [{"r... | 200 | 1011.23 | ✅ 通过 | - |
| 123 | qwen3-vl-32b-instruct | {"model": "qwen3-vl-32b-instruct", "messages": [{"... | 200 | 2097.5 | ✅ 通过 | - |
| 124 | qwen3-vl-8b-thinking | {"model": "qwen3-vl-8b-thinking", "messages": [{"r... | 200 | 5761.62 | ✅ 通过 | - |
| 125 | qwen3-vl-32b-thinking | {"model": "qwen3-vl-32b-thinking", "messages": [{"... | 200 | 7107.06 | ✅ 通过 | - |
| 126 | ernie-5.0-thinking-preview | {"model": "ernie-5.0-thinking-preview", "messages"... | 200 | 7754.38 | ✅ 通过 | - |
| 127 | qianfan-qi-vl | {"model": "qianfan-qi-vl", "messages": [{"role": "... | - | - | ⏱️ 超时 | 请求超时 |
| 128 | ernie-5.0-thinking-latest | {"model": "ernie-5.0-thinking-latest", "messages":... | 200 | 16887.57 | ✅ 通过 | - |
| 129 | qwen3-embedding-4b | {"model": "qwen3-embedding-4b", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 130 | stable-diffusion-xl | {"model": "stable-diffusion-xl", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 131 | qwen3-embedding-0.6b | {"model": "qwen3-embedding-0.6b", "messages": [{"r... | - | - | ⏱️ 超时 | 请求超时 |
| 132 | qianfan-funccaller | {"model": "qianfan-funccaller", "messages": [{"rol... | - | - | ⏱️ 超时 | 请求超时 |
| 133 | deepseek-ocr | {"model": "deepseek-ocr", "messages": [{"role": "u... | 200 | 626.99 | ✅ 通过 | - |
| 134 | musesteamer-air-image | {"model": "musesteamer-air-image", "messages": [{"... | 500 | 629.65 | ❌ 失败 | HTTP错误: 500 |
| 135 | deepseek-v3-250324-test | {"model": "deepseek-v3-250324-test", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 136 | musesteamer-2.0-lite-i2v | {"model": "musesteamer-2.0-lite-i2v", "messages": ... | - | - | ⏱️ 超时 | 请求超时 |
| 137 | ernie-5.0-thinking-exp | {"model": "ernie-5.0-thinking-exp", "messages": [{... | 403 | 457.38 | ❌ 失败 | HTTP错误: 403 |
| 138 | musesteamer-2.0-pro-i2v | {"model": "musesteamer-2.0-pro-i2v", "messages": [... | - | - | ⏱️ 超时 | 请求超时 |
| 139 | musesteamer-2.0-turbo-i2v | {"model": "musesteamer-2.0-turbo-i2v", "messages":... | - | - | ⏱️ 超时 | 请求超时 |
| 140 | musesteamer-2.0-turbo-i2v-audio | {"model": "musesteamer-2.0-turbo-i2v-audio", "mess... | - | - | ⏱️ 超时 | 请求超时 |
| 141 | musesteamer-2.1-lite-i2v | {"model": "musesteamer-2.1-lite-i2v", "messages": ... | 500 | 432.19 | ❌ 失败 | HTTP错误: 500 |
| 142 | musesteamer-2.0-turbo-i2v-effect | {"model": "musesteamer-2.0-turbo-i2v-effect", "mes... | - | - | ⏱️ 超时 | 请求超时 |
| 143 | musesteamer-2.1-turbo-i2v | {"model": "musesteamer-2.1-turbo-i2v", "messages":... | 500 | 526.51 | ❌ 失败 | HTTP错误: 500 |
| 144 | qwen3-reranker-8b | {"model": "qwen3-reranker-8b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 145 | qwen3-reranker-0.6b | {"model": "qwen3-reranker-0.6b", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 146 | kling-identify-face | {"model": "kling-identify-face", "messages": [{"ro... | 500 | 545.44 | ❌ 失败 | HTTP错误: 500 |
| 147 | kling-advanced-lip-sync | {"model": "kling-advanced-lip-sync", "messages": [... | 500 | 658.54 | ❌ 失败 | HTTP错误: 500 |
| 148 | qianfan-ocr | {"model": "qianfan-ocr", "messages": [{"role": "us... | 200 | 1124.3 | ✅ 通过 | - |
| 149 | viduq2-pro_reference2video | {"model": "viduq2-pro_reference2video", "messages"... | 500 | 559.67 | ❌ 失败 | HTTP错误: 500 |
| 150 | viduq3-pro_img2video | {"model": "viduq3-pro_img2video", "messages": [{"r... | 500 | 551.41 | ❌ 失败 | HTTP错误: 500 |
| 151 | viduq3-pro_text2video | {"model": "viduq3-pro_text2video", "messages": [{"... | 500 | 659.43 | ❌ 失败 | HTTP错误: 500 |
| 152 | qianfan-ocr-fast | {"model": "qianfan-ocr-fast", "messages": [{"role"... | 200 | 917.1 | ✅ 通过 | - |
| 153 | search_lighting_nearline_test_l2_26 | {"model": "search_lighting_nearline_test_l2_26", "... | 200 | 2446.42 | ✅ 通过 | - |
| 154 | qianfan-vl-1.5-flash | {"model": "qianfan-vl-1.5-flash", "messages": [{"r... | 200 | 1626.32 | ✅ 通过 | - |
| 155 | minimax-m2.1 | {"model": "minimax-m2.1", "messages": [{"role": "u... | 200 | 1437.55 | ✅ 通过 | - |
| 156 | minimax-m2.5 | {"model": "minimax-m2.5", "messages": [{"role": "u... | 200 | 1164.08 | ✅ 通过 | - |
| 157 | qwen3.5-35b-a3b | {"model": "qwen3.5-35b-a3b", "messages": [{"role":... | 200 | 761.13 | ✅ 通过 | - |
| 158 | viduq3-turbo_start-end2video | {"model": "viduq3-turbo_start-end2video", "message... | 500 | 498.72 | ❌ 失败 | HTTP错误: 500 |
| 159 | viduq3-pro_start-end2video | {"model": "viduq3-pro_start-end2video", "messages"... | 500 | 481.2 | ❌ 失败 | HTTP错误: 500 |
| 160 | viduq3-turbo_img2video | {"model": "viduq3-turbo_img2video", "messages": [{... | 500 | 470.28 | ❌ 失败 | HTTP错误: 500 |
| 161 | qwen3.5-122b-a10b | {"model": "qwen3.5-122b-a10b", "messages": [{"role... | 200 | 1324.76 | ✅ 通过 | - |
| 162 | viduq3-turbo_text2video | {"model": "viduq3-turbo_text2video", "messages": [... | 500 | 553.08 | ❌ 失败 | HTTP错误: 500 |
| 163 | qwen3.5-397b-a17b | {"model": "qwen3.5-397b-a17b", "messages": [{"role... | 200 | 1711.86 | ✅ 通过 | - |
| 164 | kling-image-o1_omni-image | {"model": "kling-image-o1_omni-image", "messages":... | 500 | 558.21 | ❌ 失败 | HTTP错误: 500 |
| 165 | kling-v3-omni_omni-image | {"model": "kling-v3-omni_omni-image", "messages": ... | 500 | 480.46 | ❌ 失败 | HTTP错误: 500 |
| 166 | kling-v3_image2video | {"model": "kling-v3_image2video", "messages": [{"r... | 500 | 831.2 | ❌ 失败 | HTTP错误: 500 |
| 167 | kling-v3_generations | {"model": "kling-v3_generations", "messages": [{"r... | 500 | 477.28 | ❌ 失败 | HTTP错误: 500 |
| 168 | kling-m1_ai-multi-shot | {"model": "kling-m1_ai-multi-shot", "messages": [{... | 500 | 507.41 | ❌ 失败 | HTTP错误: 500 |
| 169 | vidu-tts | {"model": "vidu-tts", "messages": [{"role": "user"... | 500 | 490.38 | ❌ 失败 | HTTP错误: 500 |
| 170 | vidu-audio-tts | {"model": "vidu-audio-tts", "messages": [{"role": ... | 500 | 592.12 | ❌ 失败 | HTTP错误: 500 |
| 171 | kling-v3_motion-control | {"model": "kling-v3_motion-control", "messages": [... | 500 | 466.79 | ❌ 失败 | HTTP错误: 500 |
| 172 | vidu-motion-sync_image2dance | {"model": "vidu-motion-sync_image2dance", "message... | 500 | 460.85 | ❌ 失败 | HTTP错误: 500 |
| 173 | vidu-audio-clone | {"model": "vidu-audio-clone", "messages": [{"role"... | 500 | 1001.6 | ❌ 失败 | HTTP错误: 500 |
| 174 | viduq300-turbo_text2video | {"model": "viduq300-turbo_text2video", "messages":... | 500 | 514.71 | ❌ 失败 | HTTP错误: 500 |
| 175 | kling-custom-voices_voices | {"model": "kling-custom-voices_voices", "messages"... | 500 | 521.99 | ❌ 失败 | HTTP错误: 500 |
| 176 | qwen3.5-27b | {"model": "qwen3.5-27b", "messages": [{"role": "us... | 200 | 4169.24 | ✅ 通过 | - |
| 177 | ernie-4.5-turbo-20260402 | {"model": "ernie-4.5-turbo-20260402", "messages": ... | 200 | 1517.14 | ✅ 通过 | - |
| 178 | qwen-image | {"model": "qwen-image", "messages": [{"role": "use... | - | - | ⏱️ 超时 | 请求超时 |
| 179 | qwen-image-edit | {"model": "qwen-image-edit", "messages": [{"role":... | - | - | ⏱️ 超时 | 请求超时 |
| 180 | kimi-k2.5 | {"model": "kimi-k2.5", "messages": [{"role": "user... | 200 | 6498.57 | ✅ 通过 | - |
| 181 | ernie-x1.1 | {"model": "ernie-x1.1", "messages": [{"role": "use... | 200 | 11121.94 | ✅ 通过 | - |
| 182 | glm-5 | {"model": "glm-5", "messages": [{"role": "user", "... | 200 | 10792.07 | ✅ 通过 | - |
| 183 | ernie-5.0 | {"model": "ernie-5.0", "messages": [{"role": "user... | 200 | 17911.85 | ✅ 通过 | - |
| 184 | glm-5.1 | {"model": "glm-5.1", "messages": [{"role": "user",... | 200 | 15115.64 | ✅ 通过 | - |
| 185 | musesteamer-air-i2v | {"model": "musesteamer-air-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 186 | ernie-video-1.0-i2v | {"model": "ernie-video-1.0-i2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 187 | ernie-video-1.0-t2v | {"model": "ernie-video-1.0-t2v", "messages": [{"ro... | - | - | ⏱️ 超时 | 请求超时 |
| 188 | offline-njjs-deepseekr10528 | {"model": "offline-njjs-deepseekr10528", "messages... | - | - | ⏱️ 超时 | 请求超时 |
| 189 | musesteamer-2.0-turbo-i2v-product | {"model": "musesteamer-2.0-turbo-i2v-product", "me... | - | - | ⏱️ 超时 | 请求超时 |
| 190 | musesteamer-2.0-turbo-i2v-storybook | {"model": "musesteamer-2.0-turbo-i2v-storybook", "... | - | - | ⏱️ 超时 | 请求超时 |
| 191 | musesteamer-2.0-turbo-i2v-wallpaper | {"model": "musesteamer-2.0-turbo-i2v-wallpaper", "... | - | - | ⏱️ 超时 | 请求超时 |
| 192 | paddleocr-vl-0.9b | {"model": "paddleocr-vl-0.9b", "messages": [{"role... | - | - | ⏱️ 超时 | 请求超时 |
| 193 | pp-structurev3 | {"model": "pp-structurev3", "messages": [{"role": ... | - | - | ⏱️ 超时 | 请求超时 |


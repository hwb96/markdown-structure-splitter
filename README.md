# markdown-hierarchy-splitter

[![PyPI version](https://badge.fury.io/py/markdown-hierarchy-splitter.svg)](https://badge.fury.io/py/markdown-hierarchy-splitter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个为RAG系统设计的Markdown文档分割工具，完整保留文档层级结构，解决传统切分器丢失标题层级与破坏表格完整性的问题。

## 🌟 主要特性

- **完整保留文档层级**: 每个切分片段都保留完整的标题路径(一级标题 > 二级标题 > 三级标题...)
- **智能表格处理**: 保持表格完整性，同时遵循块大小限制
- **多格式导出**: 支持导出为Markdown、Word(.docx)和CSV格式
- **灵活配置**: 可调整的分块大小，智能边界检测
- **轻量级依赖**: 主要使用Python标准库，最小化外部依赖

## 🎯 解决的问题

传统RAG系统在处理文档时通常面临两个关键问题：

1. **丢失文档结构**: 文档被分割成块后，往往丢失了章节层级关系
2. **表格破碎**: 表格常常被从中间切断，导致内容难以理解

本工具通过以下方式解决这些问题：
- 为每个文本块保留完整的标题路径
- 将表格作为原子单位处理，确保其完整性

## 🚀 安装方法

### 从PyPI安装（推荐）
```bash
pip install markdown-hierarchy-splitter
```

### 本地开发安装
1. 克隆仓库
```bash
git clone https://github.com/yourusername/markdown-hierarchy-splitter.git
cd markdown-hierarchy-splitter
```

2. 创建虚拟环境（可选但推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装开发模式
```bash
pip install -e .
```

## 📚 使用方法

### 基本用法
```python
from markdown_hierarchy_splitter import MarkdownProcessorLocal

# 初始化处理器
processor = MarkdownProcessorLocal(chunk_size=300)

# 处理Markdown文件
with open('data/input/example.md', 'r', encoding='utf-8') as f:
    markdown_text = f.read()

# 获取保留层级结构的文本块
chunks = list(processor.process_markdown(markdown_text))
```

### 导出为多种格式
```python
from markdown_hierarchy_splitter import create_output_files

# 文件会自动从 data/input 读取，并保存到 data/output
results = create_output_files(
    input_file="example.md",  # 只需提供文件名
    chunk_size=300
)
```

### 项目结构说明
```
markdown-structure-splitter/
├── data/
│   ├── input/    # 存放待处理的Markdown文件
│   └── output/   # 存放处理后的输出文件
└── src/
    └── markdown_hierarchy_splitter/
        ├── processor.py  # 核心处理逻辑
        └── config.py     # 配置文件
```

## 📋 环境要求

- Python 3.6+
- python-docx
- langchain-text-splitters

## 🎈 使用小贴士

1. **输入文件放置**：
   - 将需要处理的Markdown文件放在 `data/input` 目录下
   - 处理后的文件会自动保存在 `data/output` 目录下对应的子文件夹中

2. **参数调优**：
   - 建议将chunk_size设置在300-500之间
   - 对于包含大量表格的文档，可以适当增加chunk_size
   - 导出Word格式时会自动应用一些基础格式设置

3. **性能建议**：
   - 对于大文件处理，建议先测试小部分内容
   - 确保系统有足够的内存处理大型文档



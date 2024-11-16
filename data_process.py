from markdown_hierarchy_splitter import MarkdownProcessorLocal
from pathlib import Path

try:
    # 初始化处理器
    processor = MarkdownProcessorLocal(chunk_size=300)

    # 方式1：使用完整路径
    results = processor.create_output_files(
        input_path="D:/my_documents/example.md",
        output_dir="D:/my_documents/output"  # 可选，如果不指定则使用默认output目录
    )

    # 方式2：使用相对路径
    results = processor.create_output_files(
        input_path="./example.md",
        output_dir="./output"  # 可选
    )

    # 方式3：只生成特定格式
    results = processor.create_output_files(
        input_path="./example.md",
        create_docx=False,  # 不生成word文档
        create_csv=False  # 不生成csv文件
    )

except Exception as e:
    print(f"错误：{str(e)}")
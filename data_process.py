from markdown_hierarchy_splitter import MarkdownProcessorLocal

# 创建处理器实例，可以指定自定义的输出目录
processor = MarkdownProcessorLocal(
    chunk_size=300
)

# 处理文件
results = processor.create_output_files(
    input_path="20241116-正文.md",
)
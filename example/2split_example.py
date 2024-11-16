from markdown_hierarchy_splitter import MarkdownProcessorLocal
from pathlib import Path


def split_example():
    """
    示例：使用MarkdownProcessorLocal分割markdown文档
    可以处理原始文档或格式化后的文档
    """
    try:
        # 创建处理器实例
        processor = MarkdownProcessorLocal(
            chunk_size=300,
            default_output_dir="./output"
        )

        # 可以选择处理原始文档
        results_original = processor.create_output_files(
            input_path="./formatted_doc.md",
            output_dir="./output",
            create_md=True,
            create_docx=True,
            create_csv=True
        )

        print(f"原始文档处理完成！生成了 {len(results_original)} 个文本块")

        # 打印预览
        print("\n分割后的文本块预览:")
        print("=" * 50)
        for i, chunk in enumerate(results_original[:2], 1):
            print(f"\n块 {i}:")
            print(chunk[:200] + "...\n")

    except Exception as e:
        print(f"处理过程中发生错误：{str(e)}")


if __name__ == "__main__":
    split_example()
from markdown_hierarchy_splitter import MarkdownFormatter


def format_example():
    """
    示例：使用MarkdownFormatter格式化markdown文档
    """
    try:
        # 创建格式化器实例
        formatter = MarkdownFormatter()

        # 格式化文档
        output_file = formatter.format_file(
            input_path="./example_doc.md",
            output_path="./formatted_doc.md"
        )

        print(f"格式化完成！输出文件：{output_file}")

        # 打印格式化后的内容预览
        with open(output_file, 'r', encoding='utf-8') as f:
            print("\n格式化后的文档预览:")
            print("=" * 50)
            print(f.read()[:500] + "...\n")

    except Exception as e:
        print(f"处理过程中发生错误：{str(e)}")


if __name__ == "__main__":
    format_example()
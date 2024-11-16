from pathlib import Path
import re
from typing import Optional


class MarkdownFormatter:
    """Markdown文档格式化处理器"""

    def __init__(self, default_output_dir: Optional[Path | str] = None):
        """
        初始化格式化处理器

        Args:
            default_output_dir: 默认输出目录，如果为None则使用'output/formatted'
        """
        if default_output_dir is None:
            self.default_output_dir = Path.cwd() / 'output' / 'formatted'
        else:
            self.default_output_dir = Path(default_output_dir)

    @staticmethod
    def format_markdown(text: str) -> str:
        """格式化markdown文本的标题层级

        Args:
            text: 输入的markdown文本

        Returns:
            str: 格式化后的markdown文本
        """
        # Split text into lines
        lines = text.split('\n')
        formatted_lines = []

        # Keep track of if we've processed the first line
        first_line_processed = False

        for line in lines:
            # Skip empty lines but preserve them
            if not line.strip():
                formatted_lines.append(line)
                continue

            # First non-empty line is kept as is (assumed to be main title)
            if not first_line_processed:
                formatted_lines.append(line)
                first_line_processed = True
                continue

            # Pattern for "number.number[.number...]"
            leveln_pattern = r'^\d+(\.\d+)+'

            # Only number pattern
            only_number_pattern = r'^\d+$'

            # Pattern for number + 2 or more Chinese characters
            level2_pattern = r'^\d+\s*[\u4e00-\u9fff]{2,}'  # Number followed by 2+ Chinese characters

            line = line.strip()

            if re.match(leveln_pattern, line):
                # Count the dots to determine level (3 or more)
                dots = line.count('.')
                level = dots + 2  # 1 dot = level 3, 2 dots = level 4, etc.
                formatted_lines.append(f'{"#" * level} {line}')
            elif re.match(level2_pattern, line):
                # Level 2 title: number + (optional space) + 2+ Chinese characters
                formatted_lines.append(f'## {line}')
            elif re.match(only_number_pattern, line):
                # Keep lines with only numbers as is
                formatted_lines.append(line)
            else:
                # Keep other lines as is
                formatted_lines.append(line)

        return '\n'.join(formatted_lines)

    def format_file(
            self,
            input_path: str | Path,
            output_path: Optional[str | Path] = None
    ) -> Path:
        """处理markdown文件并保存格式化结果

        Args:
            input_path: 输入文件路径
            output_path: 输出文件路径，如果为None则使用默认路径

        Returns:
            Path: 输出文件的路径

        Raises:
            FileNotFoundError: 输入文件不存在
            ValueError: 输入文件不是markdown格式
        """
        input_path = Path(input_path)

        if not input_path.exists():
            raise FileNotFoundError(f"输入文件不存在: {input_path}")

        if input_path.suffix.lower() not in ['.md', '.markdown']:
            raise ValueError(f"不支持的文件格式: {input_path.suffix}")

        # 读取输入文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 格式化内容
        formatted_content = self.format_markdown(content)

        # 确定输出路径
        if output_path is None:
            output_path = self.default_output_dir / input_path.name
        else:
            output_path = Path(output_path)

        # 创建输出目录
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # 写入格式化内容
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)

        return output_path

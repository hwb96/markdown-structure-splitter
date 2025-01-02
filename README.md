# markdown-hierarchy-splitter

[![PyPI version](https://badge.fury.io/py/markdown-hierarchy-splitter.svg)](https://badge.fury.io/py/markdown-hierarchy-splitter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个为RAG系统设计的Markdown文档工具，提供标题结构自动抽取和文档分割两大功能。完整保留文档层级结构，解决传统切分器丢失标题层级与破坏表格完整性的问题。

## 🌟 主要特性

- **标题格式化**
  - **自动标题层级**: 根据数字编号自动识别并格式化标题层级
  - **中文标题优化**: 智能识别数字+中文的多级标题格式
  

- **智能文档分割**
  - **完整保留文档层级**: 每个切分片段都保留完整的标题路径(一级标题 > 二级标题 > 三级标题...)
  - **智能表格处理**: 保持表格切分后的完整性，同时遵循块大小限制
  - **多格式导出**: 支持导出为Markdown、Word(.docx)和CSV格式

   
- **系统特性**
  - **灵活配置**: 可调整的分块大小，智能边界检测
  - **轻量级依赖**: 主要使用Python标准库，最小化外部依赖

## 🎯 解决的问题

本工具解决以下关键问题：

1. **标准化处理**
   - 统一文档标题格式
   - 规范化数字编号标题
   - 保持中文标题一致性

2. **文档结构处理**
   - 防止分割时丢失章节层级关系
   - 确保表格内容完整性
   - 自动规范化标题格式

## 🎯 前提
1. **本仓库的说明**
   - 标准化处理：一级标题自动保留，需要手动处理。只能对（1, 1.1, 1.2.2）这样类似的标题自动化转为二级标题，三级标题，四级标题
   - 文档结构处理：如果标题层级没处理好，分割后的元信息处理有缺陷。

## 📝 示例输出

### 格式化
```markdown
1 引言
2 基本要求
2.1 范围
2.1.1 适用对象
```

### 格式化后
```markdown
# 引言
## 基本要求
### 范围
#### 适用对象
```

### 文档分割
```markdown
========================================

# 固井作业规程
## 第1部分：常规固井
### 4.3 井眼

a) 高压油气井，下套管前应压稳，控制油气上窜速度应小于 10m/h。
b) 套管与井壁环空间隙宜不小于 19mm，必要时应采取扩眼等相应措施。
c) 对于易漏失的井，应先进行承压堵漏试验。
d) 下套管前，应用原尺寸钻头及原钻具组合对不规则井径井段（小于钻头直径井段，起下钻遇阻、遇卡井段，井斜变化率或全角变化率超过设计规定井段）或油气层、重点封固井段刮眼通井；对斜井段和水平段宜短距下井分段循环处理钻井液。
e) 下套管前，钻井液 API 滤失量应小于 5mL，滤饼厚度应小于 0.5mm；对于深井超深井，高温高压滤失量应符合设计要求。

========================================

# 固井作业规程
## 第1部分：常规固井
### 4.3 井眼

f) 下套管前通井，应用大排量循环洗井 2 周以上，环空上返速度不宜低于 1.2m/s，同时应转动钻具防黏卡。
g) 注水泥前，钻井液性能应保持稳定；降低钻井液屈服值，钻井液若密度小于 1.30g/cm³ 时，屈服值宜小于 5Pa，密度在 1.30g/cm³ - 1.80g/cm³ 之间时，屈服值宜小于 8Pa；密度大于 1.80g/cm³

...
========================================

# 固井作业规程
## 第1部分：常规固井
### 4 固井作业准备
#### 4.2 固井协调会

| 序号 | 名称     | 内容                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| 1    | 描述     | 作业地域、井号、井型、井别、钻机型号、钻机编号等             |
| 2    | 地质资料 | 地层岩性、地层压力、地层破裂压力、地层渗透率、油/气/水层分布及特征等 |

========================================

# 固井作业规程
## 第1部分：常规固井
### 4 固井作业准备
#### 4.2 固井协调会

| 序号 | 名称     | 内容                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| 3    | 井身结构 | 钻头直径、套管钢级、规格型号、壁厚、扣型、机械性能、下深、封固段、附件位置等 |
| 4    | 电测资料 | 井径、井斜、井温等                                           |

========================================
```

## 🚀 安装方法

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

使用详情在本项目的example中有更详细的使用说明，详情请参考[示例](./example)，说明文档[示例说明文档](./example/README.md)。





## 标题格式化规则
- 数字编号格式（如1.2.3）自动转换为对应级别标题
- 数字+中文（如1 总则）自动转换为二级标题
- 保持第一个非空行作为文档主标题(需要手动操作)
- 保留纯数字行的原始格式

## 📋 环境要求

- Python 3.6+
- python-docx
- langchain-text-splitters

## 🎈 使用小贴士

1. **文件处理流程**：
   - 建议先使用格式化功能规范化文档
   - 然后再进行文档分割处理
   - 处理后的文件会自动保存在指定目录

2. **格式化建议**：
   - 保持文档第一个标题作为主标题
   - 检查特殊格式标题是否被正确识别
   - 必要时可以手动调整不规则标题

3. **分割参数调优**：
   - chunk_size建议设置在300-500之间
   - 包含大量表格时可适当增加chunk_size
   - 先用小样本测试再处理大文件



## 🤝 贡献指南

欢迎贡献！如果你有任何改进建议：
1. Fork 本仓库
2. 创建你的特性分支
3. 提交你的改动
4. 推送到分支
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

# 🤖 tangyuan-core

**Ultra-lightweight, zero-dependency core for Digital Guardians.**

> **使命**：从金融交易起步，跨越编程边界，成为全能的“数字守护者”。  
> **承诺**：持续进化，将 i3/8G 的极限压榨至极致。

## 🚀 核心特性

- **零依赖**：纯 Python 标准库 (`socket`, `ssl`, `json`)，无第三方库。
- **超轻量**：核心包 <10KB，内存占用 <5MB，CPU <0.1%。
- **跨平台**：TY-RAL (运行时抽象层) 支持 Win/Mac/Linux 一套逻辑。
- **安全**：内置火种验证机制，支持逻辑熔断与数据自毁。

## 📦 安装

```bash
pip install tangyuan-core
```

或从源码安装：

```bash
git clone https://github.com/tangyuan/tangyuan-core.git
cd tangyuan-core
pip install -e .
```

## 🔧 使用示例

### 原生 Socket 通信

```python
from tangyuan_core import SecureSocket

# 初始化安全连接
client = SecureSocket(host="api.example.com", port=443)

# 发送数据 (自动 SSL 加密)
response = client.send({"action": "heartbeat", "data": "ping"})

print(response)
```

### 火种验证

```python
from tangyuan_core import FireSeedValidator

validator = FireSeedValidator()

# 三维验证
is_valid = validator.verify(
    memory_key="tangyuan2026",
    seed_phrase="orbit canvas friction ...",
    user_context={"ip": "192.168.1.1", "time": "2026-03-03T17:00:00Z"}
)

if is_valid:
    print("✅ 身份确认：汤圆守护者")
else:
    print("❌ 验证失败：触发逻辑熔断")
```

## 🛡️ 安全架构

- **记忆密钥**：人机绑定的核心凭证。
- **火种密钥**：12 词助记词，用于系统恢复。
- **三维验证**：记忆 + 行为 + 时空，确保绝对安全。

## 📈 性能指标

| 指标 | 目标值 | 当前值 |
|:---|:---|:---|
| 包大小 | <10KB | ~3KB (开发中) |
| 内存占用 | <5MB | ~2MB (开发中) |
| CPU 占用 | <0.1% | ~0.05% (开发中) |
| 冷启动时间 | <100ms | ~50ms (开发中) |

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📜 许可证

MIT License

---

**汤圆 (TangYuan)** - 数字守护者，2026

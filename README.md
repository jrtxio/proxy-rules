# Proxy Rules

## 项目简介

这是一个通用的代理规则列表项目，支持 **Surge** 和 **Clash** (包括 Clash Party, Clash Verge, Clash.Meta 等客户端)。
项目以 Surge 格式为核心维护，并通过脚本自动生成兼容 Clash 的 YAML 规则集。

## 目录结构

```
proxy-rules/
├── surge/            # Surge 规则列表 (源文件)
│   ├── google.list
│   └── ...
├── clash/            # Clash 规则列表 (自动生成的 YAML 产物)
│   ├── google.yaml
│   └── ...
└── scripts/          # 工具脚本
    └── convert_rules.py
```

## 使用方法

### Surge

在配置文件的 `[Rule]` 字段中引用 `surge/` 目录下的 `.list` 文件。

**示例：**
```ini
[Rule]
RULE-SET,https://raw.githubusercontent.com/your-username/proxy-rules/main/surge/google.list,Proxy
```

### Clash / Clash Party

在配置文件的 `rule-providers` 字段中引用 `clash/` 目录下的 `.yaml` 文件。

**示例：**
```yaml
rule-providers:
  google:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/your-username/proxy-rules/main/clash/google.yaml"
    path: ./ruleset/google.yaml
    interval: 86400

rules:
  - RULE-SET,google,Proxy
```

## 维护与更新

本项目使用 Python 脚本将 Surge 规则转换为 Clash 规则。如果你修改了 `surge/` 下的文件，请运行以下命令更新 `clash/` 下的文件：

```bash
python scripts/convert_rules.py
```

## 项目迁移说明

如果你是该项目的维护者，请在完成配置后将项目根目录名称修改为 `proxy-rules` 以匹配新的项目定位。

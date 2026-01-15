# surge-list

## 项目简介

这是一个 Surge 规则列表项目，提供了多个针对不同服务的规则配置文件，方便在 Surge 中使用。

## 目录结构

```
surge-list/
├── ruleset/          # 规则列表目录
│   ├── blocked.list  # 黑名单规则
│   ├── claude.list   # Claude 相关规则
│   ├── google.list   # Google 相关规则
│   ├── netflix.list  # Netflix 相关规则
│   ├── openai.list   # OpenAI 相关规则
│   ├── telegram.list # Telegram 相关规则
│   └── unblock.list  # 白名单规则
├── example.conf      # 示例配置文件
├── hostname.txt      # 主机名列表
└── README.md         # 项目说明文件
```

## 规则列表说明

- **blocked.list** - 黑名单规则，用于拦截不需要的网站或服务
- **claude.list** - Claude 相关规则，优化 Claude 的访问
- **google.list** - Google 相关规则，优化 Google 服务的访问
- **netflix.list** - Netflix 相关规则，优化 Netflix 的访问
- **openai.list** - OpenAI 相关规则，优化 OpenAI 服务的访问
- **telegram.list** - Telegram 相关规则，优化 Telegram 的访问
- **unblock.list** - 白名单规则，用于允许特定的网站或服务

## 使用方法

### 本地使用

通过 iCloud/Surge 路径访问本地的规则列表文件。

### 远程使用

通过 URL 访问远程的规则列表文件。

## 示例配置

`example.conf` 文件提供了一个简单的配置示例，您可以参考它来设置您自己的 Surge 配置。

## 其他说明

- **hostname.txt** - 包含主机名列表，可用于规则配置参考

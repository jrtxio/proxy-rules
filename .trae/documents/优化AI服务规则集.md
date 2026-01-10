## 优化计划

### 1. 统一注释和分类风格
- **统一标题格式**：所有文件使用 `# ==========================` 作为一级标题，`# ---- Category ----` 作为二级标题
- **统一分类结构**：每个文件按功能模块（Core、API、CDN、Assets等）分类
- **统一注释风格**：使用清晰、简洁的注释，避免冗余

### 2. OpenAI规则优化 (openai.list)
- **添加缺失域名**：`gateway.openai.com`、`status.openai.com`、`platform.openai.com`
- **添加通配符**：`*.openai.com` 以覆盖所有子域名
- **完善API支持**：添加更多API端点域名
- **更新CDN资源**：添加新的CDN域名

### 3. Google/Gemini规则优化 (google.list)
- **强化Gemini支持**：添加 `gemini.googleapis.com`、`generativelanguage.googleapis.com`
- **完善Google AI服务**：添加更多Google AI相关域名
- **统一分类方式**：按功能模块重新组织规则
- **优化WebSocket支持**：确保所有实时通信域名被覆盖

### 4. Claude规则优化 (claude.list)
- **细化cloudfront规则**：将泛域名 `cloudfront.net` 替换为特定的Anthropic CDN分布
- **添加通配符**：`*.anthropic.com` 以覆盖所有子域名
- **添加缺失域名**：`console.anthropic.com`、`docs.anthropic.com`
- **完善API支持**：添加新的API端点

### 5. Telegram规则优化 (telegram.list)
- **添加CDN域名**：`*.cdn.telegram.org`、`*.cdn1.telegram.org` 等
- **添加通配符**：`*.telegram.org` 以覆盖所有子域名
- **完善API支持**：添加更多API相关域名

### 6. Netflix规则优化 (netflix.list)
- **优化分类结构**：按功能模块重新组织规则
- **添加缺失域名**：`*.netflix.com` 通配符及其他相关域名
- **完善CDN支持**：添加更多流媒体相关域名

### 7. Unblock规则优化 (unblock.list)
- **统一分类方式**：按公司或服务类型重新组织规则
- **优化规则结构**：合并相似分类，简化结构
- **添加缺失域名**：添加一些常用服务的域名

### 8. Blocked规则优化 (blocked.list)
- **统一分类方式**：按功能模块重新组织规则
- **优化规则**：添加一些常见的需要阻止的域名
- **细化规则**：避免过于宽泛的规则

### 9. 通用优化
- **避免过度宽泛的规则**：确保规则尽可能精确
- **添加必要的通配符**：使用 `*.domain.com` 覆盖所有子域名
- **优化规则顺序**：按重要性和使用频率排序
- **添加清晰的注释**：为每个分类和重要规则添加注释

## 预期效果
- 所有文件注释和分类风格统一
- AI服务（OpenAI、Gemini、Claude）规则完善，访问流畅
- 其他服务规则优化，性能提升
- 规则结构清晰，易于维护和扩展
- 避免不必要的规则冲突和性能影响
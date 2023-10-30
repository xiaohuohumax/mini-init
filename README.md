# mini-init

简单辅助工具集合: 日志, 配置文件, 环境变量等

加载依赖
------

```shell
pip install mini-init
```

读取环境变量
----------

```ini
# .env
PROJECT_NAME=mini-init
...
```

```python
from dataclasses import dataclass
from miniinit import env

@dataclass
class Env:
    # 环境变量
    PROJECT_NAME: str = ''
    ...

env_data = env.get_env(Env)
# 更换路径
# env_data = env.get_env(Env, '**/.env')

print(env_data.PROJECT_NAME)
# mini-init
```

读取项目配置
----------

```yaml
# 默认, 不可修改
# config/application.yaml
app:
  name: mini-init
  version: 0.0.1

log:
  is_use: true
  yaml_path: config/log.yaml

banner:
  is_show: true
  file_path: banner.txt
  welcome: welcome use mini-init (v0.0.1)

# 其他参数自行扩展
...
```

```python
from dataclasses import dataclass
from miniinit import config

@dataclass
class Config(config.Config):
    # 自定参数, 也可覆盖
    ...

config_data = config.get_config(Config)

print(config_data.app.name)
# mini-init
```
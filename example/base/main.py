from dataclasses import dataclass, field
import logging

from miniinit import env, config

logger = logging.getLogger(__name__)


@dataclass
class Env:
    NAME: str = ''


@dataclass
class ZipConfig:
    size: int = 0


@dataclass
class Config(config.Config):
    zip: ZipConfig = field(default_factory=ZipConfig)


if __name__ == '__main__':
    # 获取 .env
    e = env.get_env(Env)
    logger.info(e)
    # 获取配置信息
    c = config.get_config(Config)
    logger.info(c)

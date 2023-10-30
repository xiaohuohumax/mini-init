from setuptools import setup, find_packages

setup(
    name="mini-init",
    version='0.0.1',
    author='xiaohuohumax',
    license='MIT',
    url='https://github.com/xiaohuohumax/mini-init',
    description="简单辅助工具集合: 日志, 配置文件, 环境变量等",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.8",
    install_requires=[
        'dacite',
        'python-dotenv',
        'ruamel.yaml'
    ],
    keywords=[
        'mini-init',
        'init',
        'tools',
        'project-init',
        'logging',
        'env',
        'config'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
)

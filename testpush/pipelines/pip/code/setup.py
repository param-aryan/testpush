from setuptools import setup, find_packages
setup(
    name = 'pip',
    version = '1.0',
    packages = find_packages(include = ('pip*', )) + ['prophecy_config_instances.pip'],
    package_dir = {'prophecy_config_instances.pip' : 'configs/resources/pip'},
    package_data = {'prophecy_config_instances.pip' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.46'],
    entry_points = {
'console_scripts' : [
'main = pip.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
